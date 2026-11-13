# P1 — Brecha y novedad · Banco de emulación termosolar (Tesis Loreto Baima)

Entrada: H0 v1 y ficha de novedad provisional (`P0_H0_Tesis_Loreto.md`), registro del chequeo acotado (`Registro_chequeo_P0.md`).
Metodología: `Metodologia-desarrollo-de-articulo-cientifico.md`, sección P1.

**Estado: PROTOCOLO v1 APROBADO el 2026-11-03 (Jesús García). Búsqueda ejecutada el 2026-11-03, 09:50–11:22 (desviación D-1: el protocolo decía "desde el 2026-11-04"; R1 se cumple porque el protocolo quedó fijo a las 07:51 y no cambió). Corrida complementaria S4a ejecutada. Cribado confirmado por el autor (`P1_Cribado.md`); lectura, revisión de C y seguimiento de citas completos (`P1_Registro_precedentes.md`). Veredicto (parcial sin reformulación) y enunciado de novedad aprobados por el autor: P1 cerrada el 2026-11-03; sigue P2.** Cualquier cambio posterior al protocolo se registra como v2, con fecha y motivo.

## Entrada heredada de P0

- **H0 v1 (modo A):** un modelo bilineal de bajo orden del banco de 4 colectores en serie, identificado con excitación **suave** del comando de caudal (≤ 2 L/h·s, amplitud ≥ 100 L/h, ≤ 400 L/h), predice T4 a H = 1000 s con RMSE_H ≤ máx(1.5·RMSE_abrupta, RMSE_abrupta + 0.5 °C) frente al mismo modelo identificado con PRBS de caudal; potencia binaria 0 ↔ 100 % (nubes) en todos los ensayos.
- **Diferencia declarada:** excitación (solo caudal, a tasa de operación normal), evaluada al horizonte del MPC contra PRBS, en un banco que emula un receptor termosolar.
- **Veredicto provisional:** parcial. Ningún trabajo cumple D1–D4; Machado et al. (2023) cubre D2–D4 sin comparar con PRBS.
- **R# provisionales:** Rivera et al. 2009 (D1); Machado et al. 2023 (D2–D4); Mechhoud & Belkhatir 2024 (D2, D4). Respaldo: Bombois et al. 2006, Gil et al. 2022 (revisión), Pipino et al. 2020, Camacho et al. 2007.
- **Excluido por acceso:** Díaz-Salgado et al. 2023 (texto completo no disponible; clasificado por resumen, D1 probablemente "no"). Decisión del autor, 2026-11-02.

## Protocolo de búsqueda · v1 · aprobado 2026-11-03

### Bases y fuentes

| Base | Uso | Estado |
| --- | --- | --- |
| Scopus | Principal | propuesta |
| Web of Science Core Collection | Principal | propuesta |
| IEEE Xplore | Actas de control (CDC, ACC, ECC, CCTA) poco cubiertas por las anteriores | aprobada `[AUTOR, 2026-11-03]` |
| Google Scholar (primeros 100 por cadena, orden por relevancia) | Complemento: tesis y literatura gris. No sustituye a Scopus/WoS porque no admite booleanos completos, su orden no es reproducible y muestra como máximo 1000 resultados | aprobada `[AUTOR, 2026-11-03]` |

**Tipos de fuente incluidos (R5):** artículos de revista, actas de congresos con revisión por pares (IFAC, IEEE), revisiones y tesis doctorales. Se excluyen patentes, libros de texto y preprints sin revisión. `[AUTOR, 2026-11-03]`

**Idiomas:** inglés, con preferencia; también español y portugués. Ante dos trabajos equivalentes, se cita el publicado en inglés. `[AUTOR, 2026-11-03]`

**Ventana de años:** sin límite inferior en S4 y S5 (la teoría de diseño de entrada es de los años 2000); 2000–2026 en S1–S3. `[AUTOR, 2026-11-03, aprobado con el protocolo]`

### Cadenas (R2, R11)

