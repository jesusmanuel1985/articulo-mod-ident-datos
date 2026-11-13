# P0 — Pregunta motriz e hipótesis · Banco de emulación termosolar (Tesis Loreto Baima)

Fuentes: `Tesis_Loreto_Baima_v2/main.tex`, idea motriz y decisiones del autor (2026-11-02), y consulta en solo lectura de `C-digos-Sistema-de-Control` y `paper-banco-prueba2026`.
Metodología: `Metodologia-desarrollo-de-articulo-cientifico.md`, sección P0.

**Estado: H0 v1 — P0 cerrada el 2026-11-02; sigue P1.** Los campos no delegables pendientes llevan `[DECIDE AUTOR]`. Los que ya decidió el autor llevan `[AUTOR, 2026-11-02]`.

## Idea motriz (entrada)

1. Obtener modelos **fiables** a partir de datos y que se puedan **usar directamente en MPC**.
2. Lograrlo **sin hacer oscilar el proceso**: excitar el caudal (la variable manipulada) de forma suave.
3. El sistema parece **no lineal cuando se combinan la potencia y el caudal másico**.
4. La **potencia representa las nubes**: en una planta real no se manipula y sus cambios son bruscos. En el banco se aplica solo como transiciones binarias 0 ↔ 100 %.

**Integración en una sola H0 (R8).** La pregunta compara formas de excitar el caudal (punto 2). El observable es el error de predicción al horizonte del MPC (punto 1). El mecanismo es la estructura bilineal ṁ·cp·(T_{i−1} − T_i) del balance por etapa (punto 3). La potencia entra como perturbación medida y binaria en todos los ensayos (punto 4). La no linealidad pasa a P2/P3 como premisa S1 con su propio ensayo.

---

```text
FASE P0 — Pregunta motriz e hipótesis
Propósito ............ fijar, antes de la evidencia, qué se pregunta, qué se espera
                       y qué resultado lo refutaría

ENTRADA
  Idea difusa ......... ver "Idea motriz"
  Modo ................ A: campaña nueva completa en el banco    [AUTOR, 2026-11-02]
                        (referencia, rama suave y validación se adquieren en la
                        misma campaña; H0 confirmatoria por construcción)

SALIDA CANÓNICA ...... H0 · v1 · 2026-11-02
```

### Formulario H0

