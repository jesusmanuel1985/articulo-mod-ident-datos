# P1 · Registro de precedentes (lectura completa)

Entrada: N1 de prioridad A (`P1_Cribado.md`), PDF en `Articulos iniciales para leer/`. Lectura de Claude, 2026-11-03.
**Estado: completo (2026-11-03).** Prioridades A y B leídas, C revisada por resumen, seguimiento de citas hacia atrás y hacia adelante hecho. Veredicto y enunciado de novedad en `P1_Brecha_novedad.md`, pendientes de aprobación del autor.

## Elementos de H0 contra los que se compara

| Dimensión (metodología) | En H0 v1 |
| --- | --- |
| Sistema | 4 colectores FP3.0E en serie (banco de emulación); el caudal es la entrada manipulada; potencia binaria 0 ↔ 100 % |
| Condición | Excitación **suave y diseñada** del comando de caudal (≤ 2 L/h·s, amplitud ≥ 100 L/h, ≤ 400 L/h) frente a PRBS de caudal |
| Observable | T4 predicha a H = 1000 s (horizonte del MPC) |
| Criterio | No inferioridad: RMSE_H(suave) ≤ máx(1.5·RMSE_H(abrupta), RMSE_H(abrupta) + 0.5 °C) |
| Referencia | El mismo modelo bilineal de bajo orden identificado con PRBS |

## Registro (prioridad A)

Leyenda de D1a–D4: s = sí, p = parcial, n = no. "Toca" usa las dimensiones de la metodología.

| R# | Trabajo | D1a D1b D2 D3 D4 | Toca | Veredicto | Qué tiene y qué le falta respecto a H0 |
| --- | --- | --- | --- | --- | --- |
| R1 | **Bagle, Sartori & Goia 2026**, *Applied Energy* 414, 127756 | s s p s n | condición, observable, referencia | **parcial** (el más cercano) | Identifica un modelo gris 2R2C (LTV) de una sala de oficina con 2 semanas de **operación normal** y lo compara con el mismo tipo de modelo identificado con **PRBS** (otro periodo, sala desocupada), por NRMSE de **simulación a 24 h** en receding horizon. Los modelos de operación normal igualan o superan al de PRBS; con re-identificación diaria, hasta ≈ 200 % mejor. Los autores lo atribuyen a que el PRBS deja las condiciones de borde "lejos de la operación normal". **Le falta:** caudal como entrada (la entrada es potencia de radiador; el caudal de ventilación solo cambia de modo), estructura bilineal, excitación suave **diseñada** (usan datos pasivos), comparación en las mismas condiciones (periodos distintos y adaptación mezclada en el efecto) y criterio de no inferioridad. Cita a Zhan et al. 2022: con igual RMSE de predicción, el MPC con modelo de PRBS siguió mejor la referencia |
| R2 | **Braun, Ortiz-Mojica & Rivera 2002**, *Control Eng. Pract.* 10(3), 301–313 | s s n p p | condición, referencia | parcial | Multiseno de mínimo factor de cresta (**pasos de entrada más pequeños**, compatible con límites de velocidad del actuador) frente a **PRS multinivel**, en un CSTR no adiabático simulado (entrada: temperatura de camisa). El multiseno da RMS de validación menor o igual con una prueba 4,2 h más corta, y desempeño de MPC equivalente. **Le falta:** sistema real, caudal como entrada, modelo paramétrico (usa *Model-on-Demand*) y error a horizonte definido |
| R3 | **Rivera, Lee, Mittelmann & Braun 2009**, *J. Process Control* 19(4), 623–635 | s p n p p | condición | parcial | Diseño de multisenos con **límite explícito de tamaño de movimiento** (Δu_max) y de amplitud de salida, en una columna de destilación simulada (entradas: caudales de reflujo y de vapor). Compara contra multisenos sin restricción, no contra PRBS; evalúa en lazo cerrado. Es el antecedente de método de la rampa limitada de H0. **Le falta:** comparación con excitación abrupta, sistema térmico real, D3 |
| R4 | **Machado et al. 2023**, *Applied Energy* 339, 120944 | s n s s s | sistema, observable | parcial | Colector Fresnel real; modelo EDP con parámetros identificados (4 días) y ANFIS (19 días), todo con **datos de operación**; validación por **simulación libre de varios días** (6 días; error medio ≤ 0,51 °C, desviación ≤ 5,09 °C). **Le falta:** cualquier comparación de excitaciones; el error no se reporta a un horizonte de MPC |
| R5 | **Ampuño, Roca, Gil, Berenguel & Normey-Rico 2019**, *Solar Energy* 177, 241–254 | n n s s s | sistema, observable (estructura) | parcial | Campo de placa plana (AQUASOL II) con **caudal manipulado** y **modelo bilineal concentrado** (término Q·ΔT; Roca et al. 2008, 2009), calibrado con **escalones** de caudal, irradiancia y T de entrada; validación por RMSE y error máximo de simulación. Añade retardos aparentes que dependen del caudal. **Es la estructura más parecida a la de H0. Le falta:** comparación de excitaciones; horizonte de MPC |
| R6 | **Brus & Zambrano 2010**, *Control Eng. Pract.* 18(10), 1133–1146 | n n p s s | sistema, observable | parcial | Colectores de la planta de frío solar de Sevilla; caudal manipulado **con escalones** en un día parcialmente nublado; modelo de caja negra no lineal con retardo variable con el caudal; señala el carácter bilineal T·caudal; MSE de la **salida simulada**. Menciona que el tiempo de ensayo en la planta era limitado (planta compartida y necesidad de nubes): argumento útil para la motivación. **Le falta:** comparación de excitaciones |
| R7 | **Núñez-Reyes & Bordons 2005**, *CDC-ECC 2005*, 10.1109/CDC.2005.1582347 | s n n n s | condición, sistema | parcial | MPC con identificación simultánea en la planta solar de Sevilla: identifica un modelo de primer orden con retardo **durante la operación**, con |Δu| ≤ 20 %, y evita "el tedioso procedimiento de identificación" previo. Critica que imponer excitación persistente degrada el control. **Le falta:** comparación con excitación abrupta y error de predicción reportado |

