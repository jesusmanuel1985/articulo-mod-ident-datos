# Instructivo: sesión de cierre del chequeo de novedad (P0)

**Para:** quien apoya el artículo del banco de emulación termosolar
**Encarga:** Jesús García · **Versión:** 2 · **Fecha:** 2026-11-02
**Tiempo máximo:** 45 minutos de búsqueda. **No se extiende.**

---

## 1. Qué se te pide

Dos agentes de IA ya hicieron una primera búsqueda, pero sin acceso a Scopus ni a Web of Science. Encontraron trabajos útiles, pero quedaron tres huecos que **solo se cierran con esas bases**. Tu sesión cubre exactamente esos tres huecos:

| Tarea | Qué falta | Tiempo orientativo |
| --- | --- | --- |
| **A** | Encontrar **una revisión** publicada en los últimos 5 años (desde noviembre de 2021) | 15 min |
| **B** | Volver a ejecutar dos búsquedas con operadores booleanos reales | 20 min |
| **C** | Leer los resúmenes de 3 trabajos ya encontrados y confirmar sus datos | 10 min |

Al final, deja registrado **exactamente** qué buscaste, para que otra persona pueda repetirlo.

## 2. Qué NO es esta tarea

- **No es una revisión del estado del arte.** Esa búsqueda se hace después (fase P1).
- **No se leen artículos completos.** Basta con título y resumen.
- **No se cambia la pregunta.** Si tienes ideas sobre ella, anótalas en "Observaciones".
- **No se repite el trabajo de los agentes.** Lo que ya está verificado (sección 4) solo se confirma.

## 3. La pregunta y cómo comparar trabajos

> ¿Un modelo bilineal de bajo orden de un banco de colectores solares en serie (calentado por resistencias eléctricas), **identificado con una excitación suave del caudal** (cambios lentos, como en la operación normal), predice la temperatura de salida a 1000 s **casi tan bien** como el mismo modelo identificado con una excitación abrupta (PRBS)? En ambos casos la potencia solo cambia en forma binaria, como el paso de nubes.

Evalúa cada trabajo en cuatro dimensiones, con **sí**, **no** o **nd** (no se puede saber con el resumen):

| Dimensión | Cuenta como "sí" | No basta |
| --- | --- | --- |
| **D1. Excitación** *(la central)* | **Compara** una excitación suave, restringida, de mínimo costo o de operación normal contra una fuerte (PRBS, escalones grandes); o diseña la entrada minimizando la perturbación con un requisito de calidad del modelo | Usar PRBS o escalones sin comparar |
| **D2. Estructura** | Modelo bilineal, LPV o físico de pocos parámetros, donde el caudal multiplica a la temperatura | Redes neuronales o cajas negras |
| **D3. Predicción** | **Reporta como resultado el error de predicción a varios pasos** (simulación libre u horizonte de MPC) | Usar un MPC y reportar solo el seguimiento en lazo cerrado; ajuste a un paso |
| **D4. Sistema** | Colectores solares, campo solar, receptor termosolar o proceso térmico con caudal y calentamiento variables | Fotovoltaica; edificios sin caudal manipulado |

**Si encuentras un trabajo con las cuatro dimensiones en "sí", detente y avisa a Jesús ese mismo día con el DOI.**

## 4. Lo que ya encontraron los agentes (no hay que buscarlo de nuevo)

| ID | Trabajo | DOI | Estado | D1 | D2 | D3 | D4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Rivera, Lee, Mittelmann & Braun (2009). Constrained multisine input signals for plant-friendly identification of chemical process systems. *J. Process Control* 19(4):623–635 | 10.1016/j.jprocont.2008.08.006 | DOI verificado; **resumen sin confirmar** | sí | no | **nd** | no |
| R2 | Bombois, Scorletti, Gevers, Van den Hof & Hildebrand (2006). Least costly identification experiment for control. *Automatica* 42(10):1651–1662 | 10.1016/j.automatica.2006.05.016 | DOI verificado; **resumen sin confirmar** | sí | no | no | no |
| P1 | Pipino, Morato, Bernardi, Adam & Normey-Rico (2020). Nonlinear temperature regulation of solar collectors with a fast adaptive polytopic LPV MPC formulation. *Solar Energy* | 10.1016/j.solener.2020.09.005 | DOI verificado; **volumen y páginas sin confirmar** (un agente informó 209, 214–225) | no | sí | no | sí |

Respaldo, que no hay que revisar ahora: Camacho et al. (2007), *Solar Energy* 81(10), Parte I (10.1016/j.solener.2007.01.002) y Parte II (10.1016/j.solener.2007.01.001); Narasimhan & Rengaswamy (2011), *IEEE TAC* (10.1109/TAC.2011.2132290); Narasimhan & Bombois (2012), IFAC (10.3182/20120711-3-BE-2027.00124).

## 5. Preparación (≈ 5 min, no cuenta en el tiempo)

1. Entra a **Scopus** y **Web of Science** desde la red de la universidad o la VPN.
2. Abre una copia de la plantilla de entrega (sección 9).
3. **Anota la hora de inicio** al lanzar la primera búsqueda.

## 6. Tarea A: encontrar una revisión reciente (≈ 15 min)

**Scopus** (búsqueda avanzada):

```text
C4  TITLE-ABS-KEY ( ( "system identification" OR "data-driven" OR modeling OR modelling ) AND ( "solar thermal" OR "concentrated solar power" OR "solar collector" OR "solar field" ) AND ( control OR identification ) ) AND PUBYEAR > 2020
    → filtro Document type = Review
```

