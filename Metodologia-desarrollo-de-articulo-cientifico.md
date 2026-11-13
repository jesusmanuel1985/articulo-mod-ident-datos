# Metodología por fases para artículos científicos

## Escalera y cobertura

La metodología recorre once fases, de P0 a P10. Todas están redactadas; las decisiones abiertas se listan en Pendientes.

| Fase | Nombre | Propósito | Estado |
| --- | --- | --- | --- |
| P0 | Pregunta motriz e hipótesis | Fijar, antes de la evidencia, qué se pregunta, qué se espera y qué resultado lo refutaría | Redactada |
| P1 | Brecha y novedad | Someter el veredicto provisional de P0 a una búsqueda sistemática y fijar el enunciado de novedad | Redactada |
| P2 | Claims | Convertir H# en afirmaciones atómicas, tipificadas y con etiqueta de confirmación | Redactada |
| P3 | Jerarquía | Hacer explícito qué sostiene qué antes de invertir en evidencia | Redactada |
| P4 | Evidencia | Asignar evidencia a cada hoja del grafo: especifica en modo A, audita en modo B | Redactada |
| P5 | Diseño de experimento | Instrumentar la evidencia planificada, con criterios de validez fijados antes de adquirir | Redactada |
| P6 | Ejecución y adquisición | Ejecutar el ensayo y emitir su desenlace: sostenido, NEG, PAR o INV | Redactada |
| P7 | Estructura y plan de figuras | Fijar el orden argumental y la figura que sostiene cada claim, antes de redactar | Redactada |
| P8 | Redacción | Producir el texto a partir de las salidas previas | Redactada |
| P9 | Verificación | Métricas, lector frío (comprensibilidad) y revisor experto (corrección técnica) | Redactada |
| P10 | Cierre | Checklist final y archivo del registro | Redactada |

**Modos.** El modo se declara por claim. En modo A (investigación) los datos están por generar: P4 especifica la evidencia, P5 diseña el ensayo y P6 lo ejecuta. En modo B (auditoría) los datos ya existen: P4 audita la cobertura, y P5 y P6 solo se usan para ensayos acotados (HUE). Un artículo con claims de ambos modos es mixto.

**Matriz de cobertura.** Cada atributo que la metodología pretende garantizar queda asignado a las fases que lo verifican.

| Atributo | Fases que lo aseguran |
| --- | --- |
| Relevante | P0 (consecuencia para ambos resultados), P1 |
| Novedoso | P0 (chequeo acotado), P1 (búsqueda sistemática), P2 (regla de novedad) |
| Robusto | P4 (paridad y anclaje), P5, P6, P9 |
| Honesto | P0 (registro de predicciones), P1 (búsqueda documentada), P4 (exclusiones y anclaje), P9, P10, protocolo de IA |
| Comprensible | P3 (lectura de la jerarquía), P7, P8, P9 (lector frío) |

## Plantilla canónica y reglas de construcción

Toda fase se redacta con la misma plantilla. Los campos son obligatorios salvo IA y Notas.

```text
FASE P<n> — <nombre>
Propósito ............ una línea: qué decisión queda tomada al cerrar la fase

ENTRADA .............. objetos de fases previas, por ID
SALIDA CANÓNICA ...... formulario con estructura fija; cada objeto con ID
REQUISITOS ........... checklist binaria (sí/no), numerada R1…Rn
MODOS DE FALLO ....... código P<n>.<XXX> · fallo · requisito que lo detecta
RETORNOS QUE EMITE ... destino · código del grafo · condición en una línea
                       (o "Ninguno" + qué ocurre si la fase no se completa)
AVANCE ............... qué entrega a la fase siguiente
RETORNOS QUE RECIBE .. código · origen · acción que se ejecuta aquí
REGISTRO MÍNIMO ...... lo que un tercero necesita para reproducir la decisión
IA (opcional) ........ delegable · no delegable · cómo se verifica
NOTAS (opcional) ..... fronteras con otras fases y propagaciones
```

**Reglas de construcción**

1. La salida canónica es un formulario. Si la fase no puede llenarlo, la fase no está completa.
2. Los requisitos son binarios. Palabras como "razonable" o "suficiente" están prohibidas; lo cualitativo pasa a ser un campo de salida. Un requisito binario verifica que el juicio se hizo y quedó registrado, no que sea correcto (ver GARANTÍA en campos transversales).
3. Todo modo de fallo tiene código y corresponde al menos a un requisito que lo detecta. Un fallo sin detector es decoración.
4. Los retornos van siempre hacia una fase anterior y su condición cabe en una línea. El avance y la entrada no se listan como retornos. Los códigos se toman del grafo; un código nuevo exige actualizar el grafo.
5. Una fase puede no emitir retornos. En ese caso declara qué ocurre si no se completa (por ejemplo, descartar o postergar la idea), y esa decisión se registra.
6. Toda fase declara qué acción ejecuta ante cada retorno que recibe.
7. El registro mínimo no es exhaustivo: contiene lo necesario para que un tercero reproduzca cada decisión.

## Campos transversales

Estos campos rigen en todas las fases; ninguna fase repite su contenido, para que no existan copias divergentes.

```text
MODO            Se declara POR CLAIM: A (investigación) | B (auditoría).
                Un artículo con claims de ambos modos es "mixto".

NOMENCLATURA    objetos:  H#  C#  E#  F#  R#  S# (premisa)  J# (grafo)
                fallos:   P<n>.<XXX>   (p. ej., P3.DESC)
                retornos: lista cerrada en el grafo de retornos.
                          Un código nuevo exige actualizar el grafo.
                paridad:  PA1…PA6 (categorías de P4)

IDENTIFICADORES H# identifica el par pregunta‑hipótesis (versionado junto).
                C0 es siempre el claim raíz.
                Un ID no se reutiliza; si el objeto cambia, cambia
                la versión, no el ID.

ETIQUETAS       a cada C#: confirmatorio | exploratorio.
                A H#: solo en modo B (confirmatorio en modo A por
                construcción). Registrar qué datos se habían visto.

VERSIONADOS     H#                     pregunta e hipótesis (P0)
                ficha P1               protocolo y ficha de novedad
                C‑set                  tabla de claims (P2)
                J#                     grafo de jerarquía (P3)
                E‑set                  evidencia, incluidas exclusiones
                límite de factibilidad (P0; fijado antes de veredictos)
                diseño P5              criterios de aceptación y validez
                F‑set                  plan de figuras (P7)

VERSIÓN         fecha + versión. Un objeto cambia de versión solo si
                se modifica DESPUÉS de cerrada su fase; las ediciones
                con la fase abierta son borrador.

IA              toda cifra o referencia producida por IA se verifica
                contra fuente primaria; uso declarado según revista.

GARANTÍA        la plantilla garantiza que el juicio se hizo y quedó
                registrado; NO que sea correcto.
                Comprensibilidad → P9 lector frío (ajeno al área).
                Corrección técnica → P9 revisor experto interno
                o revisión por pares externa.
```

## Grafo de retornos

La escalera es un grafo con 20 retornos tipados: 12 de construcción, que son el flujo normal de trabajo, y 8 de auditoría, que salen de P9 y P10 y señalan defectos detectados tarde.

### Retornos de construcción

Los dispara una fase de producción al consumir su entrada o generar su salida.

| Borde | Código | Condición |
| --- | --- | --- |
| P1 → P0 | PRE | Brecha inexistente o parcial que exige modificar H# |
| P2 → P1 | NOV | Claim no cubierto por el enunciado de novedad |
| P3 → P2 | RTP | Claim faltante o mal tipificado |
| P4 → P2 | SEV | Claim sin evidencia o paridad violada: debilitar o eliminar (C0: no concluyente) |
| P4 → P3 | PNS | Premisa no sostenida: reestructurar la jerarquía |
| P4 → P5 | HUE | Modo B: hueco o paridad violada que exige ensayo acotado (tope: uno por claim) |
| P5 → P4 | NOB | Evidencia especificada no obtenible |
| P6 → P2 | NEG | Hipótesis o claim refutado: cambio de signo |
| P6 → P2 | PAR | Sostenido en parte: claim acotado más claim L; P0 intacta |
| P6 → P5 | INV | Ensayo inválido, incluida paridad violada en modo A: rediseñar y reejecutar (reintentos ≤ N fijado en P5, todos reportados) |
| P7 → P4 | FSD | Figura sin dato que sostenga su claim |
| P8 → P7 | RED | La prosa no puede narrar el ancla sin ambigüedad: reestructurar el display item sin modificar los datos |

La reentrada P6 → P4 (tras un HUE, o ante un desenlace no concluyente en cualquier modo) no lleva código: es la continuación prevista del ciclo, y su desenlace se registra en P4.

### Retornos de auditoría

Salen de P9, salvo CRN y la segunda vía de EVT, que salen de P10. El color indica qué tan atrás está el defecto.

| Color | Borde | Código | Condición |
| --- | --- | --- | --- |
| Verde | P9 → P8 | PRO | Defecto de prosa |
| Amarillo | P9 → P7 | EST | Defecto de estructura o figuras |
| Amarillo | P9 → P3 | JER | Defecto de jerarquía |
| Amarillo | P9 → P2 | AUS | Límite o claim ausente |
| Rojo | P9 → P4 | EVT | Evidencia tardía: incidente, auditar P0–P3 y P7 |
| Amarillo | P9 → P1 | PRC | Precedente omitido: revisar la ficha y el enunciado de novedad; H# no se modifica |
| Amarillo | P10 → P2 | CRN | Violación cronológica: los claims afectados pasan a exploratorios; P8 actualiza la transparencia y P9 reaudita |
| Rojo | P10 → P4 | EVT | La reproducción en entorno limpio discrepa de P8: incidente, auditar P0–P3 y P7 |

Verde: defecto en la fase inmediatamente anterior. Amarillo: defecto en una fase previa que no compromete la evidencia. Rojo: defecto que compromete la evidencia y abre un incidente.

**Diagnóstico del lector frío.** Cuando el lector frío no logra enunciar un elemento, el destino depende de la causa.

| El lector no enuncia | Causa | Retorno |
| --- | --- | --- |
| La pregunta o la respuesta | Jerarquía confusa | P9 → P3 (JER) |
| La pregunta o la respuesta | Estructura o figuras | P9 → P7 (EST) |
| El límite | No existe como claim | P9 → P2 (AUS) |
| El límite | Existe, pero mal ubicado en la jerarquía | P9 → P3 (JER) |
| El límite | Existe y está bien ubicado, pero no se ve | P9 → P7 (EST) o P9 → P8 (PRO) |
| La novedad | No se distingue del contexto en la estructura | P9 → P7 (EST) |
| La novedad | Redacción ambigua o diluida en el resumen | P9 → P8 (PRO) |

### Reglas de registro

1. Todo retorno se registra en una línea: fecha, código, objeto modificado y motivo.
2. INV se reporta además en el artículo, con su causa.
3. EVT abre un incidente interno (auditoría de P0–P3 y P7); no se reporta en el artículo.
4. La frecuencia de amarillos y rojos por fase, acumulada entre artículos, indica qué fase reforzar.

### Invariantes

- P0 solo recibe PRE desde P1. Ningún otro retorno llega a P0.
- Después de la evidencia, la pregunta no cambia: NEG y PAR modifican claims (P2), nunca H#.
- Los criterios de validez del ensayo se fijan en P5 antes de adquirir; sin ellos, INV no puede invocarse.
- El límite de factibilidad se fija antes de los veredictos de cobertura; sin él, HUE no puede invocarse.
- Un HUE por claim; los reintentos por INV no consumen ese tope.
- Si H# es exploratoria, C0 es exploratorio.

## P0 — Pregunta motriz e hipótesis

**Propósito:** fijar, antes de la evidencia, qué se pregunta, qué se espera y qué resultado lo refutaría.

### Entrada

- Idea difusa que motiva el trabajo
- Modo previsto por claim (A o B); el artículo es mixto si habrá ambos
- Modo B: inventario de datos existentes

### Salida canónica (formulario H#, versión, fecha)