## Registro (prioridad B y seguimiento de citas hacia atrás)

Lectura de Claude, 2026-11-03: resumen, conclusiones y secciones de método y datos de los 16 de prioridad B, más Zhan et al. 2022 (citado por Bagle 2026). p = parcial.

| R# | Trabajo | D1a D1b D2 D3 D4 | Toca | Veredicto | Qué tiene y qué le falta respecto a H0 |
| --- | --- | --- | --- | --- | --- |
| R8 | **Medinelli Sanino & Rojas Reischel 2007**, *Solar Energy* 81, 570–580 | p n s s s | sistema, observable (estructura) | parcial | Calentador solar de agua real (Viña del Mar). Modelo semifísico **lineal en los parámetros con regresores no lineales del tipo T·u** (temperatura × bomba), es decir, estructura bilineal; predicción a k pasos. La bomba es binaria (histéresis ON/OFF), así que los datos son de operación pero con excitación abrupta. **Le falta:** comparación de excitaciones; caudal continuo |
| R9 | **Larsson, Rojas, Bombois & Hjalmarsson 2015**, *J. Process Control* 31, 1–16 | s s n p p | condición, referencia | parcial | MPC con excitación (MPC-X) en una **depropanizadora industrial real, durante la operación normal**. Compara el modelo así obtenido con el de la identificación en lazo abierto de la puesta en marcha: ajuste 42 % frente a −200 % en datos de lazo cerrado, 19 % frente a 32 % en datos de lazo abierto; el desempeño de control mejora. **Le falta:** sistema con caudal y calentamiento como en H0, estructura bilineal, error a horizonte fijo |
| R10 | **Záceková, Váňa & Cigler 2014**, *Applied Energy* 135, 53–62; y **Záceková et al. 2015**, *ACC* | s n s s p | condición, observable, criterio | parcial | Edificios reales; identificación **con datos de operación real** (sin experimento dedicado) y **minimización del error de predicción a varios pasos** (MRI); error medio ≈ 0,3 °C a 2 días, donde el modelo gris de un paso resultó inestable. En 2015 el MPC manipula caudal másico de la UTA. **Le falta:** comparación con excitación abrupta |
| R11 | **Sturzenegger et al. 2014**, *IFAC WC* | n p s s p | condición, observable | parcial | Sala de oficina real: ETFE con **PRBS** (≥ 3 periodos de 17 h) frente a ensayo de **relé** (más corto), y modelo RC físico; validación de predicción en 134 h. Compara experimentos por eficiencia de tiempo, no por suavidad (ambas excitaciones son abruptas). **Le falta:** excitación suave; caudal manipulado (caudal de aire constante) |
| R12 | **Toyoda & Wada 2001**, *Electr. Eng. Japan* 137(2), 26–35 | n n p s s | sistema, observable | parcial | Caldera de central térmica real: ARX con parámetros que dependen de la carga (tipo LPV), con caudal en el modelo físico del intercambiador; predicción a varios pasos. Identificado en lazo cerrado con **secuencia M** (tipo PRBS) a carga fija. **Le falta:** excitación suave y comparación |
| R13 | **Chook & Tan 2007**, *IEEE TIM* 56(6), 2262–… | n n s p p | estructura | parcial | Horno eléctrico real: **el modelo bilineal ajusta mejor que el lineal y el dependiente de dirección**. Identificado con **escalones** (no ensayos continuos de más de ~50 h para no acortar la vida del horno: argumento de costo del experimento). Entrada: potencia (PWM), sin caudal |
| R14 | **Mendes, Normey-Rico et al. 2014**, *IREC* | n n s p s | sistema, estructura | parcial | Campo solar con caudal manipulado; **predictor bilineal por subespacios** identificado de datos, dentro de un control con predictor de Smith. Simulación. **Le falta:** comparación de excitaciones y error de predicción reportado |
| R15 | **Saloux & Candanedo 2018**, *J. Build. Perform. Simul.* | s n s p s | sistema, observable | parcial | Comunidad solar real (Drake Landing): modelos RC de colectores, tanques y almacenamiento estacional, **calibrados con 2 años de operación**; predicción con actualización periódica de estado |
| R16 | **Rathod et al. 2019**, *J. Process Control* 76, 74–86 | s n s p s | sistema | parcial | Planta de frío solar real: modelos físicos + identificación, validados con datos de operación; MPC híbrido con horizonte de 6 h |
| R17 | **Si et al. 2026**, *Appl. Therm. Eng.* 289, 129730 | s n p p s | sistema, observable | parcial | Campo cilindroparabólico de 50 MW, datos de operación; modelo físico + red neuronal correctora en esquema rodante; MAE y R² de la T de salida |
| R18 | **Lee, Rivera et al. 2007** (*ACC*) y **Rivera et al. 2007** (*IEEE CSM* 27(5)) | s p n p p | condición | parcial | Misma línea que R3: multisenos *plant-friendly* con restricciones, destilación simulada; comparación entre diseños de multiseno, no contra PRBS. Se citan junto con Rivera 2009 |
| R19 | **Yang & Rivera 2001**, *ACC* | s n n n p | condición | parcial | Identificación en lazo cerrado iterativa con MPC en un CSTR simulado; la restricción de tamaño de movimiento (Δu_max = 0,5) estabiliza la convergencia. **Le falta:** casi todo lo demás |
| R20 | **Zhan, Lei, Jin, Yan & Chong 2022**, *Applied Energy* 323, 119580 (hacia atrás desde Bagle) | s p s p n | condición, criterio | parcial | Simulación de edificios con modelos RC: con datos de **operación normal** (consigna fija) basta en una zona, pero el caso multizona necesitó consignas variables para tener excitación suficiente. **Datos más informativos dieron seguimiento más robusto en MPC sin que se reflejara en el RMSE**: el RMSE no basta como indicador de desempeño de control |