```text
PREGUNTA
  Tipo .................. desempeño
  Sistema ............... Modelo bilineal de bajo orden del banco de 4 colectores FP3.0E
                          en serie (lab. FCI, UACh): balance por etapa
                          m_i·cp·dT_i/dt = ṁ·cp·(T_{i−1} − T_i) + Q_i, con parámetros
                          identificados; entradas: comando de caudal (manipulada) y
                          ciclo de trabajo de las 4 resistencias (perturbación medida);
                          salida: T4 (PT100, salida del 4.º colector)
  Observable ............ T4 predicha a H pasos [°C], promediada sobre las réplicas del
                          ensayo de validación
                          H = 1000 s ≈ t0 + 4τ del canal caudal→T4
                                                                 [AUTOR, 2026-11-02]
  Criterio .............. No inferioridad con margen híbrido:
                          RMSE_H(suave) ≤ máx(1.5·RMSE_H(abrupta),
                                              RMSE_H(abrupta) + 0.5 °C)
                          (rige el piso de 0.5 °C mientras RMSE_H(abrupta) < 1 °C;
                          sobre 1 °C rige el factor 1.5)     [AUTOR, 2026-11-02]
  Referencia ............ El mismo modelo bilineal identificado con excitación abrupta:
                          PRBS en el comando de caudal, a la tasa máxima del hardware
                          (≈ 38 L/h·s medidos)
  Condición de prueba ... Ensayo de validación nuevo con 2 máscaras de nubes binarias
                          por panel (B y C), DISTINTAS entre sí y de la usada para
                          identificar; cada máscara repetida 3 veces con entradas
                          idénticas: comando de caudal en lazo abierto, que reproduce
                          una secuencia de operación PI.     [v1.1, AUTOR, 2026-11-03] Comando
                          200–400 L/h; Ts ≈ 2.2 s
  Restricción ........... Potencia solo binaria 0 ↔ 100 %CO por resistencia en todos los
                          ensayos, porque representa nubes no manipulables
                                                                 [AUTOR, 2026-11-02]
                          Excitación suave = comando de caudal con tasa ≤ 2 L/h·s (la
                          máxima que produce el PI en operación normal), amplitud
                          ≥ 100 L/h (≥ 4 escalones de resolución del caudalímetro)
                          y comando ≤ 400 L/h (sobre ≈ 420 L/h la válvula satura)

  Frase: ¿El modelo bilineal de bajo orden del banco de emulación termosolar,
         identificado con un comando de caudal limitado a 2 L/h·s, predice T4 a
         1000 s con un RMSE no mayor que 1.5 veces (y como mínimo 0.5 °C por
         encima de) el del mismo modelo identificado con PRBS de caudal, en un ensayo de validación de operación con
         2 máscaras de nubes binarias, cada una repetida 3 veces, dado que la potencia solo cambia 0 ↔ 100 %?

HIPÓTESIS ............... Sí, porque el modelo tiene pocos parámetros físicos (inercia
                          térmica por etapa, ganancia de potencia, término ṁ·cp) y su
                          dinámica dominante es lenta (FOPDT equivalente caudal→T4:
                          τ ≈ 233 s, t0 ≈ 62 s). Un comando de caudal a ≤ 2 L/h·s con
                          ±100 L/h concentra energía bajo ≈ 0.003 Hz, donde están esas
                          constantes. Las transiciones binarias de potencia, presentes
                          en ambas ramas, bastan para identificar la ganancia de Q_i y
                          su interacción con ṁ.
REFUTACIÓN .............. H0 es falsa si, en ambas máscaras y promediando las 3 réplicas
                          de cada una, RMSE_H(suave) > máx(1.5·RMSE_H(abrupta),
                          RMSE_H(abrupta) + 0.5 °C). Si ocurre en una sola máscara, el
                          resultado es parcial.                         [v1.1]

CONSECUENCIA
  Si se confirma: el modelo de predicción del MPC del banco (y de plantas donde no se
                  puede hacer oscilar el proceso) se obtiene con maniobras de caudal
                  tan suaves como la operación normal, aprovechando las nubes como
                  única excitación brusca.
  Si se refuta:   se aprende que la operación suave no aporta información suficiente
                  para el término bilineal al horizonte del MPC, y se cuantifica en °C
                  cuánto se pierde frente a excitar con PRBS.

TRIVIALIDAD — Dirección
  Predictor 1 ........... Autor: Jesús García (registro textual)
    Respuesta predicha .. sí, el modelo puede cumplir con el criterio
    Confianza ........... baja
    Tipo de motivación .. física                              [AUTOR, 2026-11-02]
                          (antes: evidencia previa, "los modelos basados en paso
                          escalón FOPDT han mostrado su aplicabilidad en muchos tipos
                          de sistemas térmicos"; cambiado porque no había R# en la
                          ficha)
    Motivación .......... "Aunque considero que sí lo pueden hacer, este tipo de modelos
                          suaves podría estar trabajando en regiones del proceso para el
                          cual no fue diseñado, por ejemplo, si se crea usando un caudal
                          alto, la ganancia obtenida puede ser pequeña, pero si el caudal
                          es alto la ganancia puede ser muy alta. Esto da una no
                          linealidad tremenda al proceso."
                          [aclaración del autor, 2026-11-02: la segunda mención
                          de "caudal alto" significa "caudal bajo"; texto original
                          sin modificar]
    Quién / cuándo ...... Jesús García · 2026-11-02 · H0 borrador
  Predictor 2 ........... IA (Claude Opus 5.5), segundo predictor; no reemplaza al autor
    Respuesta predicha .. sí
    Confianza ........... media
    Tipo de motivación .. física
    Motivación .......... Pocos parámetros y dinámica lenta. Riesgo: con un caudal suave,
                          la información del término ṁ·T viene casi solo de las nubes,
                          y si la potencia real no se mide bien, ese término queda mal
                          identificado.
    Quién / cuándo ...... IA · 2026-11-02 · H0 borrador

TRIVIALIDAD — Magnitud  (obligatoria solo si alguna confianza de dirección es alta)
  Valor predicho ........ —                                     [DECIDE AUTOR si alta]

MEDIBILIDAD
  Fuente del observable . PT100 clase A ±0.15 °C (Raspberry Pi + tarjeta RTD); caudal
                          medido con resolución de 23.47 L/h y ≈ 1 % de exactitud
  Incertidumbre esperada vs efecto
    Sensor .............. ±0.15 °C, que se cancela en la diferencia de RMSE.
    Repetibilidad ....... Indicador obtenido con las réplicas de octubre 2026 (mismo
                          perfil de nubes, lazo cerrado): RMSE entre trayectorias de T4
                          de 0.65–1.09 °C entre réplicas PI y 1.6–2.4 °C entre réplicas
                          PI+FF. Es una cota pesimista: en lazo cerrado los caudales
                          difieren entre réplicas, y la validación propuesta usa
                          entradas idénticas.
    Efecto .............. Margen efectivo ≥ 0.5 °C por construcción (piso). Supera la
                          exactitud del sensor (±0.15 °C) más de 3 veces. Se espera que
                          supere la dispersión entre réplicas en lazo abierto, que
                          debería quedar bajo la de las réplicas PI en lazo cerrado.
                          Las 3 réplicas de validación lo confirman.
    Pendiente para P5 ... Criterios de validez:
                          (i) si σ de la diferencia de RMSE entre réplicas > margen/2
                              → no concluyente (no NEG);
                          (ii) la referencia debe alcanzar una calidad mínima (umbral
                               a fijar en P5 antes de adquirir); si no, el ensayo es
                               inválido (INV) y se repite. Esto evita que una
                               referencia mala vuelva generoso el factor 1.5.
                               Propuesta: a 1000 s, la referencia debe superar al
                               predictor de persistencia (T4(t+H) = T4(t)) y tener
                               un RMSE_H ≤ ___ °C. En P3 entra como premisa S2:
                               "el modelo bilineal identificado con PRBS predice T4
                               adecuadamente a 1000 s".
    Potencia ............ Se mide con pinza amperimétrica      [AUTOR, 2026-11-02]
                          (los sensores instalados quedan fuera de alcance).
                          Como la potencia es binaria, Q_i(t) = estado_i(t) · P_nom,i:
                          el estado se registra (duty cycle HR1–HR4) y P_nom,i se
                          obtiene con la pinza (I) y un multímetro (V), P = V·I, por
                          resistencia, al inicio y al final de cada ensayo. Control
                          cruzado: balance ṁ·cp·ΔT en las mesetas al 100 %. La deriva
                          dentro de un ensayo queda sin medir; se acota con la
                          diferencia inicio–fin.

FICHA DE NOVEDAD PROVISIONAL  (cada R# debe verificarse en fuente primaria)
  R1  Rivera, Lee, Mittelmann & Braun (2009), J. Process Control 19(4):623–635,
      10.1016/j.jprocont.2008.08.006 — excitación "plant-friendly" con restricciones (D1).
  R2  Machado et al. (2023), Applied Energy 339:120944, 10.1016/j.apenergy.2023.120944 —
      modelo identificado con operación normal de un campo solar, validado en 6 días
      (D2–D4), sin comparar con PRBS.
  R3  Mechhoud & Belkhatir (2024), J. Process Control 143:103321,
      10.1016/j.jprocont.2024.103321 — modelo bilineal de colector con caudal como
      entrada (D2, D4).
  Respaldo para P1: Bombois et al. 2006; Pipino et al. 2020; Camacho et al. 2007;
      Guzmán, Rivera et al. 2024; Díaz-Salgado et al. 2023 (ver Registro_chequeo_P0.md).
  Diferencia declarada .. Excitación: solo el caudal se excita, y a tasa de operación
                          normal; la potencia entra únicamente como nubes binarias. Se
                          evalúa al horizonte del MPC frente a PRBS de caudal, en un
                          banco que emula un receptor termosolar.
  Veredicto ............. parcial (ningún trabajo cumple D1–D4; Machado 2023 cubre D2–D4)
  Esfuerzo usado ........ ≈ 25 min sesión humana + ≈ 18 min agentes = ≈ 43 min
                                                                 [AUTOR, 2026-11-02]
                          bases: Scopus, Web of Science
                          revisión: Goel et al. (2026), WIREs Energy Environ. 15(2):e70027,
                          10.1002/wene.70027
                          alternativas: Gil et al. (2022), RSER 163:112461 (lectura
                          prioritaria en P1); Kowalik (2025); Untrau et al. (2022)
                          cadenas: C1, C2 y C4b (v2, filtro Review) en ambas bases;
                          C3 solo por agentes
                          registro: Registro_chequeo_P0.md
  Cadenas propuestas (Scopus y Web of Science):
    C1  ("plant-friendly" OR "input design" OR "least costly") AND identification
        AND ("thermal" OR "solar")
    C2  ("bilinear" OR "LPV") AND ("solar collector" OR "solar field") AND
        ("identification" OR "model predictive control")
    C3  ("identification for control" OR "application-oriented input design") AND
        ("MPC" OR "model predictive control") AND ("heat exchanger" OR "thermal")
    C4  review AND ("system identification" OR "data-driven") AND ("solar thermal"
        OR "concentrated solar power") — filtro 2021–2026

LÍMITE DE FACTIBILIDAD  (objeto propio; presupuesto para HUE, aparte de la campaña base)
  Presupuesto de rescate  ≈ 4 ensayos de 6000 s + 10 h de análisis
                                                                 [AUTOR, 2026-11-02]
  Fecha / versión ....... 2026-11-02 · v1

SOLO MODO B ............. N/A (modo A). Datos vistos al formular, declarados por
                          transparencia: los de la tesis; escalones de enero 2026 y
                          FOPDT del artículo del banco; métricas de control de marzo y
                          octubre 2026; repetibilidad de T4 entre réplicas de octubre
                          (calculada el 2026-11-02 para fijar δ).
```

