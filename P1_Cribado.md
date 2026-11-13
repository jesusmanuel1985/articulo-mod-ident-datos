# P1 · Cribado por título y resumen (propuesta para confirmar)

Entrada: exportaciones de `busqueda_P1/` y su `Registro_ejecucion.md`. Protocolo: v1 (`P1_Brecha_novedad.md`).
Cribado hecho por Claude el 2026-11-03. **Estado: confirmado por el autor el 2026-11-03** (las cuatro interpretaciones de la sección 5 y la lista N1). Los registros de S4a (P531–P569) se clasificaron con los mismos criterios ya confirmados.
Detalle registro por registro (529 filas, con D1a–D4, nivel, prioridad y nota): `busqueda_P1/Cribado_P1.csv`.

## 1. Volumen

| Paso | N.º |
| --- | --- |
| Paso | S1–S5 | + S4a | Total |
| --- | --- | --- | --- |
| Registros exportados | 813 (19 archivos; S2-GS dio 0) | 73 | 886 |
| Únicos tras quitar duplicados (DOI, o título normalizado) | 529 | 39 nuevos | 568 |
| Duplicados detectados a mano (versión de congreso, idioma) | 5 | 4 | 9 |
| Excluidos por título (fuera de tema) | 395 | 3 | 398 |
| Leídos por resumen | 134 | 36 | 170 |
| Excluidos por resumen (criterio del protocolo) | 2 | 0 | 2 |
| **N2 · contexto** | 92 | 21 | **113** |
| **N1 · precedente** | 35 (9 A, 14 B, 12 C) | 11 (1 A, 2 B, 8 C) | **46** (10 A, 16 B, 20 C) |
| Excluido después por no accesible (P466, Řehoř & Havlena 2009) | | | −1 N1 → **45 N1** (9 A) |
| Reclasificados a N2 tras lectura completa (P288 Micchi 2008, P270 Valenzuela 2020) | | | −2 N1 → **43 N1** (7 A), 115 N2 |

Por base, en registros únicos con presencia: Scopus 322, WoS 281, IEEE 175, Scholar 28. 221 registros aparecen en más de una base. Scholar aportó muy poco, como se esperaba.

## 2. Desviaciones de la ejecución

| N.º | Desviación | Efecto | Propuesta |
| --- | --- | --- | --- |
| D-1 | Se ejecutó el 2026-11-03 (09:50), no "desde el 2026-11-04" como decía el protocolo | El protocolo quedó fijo a las 07:51 de ese día (fecha de modificación del archivo) y no cambió después; la ejecución es posterior, así que R1 se cumple en sustancia | Registrar y aceptar. Repetirla mañana costaría 82 min y daría lo mismo |
| D-2 | S4 y S5 se ejecutaron con límite 2000–2026; el protocolo los dejaba sin límite | Pueden faltar trabajos anteriores a 2000 sobre diseño de entrada e identificación para MPC (Shook et al. 1991–92, Gevers & Ljung 1986, Hjalmarsson et al. 1996, Zhu 1998) | **Aceptada por el autor el 2026-11-03; no se repite.** Motivo: esos trabajos serían N2 (no tocan D2–D4), así que no afectan el veredicto, y se recuperan por el seguimiento de citas hacia atrás desde Rivera 2009, Bombois 2006 y Gopaluni 2002 |
| D-3 | En Scholar no se anotó el total aproximado | Ninguno práctico: Publish or Perish devolvió menos de 100 en todas | Registrar |
| D-4 | El registro de Scopus S4 copió solo el primer bloque de la cadena | Ninguno: los 115 registros contienen el bloque MPC | Corregido en el registro |

Nota: el instalador `PoP8Setup.exe` que había quedado en `busqueda_P1/` ya lo eliminó el autor (2026-11-03).

## 3. Comprobación R12 (los R# de P0 deben reaparecer)

