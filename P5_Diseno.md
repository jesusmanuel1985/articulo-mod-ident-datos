# P5 — Diseño de experimento · Banco de emulación termosolar (Tesis Loreto Baima)

Entrada: E-set v1.1 (`P4_Evidencia.md`), J2.2 (`P3_Jerarquia.md`), C-set v1.6 (`P2_Claims.md`), H0 v1.1 y campaña base (`P0_H0_Tesis_Loreto.md`).
Metodología: `Metodologia-desarrollo-de-articulo-cientifico.md`, sección P5. **Modo A** (campaña principal).

**Estado: v1.5 CONGELADA — 2026-11-27. Reemplaza a la v1.4 (archivada en `P5_Diseno_v1.4.md`); versiones anteriores en `P5_Diseno_v1.3.md`, `P5_Diseno_v1.2.md`, `P5_Diseno_v1.1.md` y `P5_Diseno_v1.md`. Autor responsable: Jesús García.** Cualquier cambio posterior exige una nueva versión fechada antes de la corrida afectada; tras una corrida INV solo se admiten los cambios que permite la sección P5 de la metodología. **Ningún dato de la campaña puede adquirirse bajo una versión posterior a su fecha de aprobación (R10).** Las corridas P y PS son piloto: se rotulan como tales y no entran al E-set. K verifica, al inicio de cada día de campaña, la calibración de corriente en la que se apoya E8 y sí entra.

---

## 0. Máscaras de potencia y conflicto con la campaña base de P0

**Qué es una máscara de potencia.** Es la secuencia de encendido y apagado (0 ↔ 100 %) de cada una de las 4 resistencias durante una corrida: el patrón de nubes. Se guarda como un archivo con, para cada panel, los instantes de cambio. **A** se usa en las dos identificaciones; **B** y **C**, distintas entre sí y de A, en la validación.

**Conflicto con P0** — resuelto `[AUTOR, 2026-11-04]`

La tabla de campaña de P0 asigna **potencia PRBS 0/100 % por panel** a la rama de referencia y **máscara de nubes A** a la rama suave. En P4 se aceptó PA1: *misma máscara de nubes durante la identificación de ambas ramas*. Si las ramas reciben potencias distintas, la comparación mezcla dos diferencias (caudal y potencia) y C0 no aísla el efecto de la excitación de caudal.

**Decisión:** ambas ramas de identificación usan **la misma secuencia binaria de potencia (máscara A)**, reproducida desde el mismo archivo. Solo cambia el comando de caudal (suave frente a PRBS). La máscara A debe tener suficientes transiciones por panel para identificar las ganancias de potencia (ver §2.3).

---

## 1. Instrumentación y cadena de adquisición

| Elemento | Especificación | Fuente |
| --- | --- | --- |
| Plataforma | Banco de 4 colectores FP3.0E en serie (lab. FCI, UACh), ≈ 9.5 L de inventario; PLC LOGO!8; Raspberry Pi + tarjeta RTD | P0 |
| Variables manipuladas | Comando de caudal 200–400 L/h (lazo interno de caudal del banco); estado de las 4 resistencias 0/100 % | P0 |
| Variables medidas | T0–T4 con PT100 clase A; caudal (Flow3) con resolución 23.47 L/h; estado de resistencias (HR1–HR4); corriente de cada resistencia (§1.1); T ambiente (sensor existente: se registra para comparar condiciones entre corridas, E9 y V3; **no es entrada de los modelos**) `[AUTOR, 2026-11-04]` | P0 |
| Incertidumbre estática | PT100: ±0.15 °C; caudal: ≈ 1 % y resolución 23.47 L/h; potencia: ver §1.1 `[AUTOR, 2026-11-25]`. Multímetro **UNI-T UT89X** para R en frío (resolución 0.1 Ω); pinza **ANENG ST181** (no true RMS, resolución 0.01 A) solo para comparaciones relativas | P0, P4 |
| Muestreo | Ts ≈ 2.2 s (fs ≈ 0.45 Hz) | P0 |
| Nyquist (R6) | Canal caudal→T4: τ ≈ 233 s, t0 ≈ 62 s → ancho de banda ≈ 1/(2π·233) ≈ 0.0007 Hz. fs supera ese ancho de banda más de 600 veces | P0 |
| Filtro anti-aliasing | No aplica (dinámica mucho más lenta que fs); sin filtro en la tarjeta RTD, según el autor `[AUTOR, 2026-11-04]` | — |
| Conversión A/D | No se exige en bits: se declara la **resolución efectiva** observada en datos existentes del banco (menor salto de T y de caudal) | Datos de otros proyectos (solo lectura) |
| Almacenamiento | Datos crudos sin filtrar, un archivo por corrida con marca de tiempo, versión de P5 y rol de la corrida (piloto / identificación / validación / INV). CSV del sistema de adquisición actual (`run_18_Test_taken_at_…`) en `datos_campana/crudos/` `[AUTOR, 2026-11-04]` | — |

### 1.1 Potencia de las resistencias (E8) `[AUTOR, 2026-11-25]`