### Campaña base (para dimensionar; el diseño fino es P5)

**Antes de la campaña** (condiciones de validez, no ensayos):
- medir la potencia de cada resistencia con pinza y multímetro (P = V·I) al inicio y al final de cada ensayo, y no tocar los potenciómetros durante la campaña. Los sensores de corriente instalados quedan pendientes, por decisión del autor;
- anti-windup en el lazo interno de caudal: con un comando de 500 L/h y la válvula saturada en ≈ 420 L/h, el integrador se carga y retrasa ≈ 50 s la respuesta. Basta con que el comando no supere 400 L/h;
- revisar los caudalímetros 1 y 2 (opcional: Flow3 sirve porque los paneles están en serie).

| Rol | Caudal (comando, lazo abierto) | Potencia (binaria) | Ensayos |
| --- | --- | --- | --- |
| Referencia | PRBS 200–400 L/h a la tasa del hardware | PRBS 0/100 % por panel | 1 |
| Rama suave | Señal de tasa ≤ 2 L/h·s, ±100 L/h | Máscara de nubes A | 1 |
| Validación | Secuencia de un PI registrada, reproducida en lazo abierto | Máscara de nubes B (distinta) | 3 réplicas |
| No linealidad (claim S1) | Fijo en 200 / 300 / 400 L/h, en tramos | Escalones 0 ↔ 100 % en cada tramo | 1 |
| **Total** | | | **6 ensayos, ≈ 4–6 jornadas** |