| Trabajo | ¿Aparece? | Dónde | Lectura |
| --- | --- | --- | --- |
| Bombois et al. 2006 | Sí | S4 (Scopus, WoS) | ✓ |
| Machado et al. 2023 | Sí | S3 (solo WoS) | ✓. Scopus no lo devolvió con S3; dato útil para el seguimiento de citas |
| **Rivera et al. 2009** | **Sí, con S4a** | S4a (Scopus, WoS) | ✓ tras la ampliación. S1–S5 no lo devolvían: su resumen no menciona MPC ni "identification for control", que S4 exige |
| Mechhoud & Belkhatir 2024 | No | — | Justificable: S3 exige MPC, varios pasos o predicción, y en P0 se clasificó con D3 = no ("solo control"). Por el protocolo quedaría excluido ("solo diseña el controlador") o en N2; no afecta el veredicto. Aparece Mechhoud 2016 (ACC), del mismo grupo |

## 4. Corrida complementaria S4a (≈ 10 min, solo Scopus y WoS, sin límite de años)

No cambia el protocolo: S4a es la ampliación que R12 prevé para Rivera 2009. (S4-pre y S5-pre se descartaron: ver D-2.)

```text
S4a Scopus  TITLE-ABS-KEY ( "plant-friendly" AND ( identification OR "input signal*" OR "input design" ) )
S4a WoS     TS=("plant-friendly" AND (identification OR "input signal*" OR "input design"))
```

**Ejecutada el 2026-11-03:** Scopus 42, WoS 31 (73 registros, 39 nuevos, desde 1997). Recuperó Rivera 2009 y su familia: Braun, Rivera & Stenman 2001 (PRS multinivel frente a PRBS en un reactor RTP), Rivera et al. 2007 (IEEE CSM, destilación) y la línea de Narasimhan sobre límites al tamaño de movimiento de la entrada, que es la referencia de método más cercana a la rampa limitada de H0 (N2, no afecta el veredicto).

## 5. Interpretaciones aplicadas (confirmadas por el autor el 2026-11-03; Vallianos 2022 queda excluido)

1. **"Otra dimensión" en N1 significa D2, D3 o D4.** Si D1a + D1b contara, Bombois 2006 y toda la familia *least costly* serían N1, en contra de la clasificación esperada que aprobaste.
2. **Exclusión por título = fuera de tema:** no identifica modelos dinámicos para control o predicción de un sistema térmico, ni trata diseño de excitación ni criterios de predicción a varios pasos (baterías, motores, clima, redes eléctricas, etc.). El protocolo no lo decía explícitamente; si lo aplico al pie de la letra ("al menos una dimensión en sí"), casi todo trabajo de ML sobre colectores sería N2.
3. **Destilación y reactores con camisa o CSTR no adiabático: D4 = nd.** Tienen caudales y calentamiento, pero no son colectores. Esto mete en N1 a Micchi 2008, Larsson 2015 y Yang & Rivera 2001.
4. **Vallianos et al. 2022** (modelos RC desde termostatos, predicción a 24 h, datos de operación normal) quedó **excluido** por "edificio sin caudal manipulado". Es muy afín en D1a–D3; dime si prefieres pasarlo a N2.

## 6. Resultado: N1 por prioridad

**Prioridad A** (sistema térmico o solar con D1, o comparación suave/abrupta explícita). Lectura completa obligatoria.

