# Registro del chequeo acotado de novedad (P0) — H0 borrador

Reconstruido el 2026-11-02 a partir de seis exportaciones (WoS `.txt`, Scopus `.csv`) entregadas por el autor, más dos ejecuciones previas con agentes de IA.
Las cadenas de C4b (v2) las confirmó el autor; las de C1 y C2 son las del instructivo v2. No quedan campos por confirmar.

## A. Registro de búsqueda

| Código | Base | Fecha | Cadena | Filtros | Registros exportados | Observación |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | Web of Science | 2026-11-02 (campo DA) | `TS=(("plant-friendly" OR "input design" OR "least costly") AND identification AND (thermal OR solar))` (instructivo v2, sin variante declarada) | ninguno | 5 (conjunto completo) | 1 pertinente (Lepsien 2025); 1 de D1 (Guzmán-Rivera 2024); 3 fuera de tema |
| C1 | Scopus | 2026-11-02 | `TITLE-ABS-KEY ( ( "plant-friendly" OR "input design" OR "least costly" ) AND identification AND ( thermal OR solar ) )` (instructivo v2) | ninguno | 4 (conjunto completo) | 1 pertinente (Lepsien 2025); 3 fuera de tema ("plant-friendly" en biología, ciberseguridad) |
| C2 | Web of Science | 2026-11-02 | `TS=((bilinear OR LPV) AND ("solar collector" OR "solar field") AND (identification OR "model predictive control"))` (instructivo v2) | ninguno | 1 | Morato et al. 2022 |
| C2 | Scopus | 2026-11-02 | `TITLE-ABS-KEY ( ( bilinear OR LPV ) AND ( "solar collector" OR "solar field" ) AND ( identification OR "model predictive control" ) )` (instructivo v2) | ninguno | 1 | Morato et al. 2022 (mismo registro) |
| C3 | — | — | `("identification for control" OR "application-oriented input design") AND (MPC OR "model predictive control") AND ("heat exchanger" OR thermal)` | — | — | No forma parte de la sesión humana (el instructivo v2 no la pide); la ejecutaron solo los agentes |
| C4b (v1) | Web of Science | 2026-11-02 | `TS=(("system identification" OR "data-driven" OR modeling OR modelling) AND ("solar thermal" OR "concentrated solar power" OR "solar collector" OR "solar field") AND (control OR identification)) AND PY=(2021-2026)` (instructivo v2) | años 2021–2026; **sin filtro "Review"** (solo 1 de 50 registros es revisión) | 50 exportados | Superada por v2 |
| C4b (v2) | Web of Science | 2026-11-02 | `("system identification" OR "data-driven" OR modeling OR modelling) AND ("solar thermal" OR "concentrated solar power" OR "solar collector" OR "solar field") AND (control OR identification)` (texto confirmado por el autor; campo Topic) | Document Types = Review; los 50 exportados son de 2022–2026, así que el límite de años se aplicó como filtro | **54 resultados**; se exportaron los 50 primeros por relevancia | Pertinentes: Goel 2026, Kowalik 2025, **Gil et al. 2022** y **Untrau et al. 2022** (ver B) |
| C4b (v1) | Scopus | 2026-11-02 | misma cadena que v2 | **sin filtro "Review"** | > 200 exportados | Exportación amplia; la mayoría fuera de tema. Superada por v2 |
| C4b (v2) | Scopus | 2026-11-02 | `TITLE-ABS-KEY ( ( "system identification" OR "data-driven" OR modeling OR modelling ) AND ( "solar thermal" OR "concentrated solar power" OR "solar collector" OR "solar field" ) AND ( control OR identification ) ) AND PUBYEAR > 2020` (texto confirmado por el autor) | Document type = Review; límite de año **no aplicado** en la exportación | 50 resultados (conjunto completo, ordenado por relevancia). **Con el límite de año aplicado: 30 resultados** (informado por el autor) | Los 50 son revisiones, pero **18 son anteriores a 2021** (2013–2020): el límite `PUBYEAR > 2020` no quedó aplicado en esa ejecución. No cambia la elección: Goel 2026 y Kowalik 2025 aparecen y están dentro de la ventana |