## Cómo fijar H y δ

**H, el horizonte del MPC.** En MPC se suele elegir un horizonte de predicción que cubra el tiempo de establecimiento del canal manipulado. Para caudal→T4, el FOPDT equivalente del artículo del banco da τ ≈ 233 s y t0 ≈ 62 s (paper_banco_pruebas.tex:361). Entonces t0 + 4τ ≈ 1000 s, unas 450 muestras.
- Con **H = 1000 s** se evalúa lo que el MPC realmente usa. Es exigente con el término bilineal, porque los errores de ganancia se acumulan.
- Con **H = 300 s** (≈ t0 + τ) se evalúa solo el transitorio inicial y la exigencia es menor.

Recomiendo 1000 s. Las métricas a otros horizontes pueden reportarse como secundarias en P2, pero no deciden H0.

**δ, el margen de no inferioridad.** Debe cumplir dos condiciones:
1. **Ser mayor que el ruido del experimento.** Entre réplicas PI de octubre, T4 difiere en 0.65–1.09 °C de RMSE; entre réplicas PI+FF, en 1.6–2.4 °C. Ese último rango incluye el episodio de windup del 29-oct (T4 llegó a 44.3 °C), así que mide sobre todo la variabilidad del controlador, no la del banco. Con validación en lazo abierto y entradas idénticas, la dispersión debería quedar por debajo de la de las réplicas PI.
2. **Ser pequeño frente a lo que la pregunta quiere distinguir.** Esta es la condición que el rango 1.6–2.4 °C pone en riesgo.