Se escriben en sintaxis de Scopus (`TITLE-ABS-KEY`); en WoS se usa el mismo contenido en el campo `TS=`. Cada ejecución se registra textualmente, con la fecha y el total de resultados.

| Código | Propósito | Cadena (Scopus) |
| --- | --- | --- |
| S1 | Diferenciador D1 en sistemas térmicos | `TITLE-ABS-KEY ( ( excitation OR "input design" OR "input signal*" OR "plant-friendly" OR "least costly" OR "normal operation" OR "operating data" OR "closed-loop data" ) AND ( "system identification" OR "model identification" OR "parameter estimation" ) AND ( "solar collector*" OR "solar field" OR "solar thermal" OR "heat exchanger*" OR "thermal process*" ) )` |
| S2 | Comparación de señales de excitación | `TITLE-ABS-KEY ( ( PRBS OR "pseudo-random binary" OR multisine OR "step test*" ) AND compar* AND identification AND ( thermal OR solar OR temperature ) )` |
| S3 | **Sin el diferenciador** (sistema + estructura + uso en predicción) | `TITLE-ABS-KEY ( ( "solar collector*" OR "solar field" OR "parabolic trough" OR "flat-plate collector*" OR "Fresnel collector*" ) AND ( identification OR "data-driven" OR "grey-box" OR "gray-box" OR bilinear OR LPV ) AND ( "model predictive control" OR MPC OR "multi-step" OR prediction ) )` |
| S4 | D1 fuera del dominio solar | `TITLE-ABS-KEY ( ( "plant-friendly" OR "least costly" OR "application-oriented" OR "input design" ) AND ( "model predictive control" OR MPC OR "identification for control" ) )` |
| S5 | Error de predicción a varios pasos como criterio de identificación | `TITLE-ABS-KEY ( ( "MPC-relevant identification" OR "multi-step prediction error" OR "long-range prediction" OR "multistep prediction" ) AND identification )` |

- **R11:** S3 omite la dimensión diferenciadora (D1).
- **R12, comprobación esperada:** Rivera 2009 debe aparecer en S1 o S4; Bombois 2006 en S4; Machado 2023 y Mechhoud 2024 en S3. Si alguno no aparece, se amplía la cadena y se registra la variante (S3a…), o se justifica por qué no puede aparecer.

### Criterios de inclusión y exclusión (R4) `[AUTOR, 2026-11-03]`

**Dimensiones.** Las de `Instructivo_chequeo_acotado_P0.md` (sección 3), con D1 separada en dos:

| Dimensión | Cuenta como "sí" |
| --- | --- |
| **D1a** Excitación suave | Identifica el modelo con excitación suave, restringida o de mínimo costo, o con datos de operación normal |
| **D1b** Comparación | Compara esa excitación con una abrupta (PRBS, escalones grandes), o diseña la entrada minimizando la perturbación con un requisito de calidad del modelo |
| **D2** Estructura | Bilineal, LPV o física de pocos parámetros, con el caudal multiplicando a la temperatura |
| **D3** Predicción | Reporta como resultado el error de predicción a varios pasos (simulación libre u horizonte de MPC) |
| **D4** Sistema | Colectores o campo solar, receptor termosolar, o proceso térmico con caudal y calentamiento variables |

Cada dimensión se marca "sí", "no" o "nd" (no se puede saber con lo leído). En el cribado por resumen, "nd" cuenta como posible.

**Dos niveles de inclusión.**

| Nivel | Condición | Tratamiento |
| --- | --- | --- |
| **N1 · precedente** | D1a o D1b en "sí"/"nd", más al menos otra dimensión en "sí"/"nd"; **o** D2 y D3 en "sí"/"nd" | Lectura completa, registro de precedente (dimensión que toca y veredicto), seguimiento de citas si es coincidente o parcial. **Solo N1 cuenta para el veredicto** |
| **N2 · contexto** | Al menos una dimensión en "sí", sin cumplir N1 | Solo resumen. Se registra para la introducción y los métodos; no afecta el veredicto |