La potencia entra a los modelos medida en cada muestra, no como un valor nominal:

Q_i(t) = estado_i(t) · R_i · I_i(t)²

- **Por qué no un valor nominal.** Los reguladores de ángulo de fase siguen en el circuito: sin ellos, las 4 resistencias al 100 % sobrecargarían la red. La potencia de cada resistencia cae de 1.5–1.6 kW (sola) a 1.3–1.4 kW (las 4 encendidas) por la caída de tensión de la red, así que un P_nom constante erraría hasta en ≈ 19 %. Con corriente recortada, V·I es potencia aparente, y la pinza ANENG ST181 no es true RMS: no se usa para E8.
- **I_i(t):** transmisor de corriente (entrada AC 0–20 A, salida 0–10 V) con fuente de 24 V exclusiva y filtro RC (5.1 kΩ, 1000 µF, τ ≈ 5 s) hacia el LOGO. **Calibración vigente: 27-11-2026** `[AUTOR, 2026-11-27]`, contra los medidores DIN TYZHBOUL ZS-6035VAKW (los de R2 y R3 intercambiados desde el 25-11): I = (N − N0)/S, con S = 37.31 / 42.88 / 38.75 / 37.87 cuentas/A y N0 = 5.05 / 4.15 / 4.22 / 4.05 cuentas (R1 a R4); ajuste por mínimos cuadrados con el cero, la resistencia sola y las 4 encendidas; error RMS ≤ 0.044 A; linealidad ≤ 1.2 %. Datos: `diagnostico_corriente_cal_27-11.csv` y transcripción en `banco-control-identificacion` (commit `5b653b3`); resumen en `campana/calibracion_corriente_2026-11-27.csv`. Las sensibilidades difieren ≤ 1.9 % de la calibración del 24-11 (`C-digos-Sistema-de-Control/Diagnostico sensores corriente/CALIBRACION.md`, commit `1ab8ad0`): los transmisores son estables. Ruido en régimen σ ≤ 2.9 cuentas (≈ 0.08 A). El CSV de adquisición registra `Current sensor k` = N × 0.02, así que N se recupera sin cambiar el código. Válida solo con duty 0 o 100 % y con las perillas en su posición del 27-11.
- **Tensión de red.** Varía ≈ 4 % en menos de una hora (con todo apagado, 218–220 V a las 09:07 y 225–226 V a las 09:50 del 27-11) y la corriente la sigue. Por eso la validez de la calibración se comprueba contra los medidores DIN en el mismo momento (corrida K), no contra corrientes absolutas de otro día.
- **R_i:** resistencia en frío medida con el multímetro UNI-T UT89X el 2026-11-25 a 17.8 °C (resolución 0.1 Ω; puntas en corto 0 Ω): 17.2, 17.7, 17.6 y 17.6 Ω (R1 a R4; media de dos lecturas). Datos en `campana/resistencias_en_frio.csv`.
- **Retardo del filtro.** τ ≈ 5 s frente a ≈ 100 s de la dinámica térmica: despreciable. Multiplicar por estado_i anula la cola del filtro tras cada apagado.
- **Escala absoluta (límite L5).** Los medidores DIN no están certificados. Contraste de I²·R_i con sus kW: R1, R3 y R4 coinciden dentro de −4.5 % a +2.2 % (resolución del medidor, 0.1 kW). En el circuito de R2 los instrumentos discrepan, y la discrepancia sigue al circuito al intercambiar los medidores (`campana/pinza_R2_R3*.csv`): la corriente de R2 está entre 9.05 A (medidor) y 9.88 A (pinza), ≈ ±4.5 % en corriente y ≈ ±9 % en potencia. Un error de escala constante por resistencia lo absorbe la ganancia identificada g_i y es igual en todos los modelos, así que no afecta a C0, C1, C3 ni C7; solo a los valores absolutos de potencia que se informen.
- **Los medidores DIN** de R2 y R3 quedan intercambiados desde el 2026-11-25 (contraste de R2). No afecta a E8: los modelos usan la corriente de los transmisores, que no se movieron, y K compara cuentas del LOGO, no lecturas de los medidores. Ambos medidores leen lo mismo dentro de ≈ 1 % en cada circuito. Las lecturas de K y cualquier recalibración registran qué medidor está en cada circuito.

---

## 2. Protocolo de ejecución

### 2.1 Matriz de corridas