**Decisión (autor, 2026-11-02): margen híbrido** RMSE_suave ≤ máx(1.5·RMSE_abrupta, RMSE_abrupta + 0.5 °C). Reemplaza el rango absoluto inicial de 1.6–2.4 °C. Razones: no exige conocer de antemano el RMSE a 1000 s; se interpreta como "hasta 50 % peor"; es robusto a condiciones de campaña que afectan a ambos modelos; evita la trivialidad. El piso de 0.5 °C impide que el margen caiga bajo el ruido si la referencia es muy buena. El caso de una referencia mala lo cubre el criterio de validez (ii) de P5. Lo que sigue queda como registro de la discusión.

**Posición inicial del autor:** δ entre 1.6 y 2.4 °C, porque el MPC no requiere modelos tan exactos.

**Riesgo de trivialidad (P0.TRIV) con δ en ese rango.** El RMSE esperado de un modelo razonable en este banco es de ≈ 0.5–1 °C (NARX de la tesis: 0.76 °C a un paso de simulación libre). Con δ = 2 °C, el modelo suave podría tener un error 3 a 4 veces mayor que el de referencia y H0 igual se confirmaría. La respuesta "sí" sería casi segura antes de medir, y el resultado no distinguiría una excitación suave buena de una mala.

**Que el MPC tolere error de modelo es cierto, pero tiene matices.** La realimentación (estimación de estado, acción integral u offset-free) corrige errores de nivel y deriva lenta. Lo que no corrige bien son los errores de ganancia y de retardo dentro del horizonte, y esos son justo los que el término bilineal debe capturar. Hay dos maneras de llevar tu argumento a la pregunta:
- **(a) Mantener el observable** (predicción a H) **con un δ que separe modelos útiles de inútiles:** por ejemplo δ = 1.0 °C, o en forma relativa RMSE_suave ≤ 1.5·RMSE_abrupta.
- **(b) Cambiar el observable al desempeño del MPC en lazo cerrado** (IAE de T4 durante las nubes, con el modelo suave frente al abrupto). Mide directamente si el MPC tolera la diferencia, pero exige implementar el MPC en el banco. Tu artículo del banco lo declara trabajo futuro y advierte límites de cómputo en el PLC.

Si eliges δ dentro de 1.6–2.4 °C, el formulario lo admite, pero hay que declarar confianza alta en la dirección. Eso activa R10c: una predicción de magnitud con confianza baja o media, y un tipo de motivación distinto de "construcción".

### Requisitos

| ID | Requisito | Estado | Nota |
| --- | --- | --- | --- |
| R1 | Sistema identificable | Sí | |
| R2 | Observable con unidad | Sí | °C |
| R3 | Umbral numérico | Sí | Margen híbrido: factor 1.5 con piso de 0.5 °C; H = 1000 s |
| R4 | Referencia nombrable | Sí | Mismo modelo identificado con PRBS de caudal |
| R5 | Condición acotada | Sí | |
| R6 | Refutación en una línea y observable | Sí | |
| R7 | Sin verbos aspiracionales | Sí | |
| R8 | Un observable y una refutación | Sí | |
| R9 | Consecuencia para ambos resultados | Sí | |
| R10 | Predicción de dirección registrada | Sí | Autor: sí, confianza baja (2026-11-02) |
| R10b | Motivación con tipo | Sí | Tipo "física" |
| R10c | Magnitud si confianza alta | N/A | Confianza baja |
| R10d | R# citado en la ficha | Sí | Ninguna motivación cita un R# |
| R10e | Quién, cuándo y versión | Sí | Jesús García · 2026-11-02 · H0 borrador |
| R11 | Ficha completa y esfuerzo en rango | Sí | ≈ 43 min, Scopus y WoS, revisión Goel 2026, 3 cercanos, veredicto parcial |
| R11b | Cadenas registradas | Sí | Textos en Registro_chequeo_P0.md; C4b confirmada por el autor, con totales (Scopus 30 con límite de año; WoS 54, revisados 50 por relevancia) |
| R12 | Incertidumbre < efecto | Sí | Margen ≥ 0.5 °C por construcción, más de 3 veces la exactitud del PT100; el criterio (i) de P5 cubre el caso contrario |
| R13 / R13b | Modo B | N/A | Modo A |
| R14 | H# con fecha y versión | Sí | Borrador 2026-11-02 |
| R15 | Límite de factibilidad | Sí | ≈ 4 ensayos de 6000 s + 10 h de análisis · 2026-11-02 · v1, separado de la restricción |

