# P2 — Claims · Banco de emulación termosolar (Tesis Loreto Baima)

Entrada: H0 v1 (`P0_H0_Tesis_Loreto.md`; modo A, confirmatoria), enunciado y ficha de novedad de P1 (`P1_Brecha_novedad.md`, veredicto parcial sin reformulación).
Metodología: `Metodologia-desarrollo-de-articulo-cientifico.md`, sección P2.

**Estado: C-set v1 — P2 cerrada el 2026-11-03; sigue P3.** Descomposición propuesta por Claude; tipo, claim raíz y destino decididos por el autor (`[AUTOR, 2026-11-03]`). Queda un punto diferido a P5 (L2).

## Claim raíz

| Campo | C0 |
| --- | --- |
| Frase | El modelo bilineal de bajo orden del banco, identificado con un comando de caudal suave, predice T4 a 1000 s con un RMSE no mayor que máx(1.5·RMSE_PRBS, RMSE_PRBS + 0.5 °C), donde RMSE_PRBS es el del mismo modelo identificado con PRBS de caudal |
| Tipo | **B — comparativa** (no inferioridad frente a un rival) `[AUTOR, 2026-11-03]`. Alternativa A (umbral absoluto RMSE_H ≤ X °C) desaconsejada: cambiaría H0 (criterio relativo a PRBS), perdería la dimensión abierta por P1 (R12) y exigiría una referencia de P0 que no existe (R14) |
| Etiqueta | confirmatorio (igual que H0) |
| Condición de validez | Comando de caudal 200–400 L/h; suave = tasa ≤ 2 L/h·s y amplitud ≥ 100 L/h; potencia binaria 0 ↔ 100 % por resistencia, con la potencia al 100 % tomada de una caracterización única por resistencia (tensión y corriente medidas una vez; ver L5); Ts ≈ 2.2 s; ensayo de validación de operación PI con 2 máscaras de nubes distintas entre sí y de la de identificación, 3 réplicas por máscara (H0 v1.1); identificación (ambas ramas) y validación en condiciones ambientales comparables y registradas (T ambiente, T0, estado inicial) |
| Modo | A |
| Falsador | Promediando las 3 réplicas, RMSE_H(suave) > máx(1.5·RMSE_H(PRBS), RMSE_H(PRBS) + 0.5 °C) |
| Evidencia exigida | RMSE_H de ambas ramas sobre las mismas 3 réplicas de validación, mismo modelo, mismo procedimiento de estimación |
| Destino | en_paper |
| Dependencias | C1, C2 |
| Estado | por probar |
| Novedad (R12) | Porta la novedad: la dimensión abierta por P1 es la **condición** (excitación suave diseñada frente a PRBS) en un **sistema** con caudal manipulado y modelo bilineal, evaluada al horizonte del MPC |

## Claims de apoyo