```text
PREGUNTA
  Tipo .................. desempeño
                          (única plantilla vigente; caracterización y
                           mecanismo quedan pendientes)
  Sistema ............... <objeto físico o modelo identificado>
  Observable ............ <magnitud + unidad>
  Criterio .............. <métrica + umbral numérico>
  Referencia ............ <línea base o rival nombrable>
  Condición de prueba ... <rango, ensayo, estación, régimen>
  Restricción ........... <recurso o limitación dada>

  Frase: ¿[Sistema] [verbo] [Observable] con [Criterio]
         respecto de [Referencia], en [Condición],
         dado [Restricción]?

HIPÓTESIS ............... <Sí | No>, porque <mecanismo esperado>
REFUTACIÓN .............. H# es falsa si <resultado observable concreto>

CONSECUENCIA
  Si se confirma: cambia <X> para <quién>
  Si se refuta:   se aprende <Y>

TRIVIALIDAD — Dirección
  Quién predice ......... <autor | colega | IA como segundo predictor>
  Respuesta predicha .... <sí | no>
  Confianza ............. <baja | media | alta>
  Tipo de motivación .... física | evidencia previa (R#) |
                          experiencia | construcción
  Motivación ............ <una línea>

TRIVIALIDAD — Magnitud  (obligatoria si la confianza de dirección es alta)
  Valor predicho ........ <número o banda sobre el criterio>
  Confianza ............. <baja | media>   (no "alta")
  Quién / cuándo ........ <quién> · <fecha> · versión de H#

MEDIBILIDAD
  Fuente del observable . <instrumento | simulación | base de datos>
  Incertidumbre esperada vs efecto que define el criterio

FICHA DE NOVEDAD PROVISIONAL
  Trabajos más cercanos (máx. 3): R1, R2, R3 — por qué es cercano
  Diferencia declarada .. <dimensión>: <en qué difiere>
  Veredicto ............. abierta | parcial | respondida
  Esfuerzo usado ........ <minutos> min · bases: <lista> ·
                          revisión: R# (<año>) · cadenas: <texto>

LÍMITE DE FACTIBILIDAD  (objeto versionado propio; no forma parte
                         de la frase ni de H#)
  Presupuesto de rescate  <tiempo, horas de banco, costo o recursos
                           disponibles para un ensayo acotado>
  Fecha / versión ....... <fecha> · v<n>

SOLO MODO B
  Datos vistos al formular ... <lista>
  Anclaje confirmatorio ...... subconjunto reservado | ensayo acotado
                               comprometido | ninguno → H# etiquetada
                               "exploratoria"
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | El sistema es un objeto o modelo identificable, no una clase |
| R2 | El observable tiene unidad |
| R3 | El criterio tiene umbral numérico |
| R4 | La referencia es nombrable (método, modelo, controlador) |
| R5 | La condición de prueba está acotada |
| R6 | La refutación cabe en una línea y es un resultado observable |
| R7 | Ningún verbo aspiracional aparece en la frase (lista: contribuir, explorar, avanzar, desarrollar, estudiar, investigar) |
| R8 | Hay un solo observable principal y una sola refutación |
| R9 | La consecuencia está declarada para ambos resultados |
| R10 | La predicción de dirección está registrada: quién, respuesta y confianza |
| R10b | La motivación está registrada con un tipo de la taxonomía. La asigna el autor; su corrección la audita el revisor experto en P9 |
| R10c | Si la confianza de dirección es alta: el tipo de motivación no es "construcción" y existe predicción de magnitud con confianza baja o media |
| R10d | Si la motivación cita un R#, ese R# está en la ficha de novedad |
| R10e | Dirección y magnitud registran quién, cuándo y versión de H# |
| R11 | Ficha de novedad completa, veredicto distinto de "respondida" y esfuerzo en rango: 30 a 120 min, ≥ 1 revisión de ≤ 5 años, ≥ 2 bases, ≤ 3 trabajos cercanos |
| R11b | El chequeo registra las cadenas de búsqueda textuales |
| R12 | La incertidumbre esperada es menor que el efecto que define el criterio |
| R13 | (Modo B) Los datos vistos al formular están listados |
| R13b | (Modo B) Hay anclaje confirmatorio declarado, o H# está etiquetada "exploratoria" de forma explícita |
| R14 | H# tiene fecha y versión |
| R15 | El límite de factibilidad está registrado con fecha y versión, separado de la restricción de la pregunta |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P0.OBJ | Objetivo en lugar de pregunta: la frase no admite respuesta sí/no | R7 |
| P0.CIRC | Circular: la refutación es imposible por construcción | R6 |
| P0.AMP | Amplia: cambiar el sistema por un análogo no altera nada de la frase | R1 |
| P0.COMP | Compuesta: dos observables o dos refutaciones | R8 |
| P0.UMB | Sin umbral | R3 |
| P0.REF | Sin referencia | R4 |
| P0.INMED | Inmedible: incertidumbre mayor o igual que el efecto | R12 |
| P0.MOT | Confianza sin motivación, o tipo fuera de la taxonomía | R10b |
| P0.INCON | La motivación cita un R# que no está en la ficha | R10d |
| P0.POSTH | Magnitud ingresada después de ver el dato | R10e |
| P0.TRIV | Trivial: confianza alta y (tipo "construcción" o magnitud también predecible con confianza alta) | R10c |
| P0.SANC | Modo B sin anclaje confirmatorio y sin etiqueta "exploratoria" | R13b |
| P0.PREC | Pregunta ya respondida | R11 |
| P0.CHQ | Chequeo acotado fuera de rango de tiempo o fuentes | R11 |
| P0.IRREP | Búsqueda sin cadenas registradas | R11b |
| P0.LIMFAC | Límite de factibilidad ausente o fusionado con la restricción | R15 |

### Retornos que emite

Ninguno. Si la idea no produce una H# que cumpla todos los requisitos, se descarta o se posterga, y la decisión se registra.

### Avance

Hacia P1: H# con su ficha de novedad provisional, la diferencia declarada, el modo y las etiquetas.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| PRE | P1 | Reformular sobre la dimensión donde P1 halló precedente; nueva versión de H#; en modo B, registrar como posterior a datos |

Ningún otro retorno llega a P0. NEG y PAR van a P2; INV va a P5.

### Registro mínimo

- H# con historial de versiones, fechas y motivo de cada cambio
- Formulario completo de la salida canónica
- Chequeo acotado: cadenas de búsqueda, bases y tiempo usado
- Predicción de dirección (quién, cuándo, confianza, tipo y motivación)
- Predicción de magnitud, si aplica, con quién y cuándo
- Límite de factibilidad con fecha y versión
- Modo B: datos vistos y anclaje confirmatorio declarado
- Ideas descartadas en P0 y su causa

### IA (opcional)

- Delegable: detectar P0.OBJ, P0.CIRC, P0.AMP y P0.COMP por patrón léxico; sugerir trabajos cercanos (cada R# se verifica en fuente primaria antes de entrar a la ficha).
- No delegable: criterio, umbral, referencia, límite de factibilidad y predicciones de dirección y magnitud. La IA puede actuar como segundo predictor, pero se registra como tal y no reemplaza el juicio humano.

### Notas

1. Frontera P0/P1: si al llegar al límite de esfuerzo el veredicto es parcial o incierto, la ficha se marca "parcial" y P1 asume la tarea. El chequeo acotado no se extiende.
2. Propagación a P2: C0 no puede ser más fuerte que H#. Una H# exploratoria no produce un C0 confirmatorio.
3. La corrección técnica de P0 no se decide aquí; se audita en P9 (revisor experto) y en la revisión por pares.
4. Los valores de R11 son valores por defecto, ajustables según el campo.

## P1 — Brecha y novedad

**Propósito:** someter el veredicto provisional de P0 a una búsqueda sistemática y documentada, y fijar el enunciado de novedad.

### Entrada

- H# con su ficha de novedad provisional
- Diferencia declarada en P0 (dimensión y en qué difiere)
- Modo y etiquetas heredadas de P0

### Salida canónica (ficha de novedad definitiva)

```text
BÚSQUEDA SISTEMÁTICA
  Protocolo .............. cadenas, sintaxis, bases, ventana de años,
                           tipos de fuente incluidos (revistas, actas,
                           informes técnicos, tesis), criterios de
                           inclusión y exclusión
  Cadenas usadas ......... <cada una, textual>
  Bases consultadas ...... <lista>
  Fecha del protocolo .... <fecha>   ← anterior a la fecha de ejecución
  Fecha de ejecución ..... <fecha>
  Tiempo usado ........... <minutos>

RESULTADO
  Nº total de resultados . <n>
  Incluidos tras cribado . <n>
  Trabajos relevantes .... R# (con por qué se incluyen)