### Modos de fallo

```text
(P0.UMB, P0.TRIV y P0.INMED resueltos con el margen híbrido, 2026-11-02)
(P0.CHQ y P0.IRREP resueltos: ≈ 43 min y cadenas registradas, 2026-11-02)
P0.PREC   · riesgo · R11 R1–R3 podrían dejar la pregunta "respondida"
```

```text
RETORNOS QUE EMITE ... Ninguno.
AVANCE EFECTUADO ..... 2026-11-02: H0 v1 + ficha provisional (veredicto parcial) + modo A
                       → P1. P1 debe leer primero Machado 2023, Gil 2022, Díaz-Salgado
                       2023 y los resúmenes de Rivera 2009 y Bombois 2006.
AVANCE ............... Al cerrarse: H0 v1 + ficha provisional + modo A → P1.
RETORNOS QUE RECIBE .. PRE · P1 · reformular sobre la dimensión con precedente; nueva
                       versión de H0.
IA (opcional) ........ Delegado a IA: reformulación, estructura, propuestas razonadas de
                       H y δ, indicador de repetibilidad, R# candidatos, cadenas, segunda
                       predicción. No delegado: confirmar H y δ, límite de factibilidad,
                       predicción del autor. R1–R3 sin verificar.
```

## Datos de otros proyectos (consultados en solo lectura)

Mismo banco: 4 colectores FP3.0E en serie, ≈ 9.5 L de inventario, PT100, PLC LOGO!8. Con el modo A, estos datos ya no son anclaje; sirven para planificar (P5) y como antecedentes.

| Conjunto | Fecha | Uso en este trabajo |
| --- | --- | --- |
| Escalones de potencia 0→100 %CO y de caudal 500→400 L/h (FOPDT por panel) | 2026-01-05 | Constantes de tiempo para fijar H y diseñar señales |
| Escalón de caudal ≈ 250 L/h | 2025-12-29 | Exploratorio para la claim S1 (ganancia del caudal ∝ 1/ṁ²) |
| HR1–HR4, factorial de pesos T1–T11, DOE 17/27 corridas | 2025-04 a 2026-01 | Antecedentes de operación |
| Réplicas PI y PI+FF con perfil de nubes | 2026-10-28/29 | Indicador de repetibilidad para δ; máscara de nubes de referencia |
| Modelo físico distribuido de 5 nodos | — | Posible rival de caja blanca en P2 |

**Del análisis de caudal del autor (2026-11-02):**
- **Medido:** arranque de la bomba ≈ 38 L/h·s (límite del hardware); PI 6–9 L/h·s; PI+FF 14–22 L/h·s, en ventanas de 10 s. Las tasas entre dos muestras consecutivas miden la cuantización (23.47 L/h por escalón, Ts ≈ 2.3 s).
- **Comando:** PI ≤ ≈ 2 L/h·s; FF con saltos de ≈ 50 L/h·s en una muestra.
- **Windup del lazo interno de caudal** al pedir 500 L/h con la válvula saturada en ≈ 420 L/h: retraso de ≈ 50 s.

**Consecuencias para H0:** la excitación suave se define sobre el **comando**, porque es lo que el experimento controla y el caudal medido llega filtrado por la hidráulica. El límite de 2 L/h·s es la tasa de la operación normal con PI. La amplitud debe superar con holgura la resolución del caudalímetro. El comando no debe pasar de ≈ 400 L/h.

## Secuencia de búsqueda