Clasificación esperada de los trabajos conocidos: Rivera 2009 y Machado 2023 (D1a) en N1; Bombois 2006, Mechhoud 2024, Pipino 2020 y Gil 2022 en N2. Si la lectura completa cambia una dimensión, el trabajo se reclasifica y se registra el cambio.

**Se excluye** si:
- trata solo fotovoltaica, o edificios sin caudal manipulado;
- solo diseña el controlador, sin identificar el modelo con datos;
- no puede leerse el texto completo (se registra como "no accesible", igual que Díaz-Salgado 2023).

**Lectura completa** de los incluidos, para fijar D1–D4 y la dimensión que tocan según la metodología (sistema, condición, observable, criterio o referencia).

**Volumen:** si una cadena da más de 300 resultados en una base, se acota con un filtro registrado (por ejemplo, área temática) antes de cribar. No se corta por relevancia sin registrarlo.

### Seguimiento de citas (R13)

Para cada R# con veredicto coincidente o parcial: referencias (hacia atrás) y citas en Scopus o WoS (hacia adelante), cribadas con los mismos criterios. Arranque previsto: Machado 2023, Rivera 2009 y Gil 2022.

### Presupuesto y registro (R6)

- Tiempo previsto: ≈ 6 h de búsqueda y cribado, más ≈ 4 h de lectura completa. `[AUTOR, 2026-11-03]`
- Se registran: hora de inicio y fin, total por cadena y base, n.º cribados por título, por resumen y por texto completo, y los incluidos.
- **La ejecución debe tener fecha posterior a la aprobación del protocolo (R1).**

## Salida canónica · P1 cerrada el 2026-11-03 (aprobada por el autor)

```text
BÚSQUEDA SISTEMÁTICA
  Protocolo .............. v1 (esta sección), aprobado por el autor
  Cadenas usadas ......... S1–S5 + variante S4a (R12); textuales en busqueda_P1/Registro_ejecucion.md
  Bases consultadas ...... Scopus, WoS, IEEE Xplore, Google Scholar (complemento)
  Fecha del protocolo .... 2026-11-03
  Fecha de ejecución ..... 2026-11-03 (desviación D-1 registrada; R1 se cumple)
  Tiempo usado ........... 82 min de ejecución + ≈ 10 min de S4a + ≈ 20 min de citas (autor);
                           cribado y lectura por Claude en la misma jornada

RESULTADO
  Nº total de resultados . 886 exportados; 568 únicos; + ≈ 200 por seguimiento de citas
  Incluidos tras cribado . 568 → 170 leídos por resumen → 45 N1 (confirmados por el autor)
                           → 25 con lectura completa (A y B) + 3 hacia atrás + 30 de C por resumen
  Trabajos relevantes .... 28 precedentes parciales (R1–R28); ninguno coincidente
  No accesibles .......... Díaz-Salgado 2023; Řehoř & Havlena 2009

REGISTRO DE PRECEDENTE  (detalle en P1_Registro_precedentes.md)
  Condición (excitación suave/operación frente a abrupta)
    R1  Bagle et al. 2026 ............ parcial · el más cercano; edificio, datos pasivos vs PRBS
    R9  Larsson et al. 2015 .......... parcial · planta industrial real, MPC-X vs lazo abierto
    R2  Braun et al. 2002 ............ parcial · multiseno de pasos pequeños vs PRS (simulación)
    R3  Rivera et al. 2009 (+R18) .... parcial · límite de tamaño de movimiento
    R26 Oshima et al. 2024 ........... parcial · excitación dirigida vs total (simulación)
  Sistema y estructura (colectores con caudal manipulado, modelo bilineal o físico)
    R21 Roca et al. 2008 ............. parcial · origen del modelo bilineal concentrado
    R5  Ampuño et al. 2019 (+R22) .... parcial · bilineal + retardos, calibrado con escalones
    R8  Medinelli Sanino 2007 ........ parcial · regresores T·u, predicción a k pasos
    R4  Machado et al. 2023 .......... parcial · EDP con datos de operación, simulación de días
    R6  Brus & Zambrano 2010 ......... parcial · caja negra, escalones de caudal
  Observable y criterio (error a varios pasos / simulación libre)
    R10 Záceková et al. 2014, 2015 ... parcial · MRI con datos reales de edificio
    R20 Zhan et al. 2022 ............. parcial · RMSE no refleja desempeño de control
  Resto (R7, R11–R17, R19, R23–R25, R27, R28) ... parcial, menor peso

VEREDICTO FINAL ......... PARCIAL SIN REFORMULACIÓN. Ningún trabajo reúne sistema, condición,
                          observable, criterio y referencia de H0; cada dimensión está cubierta
                          por separado. H0 v1 se mantiene; el enunciado de novedad se acota.

ENUNCIADO DE NOVEDAD .... (abajo)
```

