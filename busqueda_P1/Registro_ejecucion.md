# Registro de ejecución · búsqueda P1 (protocolo v1)

Ejecutó: Jesús García. Transcrito de la tabla que entregó el autor el 2026-11-03; las observaciones entre corchetes las agregó Claude al verificar las exportaciones.

| Código | Base | Fecha y hora | Cadena (o variante) | Filtros | Total | Exportados | Archivo | Observación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Scopus | 2026-11-03 09:52 | tal cual | PUBYEAR > 1999 | 37 | 37 | S1_scopus.csv | |
| S2 | Scopus | 2026-11-03 09:56 | tal cual | PUBYEAR > 1999 | 35 | 35 | S2_scopus.csv | |
| S3 | Scopus | 2026-11-03 10:00 | tal cual | PUBYEAR > 1999 | 78 | 78 | S3_scopus.csv | |
| S4 | Scopus | 2026-11-03 10:02 | tal cual [el registro copió solo el primer bloque; los 115 registros contienen el bloque MPC, así que la cadena se aplicó completa] | PUBYEAR > 1999 [no previsto en el protocolo] | 115 | 115 | S4_scopus.csv | |
| S5 | Scopus | 2026-11-03 10:05 | tal cual | PUBYEAR > 1999 [no previsto] | 64 | 64 | S5_scopus.csv | |
| S1 | WoS | 2026-11-03 10:10 | tal cual | PY=(2000-2026) | 18 | 18 | S1_WoS.txt | |
| S2 | WoS | 2026-11-03 10:14 | tal cual | PY=(2000-2026) | 28 | 28 | S2_WoS.txt | |
| S3 | WoS | 2026-11-03 10:18 | tal cual | PY=(2000-2026) | 69 | 69 | S3_WoS.txt | |
| S4 | WoS | 2026-11-03 10:21 | tal cual | PY=(2000-2026) [no previsto] | 92 | 92 | S4_WoS.txt | |
| S5 | WoS | 2026-11-03 10:23 | tal cual | PY=(2000-2026) [no previsto] | 74 | 74 | S5_WoS.txt | |
| S1 | IEEE Xplore | 2026-11-03 10:50 | tal cual (sin error de comodines) | 2000–2026 | 29 | 29 | S1_ieee.csv | |
| S2 | IEEE Xplore | 2026-11-03 10:55 | tal cual | 2000–2026 | 45 | 45 | S2_ieee.csv | |
| S3 | IEEE Xplore | 2026-11-03 10:57 | tal cual | 2000–2026 | 14 | 14 | S3_ieee.csv | |
| S4 | IEEE Xplore | 2026-11-03 10:59 | tal cual | 2000–2026 [no previsto] | 70 | 70 | S4_ieee.csv | |
| S5 | IEEE Xplore | 2026-11-03 11:00 | tal cual | 2000–2026 [no previsto] | 17 | 17 | S5_ieee.csv | |
| S1-GS | Google Scholar (PoP) | 2026-11-03 11:10 | tal cual | 2000–2026, máx. 100 | 6 | 6 | S1_GS.csv | [total aproximado de Scholar no anotado] |
| S2-GS | Google Scholar (PoP) | 2026-11-03 11:15 | tal cual | 2000–2026, máx. 100 | 0 | 0 | — | 0 resultados |
| S3-GS | Google Scholar (PoP) | 2026-11-03 11:17 | tal cual | 2000–2026, máx. 100 | 6 | 6 | S3_GS.csv | |
| S4-GS | Google Scholar (PoP) | 2026-11-03 11:19 | tal cual | 2000–2026 [no previsto], máx. 100 | 10 | 10 | S4_GS.csv | |
| S5-GS | Google Scholar (PoP) | 2026-11-03 11:20 | tal cual | 2000–2026 [no previsto], máx. 100 | 6 | 6 | S5_GS.csv | |

Hora de inicio: 09:50   Hora de fin: 11:22   Minutos: 82

## Corrida complementaria S4a (ampliación por R12, para recuperar Rivera 2009)

| Código | Base | Fecha y hora | Cadena | Filtros | Total | Exportados | Archivo | Observación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S4a | Scopus | 2026-11-03 ≈ 11:45 [hora del archivo] | `TITLE-ABS-KEY ( "plant-friendly" AND ( identification OR "input signal*" OR "input design" ) )` | sin límite de años | 42 | 42 | S4a_scopus.csv | [conteo verificado por Claude] |
| S4a | WoS | 2026-11-03 ≈ 11:47 [hora del archivo] | `TS=("plant-friendly" AND (identification OR "input signal*" OR "input design"))` | sin límite de años | 31 | 31 | S4a_WoS.txt | [conteo verificado por Claude] |

**Verificación de Claude (2026-11-03):** los 19 archivos tienen exactamente el número de registros anotado (813 en total). Mínimo año en S4/S5 de Scopus: 2001 y 2000.
