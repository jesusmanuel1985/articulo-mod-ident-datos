# P4 — Evidencia · Banco de emulación termosolar (Tesis Loreto Baima)

Entrada: J2 (`P3_Jerarquia.md`), C-set v1.4 (`P2_Claims.md`), H0 v1 y límite de factibilidad v1 (`P0_H0_Tesis_Loreto.md`).
Metodología: `Metodologia-desarrollo-de-articulo-cientifico.md`, sección P4. **Modo A: se especifica** (rama A); no hay auditoría de datos existentes.

**Estado: E-set v1 — P4 cerrada el 2026-11-03; sigue P5.** Observables y paridad propuestos por Claude; paridad, exclusiones, anclaje y medición de potencia decididos por el autor (`[AUTOR, 2026-11-03]`). Quedan para P5 solo los valores numéricos marcados como tales (umbral de E4, tolerancia de E9, duración del transitorio).

## Tabla de exigencias

Todas las E# están **planificadas** y **no vistas**: provienen de la campaña nueva del modo A.

| E# | Hoja | Observable [unidad] | Comparador | Condición | Resuelve |
| --- | --- | --- | --- | --- | --- |
| E1 | C0 | RMSE_H de T4 predicha a H = 1000 s [°C], rama suave y rama PRBS, promedio de las 3 réplicas de validación | Rama PRBS, mismo modelo (referencia de H0) | Condición de validez de C0 | — |
| E2 | C0 (criterio de validez i de P0) | Desviación estándar entre réplicas de la diferencia RMSE_H(suave) − RMSE_H(PRBS) [°C] | Absoluto: ≤ margen/2; si no, no concluyente (no NEG) | Las 3 réplicas de validación | — |
| E3 | C1 | RMSE_H [°C] del modelo bilineal y del FOPDT, ambos identificados con los datos PRBS | FOPDT (rival de C1) | Las mismas 3 réplicas y H que E1 | — |
| E4 | C1 (criterio de validez ii de P0) | RMSE_H del bilineal (PRBS) frente a la persistencia T4(t+H) = T4(t), y frente a un umbral absoluto [°C] | Persistencia; umbral `[DECIDE AUTOR en P5, antes de adquirir]` | Igual que E3 | — |
| E5 | C2 | Tasa máxima del comando [L/h·s], amplitud [L/h] y comando máximo [L/h] de la rama suave | Absoluto: ≤ 2 L/h·s; ≥ 100 L/h; ≤ 400 L/h | Ensayo de identificación suave | — |
| E6 | C3 | Parámetros del término ṁ·cp estimados en cada rama, con intervalo al 95 % (bootstrap o covarianza) [unidades del parámetro] | Entre ramas (solapamiento de intervalos) | Identificación de ambas ramas | — |
| E7 | C4 | RMSE_H de la rama suave por tramo de caudal [°C]: 200–267, 267–333, 333–400 L/h | Entre tramos | Validación | — |
| E8 | S1 | Potencia de cada resistencia en cada muestra, Q_i = estado_i·R_i·I_i² [W]: corriente del transmisor calibrado y R_i en frío | Entrada de potencia de todos los modelos, en ambas ramas | Calibración de corriente vigente (27-11-2026), verificada contra los medidores DIN en la corrida K al inicio de cada día de campaña (P5 v1.4) `[AUTOR, 2026-11-27]` | S1; L5 queda reducido a la escala absoluta |
| E10 | C7 | Ganancia estática K = ΔT4/ΔQ [°C/kW] en cada meseta de 200, 300 y 400 L/h, y cociente K(200)/K(400), con incertidumbre | Absoluto: cociente ≥ 1.5 y K decreciente | Corrida NL (P5) | — |
| E9 | S5 | T ambiente, T0 y temperatura inicial de los colectores [°C], por ensayo | Entre ensayos; tolerancia `[DECIDE AUTOR en P5]` | Todos los ensayos | S5 (parcialmente: muestra comparabilidad, no la garantiza) |

### Límites (R4)