**Desviaciones respecto del instructivo:**
1. En la primera ejecución de C4b no se aplicó el filtro *Review*. Se corrigió en ambas bases (v2).
2. En C4b v2 de Scopus el límite de año no se aplicó en la exportación. Al repetirla con el límite quedan 30 resultados, todos incluidos entre los 50 ya revisados, así que el cribado no cambia; el texto que transcribió el autor omite `TITLE-ABS-KEY (` y deja un paréntesis sin abrir, lo que sugiere un error al pegar la cadena. Se registra la cadena del instructivo, que el autor confirmó.
3. Los totales los informó el autor después de la sesión: C4b v2 dio 30 en Scopus (con límite de año; 50 sin él) y 54 en WoS (se revisaron los 50 primeros por relevancia). En C1 y C2 el total coincide con lo exportado.

## B. Revisión reciente (≤ 5 años)

**Goel, A.; Manik, G.; Kumar, S.; Deshawar, D.; Tiwari, V.; Srivastava, U.; Chattopadhyay, S. (2026).** *Parabolic Trough Solar Collectors for Industrial Process Heat Applications: A Review Around Feasibility, Optimization, and Control.* WIREs Energy and Environment 15(2), e70027. DOI 10.1002/wene.70027.
Pertinente porque revisa el modelado dinámico y el control de colectores ante entrada solar fluctuante. Limitación: centrada en cilindro-parabólicos, no en placa plana.

Alternativas encontradas en las mismas exportaciones (Kowalik y Ochoa-Barragán también aparecen en C4b v2, con filtro *Review*):
- Kowalik, R. (2025). *Adaptive and Stepwise Solar Tracking Systems in Flat-Plate and Tubular Collectors: A Comprehensive Review…* Energies 18(23), 6106. DOI 10.3390/en18236106 (incluye modelado y control predictivo, placa plana).
- Ochoa-Barragán, R. et al. (2026). *Artificial Intelligence Enabling Intelligent Solar Energy Systems…* Processes 14(7), 1167. DOI 10.3390/pr14071167.
- **Gil, J.D.; Topa, A.; Álvarez, J.D.; Torres, J.L.; Pérez, M. (2022).** *A review from design to control of solar systems for supplying heat in industrial process applications.* Renew. Sustain. Energy Rev. 163, 112461. DOI 10.1016/j.rser.2022.112461. Revisa técnicas de control (incluido MPC) de campos solares térmicos de proceso, con placa plana; es la más cercana al banco. Publicada en julio de 2022, dentro de la ventana. **Lectura prioritaria en P1.**
- Untrau, A. et al. (2022). *Analysis and future perspectives for the application of Dynamic Real-Time Optimization to solar thermal plants: A review.* Solar Energy 241, 275–291. DOI 10.1016/j.solener.2022.05.058 (MPC, estimación de parámetros y operación óptima de plantas solares térmicas).
- Española, J.P. & Palconit, E.V. (2026). *Model predictive control and digital twin integration for optimisation of hybrid solar thermal–biomass drying systems: a comprehensive review.* Int. J. Ambient Energy 47(1), 2748554. DOI 10.1080/01430750.2026.2748554 (MPC con modelos de predicción en secado solar; útil para P1).

## C. Confirmación de R1, R2 y P1

| ID | Fuente de la confirmación | Estado |
| --- | --- | --- |
| R1 Rivera et al. 2009 | No aparece en las exportaciones | DOI verificado por los agentes; **resumen sin leer** `[PENDIENTE]` |
| R2 Bombois et al. 2006 | No aparece en las exportaciones | DOI verificado por los agentes; **resumen sin leer** `[PENDIENTE]` |
| P1 Pipino et al. 2020 | Citado por Sánchez-Amores 2023, Gholaminejad 2022 y Zhang 2025 como *Sol. Energy* **209, p. 214**, DOI 10.1016/j.solener.2020.09.005 | Volumen y página inicial confirmados por tres fuentes; página final y resumen sin confirmar |