| C# | Frase | Tipo | Etiqueta | Condición de validez | Falsador | Evidencia exigida | Destino | Dep. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | El modelo bilineal identificado con PRBS predice T4 a 1000 s con un RMSE menor que el de un modelo lineal de primer orden con retardo (FOPDT) identificado con los mismos datos | B `[AUTOR, 2026-11-03]` | confirmatorio | La de C0 | RMSE_H(bilineal, PRBS) ≥ RMSE_H(FOPDT, PRBS) | RMSE_H de ambos modelos en las mismas réplicas; paridad (P4): mismos datos PRBS, retardo y constante de tiempo del FOPDT estimados, mismo H y mismas 3 réplicas | en_paper | — |
| C2 | La rama suave aplicada en el banco cumple tasa ≤ 2 L/h·s, amplitud ≥ 100 L/h y comando ≤ 400 L/h | A (no D: las señales con tasa limitada tienen precedentes, R3) | confirmatorio | Ensayo de identificación suave | Tasa del **comando** > 2 L/h·s en algún tramo, o amplitud del comando < 100 L/h, o comando > 400 L/h | Registro del comando; el caudal medido solo verifica que el comando se siguió (está cuantizado en 23.47 L/h por escalón) | en_paper `[AUTOR, 2026-11-03]` | — |
| C3 | Los parámetros del término ṁ·cp estimados con la rama suave difieren de los estimados con PRBS en menos de su incertidumbre combinada | C | exploratorio `[AUTOR, 2026-11-03]` | La de C0 | Diferencia mayor que la incertidumbre combinada (intervalos sin solapamiento) | Estimaciones con incertidumbre (p. ej., bootstrap o covarianza) | en_paper `[AUTOR, 2026-11-03]` | — |
| C4 | El error de predicción de la rama suave es mayor en los tramos de caudal bajo (≈ 200 L/h) que en los de caudal alto | C | exploratorio `[AUTOR, 2026-11-03]` | Validación, por tramos de caudal | Error por tramo sin diferencia, o mayor en caudal alto | RMSE_H por tramo de caudal | en_paper `[AUTOR, 2026-11-03]` | C0 |
| C7 | En el banco, la ganancia estática potencia→T4 disminuye con el caudal: la medida a 200 L/h es al menos **1.5 veces** la medida a 400 L/h (el balance por etapa predice ≈ 2, proporcional a 1/ṁ; un sistema lineal daría 1) | A `[AUTOR, 2026-11-04]` | confirmatorio (datos no vistos) | Caudal fijo en 200, 300 y 400 L/h; escalones simultáneos 0 ↔ 100 % de las 4 resistencias; régimen permanente en cada meseta | K(200)/K(400) < 1.5 `[AUTOR, 2026-11-04]`, o K no decrece de 200 a 300 a 400 L/h | Corrida NL de P5: ΔT4/ΔQ en cada meseta, con incertidumbre | en_paper `[AUTOR, 2026-11-04]` | — |
| ~~C6~~ | ~~Durante todos los ensayos, la potencia de cada resistencia en estado encendido se mantiene en P_nom ± x %~~ | A | — | — | — | Registro continuo de tensión y corriente: **no disponible** | **descartado** `[AUTOR, 2026-11-03]`: sin hardware de medición continua; se sustituye por una caracterización única (premisa S1 en P3) y el límite L5 | — |
| ~~C5~~ | ~~El banco de emulación representa la dinámica de un campo de colectores solares con caudal manipulado~~ | E | — | — | — | Comparación banco ↔ planta solar real: no disponible | **descartado** `[AUTOR, 2026-11-03]`: no se afirma representatividad; se sustituye por X5 (estructura común, verificable) y por la advertencia L4 | — |

C3 y C4 provienen de la motivación del autor en P0 (el riesgo de que, con caudal suave, la información del término ṁ·T venga casi solo de las nubes, y la duda sobre el comportamiento a caudal bajo). C1 asegura que el rival PRBS está bien puesto: si el modelo bilineal no supera a un FOPDT lineal, la estructura bilineal no se justifica. C7 (idea motriz 3 de P0) muestra la no linealidad de forma directa, sin modelo: es la evidencia física de que el término ṁ·cp·(T_{i−1} − T_i) es necesario. Como es un cociente de ganancias medidas con la misma potencia, el error de P_nom (S1) se cancela.

## Claims de contexto (con fuente R# de P1)

| C# | Frase | Fuente |
| --- | --- | --- |
| X1 | Modelos identificados con datos de operación o con excitación de baja perturbación igualaron o superaron a los de excitación abrupta, con modelos lineales en la entrada | R1 (Bagle 2026), R9 (Larsson 2015) |
| X2 | La estructura bilineal es la descripción establecida de campos de colectores con caudal manipulado | R21 (Roca 2008), R5/R22 (Ampuño 2018, 2019) |
| X3 | Igual error de predicción no garantiza igual desempeño de control con MPC | R20 (Zhan 2022) |
| X4 | Las señales con pasos de entrada limitados tienen antecedentes en identificación *plant-friendly* | R2 (Braun 2002), R3 (Rivera 2009) |
| X5 | El modelo del banco tiene la misma estructura bilineal (término ṁ·cp·(T_{i−1} − T_i)) que los modelos de campos de colectores usados para control | R21 (Roca 2008), R5 (Ampuño 2019); verificable comparando ecuaciones |

## Límites (R13: al menos uno sobre C0, dentro del rango de P0)

| C# | Frase | Subtipo | Ref. | Rango de P0 del que proviene |
| --- | --- | --- | --- | --- |
| L1 | C0 no se probó en desempeño de control en lazo cerrado: solo en error de predicción a 1000 s | declarado | C0 | Operación del banco a 200–400 L/h con MPC, que es el uso previsto del modelo |
| L2 | C0 se probó en una sola campaña y con 2 máscaras de nubes de validación; no se probó en otras condiciones ambientales ni en otras campañas | declarado `[AUTOR, 2026-11-03]` (reducido: antes una sola máscara) | C0 | Ensayo de validación de H0 v1.1 |
| L3 | (se crea en P6 si C0 resulta PAR: tramo donde no se sostiene) | medido | C0 | — |