| Límite | Subtipo | Evidencia o restricción |
| --- | --- | --- |
| L1 (sin desempeño de control) | declarado | Restricción: la campaña no incluye ensayos de MPC en lazo cerrado; el alcance de H0 es el error de predicción |
| L2 (una campaña, una máscara) | declarado | Restricción de tiempo de banco; ampliación a 2 secuencias de nubes pendiente en P5 |
| L4 (sin planta solar) | declarado | Ausencia justificada: no hay acceso a una planta solar real |
| L5 (escala absoluta de la potencia sin referencia certificada) | declarado | Medidores DIN no certificados; en R2 los instrumentos discrepan ≈ ±4.5 % en corriente (≈ ±9 % en potencia). La variación entre muestras y ensayos sí se mide (E8) `[AUTOR, 2026-11-25]` |
| L3 | medido | Se crea en P6 si C0 resulta parcial; su evidencia será E1/E7 en el tramo donde falle |

## Decisión sobre la potencia (S1, E8) `[AUTOR, 2026-11-03]`

Se aplica la **caracterización única** (opción c): tensión y corriente de cada resistencia al 100 %, una vez, antes de la campaña. Sustituye lo decidido en P0 (medición al inicio y al final de cada ensayo), por disponibilidad del autor. El autor intentará instalar sensores en línea; si lo logra antes de P6, E8 se amplía (medición por ensayo o continua) y L5 se reduce, con registro de versión.

**Actualización `[AUTOR, 2026-11-25]` (retorno RTP desde P5).** Se cumplió esa condición: los transmisores de corriente quedaron calibrados el 24-11-2026 y E8 pasa a medición continua, Q_i = estado_i·R_i·I_i². Motivos: los reguladores de ángulo de fase siguen en el circuito (V·I es potencia aparente), la pinza no es true RMS, nadie asegura que las perillas no se muevan y la potencia por resistencia cae ≈ 15–19 % cuando se encienden las 4. Protocolo en P5 v1.3, §1.1.

Nota: el balance ṁ·cp·ΔT en las mesetas al 100 % puede calcularse después con los sensores existentes (caudal y PT100) sin costo de hardware. No se exige como evidencia, pero queda disponible como verificación en P7.

## Entrada de caudal del modelo `[AUTOR, 2026-11-03]`

El modelo usa el **caudal medido**, no el comando. Consecuencias:
- La excitación suave se sigue definiendo y verificando sobre el **comando** (C2, E5); el caudal medido es lo que entra al modelo.
- El caudal medido está cuantizado en 23.47 L/h y tiene ruido. Con amplitud de 100 L/h, la rama suave recorre ≈ 4 escalones; la PRBS, más. Esa diferencia de resolución relativa es parte del efecto que se estudia, no una violación de paridad, siempre que ambas ramas reciban el mismo tratamiento (PA2).
- El ruido en la entrada puede sesgar la estimación del término ṁ·cp (error en las variables). Afecta a ambas ramas; se discute al leer C3.

## Tabla de paridad

### C0: rama suave frente a rama PRBS (mismo modelo bilineal)

| Categoría | ¿Aplica? | Requisito de igualdad propuesto | Paridad |
| --- | --- | --- | --- |
| PA1 Condiciones de operación | Aplica | Mismo banco y configuración; misma máscara de nubes binaria durante la identificación de ambas ramas; mismo rango de comando (200–400 L/h); condiciones ambientales comparables (E9) | declarada `[AUTOR, 2026-11-03]` |
| PA2 Información disponible | Aplica | Mismos sensores y Ts; entrada de caudal = **caudal medido** en ambas ramas, con el mismo tratamiento (mismo filtro o ninguno, declarado antes de ver resultados); misma conversión de corriente a potencia por resistencia (E8); mismo H | declarada `[AUTOR, 2026-11-03]` |
| PA3 Presupuesto de ajuste | Aplica | Misma estructura y número de parámetros; mismo algoritmo y criterio de estimación (p. ej., minimización del error de simulación); misma inicialización y criterio de parada; ningún ajuste específico por rama | declarada `[AUTOR, 2026-11-03]` |
| PA4 Presupuesto de cómputo | No aplica | Estimación fuera de línea con costo despreciable; el mismo criterio de parada (PA3) evita ventajas | — |
| PA5 Métricas y ventana | Aplica | Misma definición de RMSE_H, mismas ventanas de validación, mismo descarte del transitorio inicial, mismas 3 réplicas | declarada `[AUTOR, 2026-11-03]` |
| PA6 Datos de ajuste | Aplica | **Misma duración y número de muestras** de identificación en ambas ramas; ninguna usa datos de validación | declarada `[AUTOR, 2026-11-03]` |