**Web of Science** (Advanced Search):

```text
C4  TS=(("system identification" OR "data-driven" OR modeling OR modelling) AND ("solar thermal" OR "concentrated solar power" OR "solar collector" OR "solar field") AND (control OR identification)) AND PY=(2021-2026)
    → filtro Document Types = Review
```

Esta C4 es más amplia que la original, porque la original dio 0 resultados en las fuentes que usaron los agentes. Regístrala como **C4b**.

- Ordena por relevancia y revisa hasta **50 títulos**.
- Una revisión es **pertinente** si trata el modelado, la identificación o el control (incluido MPC) de colectores, campos solares o plantas termosolares.
- Comprueba la fecha: debe ser de **noviembre de 2021 en adelante**.
- Elige **una**, la más pertinente, y anota su DOI. Si hay varias buenas, anota hasta 3 en "Observaciones".
- **Si no encuentras ninguna,** anótalo con la cadena y el número de resultados. Es un resultado válido.

## 7. Tarea B: repetir C1 y C2 con booleanos (≈ 20 min)

| Código | Scopus | Web of Science |
| --- | --- | --- |
| C1 | `TITLE-ABS-KEY ( ( "plant-friendly" OR "input design" OR "least costly" ) AND identification AND ( thermal OR solar ) )` | `TS=(("plant-friendly" OR "input design" OR "least costly") AND identification AND (thermal OR solar))` |
| C2 | `TITLE-ABS-KEY ( ( bilinear OR LPV ) AND ( "solar collector" OR "solar field" ) AND ( identification OR "model predictive control" ) )` | `TS=((bilinear OR LPV) AND ("solar collector" OR "solar field") AND (identification OR "model predictive control"))` |

**Por cada cadena y base:**
1. Copia la cadena **tal cual**. Si da error de sintaxis, corrígela y regístrala como variante (C1a…), con el error que daba.
2. Anota el **número de resultados** que informa la base.
3. Ordena por relevancia y revisa hasta **50 títulos** (todos, si son menos).
4. Por cada título pertinente, lee el resumen y marca D1–D4.
5. Si cumple **2 o más** dimensiones en "sí" y **no está en la sección 4**, pásalo a la tabla de nuevos candidatos.

## 8. Tarea C: confirmar R1, R2 y P1 (≈ 10 min)

Busca cada DOI en Scopus o en la página de la editorial y **lee el resumen**. Para cada uno:
- confirma revista, volumen, número, páginas y año;
- marca D1–D4 según **lo que dice el resumen**, en particular **D3 de R1**: ¿reporta el error de predicción a varios pasos?;
- escribe con tus palabras una línea de **por qué es cercano** y otra de **en qué difiere** de la pregunta.

Si un dato no coincide con la tabla de la sección 4, anota el valor correcto. Corregir es parte de la tarea.

## 9. Veredicto, regla de parada y entrega

**Veredicto.** Revisa las filas en orden y aplica la primera que se cumpla, considerando todos los trabajos: los de la sección 4 y los nuevos.

| Orden | Veredicto | Condición |
| --- | --- | --- |
| 1 | respondida | Algún trabajo cumple D1, D2, D3 y D4 |
| 2 | parcial | Algún trabajo cumple D1 y al menos otra dimensión; o alguno cumple D2, D3 y D4 a la vez |
| 3 | abierta | Ninguna de las anteriores |

Si una dimensión que decide el veredicto queda en "nd", elige **parcial**.

**Regla de parada:** a los **45 minutos** te detienes, aunque falten tareas. Anota cuáles quedaron sin hacer.

**Entrega:** un solo archivo con estas partes.

```text
A. REGISTRO DE BÚSQUEDA
| Código | Base | Fecha y hora | Cadena exacta | Filtros | N.º resultados | N.º títulos revisados |

B. REVISIÓN RECIENTE
Referencia completa · DOI · fecha de publicación · por qué es pertinente
(o "No encontrada" + cadena + n.º de resultados)

C. CONFIRMACIÓN DE R1, R2 Y P1
| ID | Datos confirmados o corregidos | D1 | D2 | D3 | D4 | Por qué es cercano | En qué difiere |

D. NUEVOS CANDIDATOS (≥ 2 dimensiones, no listados en la sección 4)
| Referencia | DOI | D1 | D2 | D3 | D4 | Nota |

E. RESUMEN
Veredicto: abierta | parcial | respondida — <una línea>
Bases usadas: Scopus, Web of Science
Tiempo: <minutos> (inicio hh:mm – fin hh:mm)
Tareas sin terminar: <lista o "ninguna">

F. OBSERVACIONES (opcional)
```

## 10. Lista de control antes de entregar

- [ ] Usé **Scopus y Web of Science**.
- [ ] Anoté hora de inicio y de fin, y no pasé de 45 min.
- [ ] Cada cadena quedó registrada **textualmente**, con filtros, n.º de resultados y n.º revisados.
- [ ] Encontré una revisión desde noviembre de 2021, o dejé constancia de que no la hay.
- [ ] Leí los resúmenes de R1, R2 y P1, y marqué D1–D4 según ellos.
- [ ] Cada referencia nueva tiene un DOI **que abrí yo**.
- [ ] Hay un único veredicto, coherente con la tabla de la sección 9.