| Corrida | Rol | Comando de caudal | Potencia (binaria) | Duración | n |
| --- | --- | --- | --- | --- | --- |
| K | Verificación de la calibración de corriente (E8), al inicio de cada día de campaña `[AUTOR, 2026-11-27]` | Fijo 300 L/h | Apagadas 60 s; cada resistencia sola 60 s, con 60 s apagadas entre ellas; las 4 juntas 90 s; apagadas 60 s | 690 s más reposo | 1 por día |
| P | Piloto (no entra al E-set) | Prueba de las señales y del registro, más **dos repeticiones idénticas de un tramo de 2500 s de la PS réplica 1** (t = 1000–3500 s: comando que envió el PI y máscara PS en ese intervalo, distinta de A, B y C) `[AUTOR, 2026-11-27]` | Prueba | 2 × 2500 s (≈ 1.4 h) más reposo | 1 |
| IS | Identificación, rama suave | Señal suave (§2.2) | Máscara A | 6000 s | 1 |
| IP | Identificación, rama PRBS | PRBS de caudal (§2.2) | Máscara A (misma) | 6000 s | 1 |
| NL | No linealidad (C7, E10) `[AUTOR, 2026-11-04]` | Fijo en 200, 300 y 400 L/h, en orden sorteado | Las 4 resistencias a la vez: 0 → 100 → 0 %, mesetas de 1200 s | ≈ 3 h | 1 |
| PS | Registro de la secuencia PI (piloto, no entra al E-set) `[AUTOR, 2026-11-04]` | PI en lazo cerrado, salida limitada a 200–400 L/h; réplica 2 con consigna T4 = T inlet + 5.5 °C (T inlet: media de la ventana de reposo) `[AUTOR, 2026-11-27]` | Máscara PS (§2.3) | ≈ 7000 s | 2 (la 1 no apta para validación) |
| V1–V3 | Validación | Secuencia PI registrada en PS réplica 2 (t = 1000–7000 s), reproducida en lazo abierto | Máscara B | 6000 s | 3 |
| V4–V6 | Validación con 2.ª máscara `[AUTOR, 2026-11-03]` | La misma secuencia PI | Máscara C | 6000 s | 3 |

Subconjuntos declarados para la regla de desenlace "parcial": **las dos máscaras de validación, B y C**. La validación con 2 máscaras × 3 réplicas cambia la condición de prueba de H0: retorno PRE a P0, registrado.

**PS réplica 1 (2026-11-27), no apta para validación** `[AUTOR, 2026-11-27]`. Con consigna 31 °C, el PI pasó 46 % del tiempo en el mínimo de 200 L/h y nunca superó 300 L/h (T4 media 27.3 °C): con la máscara PS (≈ 2 resistencias encendidas en promedio) la consigna era inalcanzable. Su índice de calor medido es ≈ 1650 L/h·°C (ΔT ≈ 7.3 °C a ≈ 227 L/h), no los ≈ 3750 L/h·°C supuestos en §8. Con ese índice, un caudal medio de ≈ 300 L/h pide ΔT ≈ 5.5 °C, de ahí la consigna relativa de la réplica 2. La réplica 1 sí sirve para la piloto P, que solo exige entradas idénticas en sus dos repeticiones: `comando_P` y `mascara_P` salen de ella (`generar_senales.py`, con el hash del CSV de origen en el manifiesto).

La corrida NL recupera la corrida de no linealidad de P0, que había quedado fuera del C-set por un error de numeración (P0 la asignó a "premisa S1"; en P3 S1 pasó a ser la potencia). Ahora sostiene el claim C7 (retorno RTP a P2–P4, registrado). Las ganancias se calculan como ΔT4/ΔQ entre los promedios de los últimos 300 s de mesetas consecutivas.

**Corrida K** `[AUTOR, 2026-11-27]`. Se corre al inicio de cada día de campaña en que se ejecute una corrida del E-set (NL, IS, IP, VB, VC). Repite la secuencia de la calibración dentro del script de campaña. A los 25 s de cada etapa con resistencias encendidas, el script avisa en pantalla y el operador lee en voz alta V, A y kW de los medidores DIN encendidos; la grabación se transcribe junto al CSV. Para cada resistencia se calcula la corriente del transmisor (media desde los 25 s de la etapa, con la calibración vigente) en su etapa sola y en la etapa con las 4 encendidas, y se compara con la corriente del medidor DIN leída en esa misma etapa. **Criterio:** las 8 comparaciones dentro de **5 %**. Si alguna lo supera, se recalibra ese día (procedimiento de `CALIBRACION.md` §9, script `diagnostico_sensores_corriente.py`) y se repite K; ninguna corrida del E-set se ejecuta ese día hasta que K cumpla. K se rotula con réplica correlativa (3, 4, …) y se exceptúa de la regla de las 09:00 del horario, porque su criterio no depende de T inlet ni de T ambiente.

### 2.2 Señales de caudal

| Señal | Diseño | Por qué |
| --- | --- | --- |
| Suave (IS) | Niveles aleatorios en {200, 250, 300, 350, 400} L/h, unidos por rampas a **1.8 L/h·s** (margen bajo el tope de 2 L/h·s), con permanencias aleatorias de 300–900 s; cada salto entre niveles consecutivos ≥ 100 L/h | Cubre el mismo rango que la PRBS (PA1); permanencias del orden de τ–4τ para excitar la dinámica dominante |
| PRBS (IP) | Dos niveles 200 / 400 L/h, registro de 6 bits (63 bits), reloj de 90 s → periodo de 5670 s, repetido periódicamente hasta completar 6000 s (PA6), a la tasa del hardware (≈ 38 L/h·s) | Reloj ≈ 0.4 τ: concentra energía en la banda de la dinámica dominante; mismo rango que la suave |