### C1: modelo bilineal frente a FOPDT (ambos con datos PRBS)

| Categoría | ¿Aplica? | Requisito de igualdad propuesto | Paridad |
| --- | --- | --- | --- |
| PA1 | Aplica | Los mismos datos PRBS (identidad) | declarada |
| PA2 | Aplica | El FOPDT recibe las mismas entradas que el bilineal: caudal medido y potencia de las 4 resistencias (FOPDT multientrada con retardos) | declarada `[AUTOR, 2026-11-03]` |
| PA3 | Aplica | Ganancias, constantes de tiempo y retardos del FOPDT **estimados** con el mismo criterio que el bilineal, con búsqueda del retardo declarada | declarada `[AUTOR, 2026-11-03]` |
| PA4 | No aplica | Igual que en C0 | — |
| PA5 | Aplica | Igual que en C0 | declarada |
| PA6 | Aplica | Mismos datos de ajuste (PRBS) | declarada |

## Exclusiones previsibles (R7, antes de ver resultados) `[AUTOR, 2026-11-03]`

1. Se descarta el transitorio inicial de cada ensayo hasta que T4 se estabilice (duración a fijar en P5, igual para todos).
2. Se descartan muestras con fallo de sensor (valores no físicos o faltantes) y se registra cuántas.
3. Un ensayo cuyo comando de caudal supere ≈ 420 L/h (saturación de la válvula) o se desvíe de lo programado es inválido (INV) y se repite.
4. No se excluyen réplicas de validación por su resultado.

## Anclaje (R5)

Toda la evidencia de C0 proviene de datos no vistos (campaña nueva, modo A). C0 se mantiene confirmatorio.

## Límite de factibilidad (R13)

v1, 2026-11-02 (P0): ≈ 4 ensayos de 6000 s + 10 h de análisis. Fecha anterior a la entrada en P6. En modo A no se usa HUE; el límite rige si P6 devuelve un ensayo acotado.

## Hacia P5

E1–E9 planificadas; tabla de paridad declarada; exclusiones; límites con subtipo; límite de factibilidad v1. Pendientes ya acumulados: umbral de E4, tolerancia de E9, protocolo de potencia (E8), 2 secuencias de nubes (L2), duración del transitorio descartado.

## Historial

| Versión | Fecha | Cambio | Motivo |
| --- | --- | --- | --- |
| E-set v0 | 2026-11-03 | Borrador: E1–E9, paridad de C0 y C1, exclusiones, anclaje | Inicio de P4 |
| **E-set v1** | 2026-11-03 | Potencia por caracterización única (sustituye lo decidido en P0); caudal medido como entrada; FOPDT con caudal y potencia; paridad PA1–PA6 y exclusiones aceptadas. **P4 cerrada** | Decisiones del autor |
| E-set v1.1 | 2026-11-04 | E10 para C7 (RTP desde P5) | Decisión del autor |
| E-set v1.3 | 2026-11-27 | E8: verificación con K diaria contra los medidores DIN; sin compuerta V6 (RTP desde P5 v1.4) | Decisión del autor |
| E-set v1.2 | 2026-11-25 | E8 pasa de caracterización única (V·I) a potencia medida en cada muestra; L5 reducido a la escala absoluta (RTP desde P5) | Reguladores de fase, pinza no true RMS, perillas no aseguradas; decisión del autor |