| ID | Trabajo | D1a D1b D2 D3 D4 | Por qué |
| --- | --- | --- | --- |
| P085 | Bagle, Sartori & Goia 2026, *Applied Energy*, 10.1016/j.apenergy.2026.127756 | s s nd s nd | **El más cercano a la diferencia declarada.** Identifica con dos semanas de operación normal y compara contra un modelo identificado con PRBS, con NRMSE de simulación a un día. Edificio con radiadores, no colectores |
| P288 | Micchi & Pannocchia 2008, *J. Process Control*, 10.1016/j.jprocont.2007.10.003 | s s no nd nd | Entradas generadas en lazo cerrado frente a señales aleatorias en lazo abierto; los modelos de lazo cerrado rinden mejor en MPC |
| P010 | Braun, Ortiz-Mojica & Rivera 2002, *Control Eng. Practice*, 10.1016/S0967-0661(01)00137-X | s s no nd nd | Multiseno *plant-friendly* frente a PRS multinivel; ejemplo en un proceso térmico rápido (RTP) |
| ~~P466~~ | ~~Řehoř & Havlena 2009, actas (sin DOI)~~ | s no s s nd | **Excluido por no accesible** (el autor no encontró el texto completo, 2026-11-03). Era el único A con D2 + D3 y datos poco excitados; según el resumen trata una central eléctrica, sin comparación suave/abrupta, así que no cambiaría lo que Bagle 2026 ya cubre |
| P270 | Valenzuela et al. 2020, *IEEE TCST*, 10.1109/TCST.2019.2917675 | no s no nd s | Diseño de experimento de costo mínimo para MPC de HVAC (temperaturas y caudales), banco real |
| P179 | Machado et al. 2023, *Applied Energy* (R2 de P0) | s no s s s | Ya en P0; PDF disponible |
| P150 | Brus & Zambrano 2010, *Control Eng. Practice*, 10.1016/j.conengprac.2010.06.006 | no no nd nd s | Colectores con retardo que depende del caudal; reporta error de predicción |
| P166 | Ampuño et al. 2019, *Solar Energy*, 10.1016/j.solener.2018.11.014 | no no s nd s | Campo de placa plana: modelos simplificados para control con ensayos reales |
| P221 | Núñez-Reyes & Bordons 2005, *CDC*, 10.1109/CDC.2005.1582347 | nd no no nd s | MPC con identificación simultánea en planta solar de aire acondicionado |
| P543 | Rivera, Lee, Mittelmann & Braun 2009, *J. Process Control* 19(4), 623–635 (R1 de P0) | s s no nd nd | Recuperado por S4a; PDF disponible |

**Prioridad B** (16): método cercano fuera del dominio, o sistema térmico con D2/D3: Braun, Rivera & Stenman 2001, Rivera et al. 2007 (IEEE CSM), Yang & Rivera 2001, Larsson et al. 2015 (MPC-X), Lee & Rivera 2007, Gopaluni et al. 2002, Záceková et al. 2014 y 2015, Sturzenegger et al. 2014, Chook & Tan 2007 (horno, bilineal mejor que lineal), Toyoda & Wada 2001, Saloux & Candanedo 2019, Sanino & Reischel 2007, Rathod et al. 2019, Si et al. 2026, Mendes & Normey-Rico 2014 (predictor bilineal).

**Prioridad C** (20): entran solo por "nd" y es probable que bajen a N2 al leerlos (congresos de central térmica, Koopman o LPV fuera de dominio, modelos grises de tanques; de S4a, trabajos plant-friendly en destilación y reactores con modelos Volterra).

## 7. Qué cambia respecto a P0

- **Bagle et al. 2026 debilita la novedad en D1b.** Ya existe una comparación entre datos de operación normal y PRBS, evaluada en simulación a horizonte largo, en un sistema térmico. Lo que sigue sin aparecer: un sistema con caudal manipulado y calentamiento (colector o receptor), la estructura bilineal, el horizonte del MPC como criterio y la excitación suave diseñada (rampa limitada) en lugar de datos de operación.
- **Micchi & Pannocchia 2008 y Braun et al. 2002** son precedentes de método para la comparación suave/abrupta, fuera del dominio solar.
- Si la lectura confirma esto, el veredicto se mantiene en **parcial**, pero el enunciado de novedad tiene que nombrar Bagle 2026 y acotarse al sistema y a la excitación diseñada. Esto se decide después de la lectura completa, no ahora.

## 8. Siguiente paso

1. ~~Confirmar interpretaciones y lista N1~~ (hecho, 2026-11-03).
2. ~~Ejecutar S4a~~ (hecho, 2026-11-03).
3. ~~Conseguir los PDF de prioridad A~~ (hecho, 2026-11-03: 7 de 8; P466 no accesible). Los 9 A legibles (P085, P288, P010, P270, P179, P150, P166, P221, P543) están en `Articulos iniciales para leer/`.
4. Después: lectura completa de A y B, registro de precedentes y seguimiento de citas desde Machado 2023, Rivera 2009, Gil 2022 y, ahora también, Bagle 2026.