Ambas señales se generan antes de la campaña con un script con semilla fija, que además verifica tasa, amplitud y tope (C2) y archiva los archivos de comando y de máscaras. El comando nunca supera 400 L/h (evita el windup de la válvula). El script se escribe tras congelar P5.

### 2.3 Máscaras de potencia

- **A (identificación, ambas ramas):** secuencia binaria por panel con permanencias aleatorias de 300–900 s, al menos **6** transiciones por panel en 6000 s `[AUTOR, 2026-11-04]`, paneles no sincronizados.
- **B (validación):** distinta de A, generada igual con otra semilla `[AUTOR, 2026-11-04]`.
- **C (validación):** distinta de A y de B, generada igual con una tercera semilla.
- **PS (registro de la secuencia PI):** distinta de A, B y C, generada igual con una cuarta semilla, para ≈ 7000 s.
- **Por qué no se reutiliza la nube actual:** la tabla `fast_cloud_data` de `main_control_rec.py` dura ≈ 1190 s y no es binaria. El script exporta cada máscara en ese mismo formato [t, p1, p2, p3, p4], con dos filas por transición separadas por un intervalo mínimo (la interpolación lineal del código no debe crear rampas) y cubriendo toda la corrida.

### 2.4 Secuencia y reposo

- **Orden:** K, PS réplica 1 y P, en ese orden (después, K al inicio de cada día de campaña, §2.1), porque el comando de P es un tramo de la PS réplica 1. P termina y n_rep queda fijado antes de IS e IP. La PS réplica 2 se corre cualquier día antes de la primera validación. IS e IP el mismo día, en orden sorteado y registrado. Validación en los días siguientes, consecutivos, **alternando máscaras y horarios** para que ni el día ni la hora coincidan con una máscara: día 1 B y C; día 2 C y B; día 3 B y C (con n_rep = 5, día 4 C y B; día 5 B y C). NL en cualquier día, tras K.
- **Horario** `[AUTOR, 2026-11-04]`: dos turnos por jornada, inicio de corrida a las **09:00** y a las **11:30** (reposo previo incluido antes de esa hora), con un margen de ± 30 min. Ninguna corrida del E-set parte antes de las 09:00, salvo K (§2.1). En IS e IP, el sorteo asigna la rama a cada turno. Motivo, según los ensayos de octubre y noviembre de 2026: antes de las 09:00 T inlet sube ≈ 1 °C en ≈ 1.5 h (16.6 → 17.6 °C el 3-nov), lo que agotaría la tolerancia de T0 entre IS e IP; en los ensayos iniciados cerca de las 09:00 varía ≈ 0.1 °C, y en el del 30-oct a las 12:24 bajó ≈ 0.6 °C. V3 controla igual la diferencia entre IS e IP. T ambiente sube ≈ 2 °C entre las 08:00 y las 15:00.
- **Reposo y transitorio:** antes de cada corrida, banco a 300 L/h con todas las resistencias en el estado inicial de la máscara hasta que la pendiente de T4, ajustada por mínimos cuadrados sobre los últimos 300 s, tenga valor absoluto < 0.05 °C/min. La derivada muestra a muestra no se usa porque el ruido del sensor la vuelve inservible. La corrida parte en forma automática al cumplirse el criterio, así que el script se lanza con antelación al turno. En PS, el PI se mantiene en 300 L/h durante el reposo para arrancar sin salto; luego su salida se limita a 200–400 L/h con anti-windup. Los primeros **900 s** (≈ 4τ) de cada corrida se descartan en el análisis.
- **Paso del reposo al comando:** el caudal pasa de 300 L/h al primer valor del archivo en t = 0, lo que puede ser un escalón (en IS, 300 → 250 L/h). Cae dentro de los 900 s descartados y C2 se verifica sobre el archivo de comando.

### 2.5 Réplicas: justificación (R3)

- n_rep = 3 en validación (fijado en H0).
- Ambos modelos predicen **la misma T4 medida** en cada réplica, así que la variación entre réplicas afecta a los dos RMSE de forma parecida: la diferencia RMSE_suave − RMSE_PRBS varía menos que cada RMSE por separado.
- Cota pesimista disponible: RMSE entre trayectorias de réplicas PI de octubre (lazo cerrado) 0.65–1.09 °C. En lazo abierto con entradas idénticas se espera menos.
- La incertidumbre de la media de la diferencia es σ_d/√n_rep; con n_rep = 3, σ_d/√3. El margen efectivo mínimo es 0.5 °C; se exige σ_d ≤ margen/2 (E2), lo que da una incertidumbre de la media ≤ 0.14 °C, menor que el efecto. **Esta justificación depende de σ_d, que no se conoce antes de medir.** Si E2 falla, el desenlace es "no concluyente", no NEG.
- **Piloto para revisar n_rep** `[AUTOR, 2026-11-03]`: la piloto no puede medir σ_d (aún no hay modelos), pero sí la repetibilidad de T4 con entradas idénticas (σ_T4, RMSE entre las dos repeticiones del tramo). Definición: σ_T4 = RMSE(T4_rep1 − T4_rep2)/√2 sobre el tramo, tras sus primeros 900 s (quedan 1600 s). Regla propuesta: si σ_T4 > 0.25 °C (la mitad del margen mínimo de 0.5 °C), n_rep sube a 5 por máscara `[AUTOR, 2026-11-04]`. La regla queda fijada en la versión congelada; la piloto se corre después de PS y solo la aplica, sin nueva congelación. El valor de σ_T4 y el n_rep resultante se registran antes de la primera corrida de identificación `[AUTOR, 2026-11-04: opción a]`. La piloto no entra al E-set.