La búsqueda sistemática se hace en P1 (decisión del autor, 2026-11-02). En P0 solo queda el chequeo acotado: 30–120 min, ≥ 2 bases, ≥ 1 revisión de ≤ 5 años y cadenas registradas. Si P1 encuentra precedentes, el retorno PRE devuelve a P0.

## Registro mínimo — historial e ideas descartadas

| Fecha | Cambio | Motivo |
| --- | --- | --- |
| 2026-11-02 | v0: "¿NARX MISO reduce el RMSE frente a BJ MISO?" | Extraída del texto de la tesis |
| 2026-11-02 | Reformulada: excitación suave + horizonte de MPC + estructura bilineal | Idea motriz del autor; v0 descartada |
| 2026-11-02 | Opción de más pruebas; búsqueda sistemática asignada a P1 | Autor |
| 2026-11-02 | Potencia PWM, PT100 ±0.15 °C, riesgo de medición de potencia, inventario de datos | Consulta en solo lectura de los otros repositorios |
| 2026-11-02 | Modo A; potencia binaria como nubes; suavidad sobre el comando de caudal (≤ 2 L/h·s); validación en lazo abierto con 3 réplicas; H = 1000 s y δ = 0.5 °C propuestos | Decisiones y análisis de caudal del autor; repetibilidad de las réplicas de octubre |

| 2026-11-02 | Potencia medida con pinza + multímetro al inicio y al final de cada ensayo; δ en el rango 1.6–2.4 °C según el autor; riesgo de trivialidad registrado | Decisiones del autor |

| 2026-11-02 | Criterio: margen híbrido máx(1.5·RMSE_abrupta, RMSE_abrupta + 0.5 °C), en reemplazo de δ absoluto; criterios de validez (i) y (ii) asignados a P5 | Decisión del autor tras discutir el riesgo de trivialidad |

| 2026-11-02 | H = 1000 s confirmado | Decisión del autor |
| 2026-11-02 | Predicción de dirección del autor registrada (sí, confianza baja, evidencia previa) | Autor, antes de cualquier ensayo de la campaña nueva |
| 2026-11-02 | Tipo de motivación del autor cambiado a "física"; "FIT3" aclarado como FOPDT | La evidencia previa no tenía R# en la ficha (R10d) |
| 2026-11-02 | Límite de factibilidad v1: ≈ 4 ensayos de 6000 s + 10 h de análisis | Decisión del autor, antes de cualquier ensayo |
| 2026-11-02 | Chequeo acotado cerrado (≈ 25 + 18 min; C4b repetida con filtro Review en Scopus y WoS); veredicto parcial | Sesión humana y exportaciones del autor |
| 2026-11-02 | Aclaración de la motivación: la segunda mención de "caudal alto" significa "caudal bajo" (nota aparte; texto original intacto) | Autor |
| 2026-11-02 | **H0 v1. P0 cerrada; avance a P1** | R1–R15 en Sí o N/A |
| 2026-11-03 | **H0 v1.1** (retorno PRE desde P5): validación con 2 máscaras de nubes × 3 réplicas; refutación por máscara y resultado parcial si falla en una sola | Decisión del autor en P5: reducir el límite L2 (una sola secuencia de nubes) |
| 2026-11-03 | Nota (sin cambiar H0): la medición de potencia de MEDIBILIDAD ("pinza y multímetro al inicio y al final de cada ensayo") queda sustituida por una **caracterización única** antes de la campaña; ver P3 (S1, L5) y P4 (E8) | Disponibilidad del autor; el autor intentará instalar sensores en línea |

**Descartada (v0) y su causa:** la pregunta NARX vs BJ MISO no responde a la idea motriz, usaba un rival débil (FIT −47 %) y no tenía anclaje confirmatorio. Sus resultados quedan como evidencia exploratoria de la premisa de no linealidad.

**Estado del pipeline:** `estado.json` marca P0 completada y P1 como fase actual; su artefacto P0 es este archivo. El original quedó en `estado.json.bak-2026-11-02`.

## Decisiones pendientes del autor para cerrar P0

1. ~~Chequeo acotado~~ — cumplido el 2026-11-02 (≈ 43 min, Scopus + WoS, Goel 2026).
2. ~~Aclarar "caudal alto/bajo"~~ — confirmado por el autor el 2026-11-02: la segunda mención es "caudal bajo".