## D. Candidatos nuevos (≥ 2 dimensiones; cribado por resumen)

| Referencia | DOI | D1 | D2 | D3 | D4 | Nota |
| --- | --- | --- | --- | --- | --- | --- |
| Machado et al. 2023, Appl. Energy 339, 120944 | 10.1016/j.apenergy.2023.120944 | no | sí | sí | sí | Modelo EDP identificado con 25 días de operación normal y validado en 6 días |
| Svensen et al. 2024, Heliyon 10, e31027 | 10.1016/j.heliyon.2024.e31027 | no | sí | nd | sí | Caja gris (EDE) con datos reales de planta |
| Pataro et al. 2024, IEEE TCST 32(1), 99–111 | 10.1109/TCST.2023.3298230 | no | sí | nd | sí | Identificación paramétrica del campo AQUASOL-II |
| Morato et al. 2022, IFAC-PapersOnLine 55(16), 278–283 | 10.1016/j.ifacol.2022.09.037 | no | sí | no | sí | MPC LPV con colector solar de referencia |
| Mechhoud & Belkhatir 2024, J. Process Control 143, 103321 | 10.1016/j.jprocont.2024.103321 | no | sí | no | sí | Modelo bilineal con caudal como entrada; solo control |
| Goel et al. 2023, IEEE Access 11, 33381–33392 | 10.1109/ACCESS.2023.3263473 | no | sí | no | sí | Función de transferencia caudal→temperatura desde modelo analítico |
| Castilla et al. 2024, Eng. Appl. AI 133, 108387 | 10.1016/j.engappai.2024.108387 | no | no | sí | sí | Gemelo digital RNA de campo de placa plana |
| Khanghah et al. 2025, ICCAD 2025 | 10.1109/ICCAD64771.2025.11099485 | no | no | nd | sí | Compara ARX, ARMAX, NARX, LSTM en colector de placa plana |
| Díaz-Salgado et al. 2023, Int. J. Basic Appl. Sci. 12(1), 14–21 | 10.14419/k81wh647 | nd | sí | nd | sí | Identificación por mínimos cuadrados; estudia la forma de la señal de excitación en planta a escala. Revista de baja visibilidad. Texto completo no accesible al 2026-11-02 (sitio de la revista caído; sin copia del PDF en Wayback Machine); clasificado solo por resumen. Último autor fue editor de la revista (2018–2020, según OpenAlex) |

**Cercanos a D1 fuera de sistemas térmicos solares:** Guzmán, Rivera, Berenguel & Dormido 2024, IFAC-PapersOnLine 58(7), 61–66, DOI 10.1016/j.ifacol.2024.08.011 (diseño de experimentos *plant-friendly*); Lepsien, Kügler & Schaum 2025, IEEE Access 13, 211944–211959, DOI 10.1109/ACCESS.2025.3636666 (diseño óptimo de entrada en lazo cerrado en un proceso térmico; maximiza información en vez de minimizar perturbación); Zhang et al. 2025, Electronics 14(10), 2048, DOI 10.3390/electronics14102048 (control dual con exploración en campo de colectores, simulado).

## E. Resumen

- **Veredicto:** parcial. Ningún trabajo cumple D1–D4. La fila 2 se cumple por D2 + D3 + D4 (Machado 2023). Díaz-Salgado 2023 tiene D1 y D3 sin determinar, pero aunque ambas fueran "sí" no cubriría la comparación suave/abrupta descrita en la pregunta; queda para P1.
- **Bases:** Scopus y Web of Science (sesión humana); Crossref, OpenAIRE, Europe PMC, arXiv y HAL (agentes, como apoyo).
- **Tiempo:** sesión humana ≈ 25 min (autor) + agentes ≈ 18 min (5 + 13) = **≈ 43 min**, dentro del rango 30–120 min.
- **Pendiente para P1 (no bloquea P0):** leer los resúmenes de Rivera 2009 y Bombois 2006; leer Díaz-Salgado 2023 completo.