---

## 3. Exclusiones objetivas

| Regla de descarte | Detalle |
| --- | --- |
| Transitorio inicial | Primeros 900 s de cada corrida |
| Fallo de sensor | Muestra con T fuera de 0–100 °C, caudal fuera de 0–500 L/h, corriente fuera de 0–20 A, o valor faltante |
| Saturación | Muestras con comando > 400 L/h o caudal medido > 420 L/h |
| **Umbral a INV** | Si se descarta más del **5 %** de las muestras de una corrida (sin contar el transitorio), la corrida completa es INV `[AUTOR, 2026-11-04]` |

No se excluye ninguna réplica de validación por su resultado (P4).

---

## 4. Compuertas de validez (disparan INV en P6) `[AUTOR, 2026-11-04]`

| Compuerta | Criterio propuesto |
| --- | --- |
| V1 Integridad física | Pérdida de muestras > 2 %; cualquier PT100 saturado o fuera de rango; comando fuera del archivo programado en más de 1 muestra seguida; T1–T4 ≥ 48 °C, que además corta la corrida en forma automática porque en lazo abierto nada reduce la temperatura |
| V2 Estabilidad | Antes de iniciar: pendiente de T4 (mínimos cuadrados, 300 s previos) con valor absoluto ≥ 0.05 °C/min |
| V3 Paridad en línea | Ver §6 (diferencias de T ambiente y T0 entre IS e IP fuera de tolerancia). Corridas de validación: T ambiente media dentro de ± **5 °C** de la media de IS e IP; si no, INV y se repite |
| V4 Exclusión excesiva | Descarte > 5 % (§3) |
| **V5 Calidad de la referencia** (criterio ii de P0, E4) | En la validación, el modelo bilineal-PRBS a 1000 s **no supera a la persistencia**, **o** su FIT_H = 1 − RMSE_H / std(T4) es **< 50 %** (equivale a r²_H < 0.75 y a RMSE_H > 0.5·std(T4)) → la identificación es INV y se repite `[AUTOR, 2026-11-04]`. El IAE se informa, pero no sirve como compuerta: depende de la escala y de la duración |

---

## 5. Plan de análisis y regla de desenlace

### 5.0 Construcción de los modelos

**Cuándo.** Tras adquirir IS e IP se estiman los tres modelos (bilineal-suave, bilineal-PRBS, FOPDT-PRBS) y se **congelan** (parámetros, código y hash) **antes de abrir los datos de validación**. Se registra la fecha de congelación. Ningún modelo se reajusta después de ver la validación.

**Estructura bilineal** (balance por etapa de P0), en **variables absolutas** (temperaturas en °C y caudal real, sin punto de operación) `[AUTOR, 2026-11-04]`: para i = 1…4,
C_i·dT_i/dt = ṁ·cp·(T_{i−1} − T_i) + g_i·Q_i − h_i·(T_i − T_amb),
con ṁ el caudal medido, cp del agua conocido, Q_i(t) = estado_i(t)·R_i·I_i(t)² medida (E8, §1.1) y T_0 medida.
Parámetros por etapa: **C_i** (capacidad térmica, que pondera el término ṁ·cp), **g_i** (ganancia de potencia) y **h_i** (pérdidas). **Retardo de transporte: sin retardo entre etapas, con un retardo global** `[AUTOR, 2026-11-04]`. Es un retardo constante d, el mismo para todas las entradas (caudal medido, T0 y potencias): las ecuaciones se alimentan con u(t − d). En un sistema invariante en el tiempo equivale a retrasar la salida, y en MPC discreto suma d/Ts estados de retardo. d se estima en cada rama por búsqueda en grilla 0–200 s cada Ts, con el mismo procedimiento en ambas (PA3); los demás parámetros se estiman para cada d de la grilla y se queda el de menor costo. En la métrica (§5.1) se usan las entradas medidas desde t − d. **T ambiente no entra como variable:** en el término de pérdidas, T_amb es una constante estimada junto con los demás parámetros, igual en ambas ramas `[AUTOR, 2026-11-04]`.

**Estimación.** Minimización del error de simulación libre de T1–T4 sobre todo el registro útil (tras 900 s), con parámetros positivos y acotados, integración con paso Ts, 10 puntos de partida aleatorios con semilla fija; se queda el de menor costo. Idéntico en ambas ramas (PA3).

**Incertidumbre de parámetros (C3).** **Bootstrap por bloques** `[AUTOR, 2026-11-04]`: el registro útil se parte en bloques de 1000 s; cada bloque se simula desde las temperaturas medidas en su inicio; se remuestrean bloques con reposición (200 remuestreos) y se reestima partiendo del óptimo. Intervalo al 95 % por percentiles. C3 compara los **C_i** entre ramas.