### Enunciado de novedad (aprobado por el autor, 2026-11-03)

> Se ha mostrado que los modelos identificados con datos de operación normal o con excitaciones de baja perturbación pueden igualar o superar a los identificados con excitaciones abruptas (Bagle et al., 2026; Larsson et al., 2015), pero en ambos casos con modelos lineales en la entrada. En un colector solar la entrada manipulada, el caudal, multiplica a la temperatura y cambia la ganancia, la constante de tiempo y el retardo (Roca et al., 2008; Ampuño et al., 2019). Una excitación suave, que recorre menos rango de caudal, podría identificar peor justamente esa dependencia. No se ha comparado, en un mismo sistema de colectores con caudal manipulado y modelo bilineal, y bajo las mismas perturbaciones, un modelo bilineal de bajo orden identificado con una excitación suave y diseñada del caudal con el mismo modelo identificado con PRBS, evaluando el error de predicción al horizonte del MPC con un criterio de no inferioridad fijado de antemano. Este trabajo hace esa comparación en un banco de emulación de cuatro colectores en serie.

Notas de redacción:
- "Modelos lineales en la entrada" verificado en el texto completo: Bagle 2026 usa modelos grises 2R2C LTI/LTV lineales en la potencia de calefacción; Larsson 2015 formula MPC-X para un sistema lineal invariante en el tiempo.
- Braun et al. 2002 sale del enunciado y se cita en métodos, junto con Rivera et al. 2009, como antecedente de señales con pasos de entrada pequeños.
- Ampuño et al. 2018 y Medinelli Sanino y Rojas Reischel 2007 se citan en la introducción al describir la estructura bilineal.

### Consecuencias para P2

- **Amenaza a la validez** (Zhan et al., 2022): igual error de predicción no garantiza igual desempeño de control. Declararlo como límite o añadir una medida de control en lazo cerrado.
- **Comparación justa**: Bagle compara periodos distintos; H0 debe usar las mismas condiciones de potencia para ambas excitaciones (ya previsto).
- **Antecedentes de método** para la rampa limitada: Rivera et al. 2009 y la línea de Narasimhan (límites de tamaño de movimiento).
- **Motivación**: el tiempo de ensayo en plantas solares es escaso y dependiente del clima (Brus y Zambrano, 2010); los ensayos largos desgastan el equipo (Chook y Tan, 2007); la excitación persistente degrada el control (Núñez-Reyes y Bordons, 2005); un ensayo corto puede bastar (Leconte et al., 2012).

## Historial

