# Seguimiento de citas hacia adelante (R13)

Exportaciones de Scopus (*Cited by*) entregadas por el autor el 2026-11-03; cribado de Claude por título y resumen con los criterios confirmados de P1.
Los CSV se pegaron en la conversación; conviene guardarlos aquí como `citas_<autor>.csv` para la trazabilidad.

| Semilla | Citas en Scopus | Ya estaban en la búsqueda | Nuevos N1 | Nuevos N2 | Resto |
| --- | --- | --- | --- | --- | --- |
| Bagle 2026 | 0 | — | — | — | — |
| Rivera 2009 | ≈ 89 | Narasimhan 2011 (×2), Narasimhan & Bombois 2012, Kumar & Narasimhan 2013, Steenis & Rivera, Banerjee 2026, Ghosh 2014, Yap 2016, Hägg 2013, Deshpande 2013 | 3 (C) | ≈ 20 | fuera de tema (salud conductual, baterías, aeronáutica, audio, etc.) |
| Larsson 2015 | ≈ 41 | Özkan 2016, Larsson 2016, Annergren 2017, Valenzuela 2020, Mesbah 2018, Bavdekar 2016, Jakowluk 2019 | 2 (C) | ≈ 25 | fuera de tema |
| Medinelli Sanino 2007 | 16 | — | 3 (C) | 3 | revisiones generales de energía solar |
| Machado 2023 | ≈ 37 | — | 1 (C) | 5 | gemelos digitales genéricos, FV, hidrógeno, eólica |
| Ampuño 2019 | 12 | Pipino 2020, Morato 2021, Pataro 2024 | 1 (C) | 5 | revisiones |

**Ninguna cita nueva llega a prioridad A o B.** Ninguna compara excitación suave con abrupta en un sistema con caudal manipulado.

## Nuevos N1 (prioridad C)

| Trabajo | Semilla | D1a D1b D2 D3 D4 | Nota |
| --- | --- | --- | --- |
| Esmaili et al. 2018, *Control Eng. Pract.* 72, 206–218, 10.1016/j.conengprac.2017.12.003 | Rivera 2009 | s n n d d | Identificación en lazo cerrado **sin excitación** (solo realimentación) en plantas con MPC, incluida una planta industrial de hidrógeno; alternativa a los ensayos en lazo abierto |
| Chinen et al. 2025, *Ind. Eng. Chem. Res.* 64(40), 19549–19564, 10.1021/acs.iecr.5c01802 | Rivera 2009 | n p n d d | Planta piloto real de captura de CO₂: ensayos dinámicos con PRBS y con multiseno de Schroeder frente a cientos de ensayos estacionarios |
| Otálora et al. 2026, *Control Eng. Pract.* 168, 106742, 10.1016/j.conengprac.2025.106742 | Rivera 2009 | s n n s n | Multisenos control-relevantes y *Model-on-Demand*; buen ajuste en un amplio rango de horizontes de predicción (fotobiorreactor real) |
| Zhang, Wang, Chen, Song & Zhao 2025, *Electronics* 14(10), 2048, 10.3390/electronics14102048 | Larsson 2015 | p n n n s | MPC dual estocástico con exploración en un campo de colectores (simulado); ya identificado en P0 |
| Oshima et al. 2022 (*CACE* 49) y 2024 (*J. Process Control* 136, 103190) | Larsson 2015 | s s n n p | Excitación dirigida: solo se excitan las entradas con desajuste planta–modelo para no degradar el control; FCC simulado |
| Leconte, Achard & Papillon 2012, *Solar Energy* 86(7), 2001–2016, 10.1016/j.solener.2012.04.003 | Sanino 2007 | p n p s s | Modelo gris (física + red neuronal) de un sistema combinado solar identificado con un **ensayo corto de 12 días** que predice el desempeño anual |
| Kishor et al. 2010, *Solar Energy* 84(6), 948–955, 10.1016/j.solener.2010.03.002 | Sanino 2007 | n n p d s | Modelo gris difuso de calentador solar termosifón; predicción de T de salida |
| Khalfallaoui et al. 2011, *Int. J. Sustain. Energy* 30(3), 129–148 | Sanino 2007 | n n s d s | Modelo físico dinámico de calentador solar validado con piloto |
| Castilla, Redondo, Martínez & Álvarez 2024, *Eng. Appl. Artif. Intell.* 133, 108387, 10.1016/j.engappai.2024.108387 | Machado 2023 | s n n d s | Gemelo digital con red neuronal de un campo de placa plana, entrenado con un año de operación |
| Rodríguez-Ossorio et al. 2025, *CCIS* 2581, 141–153 | Ampuño 2019 | s n n d s | ESN con entradas retardadas para la T de salida de AQUASOL-II con datos reales |

## Nuevos N2 relevantes para la introducción o los métodos

- Kumar & Narasimhan 2016, *IECR* 55(14): diseño de entrada con intercambiador de calor simulado.
- Sha'aban 2019 (*IFAC J. Syst. Control* 8) y 2022 (*CSPA*): MPC a partir de datos rutinarios de planta.
- Heirung et al. 2017 (*Automatica* 80) y 2018 (*AIChE J.* 64): MPC dual y aprendizaje activo.
- Pataro et al. 2023 (*IEEE TCST* 31(6)): control de temperatura en AQUASOL-II.
- Aleksiejuk-Gawron & Chochowski 2020 (*Processes* 8): dinámica e identificación paramétrica de un colector de placa plana.
- Ruiz-Moreno et al. 2025 (*ISA Trans.* 158): identificación con RNN y EKF en ACUREX.