**FOPDT (C1).** T4 = suma de 5 canales de primer orden con retardo (caudal medido y 4 potencias), en **variables de desviación** respecto de un punto de operación calculado **solo con los datos de IP** (medias tras los primeros 900 s) y mantenido igual en la validación `[AUTOR, 2026-11-04]`; ganancias y constantes estimadas con el mismo criterio de error de simulación; retardos por búsqueda en grilla 0–200 s cada Ts.


### 5.1 Métrica (E1, E3, E7)

- Para cada instante t de la ventana de evaluación (tras el transitorio y hasta el final de la corrida menos H): se predice T4(t + 1000 s) con las entradas medidas (caudal medido y potencia medida Q_i de E8, §1.1) y se compara con la medición.
- **Bilineal:** se inicializa con las temperaturas medidas en t y se simula 1000 s.
- **FOPDT:** sus estados internos no se miden; se simula de forma continua en toda la corrida, con salida y, y se ancla al valor medido: T̂4(t + H) = T4(t) + [y(t + H) − y(t)] `[AUTOR, 2026-11-04]`. Ambos modelos parten así del T4 medido en t (PA2 de C1).
- RMSE_H = raíz del promedio de los errores al cuadrado sobre todos los t de la ventana, por réplica.
- Agregación: media de RMSE_H sobre las n_rep réplicas de cada máscara, por modelo.
- E7: el mismo cálculo, separando los t según el caudal medido promedio en [t, t + H] en los tramos 200–267, 267–333 y 333–400 L/h.

### 5.2 Incertidumbre

Por máscara, con d_j = RMSE_H,j(suave) − RMSE_H,j(PRBS) en la réplica j, d̄ su media y σ_d su desviación estándar muestral:

- **Tipo A (entre réplicas):** u_A = σ_d/√n_rep.
- **Tipo B (PT100):** u_T = 0.15/√3 = 0.087 °C (distribución rectangular). Un sesgo común b de T4 cambia cada RMSE según ∂RMSE/∂b = ē/RMSE, con ē el error medio; como ambos modelos usan la misma medición, u_B = |ē_s/R_s − ē_p/R_p|·u_T, con cota u_B ≤ 2·u_T = 0.17 °C. El ruido aleatorio del sensor ya está en σ_d.
- **Combinada (ley de propagación de la GUM, primer orden):** u_comb = √(u_A² + u_B²).

**Justificación de réplicas (R3).** Con σ_d en su tope admitido (0.25 °C) y u_B en su cota, u_comb(3) = 0.23 °C y u_comb(5) = 0.21 °C, ambos menores que el efecto mínimo de 0.5 °C. σ_d real solo se conoce al medir; E2 lo controla.

### 5.3 Regla de desenlace de C0 (exhaustiva) `[AUTOR, 2026-11-04]`

Por máscara: R_p = RMSE_H(PRBS) medio, R_s = RMSE_H(suave) medio, M = máx(1.5·R_p, R_p + 0.5 °C), m = M − R_p, d̄ = R_s − R_p, y σ_d y u_comb de §5.2.

| Orden | Condición, por máscara | Desenlace de la máscara |
| --- | --- | --- |
| 0 | Falla V5 (referencia mala) | INV de la identificación (no es desenlace de C0) |
| 1 | σ_d > m/2 | No concluyente |
| 2 | σ_d ≤ m/2 y d̄ + u_comb ≤ m | Sostenido |
| 3 | σ_d ≤ m/2 y d̄ − u_comb > m | Refutado (NEG) |
| 4 | σ_d ≤ m/2, d̄ + u_comb > m y d̄ − u_comb ≤ m | No concluyente (banda intermedia) |

| Máscara B | Máscara C | Desenlace de C0 |
| --- | --- | --- |
| Sostenido | Sostenido | **Sostenido** |
| NEG | NEG | **NEG** |
| Sostenido | NEG o no concluyente (o al revés) | **PAR**, acotado a la máscara que se sostiene |
| NEG | No concluyente (o al revés) | **No concluyente** |
| No concluyente | No concluyente | **No concluyente** |

### 5.4 Reglas de los demás claims

| Claim | Sostenido | No sostenido |
| --- | --- | --- |
| C1 (B) `[AUTOR, 2026-11-04]` | Por máscara, con d₁ = RMSE_H(bilineal) − RMSE_H(FOPDT) y u_comb como en §5.2: d₁ + u_comb < 0 | NEG si d₁ − u_comb ≥ 0; no concluyente en la banda intermedia. Combinación de máscaras: la misma tabla de C0 |
| C2 (A) | Tasa máx. del comando ≤ 2 L/h·s, saltos ≥ 100 L/h, máximo ≤ 400 L/h | Cualquier violación (se verifica antes de correr: es el archivo de comando) |
| C3 (C, exploratorio) | Intervalos al 95 % de los parámetros del término ṁ·cp (los C_i, §5.0) de ambas ramas se solapan | No se solapan |
| C4 (C, exploratorio) | RMSE_H de la rama suave en 200–267 L/h mayor que en 333–400 L/h | Igual o menor |
| C7 (A) `[AUTOR, 2026-11-04]` | K(200)/K(400) ≥ 1.5 y K decreciente en 200 → 300 → 400 L/h | Cociente < 1.5 o K no decreciente; si el intervalo del cociente contiene 1.5, no concluyente |

