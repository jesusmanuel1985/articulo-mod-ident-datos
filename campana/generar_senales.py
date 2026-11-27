#!/usr/bin/env python3
"""Genera los comandos de caudal y las máscaras de potencia de la campaña (P5 v1.5).

Salidas en campana/senales/:
  comando_{IS,IP,K,NL,P}.csv ....... t [s], sp [L/h], cada 1 s
  mascara_{A,B,C,PS,K,NL,P}.csv .... t, p1, p2, p3, p4 (formato de fast_cloud_data)
  manifiesto.json .................. semillas, parámetros, verificaciones y hashes

Solo usa la biblioteca estándar. Aborta si alguna verificación falla.
"""
import bisect
import csv
import hashlib
import json
import random
from pathlib import Path

SALIDA = Path(__file__).parent / "senales"
SEMILLA_BASE = 20261104
SEMILLAS = {"IS": SEMILLA_BASE, "A": SEMILLA_BASE + 1, "B": SEMILLA_BASE + 2,
            "C": SEMILLA_BASE + 3, "PS": SEMILLA_BASE + 4, "NL": SEMILLA_BASE + 5}

DURACION = 6000            # s, IS, IP y validación
DURACION_PS = 7000         # s
NIVELES = [200, 250, 300, 350, 400]  # L/h
TASA_RAMPA = 1.8           # L/h·s
TASA_MAX = 2.0             # L/h·s, C2
SALTO_MIN = 100            # L/h, C2
COMANDO_MIN, COMANDO_MAX = 200, 400  # L/h
PERMANENCIA = (300, 900)   # s
RELOJ_PRBS = 90            # s
TRANSICIONES_MIN = 6       # por panel en 6000 s
SEPARACION_PANELES = 10    # s, mínimo entre transiciones de paneles distintos
DT_TRANSICION = 0.01       # s, separación de las dos filas de cada transición
ETAPA_K = 60               # s, cada etapa de la verificación de corriente
ETAPA_K_TODAS = 90         # s, las 4 encendidas
CAUDAL_K = 300             # L/h
CAUDALES_NL = [200, 300, 400]  # L/h
MESETA_NL = 1200           # s
DATOS_PS = Path(__file__).parent.parent / "datos_campana" / "crudos" / (
    "P5v1.4_PS_r1_run_18_Test_taken_at_2026-11-27_10-22-01_part_1.csv")
INICIO_P = 1000            # s de la PS réplica 1, tras el transitorio del PI
DURACION_P = 2500          # s


def senal_suave(rng):
    """Niveles aleatorios unidos por rampas a TASA_RAMPA; devuelve sp por segundo."""
    nivel = rng.choice(NIVELES)
    sp = []
    niveles_usados = [nivel]
    while len(sp) < DURACION + 1:
        sp.extend([float(nivel)] * rng.randint(*PERMANENCIA))
        siguiente = rng.choice([n for n in NIVELES if abs(n - nivel) >= SALTO_MIN])
        paso = TASA_RAMPA if siguiente > nivel else -TASA_RAMPA
        valor = float(nivel)
        while abs(siguiente - valor) > TASA_RAMPA:
            valor += paso
            sp.append(valor)
        sp.append(float(siguiente))
        nivel = siguiente
        niveles_usados.append(nivel)
    return sp[:DURACION + 1], niveles_usados