| L5 | La potencia de las resistencias se caracterizó una sola vez; su variación entre ensayos (p. ej., por la tensión de red) no se midió | declarado `[AUTOR, 2026-11-03]` | C0 (y la lectura de C3) | Potencia binaria 0 ↔ 100 % de P0 |
| L4 | C0 se afirma para el banco, cuyo aporte de calor son resistencias; no se ha contrastado con una planta solar real | declarado (fuera del rango de P0: no cuenta para R13, pero se declara en el paper) | C0 | — |

Fuera del rango de P0, y por tanto vacuos para R13 (se mencionan en el paper, pero no cuentan): potencia continua en vez de binaria, caudal < 200 L/h o > 400 L/h, plantas solares reales (L4).

## Verificación contra los requisitos de P2

| R# | Estado en el borrador |
| --- | --- |
| R1 una sola afirmación | Sí en C0–C5 (revisar C2: tres condiciones de una misma señal; se puede partir) |
| R5 un claim raíz | Sí (C0) |
| R6 etiqueta de C0 ≤ H0 | Sí (confirmatorio = confirmatorio) |
| R8 tipo E sin evidencia | C5 queda como premisa |
| R9 sin adjetivos sin prueba | Revisado: sin "robusto", "preciso", "eficiente" |
| R12 novedad | C0 coincide con la dimensión abierta por P1 |
| R13 límite de C0 | L1 declarado, dentro del rango |
| R14 | No aplica (C0 es tipo B) |

## Decisiones pendientes del autor

1. ~~Tipo de C0~~: B `[AUTOR, 2026-11-03]`.
2. ~~L2~~: se mantiene; la ampliación a 2 secuencias de nubes se decide en P5 `[AUTOR, 2026-11-03]`.
3. ~~Ajuste al enunciado de novedad de P1~~: aplicado como retorno NOV `[AUTOR, 2026-11-03]`.

Sin decisiones pendientes en P2.

## Historial

| Fecha | Cambio | Motivo |
| --- | --- | --- |
| 2026-11-03 | Borrador v0 del C-set | Inicio de P2 tras el cierre de P1 |
| 2026-11-03 | C1: referencia FOPDT con los mismos datos; C2 en el paper (tipo A); C3 y C4 exploratorios en el paper; C5 descartado y sustituido por X5 y L4 | Decisiones del autor. C5: afirmar representatividad sin comparación con planta real expone el paper a objeciones; se acotan las conclusiones al banco |
| 2026-11-03 | C0 confirmado como tipo B. Retorno NOV emitido a P1: enunciado de novedad acotado a "sistema de colectores con caudal manipulado y modelo bilineal". L2 reescrito para aclarar su alcance | Decisiones del autor |
| 2026-11-03 | L2 se mantiene; ampliar a 2 secuencias de nubes queda para P5. **P2 cerrada (C-set v1)** | Decisión del autor |
| 2026-11-03 | Condición de validez de C0 y L2 ajustados a H0 v1.1 (2 máscaras de validación) (C-set v1.5) | Decisión del autor en P5 |
| 2026-11-03 | C1 retipificado de A a B (comparativa cabeza a cabeza con FOPDT; exige paridad en P4) (C-set v1.4) | Decisión del autor |
| 2026-11-03 | Retorno RTP desde P3: C6 descartado (sin hardware de medición continua); potencia por caracterización única en la condición de validez de C0; nuevo límite L5 (C-set v1.3) | Decisión del autor |
| 2026-11-03 | Retorno RTP desde P3: nuevo C6 (potencia constante medida con tensión y corriente); condición de validez de C0 ampliada con potencia regulada y condiciones ambientales comparables (S5) (C-set v1.2) | La premisa S1 (potencia estimada por PWM) no tenía respaldo y alcanzaba C0; el autor medirá tensión y corriente y regulará la potencia en todos los ensayos |
| 2026-11-03 | Retorno RTP desde P3: el falsador de C2 se evalúa sobre el comando, no sobre el caudal medido (C-set v1.1) | P0 define la excitación suave sobre el comando; el caudal medido está cuantizado y filtrado. Aprobado por el autor |
| 2026-11-04 | Retorno RTP desde P5: **nuevo C7** (no linealidad caudal–potencia), recuperado de la corrida de no linealidad de P0, que se había perdido al renumerar S1 en P3 (C-set v1.6) | Decisión del autor: visibilidad y peso en el análisis |
| 2026-11-04 | C7: tipo A y umbral 1.5 confirmados | Decisión del autor |