---

## 6. Operacionalización de la paridad `[AUTOR, 2026-11-04]`

| PA | Implementación | Tolerancia |
| --- | --- | --- |
| PA1 C0 | Misma máscara A (mismo archivo) en IS e IP; mismo rango 200–400 L/h; IS e IP el mismo día | T ambiente media: |IS − IP| ≤ 3 °C; T0 al inicio: ≤ 1 °C |
| PA2 C0 | Mismo script de adquisición; caudal medido **sin filtrar** en ambas ramas (o el mismo filtro, declarado aquí); misma conversión de corriente a potencia (E8: calibración y R_i de §1.1) | Identidad (mismo código y parámetros) |
| PA3 C0 | Mismo código de estimación (hash registrado), misma estructura, inicialización y criterio de parada; minimización del error de simulación | Identidad |
| PA5 C0 | Mismo script de métricas, mismas ventanas y descarte de 900 s | Identidad |
| PA6 C0 | IS e IP de igual duración | Número de muestras útiles: diferencia ≤ 1 % |
| PA2 C1 | FOPDT multientrada: caudal medido + 4 potencias, con retardo por canal | Identidad de entradas |
| PA3 C1 | Retardos buscados en una grilla declarada (p. ej., 0–200 s cada Ts), constantes y ganancias estimadas con el mismo criterio que el bilineal | Identidad de criterio |
| PA1, PA5, PA6 C1 | Mismos datos IP, mismas ventanas y réplicas | Identidad |

---

## 7. Presupuesto y reintentos

| Campo | Valor |
| --- | --- |
| Presupuesto modo A | K + P + PS + NL + IS + IP + V1–V6: 8 corridas de 6000 s + PS (≈ 2 h) + NL (≈ 3 h) + caracterización y piloto + K diaria (≈ 30 min con reposo) → **≈ 5–6 jornadas** `[AUTOR, 2026-11-03: 2 máscaras]` |
| Restricción de H0 | Respetada: potencia solo binaria; comando ≤ 400 L/h |
| N máx. de reintentos | **1** por corrida planificada `[AUTOR, 2026-11-04]` |
| Al agotar N | NOB a P4 |
| Límite de factibilidad (rescate) | v1, 2026-11-02: ≈ 4 ensayos de 6000 s + 10 h de análisis (no se usa en modo A salvo retorno desde P6) |

---

## 8. Decisiones del autor para congelar P5

Congelaciones de la v1, la v1.1 y la v1.2 autorizadas y efectuadas por el autor el 2026-11-04. v1.3 congelada por el autor el 2026-11-25 (potencia medida, umbral de 5 %). v1.4 congelada por el autor el 2026-11-27 (K diaria contra los medidores, sin V6, calibración del 27-11). v1.5 congelada por el autor el 2026-11-27 (P desde la PS réplica 1; PS réplica 2 con consigna relativa).

**Revisión de las secuencias PI existentes (2026-11-04).** Cinco ensayos PI (oct–nov y marzo 2026), con consigna T4 = 35 °C en los de octubre, tras los primeros 900 s: duran ≈ 4200–4540 s (se exigen 6000 s); comando entre 100 y ≈ 280 L/h; entre 38 % y 94 % del tiempo bajo 200 L/h, fuera del rango de H0. Tampoco son binarias: el ciclo de trabajo toma valores intermedios. Con T0 ≈ 18.5 °C y un índice de calor ≈ 3750 L/h·°C, un caudal medio de 300 L/h corresponde a una consigna T4 ≈ 31 °C. **Corrección (2026-11-27):** ese índice venía de ensayos con las resistencias casi siempre encendidas; con la máscara PS el índice medido es ≈ 1650 L/h·°C, y la consigna de 31 °C resultó inalcanzable (§2.1, PS réplica 1).

## Historial