**Bajan a N2 tras la lectura:** Gopaluni et al. 2002 (diseño de espectros óptimos para MRI con restricción de potencia, solo teoría y simulación: D3 = s, D1 = n) y Braun, Rivera & Stenman 2001 (diseño de PRS multinivel para *Model-on-Demand*; compara métodos de estimación, no señales).

## Reclasificados tras la lectura completa

| Trabajo | Antes | Ahora | Motivo |
| --- | --- | --- | --- |
| Micchi & Pannocchia 2008, *J. Process Control* 18(6), 582–593 | N1-A | **N2** | Solo simulación con modelos lineales de destilación. Compara datos de lazo cerrado con setpoints aleatorios frente a GBN de lazo abierto, por **direcciones** de excitación (sistemas mal condicionados), no por suavidad; evalúa error de respuesta en frecuencia y desempeño de MPC. D1a = n, D1b = p, D2–D4 = n |
| Valenzuela et al. 2020, *IEEE TCST* 28(5), desde p. 1681 | N1-A | **N2** | El diseño **maximiza la información** (log det de Fisher) con entrada de válvula entre 10 y 90 %; compara contra ruido blanco solo por información, no por perturbación ni por error de predicción. D1a = n, D1b = n, D4 = s |

## Lectura de conjunto (provisional, a confirmar con C y el seguimiento de citas hacia adelante)

Ningún trabajo leído (A y B) reúne las cinco dimensiones de H0. Cada una está cubierta por separado:

- **Condición** (excitación suave o de operación frente a abrupta): Bagle 2026 (datos de operación frente a PRBS, edificio real), Larsson 2015 (excitación en operación normal frente a identificación en lazo abierto, planta industrial real), Braun 2002 (multiseno de pasos pequeños frente a PRS, simulación), Rivera 2009 y su línea (límite de tamaño de movimiento).
- **Sistema y estructura** (colector con caudal manipulado, modelo bilineal o físico): Ampuño 2019, Sanino 2007 (regresores T·u), Mendes 2014 (predictor bilineal), Machado 2023, Brus 2010; fuera del dominio solar, Chook & Tan 2007 (bilineal mejor que lineal en un horno).
- **Observable y criterio** (simulación libre o error a varios pasos): Bagle 2026, Záceková 2014, Sanino 2007, Machado 2023, Ampuño 2019, Brus 2010, Toyoda 2001.

El trabajo que más se acerca por el lado del sistema es Sanino 2007 (estructura bilineal y predicción a k pasos en un sistema solar con bomba), pero su excitación es la operación ON/OFF de la bomba, sin comparación. Por el lado de la condición, Bagle 2026 y Larsson 2015, ambos en sistemas sin la dinámica bilineal caudal–temperatura.

La combinación de H0 (excitación suave **diseñada** del caudal, comparada con PRBS en el **mismo** sistema y periodo, con el modelo bilineal de colectores, evaluada a **H = 1000 s** con criterio de no inferioridad) no aparece.

**Veredicto provisional: parcial, sin reformulación de H0.** El enunciado de novedad debe:

1. reconocer que la ventaja de los datos de operación normal o de la excitación restringida sobre la excitación abrupta ya se observó en edificios (Bagle 2026), en una planta industrial (Larsson 2015) y en simulación de procesos químicos (Braun 2002);
2. situar la contribución en la transferencia y prueba de esa comparación a un sistema con **caudal manipulado y dinámica bilineal**, donde la excitación suave cambia el punto de operación y, con él, la ganancia y la constante de tiempo;
3. usar Ampuño 2019 y Sanino 2007 como referencias de la estructura bilineal, y Chook & Tan 2007 como apoyo de que lo bilineal mejora a lo lineal en procesos térmicos.

**Amenaza a la validez** (para P2), confirmada al leer Zhan et al. 2022: datos más informativos dieron mejor seguimiento en MPC **sin diferencia en el RMSE de predicción**. H0 mide error de predicción, no desempeño de control; hay que declararlo como límite o agregar una medida de control.

**Argumentos para la motivación** que aparecen en la lectura: el tiempo de ensayo en plantas solares es escaso y depende del clima (Brus 2010); los ensayos prolongados acortan la vida del equipo (Chook & Tan 2007); imponer excitación persistente degrada el control (Núñez-Reyes 2005).

## Seguimiento de citas hacia atrás desde Ampuño 2019 (R13): resultado

Leídos el 2026-11-03 (resumen, conclusiones y secciones de modelo y validación).

| R# | Trabajo | D1a D1b D2 D3 D4 | Toca | Veredicto | Nota |
| --- | --- | --- | --- | --- | --- |
| R21 | **Roca, Berenguel, Yebra & Alarcón-Padilla 2008**, *Solar Energy* 82(9), 772–786 | n n s p s | sistema, estructura | parcial | **Origen del modelo bilineal concentrado** (caudal × gradiente de temperatura) del campo CPC de AQUASOL (PSA), con retardos de transporte; pérdidas térmicas calibradas con datos reales (escalones) y validación contra la planta; usado para control por linealización por realimentación. Referencia obligada para la estructura del modelo de H0 |
| R22 | **Ampuño, Roca, Berenguel, Gil, Pérez & Normey-Rico 2018**, *Solar Energy* 170, 369–378 | n n s s s | sistema, estructura, observable | parcial | Modelo del campo de placa plana de AQUASOL-II (balances + retardos obtenidos con **escalones** de caudal y T de entrada); RMSE de simulación 0,6–1,3 °C por lazo. Antecesor directo de R5; se cita junto con Ampuño 2019 |

Roca, Guzmán, Normey-Rico, Berenguel & Yebra 2009 (*Control Eng. Pract.* 17(9), 1076–1088) queda en **N2**: usa el mismo modelo bilineal para un control GPC con linealización y predictor de Smith; no aporta identificación.

Ninguno compara excitaciones: los tres identifican o calibran con escalones o datos de operación. Confirman que la estructura bilineal de colectores con caudal manipulado está establecida, y que la condición de H0 (excitación suave diseñada frente a PRBS) no se ha probado en ella.

## Revisión de prioridad C (30 trabajos: 20 de la búsqueda y 10 del seguimiento hacia adelante)

Revisión de Claude por resumen, 2026-11-03. Se mantienen 6 como precedentes parciales; 24 bajan a N2.