def senal_prbs():
    """PRBS de 6 bits (x^6 + x^5 + 1, periodo 63), repetida hasta DURACION."""
    registro = 0b111111
    bits = []
    for _ in range(63):
        bits.append(registro & 1)
        nuevo = ((registro >> 5) ^ (registro >> 4)) & 1
        registro = ((registro << 1) | nuevo) & 0b111111
    return [float(COMANDO_MAX if bits[(t // RELOJ_PRBS) % 63] else COMANDO_MIN)
            for t in range(DURACION + 1)], bits


def transiciones_panel(rng, duracion):
    """Instantes de cambio de un panel, con permanencias de PERMANENCIA."""
    instantes = []
    t = rng.randint(*PERMANENCIA)
    while t < duracion:
        instantes.append(t)
        t += rng.randint(*PERMANENCIA)
    return instantes


def mascara(rng, duracion):
    """Genera 4 paneles no sincronizados; repite el sorteo hasta cumplir."""
    while True:
        cambios = [transiciones_panel(rng, duracion) for _ in range(4)]
        todos = sorted(t for panel in cambios for t in panel)
        separados = all(b - a >= SEPARACION_PANELES for a, b in zip(todos, todos[1:]))
        util = [sum(1 for t in panel if t <= DURACION) for panel in cambios]
        if separados and min(util) >= TRANSICIONES_MIN:
            return [rng.randint(0, 1) for _ in range(4)], cambios


def filas_mascara(iniciales, cambios, duracion):
    """Tabla [t, p1..p4] con dos filas por transición, para evitar rampas al interpolar."""
    estado = list(iniciales)
    filas = [[0.0] + estado]
    eventos = sorted((t, i) for i, panel in enumerate(cambios) for t in panel)
    for t, i in eventos:
        filas.append([t - DT_TRANSICION] + estado)
        estado[i] = 1 - estado[i]
        filas.append([float(t)] + estado)
    filas.append([float(duracion)] + estado)
    return filas


def corrida_k():
    """Verificación de corriente K: 300 L/h fijo; apagadas, cada resistencia sola, las 4 juntas."""
    apagadas = [0, 0, 0, 0]
    etapas = [(apagadas, ETAPA_K)]
    for i in range(4):
        etapas += [([1 if j == i else 0 for j in range(4)], ETAPA_K), (apagadas, ETAPA_K)]
    etapas += [([1, 1, 1, 1], ETAPA_K_TODAS), (apagadas, ETAPA_K)]
    filas = [[0.0] + apagadas]
    t = 0
    for (estado, duracion), (siguiente, _) in zip(etapas, etapas[1:]):
        t += duracion
        filas.append([t - DT_TRANSICION] + estado)
        filas.append([float(t)] + siguiente)
    t += etapas[-1][1]
    filas.append([float(t)] + apagadas)
    return [float(CAUDAL_K)] * (t + 1), filas


def corrida_nl(rng):
    """Corrida NL: caudal fijo en orden sorteado; las 4 resistencias 0 → 100 → 0 %."""
    orden = rng.sample(CAUDALES_NL, 3)
    sp = []
    filas = [[0.0, 0, 0, 0, 0]]
    for k, caudal in enumerate(orden):
        sp.extend([float(caudal)] * (3 * MESETA_NL))
        inicio = k * 3 * MESETA_NL
        for t, antes, despues in [(inicio + MESETA_NL, 0, 1), (inicio + 2 * MESETA_NL, 1, 0)]:
            filas.append([t - DT_TRANSICION] + [antes] * 4)
            filas.append([float(t)] + [despues] * 4)
    sp.append(sp[-1])
    filas.append([float(9 * MESETA_NL), 0, 0, 0, 0])
    return sp, filas, orden


def corrida_p(filas_ps):
    """Piloto P: tramo [INICIO_P, INICIO_P + DURACION_P) de la PS réplica 1.

    El comando es el que el PI envió en cada muestra (columna sp F1), retenido hasta la muestra
    siguiente y llevado a 1 s; la máscara es la de PS en el mismo intervalo, desplazada a t = 0.
    """
    with DATOS_PS.open(encoding="utf-8") as f:
        muestras = [(float(r["t_corrida (s)"]), float(r["sp F1"]))
                    for r in csv.DictReader(f) if r["fase"] == "ensayo"]
    tiempos = [t for t, _ in muestras]
    sp = []
    for t in range(INICIO_P, INICIO_P + DURACION_P + 1):
        i = bisect.bisect_right(tiempos, t) - 1
        sp.append(round(muestras[i][1], 1))
    fin = INICIO_P + DURACION_P
    estado = next(f[1:] for f in reversed(filas_ps) if f[0] <= INICIO_P)
    filas = [[0.0] + estado]
    for fila in filas_ps:
        if INICIO_P < fila[0] < fin:
            filas.append([round(fila[0] - INICIO_P, 2)] + fila[1:])
    filas.append([float(DURACION_P)] + filas[-1][1:])
    return sp, filas


def verificar_c2(sp, niveles):
    """C2 sobre el archivo de comando (§5.4). Devuelve los valores medidos."""
    tasa = max(abs(b - a) for a, b in zip(sp, sp[1:]))
    saltos = [abs(b - a) for a, b in zip(niveles, niveles[1:])]
    medido = {"tasa_max_L_h_s": round(tasa, 3), "salto_min_L_h": min(saltos),
              "comando_min_L_h": min(sp), "comando_max_L_h": max(sp)}
    assert tasa <= TASA_MAX, medido
    assert min(saltos) >= SALTO_MIN, medido
    assert max(sp) <= COMANDO_MAX and min(sp) >= COMANDO_MIN, medido
    return medido


def verificar_prbs(sp, bits):
    medido = {"bits_1": sum(bits), "bits_0": 63 - sum(bits), "comando_min_L_h": min(sp),
              "comando_max_L_h": max(sp), "muestras": len(sp)}
    assert sum(bits) == 32 and len(bits) == 63, medido
    assert set(sp) == {float(COMANDO_MIN), float(COMANDO_MAX)}, medido
    return medido


def verificar_mascara(iniciales, cambios, filas, duracion):
    """Comprueba que la tabla sea binaria, cubra la corrida y cumpla las permanencias."""
    assert all(valor in (0, 1) for fila in filas for valor in fila[1:])
    assert [f[0] for f in filas] == sorted(f[0] for f in filas)
    assert filas[-1][0] >= duracion
    for panel in cambios:
        for a, b in zip([0] + panel, panel):
            assert PERMANENCIA[0] <= b - a <= PERMANENCIA[1]
    return {"estado_inicial": iniciales,
            "transiciones_por_panel": [len(p) for p in cambios],
            "transiciones_en_6000_s": [sum(1 for t in p if t <= DURACION) for p in cambios]}


def escribir(nombre, encabezado, filas):
    ruta = SALIDA / nombre
    with ruta.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, lineterminator="\n")
        escritor.writerow(encabezado)
        escritor.writerows(filas)
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def main():
    SALIDA.mkdir(exist_ok=True)
    manifiesto = {"P5": "v1.5", "semillas": SEMILLAS, "archivos": {}, "verificaciones": {}}

    sp, niveles = senal_suave(random.Random(SEMILLAS["IS"]))
    manifiesto["verificaciones"]["C2_IS"] = verificar_c2(sp, niveles)
    manifiesto["verificaciones"]["niveles_IS"] = niveles
    manifiesto["archivos"]["comando_IS.csv"] = escribir(
        "comando_IS.csv", ["t", "sp"], [[t, round(v, 1)] for t, v in enumerate(sp)])

    sp, bits = senal_prbs()
    manifiesto["verificaciones"]["PRBS_IP"] = verificar_prbs(sp, bits)
    manifiesto["archivos"]["comando_IP.csv"] = escribir(
        "comando_IP.csv", ["t", "sp"], [[t, v] for t, v in enumerate(sp)])

    generadas = {}
    for nombre, duracion in [("A", DURACION), ("B", DURACION), ("C", DURACION), ("PS", DURACION_PS)]:
        iniciales, cambios = mascara(random.Random(SEMILLAS[nombre]), duracion)
        filas = filas_mascara(iniciales, cambios, duracion)
        manifiesto["verificaciones"][f"mascara_{nombre}"] = verificar_mascara(
            iniciales, cambios, filas, duracion)
        generadas[nombre] = cambios
        if nombre == "PS":
            filas_ps = filas
        manifiesto["archivos"][f"mascara_{nombre}.csv"] = escribir(
            f"mascara_{nombre}.csv", ["t", "p1", "p2", "p3", "p4"], filas)
    assert len({json.dumps(c) for c in generadas.values()}) == 4, "máscaras repetidas"

    sp, filas = corrida_k()
    manifiesto["archivos"]["comando_K.csv"] = escribir(
        "comando_K.csv", ["t", "sp"], [[t, v] for t, v in enumerate(sp)])
    manifiesto["archivos"]["mascara_K.csv"] = escribir(
        "mascara_K.csv", ["t", "p1", "p2", "p3", "p4"], filas)

    sp, filas, orden = corrida_nl(random.Random(SEMILLAS["NL"]))
    manifiesto["verificaciones"]["orden_NL"] = orden
    manifiesto["archivos"]["comando_NL.csv"] = escribir(
        "comando_NL.csv", ["t", "sp"], [[t, v] for t, v in enumerate(sp)])
    manifiesto["archivos"]["mascara_NL.csv"] = escribir(
        "mascara_NL.csv", ["t", "p1", "p2", "p3", "p4"], filas)

    sp, filas = corrida_p(filas_ps)
    assert COMANDO_MIN <= min(sp) and max(sp) <= COMANDO_MAX
    manifiesto["verificaciones"]["P"] = {
        "origen": DATOS_PS.name, "sha256_origen": hashlib.sha256(DATOS_PS.read_bytes()).hexdigest(),
        "tramo_s": [INICIO_P, INICIO_P + DURACION_P], "comando_min_L_h": min(sp),
        "comando_max_L_h": max(sp), "comando_medio_L_h": round(sum(sp) / len(sp), 1),
        "transiciones_mascara": (len(filas) - 2) // 2}
    manifiesto["archivos"]["comando_P.csv"] = escribir(
        "comando_P.csv", ["t", "sp"], [[t, v] for t, v in enumerate(sp)])
    manifiesto["archivos"]["mascara_P.csv"] = escribir(
        "mascara_P.csv", ["t", "p1", "p2", "p3", "p4"], filas)

    ruta = SALIDA / "manifiesto.json"
    ruta.write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifiesto["verificaciones"], ensure_ascii=False))


if __name__ == "__main__":
    main()