REGISTRO DE PRECEDENTE  (por cada R# relevante)
  Dimensión que toca ..... sistema | condición | observable |
                           criterio | referencia
  Veredicto .............. coincidente | parcial | no la toca
  Se revisan referencias y citas de los coincidentes y parciales
  (hacia atrás y hacia adelante).

VEREDICTO FINAL
  [ ] abierta
  [ ] parcial SIN reformulación  (H# intacta; la parte ya respondida
                                  se declara contraste o replicación)
  [ ] parcial CON reformulación  → PRE a P0
  [ ] respondida                 → PRE a P0, o descarte registrado

ENUNCIADO DE NOVEDAD  (si "abierta" o "parcial sin reformulación")
  "A diferencia de <R#>, este trabajo <dimensión y en qué difiere>,
   bajo <condición de prueba>, según <criterio>."
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Protocolo registrado; fecha del protocolo anterior a la de ejecución |
| R2 | Toda cadena usada está escrita textualmente |
| R3 | Toda base consultada está listada |
| R4 | Los criterios de inclusión y exclusión están escritos en el protocolo |
| R5 | Los tipos de fuente incluidos están declarados |
| R6 | Tiempo usado y fecha de ejecución registrados |
| R7 | Por cada R# relevante se anotó qué dimensión toca |
| R8 | El veredicto es coherente con el registro: un precedente coincidente impide "abierta" |
| R9 | "Respondida" implica reformulación concreta de H# o descarte registrado con su causa |
| R10 | "Parcial con reformulación" declara qué parte sigue abierta y qué se propone a P0 |
| R11 | Al menos una cadena omite la dimensión diferenciadora |
| R12 | Los R# de la ficha provisional reaparecen en la búsqueda; si no, se amplían las cadenas y se registra, o se declara por qué no pueden aparecer (fuente no indexada) |
| R13 | Se revisaron referencias y citas de cada R# coincidente o parcial |
| R14 | "Parcial sin reformulación" declara la parte ya respondida como contraste o replicación, citando su R# |
| R15 | El R# y la dimensión citados en el enunciado coinciden con el registro de precedentes |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P1.SINPROT | Búsqueda sin protocolo previo | R1 |
| P1.OPACO | Búsqueda sin cadenas ni bases registradas | R2, R3 |
| P1.VAGO | Inclusión sin criterio escrito | R4 |
| P1.FUENTE | Tipos de fuente no declarados | R5 |
| P1.INCOH | Veredicto "abierta" con precedente coincidente, o dimensiones no anotadas | R7, R8 |
| P1.DESC | "Respondida" sin reformulación ni descarte registrado | R9 |
| P1.PARVAG | "Parcial con reformulación" sin subcondición declarada | R10 |
| P1.ANCLAJE | Todas las cadenas incluyen el diferenciador | R11 |
| P1.EXH | Los R# de P0 no reaparecen y no se amplió ni justificó | R12 |
| P1.CIT | Citas y referencias de coincidentes no revisadas | R13 |
| P1.PARSIN | Parcial sin reformulación que presenta como nueva la parte ya respondida | R14 |
| P1.ENUNC | Enunciado de novedad inconsistente con el registro | R15 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| PRE | P0 | Veredicto "respondida" con reformulación, o "parcial con reformulación". En modo B, registrar como posterior a datos |

### Avance

Hacia P2, con veredicto "abierta" o "parcial sin reformulación": ficha definitiva y enunciado de novedad.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| NOV | P2 | Revisar el enunciado de novedad; si exige modificar H#, emitir PRE (modifica la ficha P1) |
| PRC | P9 | Incorporar el precedente omitido al registro y acotar el enunciado de novedad; H# no se modifica. Si cambia el claim de novedad, P2 se reejecuta |

### Registro mínimo

- Protocolo de búsqueda con fecha y versión
- Cadenas textuales, bases, tipos de fuente y criterios de inclusión
- Registro de precedentes con la dimensión que toca cada R#
- Revisión de citas y referencias de coincidentes y parciales
- Veredicto final con su justificación
- Enunciado de novedad, si aplica
- Si hubo PRE: la subcondición alternativa propuesta; si hubo descarte: su causa

### IA (opcional)

- Delegable: generar cadenas candidatas a partir de H# y la diferencia declarada; agrupar resultados por la dimensión que tocan.
- No delegable: inclusión y exclusión, veredicto final, decisión de reformular o descartar.
- Verificación: todo R# sugerido por IA se valida en fuente primaria antes de entrar al registro; lo no validado no cuenta como precedente.

### Notas

1. El "hasta donde sabemos" del artículo se origina aquí, en la búsqueda documentada; P0 solo aportó un indicio.
2. P1 no genera evidencia: su salida es un juicio de precedencia verificable, no un resultado empírico.
3. La taxonomía de claims se define en P2; P1 no la introduce.

## P2 — Claims

**Propósito:** convertir H# en afirmaciones atómicas, tipificadas y con etiqueta de confirmación, listas para mapear a evidencia en P4.

### Entrada

- H# con su etiqueta (confirmatoria o exploratoria)
- Enunciado de novedad de P1
- Ficha de novedad definitiva de P1

### Salida canónica (tabla de claims, C‑set)

```text
POR CADA CLAIM C#
  C# .................... frase única, sin "y" ni condición incrustada
  tipo .................. A | B | C | D | E | L
  etiqueta .............. confirmatorio | exploratorio
  condición de validez .. rango o régimen donde se afirma
  modo .................. A | B
  falsador .............. resultado que invalidaría el claim
  evidencia exigida ..... qué clase de dato lo sostiene
  destino ............... en_paper | premisa (a P3) | contexto | descartado
  fuente (si contexto) .. R# obligatorio
  dependencias .......... C# de los que depende
  (solo L) subtipo ...... medido | declarado
  (solo L) ref .......... C# al que limita

CLAIM RAÍZ
  C0: único claim que responde directamente a H#.
  estado ................ por probar | sostenido | refutado (NEG) |
                          parcial (PAR) | no concluyente
  P2 registra "por probar"; lo actualizan P4 en modo B y P6 en
  modo A o tras un HUE. Un SEV agotado sobre C0 ⇒ no concluyente.
```

### Taxonomía de claims

| Tipo | Afirma | Exige |
| --- | --- | --- |
| A — Factibilidad | El enfoque funciona en este sistema | Demostración sobre datos del sistema, con condición de validez explícita. No es novedad metodológica |
| B — Comparativa | X supera a Y | Prueba cabeza a cabeza, mismo protocolo, misma métrica, rival bien puesto (paridad en P4) |
| C — Hallazgo | Una propiedad medida del sistema | Medición con incertidumbre o tamaño de efecto declarado |
| D — Contribución metodológica | Un método o lógica nueva | Contraste con P1; la dimensión abierta por P1 debe ser el método mismo |
| E — Representatividad | La plataforma A sustituye a B | Evidencia comparativa A↔B; sin ella, se degrada a premisa (P3) o se elimina |
| L — Límite | El claim C# no se sostiene, o no fue probado, en una condición | Subtipo medido (evidencia de la falla) o declarado (condición fuera del ensayo); siempre indexado a un C# |

**Regla de novedad.** El claim que nombra el enunciado de novedad debe coincidir con la dimensión que P1 dejó abierta, sea cual sea su tipo. D exige además que esa dimensión sea el método mismo. Un método estándar aplicado a un sistema nuevo es A, no D.

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Cada C# es una sola afirmación falsable |
| R2 | Cada C# tiene un tipo único de la taxonomía A–E o L |
| R3 | Cada C# tiene falsador en una línea |
| R4 | Cada C# tiene etiqueta confirmatorio o exploratorio |
| R5 | Existe exactamente un claim raíz (C0) que responde H# |
| R6 | La etiqueta de C0 es igual a la de H#, o más débil con motivo registrado; nunca más fuerte |
| R7 | Todo C# tipo D declara el veredicto de P1 que lo habilita |
| R8 | Todo C# tipo E sin evidencia comparativa está como premisa o descartado |
| R9 | Ningún claim usa verbo aspiracional (lista de P0) ni adjetivo sin prueba: robusto, eficiente, preciso, superior, significativo sin test estadístico |
| R10 | Cada C# tiene destino y dependencias registradas |
| R11 | Todo claim de contexto tiene fuente R# |
| R12 | El claim que porta la novedad coincide con la dimensión abierta por P1 |
| R13 | C0 tiene al menos un L con subtipo, cuya condición está dentro del rango de operación declarado en P0 |
| R14 | Si C0 es tipo A, se registra la referencia de P0 contra la que se compara, o se justifica por qué no existe |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P2.COMP | Claim compuesto | R1 |
| P2.SINTIP | Claim sin tipo o con tipo ambiguo | R2 |
| P2.SINFAL | Claim sin falsador | R3 |
| P2.SINETQ | Claim sin etiqueta | R4 |
| P2.MULTIRA | Más de un claim raíz | R5 |
| P2.ETQSUB | C0 más fuerte que H# | R6 |
| P2.DSINP1 | Tipo D sin veredicto de P1 | R7 |
| P2.EINFL | Tipo E presentado como hecho sin evidencia comparativa | R8 |
| P2.SIGADJ | Adjetivo sin prueba | R9 |
| P2.HUER | Claim sin destino ni dependencias | R10 |
| P2.SINCTX | Claim de contexto sin fuente R# | R11 |
| P2.NOVDIS | El claim de novedad no coincide con la dimensión de P1 | R12 |
| P2.SINLIM | C0 sin L, L sin subtipo o L fuera del rango de operación | R13 |
| P2.RAIZA | C0 tipo A sin referencia ni justificación | R14 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| NOV | P1 | Claim no cubierto por el enunciado de novedad: revisar la diferencia declarada (modifica la ficha P1) |

### Avance

Hacia P3: C0, claims de apoyo, límites y premisas.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| RTP | P3 | Agregar o retipificar el claim (modifica el C‑set) |
| SEV | P4 | Si no es C0: debilitar o eliminar. Si es C0: llega solo si HUE no es factible o ya se intentó sin resolver; estado "no concluyente" |
| NEG | P6 | Si es C0: invertir el signo; los apoyos se reinterpretan. Si no es C0: invertir el signo del C#; si C0 dependía de él, P3 se reejecuta. P0 no se toca |
| PAR | P6 | Si es C0: acotar a donde se sostuvo y crear un L medido para donde no. Si no es C0: acotar el C#, crear su L medido y revisar si se reduce la condición de validez de C0. Nada baja a "contexto" |
| AUS | P9 | Crear el claim faltante, habitualmente un L |

### Registro mínimo

- Tabla de claims con tipo, etiqueta, condición de validez, falsador, destino, dependencias y subtipo de L
- C0 con su estado y el historial de cambios de estado
- Para cada D: veredicto de P1 que lo habilita
- Para cada E sin evidencia: registro de su degradación a premisa
- Para cada L: subtipo y rango de operación del que proviene
- Historial de retornos emitidos y recibidos (NOV, RTP, SEV, NEG, PAR, AUS) con fecha y objeto modificado

### IA (opcional)

- Delegable: detectar claims compuestos y adjetivos sin prueba; proponer la descomposición de frases largas en claims atómicos.
- No delegable: asignar tipo, decidir el claim raíz, emitir el destino.
- Verificación: toda descomposición propuesta por IA se revisa contra el falsador; si la frase nueva no tiene falsador propio, no es un C# válido.

### Notas

1. Un claim confirmatorio pesa más que uno exploratorio. La calibración de la magnitud de las afirmaciones se audita en P9.
2. La promoción de exploratorio a confirmatorio ocurre solo cuando P6 (en modo A o tras un HUE) o el subconjunto reservado en modo B aportan evidencia no vista al formular. P4 y P5 solo planifican.
3. Un L cuyo rango queda fuera de la operación declarada en P0 es vacuo y no cuenta para R13.

## P3 — Jerarquía de claims y premisas

**Propósito:** hacer explícito qué sostiene qué, antes de invertir en evidencia. La jerarquía no prueba nada; localiza dónde falta.

### Entrada

- C0 con estado, tipo y etiqueta (de P2)
- C# activos con tipo, etiqueta y condición de validez
- Límites (C# tipo L) con subtipo
- Premisas degradadas desde E en P2
- Supuestos declarados en P2

### Salida canónica (grafo J#, versión, fecha)

```text
NODOS
  Claim raíz ............ C0
  Claims activos ........ C# → depende de [C#, S#]
  Premisas (S#) ......... origen:   derivada | degradada de E |
                                    implícita típica
                          respaldo: R# | ∅ (supuesto declarado)
  Hojas ................. R#, S# sin respaldo (→ ∅),
                          C# marcados "requiere evidencia propia"

ARISTAS
  C# → C#     dependencia entre claims
  C# → S#     un claim depende de una premisa
  S# → R#     la premisa se apoya en una referencia
  S# → ∅      supuesto declarado, sin respaldo

CONTROL
  Ciclos ................ ninguno
  Camino a la raíz ...... todo C# activo alcanza C0
  Propagación ........... S# sin respaldo que alcanza C0 → aparece en
                          la condición de validez de C0 o como C# tipo L

LECTURA
  Qué sostiene qué ...... una línea: qué sostiene a C0 y qué lo limita
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | El grafo tiene un único claim raíz |
| R2 | Cada C# activo está en el grafo; no hay claims activos fuera de él |
| R3 | Toda arista tiene origen y destino con tipo declarado |
| R4 | C0 tiene al menos una dependencia (claim o premisa) |
| R5 | No hay ciclos, ni entre claims ni entre premisas |
| R6 | Todo S# sin respaldo que sostiene a C0, directa o transitivamente, aparece en la condición de validez de C0 o como C# tipo L declarado |
| R7 | Cada S# tiene origen y respaldo declarados; si el respaldo es un R#, fue verificado en fuente primaria |
| R8 | Se revisaron los supuestos implícitos típicos (validez del modelo, representatividad de la plataforma, calibración de instrumentos); si alguno no aplica, está justificado |
| R9 | Toda hoja del grafo es un R#, un S# sin respaldo declarado o un C# marcado "requiere evidencia propia" |
| R10 | Todo C# activo tiene un camino de dependencia hacia C0 (los L se indexan a su C#) |
| R11 | J# tiene versión, fecha y motivo del último cambio |
| R12 | La sección LECTURA identifica qué sostiene y qué limita a C0 |
| R13 | Están marcados como entrada de P4: los C# que requieren evidencia propia, los S# sin respaldo que acotan C0 y los C# tipo L con su subtipo |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P3.HUER | Claim activo fuera del grafo | R2 |
| P3.TIPO | Arista sin tipo | R3 |
| P3.RAIZ | C0 sin ningún apoyo | R4 |
| P3.CICLO | Dependencia circular entre claims o entre premisas | R5 |
| P3.SILEN | Supuesto silencioso: S# sin respaldo que alcanza C0 y no aparece en su condición de validez ni como L | R6 |
| P3.PREM | S# sin respaldo y sin declararse supuesto | R7 |
| P3.IMPLI | Algún supuesto implícito típico no fue revisado ni justificado | R8 |
| P3.HOJA | Hoja sin clasificar | R9 |
| P3.DESC | Claim activo sin camino a C0. Acción: pasar a contexto, eliminar o reservar para otro artículo | R10 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| RTP | P2 | La jerarquía revela un claim faltante o mal tipificado (modifica el C‑set) |

### Avance

Hacia P4: C# marcados "requiere evidencia propia", S# sin respaldo que acotan C0 y C# tipo L con su subtipo.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| PNS | P4 | Reestructurar la jerarquía con la evidencia disponible (modifica J#) |
| JER | P9 | Revisar J#; si el lector frío no distingue C0, la jerarquía no está comunicando |

### Registro mínimo

- J# con historial de versiones, fechas y motivo de cada cambio
- Lista de C# marcados "requiere evidencia propia"
- Lista de S# con respaldo y sin respaldo, y de los que acotan C0
- Resultado de la revisión de supuestos implícitos típicos
- Cambios en la condición de validez de C0

### IA (opcional)

- Delegable: dibujar el grafo desde las dependencias declaradas; detectar ciclos y claims sin camino a la raíz; proponer candidatos a hoja.
- No delegable: decidir si un supuesto implícito existe y si acota la validez; atribuir el origen de cada S#; marcar una hoja como "requiere evidencia propia" frente a "contexto".
- Verificación: todo nodo del grafo sugerido por IA debe existir en el C‑set de P2; nodos nuevos se rechazan.

### Notas

1. Reejecución: tras NEG o PAR sobre un C# de apoyo (vía P2), P3 se reejecuta. Se verifica que C0 conserve al menos una dependencia (R4), que no queden claims desconectados (R10) y si la condición de validez de C0 se reduce. El resultado genera una nueva versión de J#.
2. Un grafo con muchas premisas sin respaldo avisa aquí, antes de gastar en experimentos.

## P4 — Evidencia

**Propósito:** asignar a cada hoja del grafo la evidencia que la sostiene y declarar qué falta. En modo A especifica; en modo B audita.

### Entrada

- C# marcados "requiere evidencia propia" y S# sin respaldo que acotan C0 (de P3)
- C# tipo L con subtipo (de P2)
- H# con sistema, observable, criterio, referencia, condición y restricción
- Límite de factibilidad (de P0), con fecha anterior a los veredictos de cobertura (modo B) o a la entrada en P6 (modo A)
- Modo declarado por claim
- Solo modo B: inventario de datos existentes con su cobertura real y subconjunto reservado, si existe

### Salida canónica (E‑set, versión, fecha)

```text
TABLA DE EXIGENCIAS  (una fila por hoja)
  Hoja ......... C#
  E# ........... identificador de la evidencia exigida
  Observable ... magnitud + unidad
  Comparador ... referencia nombrada + R#, o "absoluto"
  Condición .... rango, régimen, ensayo o estación
  Estado ....... planificada | disponible | no obtenible
  Visto ........ sí | no (los datos que la sostienen ya se inspeccionaron)
  Resuelve ..... S# que respaldaría, si aplica

TABLA DE PARIDAD  (una fila por claim tipo B)
  Claim ........ C#
  Referencia ... R# de la alternativa contra la que se compara
  Categorías ... PA1…PA6: aplica (con requisito concreto de igualdad)
                 o no aplica (con justificación)
  Paridad ...... declarada (modo A) | verificada | violada (modo B)

RAMA A — especificación
  E# planificadas y tabla de paridad declarada → entrada de P5
  E# no obtenibles → lista de C# que dejan sin sostén

RAMA B — auditoría
  Veredicto de cobertura por C# .. sostenido | parcial | sin evidencia
  Veredicto de paridad (tipo B) .. verificada | violada
  Huecos ......................... decisión aplicada según REGLA
  Anclaje ........................ qué E# proviene de datos no vistos
  Sin huecos ni paridad violada → avance directo a P7
```

**Categorías de paridad**

| Código | Categoría | Qué debe ser igual entre las alternativas |
| --- | --- | --- |
| PA1 | Condiciones de operación | Régimen, ensayo o estación, y perturbaciones no controladas |
| PA2 | Información disponible | Instrumentación, horizonte e información exógena |
| PA3 | Presupuesto de ajuste | Esfuerzo de sintonía, con la búsqueda y el criterio de selección del rival declarados |
| PA4 | Presupuesto de cómputo | Límite de tiempo o recursos de cálculo, cuando la alternativa lo consuma |
| PA5 | Métricas y ventana | Métricas, ventana de evaluación y tratamiento de transitorios |
| PA6 | Datos de ajuste | Ninguna alternativa usa datos que otra no tuvo disponibles |

**Regla de decisión (modo B, tras los veredictos).** Se aplica a cada C# con cobertura insuficiente o paridad violada.

| Caso | Decisión |
| --- | --- |
| El claim es C0 | HUE; SEV solo si HUE no es factible o ya se intentó sin resolver |
| No es C0 y HUE es factible | HUE |
| En cualquier otro caso | SEV |

HUE es factible cuando cabe en el límite de factibilidad vigente y existe al menos una E# planificada ejecutable por P5. El tope es un HUE por claim, y ese HUE puede cubrir varias E# a la vez.

**Desenlace del ensayo acotado (vía P6, reentrada a P4)**

| Resultado | Consecuencia |
| --- | --- |
| Sostiene el claim | Veredicto "sostenido"; la E# cuenta como no vista (actualizar anclaje); un claim exploratorio puede promoverse, con registro |
| Refuta el claim | NEG, emitido por P6 directamente a P2 (no SEV) |
| Sostiene en parte | PAR, emitido por P6 directamente a P2 |
| No concluyente | SEV: tope alcanzado |
| Inválido | INV, con reintentos ≤ N de P5; no consume el tope de HUE |

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Toda hoja de J# tiene una fila con su E# y su estado |
| R2 | Todo E# nombra observable con unidad, comparador y condición, coherentes con la frase de H# |
| R3 | El estado es coherente con el modo: estado "disponible" implica modo B, y la etiqueta del claim lo refleja |
| R4 | Todo C# tipo L tiene E# asociado: subtipo medido exige la evidencia de la falla; subtipo declarado exige la restricción o la ausencia justificada de E# viable |
| R5 | Está identificado qué E# se sostiene con datos no inspeccionados; si ninguno, se declara y C0 queda exploratorio |
| R6 | Todo claim tipo B tiene fila en la tabla de paridad, con PA1–PA6 declaradas como "aplica" (con requisito) o "no aplica" (con justificación) |
| R7 | Las exclusiones de datos previsibles están declaradas antes de ver los resultados |
| R8 | Todo E# no obtenible enumera los C# que deja sin sostén |
| R9 | (Modo B) Cada C# activo tiene veredicto de cobertura |
| R10 | (Modo B) Cada hueco o paridad violada tiene decisión aplicada según la regla, y todo HUE cumple las dos condiciones de factibilidad |
| R11 | Ningún claim acumula más de un HUE |
| R12 | El E‑set tiene versión, fecha y motivo del último cambio |
| R13 | La fecha del límite de factibilidad es anterior a los veredictos (modo B) o a la entrada en P6 (modo A), y se registra con su versión en cada HUE |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P4.HUECO | Hoja sin fila en la tabla de exigencias | R1 |
| P4.OPACO | E# sin observable, unidad, comparador o condición | R2 |
| P4.MIX | E# disponible en un claim etiquetado confirmatorio sin datos vistos declarados | R3 |
| P4.LIMSIN | L declarado sin restricción ni ausencia justificada de E# viable | R4 |
| P4.VISTO | Toda la evidencia que confirmaría el claim proviene de datos ya inspeccionados | R5 |
| P4.PARID | Claim tipo B sin categorías de paridad declaradas | R6 |
| P4.INJUS | Paridad violada: rival sin sintonizar, datos asimétricos o ventana distinta | R6, R10 |
| P4.EXCL | Exclusión de datos no declarada antes de los resultados | R7 |
| P4.INALC | Falta un recurso o instrumento y la E# no está marcada "no obtenible" | R8 |
| P4.COV | (Modo B) Claim sin evidencia y sin decisión aplicada | R10 |
| P4.FACT | HUE fuera del límite de factibilidad o segundo intento sobre el mismo claim | R10, R11 |
| P4.LMTARD | Límite de factibilidad fijado o modificado después de los veredictos | R13 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| SEV | P2 | Claim sin evidencia o paridad violada. Si es C0, solo cuando HUE no es factible o ya se intentó sin resolver |
| PNS | P3 | Premisa no sostenida (modifica J#) |
| HUE | P5 | (Modo B) Hueco o paridad violada que exige ensayo acotado |

### Avance

- Hacia P5: E# planificadas y no obtenibles, tabla de paridad declarada, exclusiones previsibles, C# tipo L con subtipo y límite de factibilidad con fecha anterior.
- Hacia P7 (modo B): directo, si la auditoría no encontró huecos ni paridad violada.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| NOB | P5 | Marcar la E# "no obtenible" y decidir el destino de los C# afectados. Llega por inviabilidad o por agotar N; si el ensayo era un HUE, el claim pasa a SEV |
| (reentrada) | P6 | Resultado del ensayo acotado: actualizar veredicto de cobertura, anclaje y, si corresponde, etiqueta del claim. Ante un desenlace no concluyente, en cualquier modo, aplicar SEV |
| FSD | P7 | Agregar la E# faltante o degradar el claim (modifica el E‑set) |
| EVT | P9 | Incidente interno: auditar P0–P3 y P7; no se reporta en el artículo |

### Registro mínimo

- E‑set versionado: filas, estados y veredictos de cobertura
- Tabla de paridad con categorías declaradas y veredicto en modo B
- Exclusiones declaradas, con fecha anterior a los resultados
- Síntesis del anclaje: qué evidencia es no vista y cuál no
- Huecos y decisión aplicada (HUE o SEV), con el tope
- Desenlace de cada ensayo acotado, incluida la promoción de claims si ocurrió
- Comparador de cada claim tipo B, con su criterio de ajuste
- Límite de factibilidad (versión y fecha) junto a la fecha de los veredictos

### IA (opcional)

- Delegable: proponer el observable de cada claim; detectar claims sin comparador; verificar coherencia entre E# y la frase de H#; en modo B, mapear columnas del inventario a C#; prellenar la tabla de paridad para que el autor acepte o justifique cada categoría.
- No delegable: decidir si la paridad se cumple, si los datos están "no vistos" o si una E# es "no obtenible"; emitir el veredicto de cobertura; fijar o modificar el límite de factibilidad.

### Notas

1. Observación para decidir si separar esta fase. Registrar, sin reportarlo en el artículo, el número de discusiones al aplicar la regla (deseo de un tercer camino distinto de HUE o SEV) y el número de retornos de auditoría que acumula P4 en modo B frente a las demás fases. Si lo primero es frecuente, la decisión de huecos merece fase propia; si lo segundo es alto, conviene dividir P4 en "cobertura" y "rescate".
2. Para P6: en modo A, P4 solo declara la paridad. Si en la ejecución el rival quedó mal sintonizado o recibió datos asimétricos, la comparación no es válida como ensayo y corresponde INV, no NEG.

## P5 — Diseño de experimento

**Propósito:** instrumentar la evidencia planificada y fijar las compuertas de validez, el plan de análisis, la regla de desenlace y la política de reintentos antes de adquirir el primer dato de cada versión del diseño.

### Entrada

- E# planificadas y no obtenibles (de P4)
- Tabla de paridad declarada para claims tipo B, con las categorías PA aplicables (de P4)
- Exclusiones de datos previsibles (de P4)
- Claims tipo L asociados a las E# (de P2 y P4)
- H#: observable, criterio con umbral numérico, efecto que lo define y restricción (de P0)
- Límite de factibilidad vigente: versión, fecha y presupuesto de rescate (de P0; rige solo HUE en modo B)
- Solo modo B: solicitud de ensayo acotado (retorno HUE desde P4)

### Salida canónica (protocolo de diseño P5, versión, fecha)

```text
INSTRUMENTACIÓN Y CADENA DE ADQUISICIÓN (por cada E# planificada)
  E# .................... código de evidencia
  Plataforma ............ banco de pruebas | código de simulación v<n> |
                          instalación industrial | dataset externo
  Variables manipuladas . <nombre + rango de consigna + unidad>
  Variables medidas ..... <nombre + sensor / transductor + fondo de escala>
  Incertidumbre estática  <± valor o % a fondo de escala>
  Tasa de muestreo (fs) . <Hz o intervalo temporal dt>
  Cadena de acondicionamiento:
    Filtro / aliasing ... frecuencia de corte | tipo de filtro | "no aplica"
    Conversión A/D ...... resolución en bits | precisión numérica
    Almacenamiento ...... formato crudo | ruta de persistencia

PROTOCOLO DE EJECUCIÓN (por cada E#)
  Matriz de corridas .... condiciones de prueba y subconjuntos declarados
                          (partición cerrada y exhaustiva para evaluar PAR)
  Secuencia ............. orden fijo | aleatorizado (latin hypercube / bloque)
  Transitorio / reposo .. tiempo o criterio numérico de estabilización previo
  Réplicas (n_rep) ...... número entero fijo por condición
  Justificación réplicas  cálculo explícito: incertidumbre combinada prevista
                          u_comb(n_rep) < efecto del criterio de H#

EXCLUSIONES OBJETIVAS (limpieza intra-corrida)
  Regla de descarte ..... condición booleana o rango de filtrado de muestras
  Umbral a INV .......... fracción máxima de datos descartables por corrida (X%)
                          Si descarte > X% → la corrida pasa a INV completa

COMPUERTAS DE VALIDEZ PRE-ADQUISICIÓN (criterios para disparar INV en P6)
  V1: Integridad física . sensor saturado | pérdida de paquetes > Y% | drift térmico
  V2: Estabilidad ....... varianza de línea base fuera de [min, max]
  V3: Paridad en línea .. discrepancia de condiciones entre alternativas > tolerancia
  V4: Exclusión excesiva  fracción de muestras excluidas > umbral a INV (X%)

PLAN DE ANÁLISIS Y REGLA DE DESENLACE (por cada E#)
  Cálculo de métrica .... ventana temporal, tratamiento de transitorios (PA5),
                          algoritmo de agregación de réplicas
  Incertidumbre comb. ... fórmula de propagación: instrumental + entre réplicas
  Regla de desenlace (partición exhaustiva sobre el criterio de H# y u_comb):
    sostenido ........... si <condición numérica estricta>
    refutado (NEG) ...... si <condición numérica estricta>
    no concluyente ...... si cae en banda intermedia <rango numérico cerrado>
    parcial (PAR) ....... si sostenido solo en <subconjuntos declarados de la
                          matriz> y refutado o no concluyente en el resto

OPERACIONALIZACIÓN DE PARIDAD (por cada categoría PA con "aplica" en P4)
  Categoría (PA#) ....... implementación concreta en código o hardware
  Tolerancia numérica ... desviación máxima admisible entre alternativas
                          (|A - B| ≤ tol)

PRESUPUESTO Y POLÍTICA DE REINTENTOS
  Modo A (principal) .... presupuesto declarado como campo propio;
                          verificación de que el diseño respeta la
                          restricción de H#
  Modo B (rescate HUE) .. presupuesto asignado ≤ límite de factibilidad
  N máx. de reintentos .. <entero ≥ 0> por corrida planificada
  Acción al agotar N .... declarar ensayo fallido → retorno NOB a P4
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Cada E# planificada tiene plataforma, variables, incertidumbre estática y tasa de muestreo registradas |
| R2 | Toda compuerta de validez (V1–V4) tiene criterio numérico o condición booleana; ninguna usa términos cualitativos |
| R3 | El número de réplicas por condición está fijado y justifica numéricamente que la incertidumbre combinada prevista es menor que el efecto que define el criterio en P0 |
| R4 | El número máximo de reintentos N por corrida planificada está fijado como entero no negativo |
| R5 | En modo A, el diseño respeta la restricción de H# y declara su presupuesto propio; en modo B (HUE), el presupuesto no supera el límite de factibilidad vigente |
| R6 | La frecuencia de muestreo fs es mayor que el doble del ancho de banda relevante del observable (Nyquist), o cuenta con justificación física de la limitación instrumental |
| R7 | Toda categoría PA marcada "aplica" en P4 tiene implementación técnica y tolerancia numérica declaradas |
| R8 | Las exclusiones declaran regla de descarte y el umbral porcentual que convierte la exclusión parcial en invalidación completa (V4) |
| R9 | Si una E# no puede instrumentarse dentro de los recursos declarados o la restricción de H#, queda clasificada como "no obtenible" con causa técnica registrada |
| R10 | La fecha de aprobación de la versión vigente de P5 es anterior a la primera adquisición de datos crudos bajo esa versión |
| R11 | El protocolo P5 tiene versión, fecha y autor responsable |
| R12 | Cada E# tiene plan de análisis y regla de desenlace numéricos, con condiciones mutuamente excluyentes y exhaustivas: todo resultado cae en exactamente una categoría (sostenido, refutado, no concluyente o parcial, este último referido a subconjuntos predefinidos de la matriz) |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P5.CALIB | Sensor sin incertidumbre instrumental ni rango declarado | R1 |
| P5.VAGO | Compuerta de validez sin umbral numérico | R2 |
| P5.REPET | Réplicas sin cálculo que justifique u_comb frente al criterio de H# | R3 |
| P5.INF | Reintentos N no acotados | R4 |
| P5.SOBRE | Presupuesto excede el límite de factibilidad (modo B) o el diseño viola la restricción de H# (modo A) | R5 |
| P5.ALIAS | Muestreo insuficiente frente a Nyquist sin justificación física | R6 |
| P5.PARINC | Categoría PA marcada "aplica" sin implementación o tolerancia numérica | R7 |
| P5.EXCL | Exclusión sin regla previa o sin umbral de conversión a INV | R8 |
| P5.FANT | Evidencia no realizable mantenida como planificada en lugar de emitir NOB | R9 |
| P5.POST | Adquisición iniciada antes de la fecha de la versión del diseño | R10 |
| P5.DESEN | Desenlace sin regla previa, regla no exhaustiva o "parcial" sin subconjuntos predefinidos | R12 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| NOB | P4 | Evidencia no obtenible: inviabilidad de instrumentación, incompatibilidad con la restricción de H#, presupuesto insuficiente frente al límite de factibilidad o N reintentos agotados |

### Avance

Hacia P6: protocolo de diseño congelado, con instrumentación, matriz de corridas con subconjuntos cerrados, compuertas V1–V4, exclusiones con umbral a INV, plan de análisis, regla de desenlace exhaustiva, tolerancias de paridad, presupuesto según modo y N.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| HUE | P4 | Diseñar el ensayo acotado para las E# del hueco auditado, sin exceder el límite de factibilidad vigente |
| INV | P6 | Rediseño limitado a corregir la causa física o de adquisición de la compuerta violada, con nueva versión de P5 fechada antes de la nueva corrida. No pueden modificarse: umbrales V1–V4, plan de análisis completo (métrica, ventana, transitorios, agregación, propagación de incertidumbre), regla de desenlace, matriz de corridas y subconjuntos, n_rep, tolerancias de paridad, reglas de exclusión ni N. La corrida inválida se descarta completa del E‑set, su causa entra al log y consume un intento de N; agotado N, se emite NOB a P4 |

### Registro mínimo

- Ficha de diseño versionada, fechada antes de cada campaña de adquisición
- Especificaciones de sensores, actuadores, conversores y software de adquisición
- Matriz de corridas con subconjuntos predefinidos para la condición "parcial"
- Cálculo que justifica el número de réplicas frente al efecto de P0
- Umbrales de las compuertas V1–V4 y regla de exclusión con su umbral de paso a INV
- Plan de análisis completo: procesamiento, propagación de incertidumbre y regla de desenlace
- Tolerancias numéricas de cada categoría PA aplicable
- N y presupuesto declarado o contrastado según el modo
- Log de corridas inválidas: fecha, compuerta violada, datos crudos archivados con marca INV y motivo técnico
- Registro de corridas piloto: fecha, operador y confirmación de exclusión del E‑set
- Si hubo NOB: informe técnico de la inviabilidad, del conflicto con la restricción o del agotamiento de N

### IA (opcional)

- Delegable: estimar tasas de muestreo y bandas de filtros; generar matrices ortogonales o corridas aleatorizadas; implementar simbólicamente la propagación de incertidumbre según la GUM; redactar scripts base de adquisición.
- No delegable: umbrales V1–V4, plan de análisis y regla de desenlace, tolerancias de paridad, N, validación de calibraciones y congelación de cualquier versión de P5.
- Verificación: toda fórmula de propagación o código de filtrado propuesto por IA se coteja con la formulación analítica estándar antes de integrarse.

### Notas

1. Corridas piloto: los ensayos de calibración, puesta en marcha y verificación de sensores se rotulan como "piloto", con fecha, y se archivan. Ningún dato de una corrida piloto puede pasar al E‑set.
2. Muestreo en control: R6 fija el piso de Nyquist; en lazos de realimentación y transitorios rápidos, la práctica recomendada es fs entre 5 y 10 veces el ancho de banda en lazo cerrado.
3. Blindaje ante INV: impide modificar ventanas, filtros o particiones para forzar un desenlace. Toda corrida inválida queda en el log y se reporta en el artículo, según las reglas de registro del grafo.
4. NOB no se limita a HUE: en modo A, marca la E# como no obtenible y obliga a revisar los claims que quedan sin evidencia, que pasan a SEV si no hay vía alternativa.

## P6 — Ejecución y adquisición

**Propósito:** ejecutar el protocolo congelado en P5, verificar las compuertas de validez y registrar el desenlace de cada claim sin alterar las reglas de análisis fijadas.

### Entrada

- Protocolo de diseño P5 vigente: versión, fecha y autor responsable, con fecha anterior a los datos
- Matriz de corridas y subconjuntos declarados para evaluar PAR
- Número de réplicas (n_rep) por condición
- Compuertas de validez V1–V4 con umbrales numéricos
- Reglas de exclusión intra-corrida y umbral de paso a INV
- Plan de análisis congelado: cálculo de métrica, propagación de incertidumbre y regla de desenlace exhaustiva
- Tolerancias de paridad operacionalizadas para claims tipo B
- Política de reintentos: N por corrida planificada, administrada por P5

### Salida canónica (acta de ejecución P6, versión, fecha)

```text
REGISTRO DE ADQUISICIÓN (por cada corrida planificada en P5)
  ID de corrida ......... <ID> (asociada a E# y condición de la matriz)
  Condición de prueba ... punto operativo / subconjunto de la matriz P5
  Réplica ............... número de réplica [1 .. n_rep]
  Sello de tiempo ....... inicio [YYYY-MM-DD hh:mm:ss] · fin [hh:mm:ss]
  Datos crudos .......... ruta / hash SHA-256 del archivo
  Versión P5 activa ..... v<n> (verificada: fecha P5 < inicio adquisición)
  Estado de ejecución ... ejecutada | no ejecutada (con causa técnica)

DESVIACIONES DE PROTOCOLO (por corrida)
  Incidencia ............ qué ocurrió fuera de lo previsto en P5 | "ninguna"
  Clasificación ......... viola V1–V4 → INV |
                          no viola V1–V4 → corrida válida, desviación reportada

AUDITORÍA DE VALIDEZ (compuertas V1–V4)
  Exclusiones aplicadas . fracción de muestras descartadas: X%
  V1 Integridad física .. superada | violada
  V2 Estabilidad ........ superada | violada
  V3 Paridad en línea ... (|A - B| ≤ tol) superada | violada
  V4 Descarte excesivo .. (X% > umbral INV) superada | violada
  Veredicto de validez .. VÁLIDA | INVÁLIDA (retorno INV a P5)

APLICACIÓN DEL PLAN DE ANÁLISIS (solo corridas válidas)
  Condiciones completas . verificación de n_rep válidas por condición
  Tratamiento ........... ventana y transitorios según P5
  Métrica agregada ...... valor numérico calculado
  Incertidumbre comb. ... u_comb según la fórmula de P5
  Subconjuntos .......... métrica e incertidumbre por partición declarada

DESENLACE POR CLAIM (regla de P5)
  Claim evaluado ........ C#
  Desenlace ............. sostenido | NEG | PAR | no concluyente
  Destino:
    sostenido ........... registrar estado del claim; avance a P7
                          (tras un HUE: reentrada a P4 para cobertura y anclaje)
    NEG, PAR ............ retorno directo a P2
    no concluyente ...... reentrada a P4, que aplica SEV
                          (si es C0: estado "no concluyente")
    inválido ............ retorno INV a P5

BALANCE DE RECURSOS
  Recursos consumidos ... horas de banco | core-hours | presupuesto
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Toda corrida tiene sello de inicio posterior a la aprobación de la versión de P5 bajo la que se adquirió |
| R2 | Todo archivo de datos crudos tiene ruta persistente y hash registrado antes de cualquier procesamiento |
| R3 | Las compuertas V1–V4 se evaluaron explícitamente en cada corrida adquirida |
| R4 | Una corrida que viola cualquier compuerta (incluida la paridad en línea en modo A o el descarte excesivo) se clasifica INV y sus datos se excluyen íntegramente del análisis |
| R5 | Toda corrida INV queda registrada con su causa técnica y su hash, y se emite el retorno INV a P5 |
| R6 | El cálculo de la métrica y la propagación de incertidumbre reproducen sin variaciones el algoritmo y las ventanas de P5 |
| R7 | La regla de desenlace se aplica de forma determinista: el desenlace coincide con la categoría que P5 previó para ese valor |
| R8 | PAR solo se emite si el claim se sostiene exclusivamente en subconjuntos declarados a priori en la matriz de P5 |
| R9 | Ningún dato de corridas piloto entra en el cálculo del desenlace |
| R10 | Toda corrida planificada fue ejecutada o figura en el acta como no ejecutada, con su causa |
| R11 | No se agregaron corridas, puntos operativos ni réplicas fuera de la matriz y de n_rep; las corridas posteriores a un INV solo sustituyen la corrida invalidada |
| R12 | Una condición o subconjunto sin las réplicas válidas exigidas se evalúa como "no concluyente"; nunca se omite del análisis |
| R13 | Toda desviación del protocolo queda documentada y clasificada; ninguna corrida se invalida por una desviación que no viole V1–V4 |
| R14 | El acta tiene versión, fecha de cierre y registro del ejecutor |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P6.PREDAT | Corrida con sello de tiempo anterior o igual a la versión de P5 | R1 |
| P6.ALTER | Datos crudos sin hash o modificados tras la adquisición | R2 |
| P6.COMPOM | Corrida procesada sin auditar las compuertas V1–V4 | R3 |
| P6.INVLAV | Corrida que viola una compuerta y se procesa en lugar de pasar a INV | R4 |
| P6.PARNEG | Paridad violada en modo A clasificada como NEG en vez de INV | R4 |
| P6.OPTOPO | Ventana, filtro o algoritmo alterado frente a P5 | R6 |
| P6.JUICIO | Desenlace clasificado a criterio del autor, en desacuerdo con la regla de P5 | R7 |
| P6.PARPOS | PAR asignado a un subrango definido después de ver los datos | R8 |
| P6.PILOTO | Datos de corridas piloto incluidos en el resultado | R9 |
| P6.STOP | Campaña detenida, extendida con réplicas ad hoc o con condiciones omitidas | R10, R11, R12 |
| P6.DESVOP | Corrida descartada por una desviación que no viola V1–V4, o desviación no registrada | R13 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| INV | P5 | Corrida inválida por violar V1–V4 (incluye paridad violada en modo A, descarte excesivo o desviación que vulnera una compuerta). P5 contabiliza el reintento y, si agota N, emite NOB a P4 |
| NEG | P2 | El resultado cae en la condición de refutación fijada en P5 |
| PAR | P2 | El resultado se sostiene solo en subconjuntos predefinidos y se refuta o no concluye en el resto |
| (reentrada) | P4 | Tras un HUE en modo B (cobertura y anclaje), o ante un desenlace no concluyente en cualquier modo (P4 aplica SEV) |

### Avance

Hacia P7: datos procesados, métricas e incertidumbres de todos los claims evaluados, cualquiera sea su desenlace (sostenido, refutado, parcial o no concluyente), una vez que P2 a P4 hayan registrado los cambios que esos desenlaces producen.

### Retornos que recibe

Ninguno. P6 recibe de P5 el protocolo aprobado, o una versión actualizada del diseño para reintentar una corrida invalidada.

### Registro mínimo

- Acta de ejecución con identificador, fecha y versión
- Tabla de corridas con sellos de inicio y fin, condición, réplica y hash de los datos crudos
- Auditoría de compuertas V1–V4 por corrida
- Registro de desviaciones con su clasificación
- Log de corridas inválidas: corrida, causa, compuerta violada y hash (se reporta en el artículo)
- Justificación de toda corrida planificada no ejecutada
- Scripts de procesamiento ejecutados, con control de versión
- Tabla de métricas con su incertidumbre combinada
- Aplicación de la regla de desenlace y destino asignado a cada claim
- Recursos consumidos

### IA (opcional)

- Delegable: verificación de integridad de datos (NaN, saturaciones, varianzas de línea base para V1–V2); ejecución del pipeline determinista de métricas e incertidumbre; cálculo de hashes.
- No delegable: decidir si una desviación imprevista invalida una corrida; reclasificar un desenlace fuera de la regla numérica; alterar el plan de corridas de P5.
- Verificación: todo script de análisis ejecutado con IA se contrasta con una corrida testigo sintética validada, para asegurar que no altera ventanas ni agrega filtros no previstos en P5.

### Notas

1. Paridad en modo A: si el rival falla por convergencia numérica, descalibración o perturbaciones asimétricas (violando V3), el resultado no cuenta como refutación del rival ni como éxito propio. La corrida es INV y se repite bajo paridad.
2. Detención o extensión oportunista: P6 no se detiene porque los primeros datos "ya confirman" la hipótesis ni agrega réplicas porque u_comb quedó al borde del criterio. Si los datos válidos no alcanzan para discriminar, el desenlace es "no concluyente".
3. Desviaciones no críticas: un evento imprevisto que no rompe las compuertas (cambio de operador, fluctuación ambiental dentro de tolerancia) no autoriza descartar la corrida; la corrida es válida y la desviación se reporta en la metodología del artículo.
4. Un solo contador: P6 reporta cada invalidación con INV; P5 lleva la cuenta de N por corrida planificada y emite NOB si se agota.

## P7 — Estructura y plan de figuras

**Propósito:** fijar el orden argumental del manuscrito, la correspondencia de secciones y el ancla probatoria de cada claim activo, antes de redactar una sola línea de texto.

### Entrada

- C‑set consolidado: C0 con su estado final (sostenido, NEG, PAR o no concluyente), claims de apoyo, claims acotados tras PAR y límites L con subtipo (de P2 y P6)
- J# vigente y lista de S# sin respaldo que acotan C0 (de P3)
- E‑set y datos procesados: métricas e incertidumbre combinada de cada E# válida (de P4 y P6)
- Enunciado de novedad y precedentes clave R# (de P1)
- Log de corridas inválidas y desviaciones de protocolo (de P5 y P6)
- En modo B: tabla de cobertura auditada y mapa de anclaje (de P4)

### Salida canónica (F‑set y orden argumental, versión, fecha)

```text
ESQUELETO ARGUMENTAL MÍNIMO
  1. Introducción ...... claims de contexto (R#) + brecha y enunciado de
                         novedad (P1)
  2. Métodos ........... protocolo P5 + tabla de paridad (PA1–PA6) +
                         log de robustez (corridas INV, N consumido,
                         desviaciones)
  3. Resultados ........ anclas de los C# activos en el orden de
                         dependencia de J#
  4. Discusión/Límites . todos los C# tipo L (medidos y declarados) +
                         S# sin respaldo que acotan C0

MATRIZ DE ANCLAS (por cada C# activo)
  Claim ................ C#
  Tipo de ancla ........ figura (F#) | tabla (T#) | valor en texto
                         (E# + u_comb) | declaración en límites
                         (solo L declarado o S#)
  Ubicación ............ cuerpo principal | suplementario (con
                         justificación)
  Estado reportado ..... sostenido | refutado (NEG) | parcial (PAR) |
                         no concluyente

FICHA DE DISPLAY ITEM (una por F# o T#)
  Identificador ........ F# | T#
  Claims que sostiene .. lista de C# (al menos uno como ancla principal)
  E# asociadas ......... evidencia procesada de P6 (o auditada en P4)
  Tipo visual .......... serie temporal | dispersión | barras |
                         mapa de calor | tabla
  Eje X / filas ........ magnitud + unidad + escala (lineal/log)
  Eje Y / columnas ..... magnitud + unidad + escala
  Series ............... propuesta vs referencia de H# (claims tipo B)
  Incertidumbre ........ barras ± u_comb | bandas | no aplica
  Contraste ............ marca del umbral del criterio de H#
  Límite visible ....... frontera del rango de validez o del L medido
  Auto-explicación ..... mensaje que el elemento transmite sin el texto

CONTROL DE INTEGRIDAD
  Cobertura ............ todo C# activo tiene su ancla principal
  Claims sin dato ...... C# sin evidencia suficiente → FSD a P4
  Elementos huérfanos .. figuras o tablas sin claim → contexto,
                         suplementario o eliminadas
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Todo C# activo tiene exactamente un ancla principal: figura, tabla o valor en texto con su E# y ± u_comb. Los L declarados y los S# sin respaldo se anclan en la sección de límites |
| R2 | Toda figura o tabla proviene de una E# válida con datos existentes en P6 (o P4 en modo B); ninguna usa datos pendientes de adquirir |
| R3 | Si un C# no tiene dato suficiente para su ancla, se emite FSD a P4 |
| R4 | Todo display item cuantitativo representa la incertidumbre (barras de error, intervalos o bandas ± u_comb), salvo justificación física documentada |
| R5 | En claims tipo B, la figura o tabla incluye la referencia nombrada en H# y la marca del umbral del criterio |
| R6 | Las figuras de claims con L medido demarcan la frontera donde el claim deja de sostenerse |
| R7 | En Resultados, las anclas siguen el orden de dependencia de J#: ningún resultado aparece antes que lo que lo sostiene |
| R8 | Ningún display item del cuerpo principal es decorativo: todos sostienen al menos un C# activo |
| R9 | La tabla de paridad y el log de robustez (corridas INV, reintentos, desviaciones) están asignados a Métodos |
| R10 | La sección de límites contiene todos los C# tipo L (medidos y declarados) y los S# sin respaldo que acotan C0 |
| R11 | El ancla principal de C0 muestra su estado real. Las anclas de NEG, PAR y L medidos están en el cuerpo principal, nunca en material suplementario |
| R12 | El F‑set tiene versión, fecha de cierre y autor responsable |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P7.HUERF | Figura o tabla del cuerpo principal sin claim asignado | R1, R8 |
| P7.FSD | Claim activo sin dato, o figura sin datos procesados | R2, R3 |
| P7.CIEGO | Gráfico cuantitativo sin representación de la incertidumbre | R4 |
| P7.ASIM | Claim comparativo graficado sin la referencia o sin el criterio de H# | R5 |
| P7.LIMOCU | Límite medido omitido en la figura | R6 |
| P7.ANTIC | Conclusión presentada antes que su soporte en J# | R7 |
| P7.INVOCU | Tabla de paridad o log de robustez ausentes de Métodos | R9 |
| P7.LIMSEC | Sección de límites ausente o incompleta | R10 |
| P7.SUPL | NEG, PAR o límite medido desplazado a material suplementario | R11 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| FSD | P4 | Al asignar el ancla, un C# carece de evidencia suficiente o los datos no sostienen la relación esperada. P4 agrega la E# faltante (si cabe en la factibilidad) o degrada el claim con SEV |

### Avance

Hacia P8: esqueleto argumental por secciones, F‑set congelado y matriz de anclas completa, en cuerpo principal y suplementario.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| EST | P9 | Reordenar la secuencia argumental, rediseñar display items ambiguos o explicitar umbrales visuales |
| RED | P8 | Reestructurar o desacoplar paneles de la figura o tabla sin alterar los datos de P6 |

### Registro mínimo

- F‑set con identificador, versión y fecha
- Matriz de anclas: C#, tipo de ancla, ubicación y estado reportado
- Bocetos de figuras y especificación de tablas: variables, unidades, leyendas, umbrales e incertidumbre
- Inventario de la sección de límites: claims L y supuestos S#
- Resolución de los FSD emitidos a P4
- Ajustes derivados de EST
- Inventario justificado del material suplementario

### IA (opcional)

- Delegable: disposición de paneles en figuras compuestas; paletas de color accesibles; scripts de graficación reproducibles (Matplotlib, Seaborn o pgfplots) a partir de los datos de P6; borradores de epígrafes.
- No delegable: elegir el ancla principal de C0; suprimir la representación de la incertidumbre; relegar un NEG, un PAR o un L medido a suplementario; alterar el orden derivado de J#.
- Verificación: toda figura generada con scripts asistidos por IA se contrasta numéricamente con las tablas de P6, para descartar distorsiones de escala, suavizados no autorizados o umbrales desplazados.

### Notas

1. Auto-explicación: cada figura y tabla se entiende sin el texto, con ejes y unidades, leyenda, bandas ± u_comb rotuladas y la marca del umbral fijado en P0.
2. Relación asimétrica: un claim tiene un solo ancla principal; una figura puede sostener varios claims, por ejemplo el claim principal y, en la misma curva, la región donde rige su L medido.
3. La sección de límites es la traducción obligatoria de todos los L y de los S# sin respaldo que sostienen a C0. Si el lector frío no identifica los límites, la causa está en esta sección.
4. FSD es el último filtro antes de redactar: si un claim no se sostiene con los datos de P6, se devuelve a P4 para rescate o debilitamiento formal.

## P8 — Redacción

**Propósito:** producir el texto del manuscrito a partir de las salidas de las fases previas, limitando la prosa a lo que las anclas demuestran, regulando el estatus de las interpretaciones e incorporando la declaración de transparencia.

### Entrada

- Esqueleto argumental y F‑set congelado (de P7)
- Matriz de anclas: C#, F#, T# y valores en texto (de P7)
- Enunciado de novedad y precedentes clave R# (de P1)
- C‑set con tipos, etiquetas, falsadores y límites L (de P2 y P6)
- J# y lista de S# sin respaldo que acotan C0 (de P3)
- Protocolo P5, tabla de paridad y log de robustez (de P5, P6 y P7)
- Fechas de P0, P5 y P6; datos vistos en modo B y anclajes (de P0, P4, P5 y P6)
- Registro del uso de IA a lo largo del proceso (de P0 a P7)
- Lista de exclusión léxica de P0 y P2 (verbos aspiracionales y adjetivos sin prueba)

### Salida canónica (manuscrito completo, versión, fecha)

```text
ESTRUCTURA DEL MANUSCRITO
  Título ............... directo, centrado en el sistema y el observable de
                         H#; sin adjetivos elogiosos ni verbos aspiracionales
  Resumen .............. cinco oraciones:
                         1. contexto y brecha (P1)
                         2. pregunta e hipótesis, con C0 (P0, P2)
                         3. método y paridad (P5, P6)
                         4. resultado principal con métrica ± u_comb (P6, P7)
                         5. límite principal o condición de validez (P2, P7)
  1. Introducción ...... claims de contexto (R#) + enunciado de novedad
                         (dimensión y R# idénticos a P1)
  2. Métodos ........... instrumentación de P5 + tabla de paridad +
                         log de robustez (INV, N consumido, desviaciones) +
                         DECLARACIÓN DE TRANSPARENCIA:
                           - etiqueta confirmatorio/exploratorio por claim
                           - modo B: datos vistos al formular y anclaje usado
                           - fechas: diseño P5 frente a primera adquisición
                           - uso de IA según la política de la revista
  3. Resultados ........ un párrafo o subsección por ancla, en el orden de
                         J#; cada C# se enuncia citando su ancla
  4. Discusión ......... (a) interpretación: mecanismos y comparación con R#,
                             con estatus regulado (hipótesis explicativa,
                             claim exploratorio o de contexto con R#)
                         (b) límites y alcance: todos los C# tipo L y
                             los S# sin respaldo
  5. Conclusiones ...... respuesta a H# según el estado de C0; sin claims
                         nuevos

TRAZABILIDAD TEXTUAL (por párrafo)
  Párrafo .............. C# que narra | ancla citada | R# citado |
                         estatus (confirmatorio | exploratorio | hipótesis)

CONTROL LÉXICO
  Verbos aspiracionales  cero ocurrencias
  Adjetivos de grado ... respaldo numérico o estadístico en cada caso
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | Cada C# activo del manuscrito está redactado y vinculado a su ancla principal (figura, tabla o valor en texto ± u_comb) |
| R2 | Resultados describe y compara los datos de las anclas; no introduce interpretaciones de mecanismo ni afirmaciones causales que no sean un C# activo en J# |
| R3 | La oración de novedad de la Introducción nombra la dimensión diferenciadora y cita exactamente los mismos R# que el enunciado de P1 |
| R4 | Métodos incluye la descripción de paridad (claims tipo B) y el log de robustez: corridas INV con causa, reintentos y desviaciones |
| R5 | La Discusión contiene una subsección "Límites y alcance" con todos los C# tipo L (medidos y declarados) y los S# sin respaldo que acotan C0 |
| R6 | El estado final de C0 se declara en el Resumen, en Resultados y en Conclusiones, sin suavizar veredictos negativos ni omitir límites |
| R7 | Las Conclusiones responden solo a H# mediante el estado de C0 y sus apoyos inmediatos; no aparecen claims nuevos ni extrapolaciones |
| R8 | Ningún verbo aspiracional (contribuir, explorar, avanzar, desarrollar, estudiar, investigar) califica la contribución o el hallazgo |
| R9 | Ningún adjetivo de desempeño o grado (superior, óptimo, eficiente, robusto, significativo) aparece sin respaldo numérico o prueba estadística |
| R10 | Toda cifra de la prosa coincide exactamente con las tablas de P6 y con las figuras de P7 |
| R11 | El manuscrito tiene versión, fecha de cierre y autor responsable |
| R12 | Toda interpretación en la Discusión está respaldada por un C# exploratorio o de contexto (con R#), o se declara como hipótesis no probada; ninguna aparece como hallazgo ni en el Resumen o las Conclusiones |
| R13 | Métodos contiene la declaración de transparencia: etiqueta de cada C#, datos vistos y anclaje en modo B, fechas del diseño frente a la adquisición y uso de IA |
| R14 | Todo claim exploratorio se redacta como tal; ninguno se formula con la contundencia de uno confirmatorio |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P8.DESAN | Claim redactado sin citar su ancla | R1 |
| P8.EXTRAP | Resultados afirma mecanismos o generalizaciones que no son C# | R2 |
| P8.NOVINCOH | Novedad con dimensión o R# distintos de P1 | R3 |
| P8.INVSIL | Métodos omite el log de robustez | R4 |
| P8.LIMDIL | Límites dispersos o ausentes, en vez de agrupados en su subsección | R5 |
| P8.SUAVIZ | Veredicto NEG, PAR o no concluyente matizado con lenguaje especulativo o triunfalista | R6 |
| P8.CONCLNEW | Conclusión con claims, aplicaciones o extrapolaciones ausentes del C‑set | R7 |
| P8.ASPIR | Verbos aspiracionales que califican la contribución | R8 |
| P8.ADJGRAT | Adjetivos de grado sin soporte numérico o estadístico | R9 |
| P8.DISCREP | Cifra de la prosa distinta de P6 o P7 | R10 |
| P8.INTERP | Mecanismo o explicación presentado como hallazgo sin ser C# confirmatorio | R12 |
| P8.OPACO | Declaración de transparencia ausente o incompleta | R13 |
| P8.FUERZA | Claim exploratorio redactado como confirmatorio | R14 |

### Retornos que emite

| Código | Destino | Condición |
| --- | --- | --- |
| RED | P7 | La prosa no puede narrar el ancla sin ambigüedad, dos paneles deben desacoplarse para sostener claims distintos o la escala no muestra el efecto. P7 reestructura el display item o reordena el F‑set sin modificar los datos de P6 |

### Avance

Hacia P9: manuscrito completo con trazabilidad por párrafo, declaración de transparencia y secciones cerradas, listo para el lector frío y el revisor experto.

### Retornos que recibe

| Código | Origen | Acción |
| --- | --- | --- |
| PRO | P9 | Corregir sintaxis confusa, ambigüedades, oraciones sobrecargadas o discrepancias de tono, sin alterar estructura ni datos |

### Registro mínimo

- Manuscrito versionado (fuente y documento compilado)
- Tabla de trazabilidad: párrafo → C# → ancla → estatus
- Declaración de transparencia incorporada al texto
- Reporte del escaneo léxico (verbos aspiracionales y adjetivos sin sustento)
- Concordancia numérica entre texto, tablas y figuras
- Registro de RED, si se emitió, con el ajuste realizado en P7

### IA (opcional)

- Delegable: corrección gramatical y ortotipográfica; escaneo léxico automático; concordancia de referencias cruzadas y formato bibliográfico; borradores de párrafos descriptivos de Resultados, estrictamente anclados a tablas y figuras.
- No delegable: Resumen y Conclusiones; estatus epistémico de las interpretaciones; moduladores de certeza de los claims exploratorios; declaración de transparencia.
- Verificación: todo texto sugerido por IA pasa por una revisión de diferencias, para asegurar que no introduce adjetivos sin prueba, no atenúa veredictos adversos y no borra la frontera entre claims confirmatorios y exploratorios.

### Notas

1. Narración de anclas: Resultados guía al lector por las anclas (variables, curvas por alternativa, valores medios ± u_comb y su posición frente al criterio de P0), sin disertación libre.
2. RED formaliza el ajuste cuando la prosa revela fallas del ancla visual: series sobrecargadas, ejes mal resueltos o leyendas ambiguas.
3. Regular la interpretación en la Discusión (R12) evita dos extremos: prohibir toda explicación física y hacer pasar hipótesis plausibles por conclusiones demostradas.

## P9 — Verificación

**Propósito:** auditar de forma independiente la comprensibilidad (lector frío sobre resumen y figuras) y la corrección técnica (revisor experto ajeno al proceso) del manuscrito cerrado, y emitir retornos tipados antes del cierre.

### Entrada

- Manuscrito completo en versión cerrada (de P8)
- Paquete de lectura fría: título, resumen y F‑set completo con epígrafes (de P7 y P8)
- Tabla de trazabilidad: párrafo → C# → ancla → estatus (de P8)
- C‑set con tipos, etiquetas y límites L (de P2 y P6)
- J# y lista de S# sin respaldo (de P3)
- Ficha de novedad definitiva (de P1)
- Formulario H# con la motivación de dirección y magnitud (de P0)
- Protocolo P5, regla de desenlace, log de robustez y actas de P6 (de P5 y P6)

### Salida canónica (acta de verificación, versión, fecha)

```text
AUDITORÍA 1: LECTOR FRÍO (no ha leído el manuscrito; ajeno al área)
  Perfil ............... nombre | afiliación | área disciplinar
  Condición de lectura . solo título, resumen y figuras | tiempo ≤ 10 min
  Contador ............. lector frío Nº <k> usado en este artículo
  Extracción ciega (respuestas textuales del lector):
    1. Pregunta ........ [texto]
    2. Respuesta (C0) .. [texto]
    3. Novedad ......... [texto]
    4. Límite principal  [texto]
  Concordancia binaria:
    Pregunta ........... sí | no  (nombra sistema y observable de H#)
    Respuesta .......... sí | no  (enuncia el estado real de C0)
    Novedad ............ sí | no  (nombra la dimensión diferenciadora de P1)
    Límite ............. sí | no  (nombra la condición de al menos un L de C0)
  Diagnóstico .......... 4/4 | falla → tabla de diagnóstico del grafo
  Comprensibilidad ..... APROBADA | OBSERVADA (con retornos tipados)

AUDITORÍA 2: REVISOR EXPERTO (sin autoría ni participación en P0–P8)
  Perfil ............... nombre | área técnica | declaración de independencia
  Verificación:
    Paridad ............ PA1–PA6 en texto y métodos
    Regla de desenlace . P6 aplicó sin desvío la regla de P5
    Incertidumbre ...... propagación de u_comb y cálculo estadístico
    Trazabilidad ....... concordancia numérica total entre texto, tablas
                         y figuras
    Validez física ..... balances, supuestos S# y formulaciones
    Transparencia ...... etiquetas, modo B, fechas y uso de IA
    Motivación P0 ...... confirmada | objetada → dictamen en acta; si el
                         resultado era previsible, AUS (nuevo límite) o
                         PRC (novedad)
    Calibración ........ sin adjetivos sin prueba; ningún exploratorio
                         redactado como confirmatorio
  Corrección técnica ... APROBADA | OBSERVADA (con retornos tipados)

VEREDICTO FINAL
  [ ] Aprobado sin observaciones → avance a P10
  [ ] Observado → reejecución en la fase destino y nueva auditoría en P9
```

El diagnóstico de las fallas del lector frío usa la tabla canónica de la sección Grafo de retornos, que incluye la novedad.

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | El lector frío recibe solo título, resumen y figuras con epígrafes, y su tiempo de lectura registrado no supera 10 minutos |
| R2 | La concordancia de los cuatro elementos se evalúa con la regla binaria: sistema y observable, estado real de C0, dimensión de P1 y condición de un L |
| R3 | Toda falla del lector frío genera el retorno indicado por la tabla de diagnóstico |
| R4 | Cada pasada del test usa un lector frío que no leyó versiones previas; el contador de lectores consumidos queda registrado |
| R5 | El revisor experto no es autor ni participó en ninguna fase de P0 a P8 |
| R6 | El revisor experto audita la paridad (PA1–PA6) y comprueba que el desenlace de P6 coincide con la regla de P5 |
| R7 | El revisor experto verifica la concordancia matemática, física y de propagación de u_comb entre datos y texto |
| R8 | El revisor experto audita la declaración de transparencia: etiquetas, fechas de P5 frente a P6, datos vistos en modo B y uso de IA |
| R9 | El revisor experto audita el tipo de motivación de P0; si lo objeta, registra el dictamen y emite AUS o PRC |
| R10 | Si el revisor detecta un precedente omitido que solapa la novedad, emite PRC a P1 |
| R11 | Toda discrepancia numérica entre texto, tablas y figuras está resuelta o clasificada con código de retorno |
| R12 | Si se emite EVT, se abre un incidente interno que audita P0–P3 y P7 |
| R13 | El acta tiene versión, fecha de cierre, veredicto e identificación de ambos evaluadores |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P9.MATFR | Lector frío con el texto completo o con más de 10 minutos | R1 |
| P9.OPACFR | El lector frío no identifica pregunta, respuesta, novedad o límite | R2, R3 |
| P9.RECAL | Lector frío reutilizado tras correcciones | R4 |
| P9.JUEZ | Revisor experto con conflicto de interés o participación previa | R5 |
| P9.DESENINC | Desenlace de P6 mal aplicado y no advertido | R6 |
| P9.ASIMEXP | Paridad del rival no verificada en claims tipo B | R6 |
| P9.FISICA | Incoherencia física, matemática o de propagación no advertida | R7 |
| P9.TRANSP | Declaración de transparencia incompleta o con fechas inconsistentes no detectada | R8 |
| P9.MOTINC | Motivación de P0 objetada sin dictamen ni AUS o PRC | R9 |
| P9.PRECOM | Precedente omitido no detectado o no enviado a P1 | R10 |
| P9.NUMINC | Discrepancia numérica ignorada | R11 |
| P9.EVTSIL | Evidencia tardía o viciada tratada como ajuste local, sin incidente | R12 |

### Retornos que emite

| Color | Código | Destino | Condición |
| --- | --- | --- | --- |
| Verde | PRO | P8 | Defecto de prosa: ambigüedad, sintaxis que entorpece la comprensión o adjetivos sin soporte |
| Amarillo | EST | P7 | Defecto de estructura o figuras: la novedad o el límite no se encuentran, display items confusos o sin umbral, desorden argumental |
| Amarillo | JER | P3 | Defecto de jerarquía: el lector confunde qué sostiene qué o C0 queda diluido |
| Amarillo | AUS | P2 | Límite o claim ausente del C‑set, incluida una motivación de P0 reclasificada como límite |
| Amarillo | PRC | P1 | Precedente omitido que solapa la dimensión abierta: P1 revisa la ficha y el enunciado de novedad; si cambia el claim de novedad, P2 se reejecuta. H# no se modifica |
| Rojo | EVT | P4 | Afirmación central sin sustento en el E‑set o datos viciados: incidente interno sobre P0–P3 y P7; no se reporta en el artículo |

### Avance

Hacia P10: acta con veredicto "Aprobado sin observaciones" y manuscrito validado por evaluadores independientes.

### Retornos que recibe

Ninguno. P9 recibe el manuscrito corregido desde la fase donde terminó el ciclo del retorno emitido (normalmente P8).

### Registro mínimo

- Acta de verificación con identificación del lector frío y del revisor experto
- Cuestionario de extracción ciega con el tiempo utilizado
- Contador de lectores fríos consumidos
- Declaración de independencia del revisor experto
- Informe técnico del revisor: paridad, desenlace, incertidumbre, física, transparencia y motivación de P0
- Matriz de retornos emitidos: fecha, código, destino, motivo y cierre tras la reentrada
- Si hubo PRC: R# del precedente y justificación del solapamiento
- Si hubo EVT: informe del incidente sobre P0–P3 y P7

### IA (opcional)

- Delegable: concordancia numérica entre tablas, figuras y texto; formato del acta; contraste de citas bibliográficas.
- No delegable: la extracción ciega del lector frío humano; el juicio técnico del revisor; la decisión de abrir EVT o emitir PRC.
- Verificación: las alertas de cualquier escaneo con IA las revisa el evaluador humano; una respuesta de un modelo de lenguaje nunca reemplaza al lector frío humano.

### Notas

1. El lector frío es un recurso no renovable: tras fallar la prueba, ya sabe qué buscaba el autor y no puede evaluar la versión corregida. El contador expone la deuda de comunicabilidad de la primera versión.
2. PRC cubre el caso en que la búsqueda de P1 omitió un trabajo que el revisor conoce. P1 acota el enunciado de novedad; H# no cambia, porque la pregunta es inalterable tras la evidencia.
3. El revisor audita la honestidad metodológica tanto como la física: su revisión de la regla de desenlace y de la declaración de transparencia asegura que el manuscrito no oculte datos vistos, fechas ni reintentos.

## P10 — Cierre y archivo del registro

**Propósito:** verificar la integridad de la cadena metodológica, congelar la cápsula reproducible separando lo público de lo interno y archivar el registro antes del envío a la revista.

### Entrada

- Acta de P9 con veredicto "Aprobado sin observaciones"
- Manuscrito final y material suplementario (de P8)
- Artefactos versionados: H# (P0), ficha P1, C‑set (P2), J# (P3), E‑set (P4), protocolo P5, actas y hashes de P6, F‑set (P7)
- Registro acumulado de retornos (P0–P9), con logs de INV, incidentes EVT si existieron y contador de lectores fríos
- Código de simulación o control, scripts de adquisición y pipelines de análisis y figuras

### Salida canónica (acta de cierre, cápsula y archivo, versión, fecha)

```text
EXPEDIENTE Y CADENA DE CUSTODIA
  Manuscrito ........... hash SHA-256 del PDF final y de las fuentes
  Historial de fases ... tabla de artefactos: ID · versión · fecha · hash
  Auditoría cronológica:
    1. H# (P0) < protocolo P1
    2. protocolo P1 < ejecución P1
    3. predicción de magnitud (P0) < acceso al resultado del observable
    4. exclusiones (P4) < primeros resultados (P6)
    5. límite de factibilidad < veredictos de P4 (modo B) o diseño P5
    6. cada versión v<k> de P5 < primera adquisición bajo v<k>
    7. aprobación P9 < cierre P10

MÉTRICAS DEL PROCESO
  Lectores fríos ....... total consumidos en P9
  Retornos de construcción  desglose (PRE, NOV, RTP, SEV, PNS, HUE, NOB,
                         NEG, PAR, INV, FSD, RED)
  Retornos de auditoría  verdes (PRO) · amarillos (EST, JER, AUS, PRC,
                         CRN) · rojos (EVT)
  Reintentos ........... corridas INV frente a N
  Tiempo de ciclo ...... inicio P0 · cierre P10 · días transcurridos

CÁPSULA PÚBLICA (acompaña al artículo)
  /data ................ crudos con hash + procesados; datos restringidos:
                         hash, justificación y protocolo de acceso
  /src ................. simulación, control, análisis y figuras
  /environment ......... Dockerfile o lockfile con versiones exactas y
                         semillas fijadas
  /records ............. protocolo P5, log de INV y desviaciones,
                         declaración de transparencia

ARCHIVO INTERNO (preservación institucional, no se publica)
  Formularios completos P0–P10; actas de P9 con identidad de evaluadores;
  incidentes EVT; discrepancias y métricas del proceso

DESTINO
  Revista o venue ...... nombre
  Políticas ............ datos abiertos, código y uso de IA
  Identificador ........ DOI, Zenodo o commit inmutable
```

### Requisitos verificables

| ID | Requisito |
| --- | --- |
| R1 | P9 tiene acta con veredicto "Aprobado sin observaciones" y ningún retorno de auditoría abierto |
| R2 | Todos los artefactos de P0 a P9 tienen versión cerrada, fecha y hash |
| R3 | La auditoría cronológica verifica los siete puntos; todo anacronismo dispara CRN hacia P2 |
| R4 | El acta contabiliza lectores fríos, reintentos por INV y frecuencia de retornos por color |
| R5 | Los datos crudos están en la cápsula pública con su hash, o declarados no publicables con hash, causa y vía de acceso; en ambos casos incluyen las corridas INV |
| R6 | El entorno declara semillas fijadas y un archivo de dependencias con versiones exactas |
| R7 | La reproducción en entorno limpio genera los valores y figuras de P8 dentro de la precisión publicada o de una tolerancia declarada a priori |
| R8 | Si la reproducción falla o discrepa fuera de tolerancia, se emite EVT hacia P4 |
| R9 | La cápsula pública omite la identidad de los evaluadores de P9, las métricas del proceso y los incidentes EVT, que quedan en el archivo interno |
| R10 | El PDF final y las fuentes están sellados con hash SHA-256 |
| R11 | El acta de cierre tiene versión, fecha y firma del autor responsable |

### Modos de fallo

| Código | Fallo | Detecta |
| --- | --- | --- |
| P10.PEND | Cierre con observaciones de P9 o retornos pendientes | R1 |
| P10.HUSTO | Artefacto sin hash o sin versión formal | R2 |
| P10.ANACR | Inconsistencia cronológica sin CRN | R3 |
| P10.METRIC | Conteo de lectores fríos o de retornos omitido | R4 |
| P10.DATIN | Datos crudos con hash distinto de P6, corridas INV omitidas o datos restringidos sin hash, causa o vía de acceso | R5 |
| P10.ENTOR | Entorno sin semillas fijadas o con versiones flotantes | R6 |
| P10.NOREP | Reproducción que discrepa de P8 fuera de tolerancia | R7, R8 |
| P10.FILTRO | Identidades de P9, métricas o incidentes publicados en la cápsula pública | R9 |
| P10.ALTER | Archivos fuente o PDF modificados después de calcular los hashes | R10 |

### Retornos que emite

| Color | Código | Destino | Condición |
| --- | --- | --- | --- |
| Amarillo | CRN | P2 | Violación cronológica: los claims afectados se degradan a exploratorios, P8 actualiza la declaración de transparencia y P9 vuelve a auditar. Se registra además como falla de verificación de P9 (P9.TRANSP) |
| Rojo | EVT | P4 | La reproducción en entorno limpio discrepa de P8 fuera de tolerancia: incidente interno sobre P0–P3 y P7 |

### Avance

Envío del manuscrito a la revista, publicación de la cápsula reproducible con identificador persistente y resguardo del archivo interno.

### Retornos que recibe

Ninguno. P10 es la fase terminal.

### Registro mínimo

- Acta de cierre con tabla de artefactos y hashes
- Auditoría cronológica de los siete puntos
- Métricas del proceso: lectores fríos, reintentos y retornos
- Reporte de la reproducción en entorno limpio, con semillas y tolerancias
- Cápsula pública verificada, sin datos de evaluadores
- Archivo interno sellado: formularios P0–P10, actas de P9, incidentes EVT y retornos CRN

### IA (opcional)

- Delegable: cálculo de hashes; generación de Dockerfile, devcontainer y lockfiles; scripts de reproducción (Makefile o pipeline); chequeo de las pautas de envío de la revista.
- No delegable: firma del acta; validación de la auditoría de fechas; certificación de la reproducción; decisión de emitir CRN o EVT; autorización del envío.
- Verificación: los scripts de hash y de reproducción se ejecutan en un contenedor aislado y deben terminar con código de salida cero.

### Notas

1. La auditoría cronológica es la prueba forense del proceso: si una fecha no cuadra, no se reescribe el registro; se emite CRN, el claim pasa a exploratorio y el hecho se declara en Métodos.
2. Reproducibilidad pragmática: en cómputo paralelo o simulación estocástica la igualdad bit a bit puede no alcanzarse; por eso R7 exige semillas fijadas y concordancia con la precisión publicada.
3. Muchos retornos amarillos o un alto consumo de lectores fríos no desmerecen el manuscrito: muestran que el control de calidad actuó antes de la revisión externa, y orientan qué fases reforzar.

## Pendientes

Todas las fases están redactadas; quedan cinco decisiones abiertas.

- [x] Redactar P5 (diseño de experimento). Su entrada ya está definida: E# planificadas, tabla de paridad declarada, exclusiones previsibles, HUE de modo B y límite de factibilidad. Su requisito central es fijar los criterios de validez del ensayo y el número máximo de reintentos N antes de adquirir.
- [x] Redactar P6 (ejecución), incluida la regla de que una paridad violada en modo A es INV y no NEG.
- [x] Redactar P10.
- [ ] Diseñar las plantillas de pregunta de caracterización y de mecanismo, cuando exista un caso real que las motive. Afectan a R4 de P0 y al tipo esperado de C0 en P2.
- [ ] Decidir si los números de requisito se congelan al cerrar cada fase, igual que los IDs de objetos, para no romper referencias en registros de artículos reales.
- [ ] Evaluar, con el uso, si P4 debe dividirse en "cobertura" y "rescate" (ver nota 1 de P4).
- [ ] Validar con el uso los valores por defecto del chequeo acotado de P0 (30 a 120 min, fuentes mínimas).
- [ ] Diseñar P11 (revisión y respuesta a pares). Principios: todo análisis pedido por revisores es exploratorio salvo que estuviera previsto en P5; los ensayos nuevos entran como modo A por P5 y P6; toda modificación de claims o estructura pasa por una nueva verificación en P9 antes del reenvío.