| R# | Trabajo | D1a D1b D2 D3 D4 | Toca | Veredicto | Nota |
| --- | --- | --- | --- | --- | --- |
| R23 | Liu et al. 2002 y 2004 (*TENCON*); Zhang et al. 2015 (congreso) | s p n n p | condición | parcial (débil) | Identificación de procesos térmicos de centrales con **datos de operación**; Liu afirma que la precisión no depende del tipo de entrada (escalón o señal de operación aleatoria), sin comparación cuantitativa. Congresos de alcance limitado |
| R24 | Moghaddam & Marques 2026, *ICCAD* | s n s p s | sistema, observable | parcial | Instalación solar térmica real: modelo físico (TRNSYS) frente a ARX y regresión polinómica con datos IoT de operación |
| R25 | Esmaili, Li, Xie & Isom 2018, *Control Eng. Pract.* 72, 206–218 | s n n n p | condición | parcial | Identificación en lazo cerrado **solo con realimentación, sin excitación añadida**, en plantas con MPC, validada en una planta industrial de hidrógeno; motivación: los ensayos en lazo abierto son costosos |
| R26 | Oshima, Kim, Shardt & Sotowa 2024, *J. Process Control* 136, 103190 (y 2022, *CACE* 49) | s s n n p | condición, referencia | parcial | **Excitación dirigida** (solo las entradas con desajuste) frente a excitar todas: mejor control durante el ensayo y mejor modelo después; FCC simulado |
| R27 | Leconte, Achard & Papillon 2012, *Solar Energy* 86(7), 2001–2016 | p n p s s | sistema, observable | parcial | Sistema combinado solar real: modelo gris identificado con un **ensayo corto de 12 días** predice el desempeño anual en 27 entornos |
| R28 | Castilla, Redondo, Martínez & Álvarez 2024, *Eng. Appl. Artif. Intell.* 133, 108387 | s n n p s | sistema, observable | parcial | Gemelo digital con red neuronal del campo de placa plana de CIESOL, entrenado con un año de operación |

**Bajan a N2 (24):** Alsharkawi & Rossiter 2017, Halvgaard 2012, Gil 2014, Li 2015, Fan 2025 (control o modelos sobre simulación); Lee & Rivera 2005 (×2), Rivera 1998, Mittelmann 2007 (línea de Rivera, ya representada por R3 y R18); Ghosh 2014 (×2), Parker 2001, Maner & Doyle 1997, Soni & Parker 2007 (diseño de excitación para destilación o modelos Volterra, simulación); Baier 2023, Khimani 2026 (LPV fuera de dominio); Chinen 2025 (PRBS frente a multiseno, ambas excitaciones diseñadas para información); Otálora 2026, Zhang 2025, Kishor 2010, Khalfallaoui 2011, Rodríguez-Ossorio 2025.

## Seguimiento de citas hacia adelante (R13): resultado

Hecho el 2026-11-03 con las exportaciones *Cited by* de Scopus (detalle en `busqueda_P1/Cribado_citas_adelante.md`). Bagle 2026 no tiene citas. De ≈ 200 trabajos que citan a las otras cinco semillas, **ninguno llega a prioridad A o B**; quedan 10 nuevos N1 de prioridad C (p. ej., Chinen 2025: PRBS frente a multiseno en una planta piloto real; Oshima 2024: excitación dirigida para no degradar el control; Leconte 2012: modelo gris de un sistema solar identificado con un ensayo corto). El veredicto no cambia.

## Seguimiento de citas (R13): semillas

| Semilla | Hacia atrás | Hacia adelante |
| --- | --- | --- |
| Bagle 2026 | ~~Zhan et al. 2022~~ (leído, R20); Arroyo et al. 2020 (*J. Build. Perform. Simul.* 13(4), 472–486); Madsen et al. 2015 (IEA Annex 58) | Probablemente pocas (2026) |
| Ampuño 2019 | Roca et al. 2008, *Solar Energy* 82(9), 772–786, 10.1016/j.solener.2008.03.002; Roca et al. 2009, *Control Eng. Pract.* 17(9), 1076–1088, 10.1016/j.conengprac.2009.04.008; Ampuño et al. 2018, *Solar Energy* 170, 369–378, 10.1016/j.solener.2018.05.076 | Citas en Scopus/WoS |
| Sanino 2007 | — | Citas en Scopus/WoS |
| Larsson 2015 | — | Citas en Scopus/WoS |
| Machado 2023 | (previsto en el protocolo) | Citas en Scopus/WoS |
| Rivera 2009 | Godfrey et al. (comparación de señales de perturbación); Doyle et al. 1999 | Citas en Scopus/WoS |
| Gil et al. 2022 (revisión) | Sección de modelado y control de campos solares | — |