| Versión | Fecha | Cambio | Motivo |
| --- | --- | --- | --- |
| v0 | 2026-11-03 | Borrador completo | Inicio de P5 |
| v0.1 | 2026-11-03 | Explicación de máscaras; 2 máscaras de validación (PAR habilitado; retorno PRE a P0); construcción de los modelos (§5.0); piloto con repeticiones para revisar n_rep; V5 relativo; resolución efectiva en vez de bits | Respuestas del autor |
| v0.2 | 2026-11-04 | Misma máscara A en IS e IP; T ambiente registrada, no usada como entrada; V5 expresado como FIT_H; definición de σ_T4; propuesta sin retardo; corrida de no linealidad señalada como omisión de P2/P3 | Respuestas del autor |
| v0.3 | 2026-11-04 | V5 FIT_H ≥ 50 %; bootstrap por bloques; corrida NL y regla de C7; validación alternando máscaras; tolerancia de T ambiente en validación (V3) | Decisiones del autor |
| v0.4 | 2026-11-04 | Confirmados: sin retardo, umbral de la piloto, compuertas V1–V4 con ±5 °C, INV 5 %, N = 1, paridad; pinza ANENG ST181 y multímetro UNI-T UT89X | Decisiones del autor |
| v0.5 | 2026-11-04 | Retardo global constante (sin retardo entre etapas); C7 tipo A con umbral 1.5 confirmado. Sin pendientes | Decisiones del autor |
| v0.6 | 2026-11-04 | La piloto aplica la regla de n_rep fijada en la versión congelada (antes decía "antes de congelar") | Inconsistencia con §2.4; opción a del autor |
| v0.7 | 2026-11-04 | Bilineal en variables absolutas; FOPDT en desviación con punto de operación de IP; inicialización anclada del FOPDT en la métrica (sin ella, RMSE_H no estaba definido para C1). Sin pendientes | Decisiones del autor |
| v0.8 | 2026-11-04 | Fórmula u_comb (GUM) y justificación numérica de n_rep; entradas y máscara C actualizadas; congelación retenida por puntos abiertos en R1 y R12, listados en §8 | Revisión previa a congelar |
| v0.9 | 2026-11-04 | Regla de C0 con u_comb y tabla de combinación; C1 por máscara; máscara A ≥ 6 transiciones; máscara B con semilla; exactitud de pinza y multímetro; sin filtro RTD; las secuencias PI registradas no cumplen H0: propuesta de corrida PS | Decisiones del autor y revisión de datos |
| v0.10 | 2026-11-04 | Máscara PS generada por el script; exportación al formato de `fast_cloud_data`; la nube actual (≈ 1190 s, no binaria) no se reutiliza | Observación del autor |
| v0.11 | 2026-11-04 | Corrida PS aprobada; propuesta de horario de corridas y alternancia de máscaras por turno | Pregunta del autor y datos de T inlet y T ambiente |
| **v1** | 2026-11-04 | Horario 09:00 y 11:30; datos crudos en `datos_campana/crudos/`; agregación por n_rep; PRBS periódica hasta 6000 s. **P5 congelada** | Decisión del autor |
| **v1.1** | 2026-11-04 | Orden K → PS → P; tramo de P de 2500 s (1600 s útiles para σ_T4); criterio de reposo por regresión sobre 300 s; corte a 48 °C (V1); arranque de PS sin salto; escalón de t = 0 declarado; V e I de K anotadas a mano; C3 precisa que los parámetros son los C_i; K entra al E-set por E8. **P5 congelada**, antes de adquirir datos. Código de campaña: commit `75690ba` de `banco-control-identificacion` | Revisión del código de campaña; decisión del autor sobre P |
| **v1.2** | 2026-11-04 | ±0.1 A y ±0.1 V no eran exactitud: resolución 0.01 A y 0.1 V; exactitud nominal de fuentes secundarias, por confirmar en los manuales; rango anotado en K. **P5 congelada**, antes de adquirir datos | Corrección del autor |
| **v1.3** | 2026-11-25 | Potencia medida en cada muestra, Q_i = estado_i·R_i·I_i² (§1.1), con transmisores calibrados el 24-11 y R en frío; K pasa a verificar la calibración (690 s, sin la etapa al 50 %) con umbral de 5 %; nueva compuerta V6 (5 % en corriente); fallo de sensor incluye la corriente; pinza solo para comparaciones relativas. Retorno RTP a P2–P4 (L5, S1, E8). Medidores DIN de R2 y R3 intercambiados, sin efecto en E8. **P5 congelada**, antes de adquirir datos | Reguladores de fase, pinza no true RMS, perillas no aseguradas y caída de tensión de red; decisión del autor |
| **v1.4** | 2026-11-27 | K al inicio de cada día de campaña, con criterio transmisor frente a medidor DIN (≤ 5 %) y exenta de la regla de las 09:00; se elimina la compuerta V6; calibración vigente del 27-11. Cambios motivados por los datos de K (réplicas 1 y 2) y de la calibración del 27-11: la tensión de red varía ≈ 4 % en una hora y el criterio de la v1.3 (cuentas absolutas frente al 24-11) fallaba sin falla de los sensores. Ninguna corrida del E-set se había ejecutado ni evaluado. K réplica 1: fuente de los transmisores a 32 V y canal de R1 defectuoso (INV, causa física corregida); K réplica 2: criterio de la v1.3 no cumplido (−8 a −10 %, tensión de red baja), por lo que se recalibró según la v1.3. **P5 congelada** | Decisión del autor |
| **v1.5** | 2026-11-27 | P sale de la PS réplica 1 (t = 1000–3500 s; antes, "tramo de la validación"); PS réplica 2 con consigna T inlet + 5.5 °C para generar `comando_V`; corrección del índice de calor de §8. Corridas del E-set aún no ejecutadas. **P5 congelada** | PS réplica 1 no apta para validación: consigna de 31 °C inalcanzable con la máscara PS (error de diseño en §8); decisión del autor |