| Fecha | Cambio | Motivo |
| --- | --- | --- |
| 2026-11-02 | Borrador del protocolo v1 | Inicio de P1 |
| 2026-11-03 | Bases: + IEEE Xplore y Google Scholar (complemento); idiomas con preferencia por inglés; presupuesto ≈ 6 h + 4 h | Decisión del autor |
| 2026-11-03 | Inclusión en dos niveles (N1 precedente, N2 contexto) con D1 separada en D1a/D1b; **protocolo v1 aprobado** | Decisión del autor tras comparar cinco alternativas: el criterio de P0 excluía a Mechhoud (R3) y Bombois, y D1 sin separar dejaba a Machado en "no" pese a usar datos de operación normal |
| 2026-11-03 | Búsqueda ejecutada (20 corridas, 82 min; `busqueda_P1/Registro_ejecucion.md`). Desviaciones D-1 a D-4 registradas en `P1_Cribado.md` | Ejecución del autor |
| 2026-11-03 | S4 y S5 se quedan con el límite 2000–2026 aplicado en la ejecución (desviación D-2 aceptada; no se repiten para años < 2000) | Decisión del autor: los trabajos anteriores serían N2 y no afectan el veredicto; se cubren con el seguimiento de citas hacia atrás |
| 2026-11-03 | Cribado por título y resumen propuesto (`P1_Cribado.md`, `busqueda_P1/Cribado_P1.csv`). R12: Rivera 2009 no reaparece → variante S4a propuesta; Mechhoud 2024 no reaparece, justificado | Claude; pendiente de confirmación del autor |
| 2026-11-03 | S4a ejecutada (Scopus 42, WoS 31; 39 registros nuevos): Rivera 2009 reaparece, R12 cumplido. Interpretaciones y lista N1 confirmadas; los registros de S4a se clasificaron con los mismos criterios (46 N1, 113 N2 en total) | Autor (ejecución y confirmación); Claude (cribado de S4a) |
| 2026-11-03 | PDF de prioridad A conseguidos (7 de 8). Řehoř & Havlena 2009 excluido por no accesible, igual que Díaz-Salgado 2023 | El autor no encontró el texto completo (actas de Elektroenergetika 2009, sin DOI) |
| 2026-11-03 | Lectura completa de prioridad A: 7 precedentes parciales (R1–R7, `P1_Registro_precedentes.md`); Micchi 2008 y Valenzuela 2020 reclasificados a N2. Veredicto provisional: parcial sin reformulación | Claude; pendiente de B, C y seguimiento de citas |
| 2026-11-03 | Lectura de prioridad B (16) y de Zhan 2022 (seguimiento hacia atrás): 13 precedentes parciales más (R8–R20); Gopaluni 2002 y Braun 2001 a N2. Veredicto provisional sin cambios. Quedan 41 N1 (7 A, 14 B, 20 C) | Claude |
| 2026-11-03 | Revisión de prioridad C (30): 6 precedentes parciales (R23–R28), 24 a N2. Salida canónica completada: veredicto parcial sin reformulación y enunciado de novedad propuestos | Claude; pendiente de aprobación del autor |
| 2026-11-03 | Enunciado de novedad reformulado: Bagle y Larsson agrupados por "modelos lineales en la entrada" (verificado en ambos textos); Braun 2002 pasa a métodos. **P1 cerrada** | Decisión del autor: la mención a edificios debía justificarse; el argumento lineal frente a bilineal explica por qué el resultado no se traslada |
| 2026-11-03 | Retorno NOV desde P2: en el enunciado, "sistema termosolar con caudal manipulado" pasa a "sistema de colectores con caudal manipulado y modelo bilineal" | Decisión del autor: P2 descartó afirmar que el banco representa un campo solar (C5); el enunciado no debe insinuarlo |
| 2026-11-03 | Seguimiento de citas hacia adelante (Scopus, 6 semillas; Bagle sin citas): 10 nuevos N1 de prioridad C, ninguno A o B. Veredicto sin cambios | Autor (exportación); Claude (cribado) |
| 2026-11-03 | Seguimiento hacia atrás desde Ampuño 2019: Roca 2008 (R21, origen del modelo bilineal) y Ampuño 2018 (R22) como precedentes parciales; Roca 2009 a N2. Veredicto sin cambios | Claude |

## Siguiente paso

Prioridades A y B leídas (`P1_Registro_precedentes.md`). Sigue: revisión de C (20), seguimiento de citas hacia atrás (Roca 2008, 2009; Ampuño 2018) y hacia adelante (citas de Bagle, Ampuño, Machado, Sanino, Larsson y Rivera 2009 en Scopus/WoS). Después: lectura completa, registro de precedentes y seguimiento de citas.
