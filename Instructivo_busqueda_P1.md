# Instructivo: ejecución de la búsqueda sistemática (P1)

**Protocolo:** v1, aprobado el 2026-11-03 (`P1_Brecha_novedad.md`)
**Ejecutar desde:** 2026-11-04. Antes de esa fecha no cuenta, porque la metodología exige que la ejecución sea posterior al protocolo.
**Tiempo de esta sesión:** ≈ 2 h para ejecutar y exportar. El cribado lo hace después Claude con las exportaciones, y tú confirmas las inclusiones.

---

## 1. Reglas de la sesión

1. **Copia las cadenas tal cual.** Si una base da error, corrígela lo mínimo, anota el error y registra la cadena corregida como variante (por ejemplo, S1a).
2. **No cribes durante la sesión.** Solo ejecuta, anota y exporta. Así el cribado queda separado y es reproducible.
3. **Anota todo en la tabla de la sección 7**, en el momento: fecha, hora, total, filtros y archivo exportado.
4. **Si una cadena supera 300 resultados**, aplica el filtro de área de la sección 6 **antes** de exportar y regístralo. No cortes por relevancia sin anotarlo.
5. Crea la carpeta `busqueda_P1/` dentro de `Articulo-Loreto/` y guarda ahí todas las exportaciones con el nombre `S#_base.ext` (por ejemplo, `S1_scopus.csv`).

## 2. Scopus (≈ 30 min)

**Dónde:** Advanced document search. Pega la cadena completa.
**Exportar:** Export → CSV → marca *Citation information* y *Abstract & keywords*. Exporta todos los resultados.

```text
S1  TITLE-ABS-KEY ( ( excitation OR "input design" OR "input signal*" OR "plant-friendly" OR "least costly" OR "normal operation" OR "operating data" OR "closed-loop data" ) AND ( "system identification" OR "model identification" OR "parameter estimation" ) AND ( "solar collector*" OR "solar field" OR "solar thermal" OR "heat exchanger*" OR "thermal process*" ) ) AND PUBYEAR > 1999

S2  TITLE-ABS-KEY ( ( PRBS OR "pseudo-random binary" OR multisine OR "step test*" ) AND compar* AND identification AND ( thermal OR solar OR temperature ) ) AND PUBYEAR > 1999

S3  TITLE-ABS-KEY ( ( "solar collector*" OR "solar field" OR "parabolic trough" OR "flat-plate collector*" OR "Fresnel collector*" ) AND ( identification OR "data-driven" OR "grey-box" OR "gray-box" OR bilinear OR LPV ) AND ( "model predictive control" OR MPC OR "multi-step" OR prediction ) ) AND PUBYEAR > 1999

S4  TITLE-ABS-KEY ( ( "plant-friendly" OR "least costly" OR "application-oriented" OR "input design" ) AND ( "model predictive control" OR MPC OR "identification for control" ) )

S5  TITLE-ABS-KEY ( ( "MPC-relevant identification" OR "multi-step prediction error" OR "long-range prediction" OR "multistep prediction" ) AND identification )
```

**Ojo con el filtro de año.** En P0 se perdió una vez. Antes de exportar S1–S3, revisa en la barra de filtros que no aparezcan años anteriores a 2000.

## 3. Web of Science (≈ 30 min)

**Dónde:** Advanced Search, base *Web of Science Core Collection*. Pega la cadena completa.
**Exportar:** Export → *Plain text file* → *Full Record*. WoS exporta hasta 1000 por archivo; si hay más, exporta por tramos (1–1000, 1001–2000) y anótalo.

```text
S1  TS=((excitation OR "input design" OR "input signal*" OR "plant-friendly" OR "least costly" OR "normal operation" OR "operating data" OR "closed-loop data") AND ("system identification" OR "model identification" OR "parameter estimation") AND ("solar collector*" OR "solar field" OR "solar thermal" OR "heat exchanger*" OR "thermal process*")) AND PY=(2000-2026)

S2  TS=((PRBS OR "pseudo-random binary" OR multisine OR "step test*") AND compar* AND identification AND (thermal OR solar OR temperature)) AND PY=(2000-2026)

S3  TS=(("solar collector*" OR "solar field" OR "parabolic trough" OR "flat-plate collector*" OR "Fresnel collector*") AND (identification OR "data-driven" OR "grey-box" OR "gray-box" OR bilinear OR LPV) AND ("model predictive control" OR MPC OR "multi-step" OR prediction)) AND PY=(2000-2026)

S4  TS=(("plant-friendly" OR "least costly" OR "application-oriented" OR "input design") AND ("model predictive control" OR MPC OR "identification for control"))

S5  TS=(("MPC-relevant identification" OR "multi-step prediction error" OR "long-range prediction" OR "multistep prediction") AND identification)
```

## 4. IEEE Xplore (≈ 30 min)

**Dónde:** Advanced Search → *Command Search*. Pega la cadena; para S1–S3 fija los años 2000–2026 con el filtro *Year* de la columna izquierda.
**Exportar:** Export → *Results* → CSV (hasta 2000 registros).

```text
S1  ("All Metadata":excitation OR "All Metadata":"input design" OR "All Metadata":"input signal*" OR "All Metadata":"plant-friendly" OR "All Metadata":"least costly" OR "All Metadata":"normal operation" OR "All Metadata":"operating data" OR "All Metadata":"closed-loop data") AND ("All Metadata":"system identification" OR "All Metadata":"model identification" OR "All Metadata":"parameter estimation") AND ("All Metadata":"solar collector*" OR "All Metadata":"solar field" OR "All Metadata":"solar thermal" OR "All Metadata":"heat exchanger*" OR "All Metadata":"thermal process*")

S2  ("All Metadata":PRBS OR "All Metadata":"pseudo-random binary" OR "All Metadata":multisine OR "All Metadata":"step test*") AND "All Metadata":compar* AND "All Metadata":identification AND ("All Metadata":thermal OR "All Metadata":solar OR "All Metadata":temperature)

S3  ("All Metadata":"solar collector*" OR "All Metadata":"solar field" OR "All Metadata":"parabolic trough" OR "All Metadata":"flat-plate collector*" OR "All Metadata":"Fresnel collector*") AND ("All Metadata":identification OR "All Metadata":"data-driven" OR "All Metadata":"grey-box" OR "All Metadata":"gray-box" OR "All Metadata":bilinear OR "All Metadata":LPV) AND ("All Metadata":"model predictive control" OR "All Metadata":MPC OR "All Metadata":"multi-step" OR "All Metadata":prediction)

S4  ("All Metadata":"plant-friendly" OR "All Metadata":"least costly" OR "All Metadata":"application-oriented" OR "All Metadata":"input design") AND ("All Metadata":"model predictive control" OR "All Metadata":MPC OR "All Metadata":"identification for control")

S5  ("All Metadata":"MPC-relevant identification" OR "All Metadata":"multi-step prediction error" OR "All Metadata":"long-range prediction" OR "All Metadata":"multistep prediction") AND "All Metadata":identification
```

**Si IEEE rechaza la cadena** (suele limitar el número de comodines `*` o de términos), cambia los comodines por las formas explícitas (`"solar collector" OR "solar collectors"`) o divide la cadena en dos (S1a y S1b). Anota el mensaje de error y la variante usada.

## 5. Google Scholar (≈ 30 min)

Scholar no exporta listas ni admite cadenas largas, así que se usa **Publish or Perish** (Harzing, gratuito: https://harzing.com/resources/publish-or-perish).

**Cómo:** *New search* → *Google Scholar*. Pega la cadena en *Keywords*; en S1–S3 pon *Years* 2000–2026; *Maximum number of results* = 100. Exporta con *Save Results* → CSV.

Estas cadenas son **versiones simplificadas** (Scholar no admite comodines ni todos los booleanos) y se registran como S#-GS:

```text
S1-GS  "system identification" ("input design" OR "plant-friendly" OR "normal operation" OR excitation) ("solar collector" OR "solar field" OR "heat exchanger")

S2-GS  identification comparison (PRBS OR multisine OR "step test") (thermal OR solar)

S3-GS  ("solar collector" OR "solar field" OR "parabolic trough") (bilinear OR LPV OR "grey-box") identification "model predictive control"

S4-GS  ("plant-friendly" OR "least costly" OR "application-oriented") identification "model predictive control"

S5-GS  ("MPC-relevant identification" OR "multi-step prediction error") identification
```

Anota también el total aproximado que muestra Scholar en la parte superior ("Aproximadamente N resultados"); con eso basta, aunque solo se revisen 100.

## 6. Filtro si una cadena supera 300 resultados

Aplícalo antes de exportar y anótalo en la tabla.

| Base | Filtro |
| --- | --- |
| Scopus | *Subject area*: Engineering; Energy; Computer Science; Chemical Engineering; Mathematics |
| WoS | *Research Areas*: Engineering; Energy & Fuels; Thermodynamics; Automation & Control Systems; Computer Science |
| IEEE Xplore | Ninguno de área. Si pasa de 300, avísame antes de exportar |

Si aun con el filtro supera 1000, no exportes: anota el total y avísame para ajustar la cadena como variante del protocolo (v2).

## 7. Registro de ejecución

Copia esta tabla en `busqueda_P1/Registro_ejecucion.md` y llénala durante la sesión.

```text
| Código | Base | Fecha y hora | Cadena (o variante) | Filtros | Total | Exportados | Archivo | Observación |
| S1 | Scopus | | tal cual | PUBYEAR > 1999 | | | S1_scopus.csv | |
| S2 | Scopus | | | | | | | |
...
| S5-GS | Google Scholar | | | 2000–2026, máx. 100 | ≈ | | S5_gs.csv | |

Hora de inicio: __:__   Hora de fin: __:__   Minutos: __
```

Son 20 filas: 5 cadenas × 4 bases.

## 8. Al terminar

1. Verifica que hay un archivo por fila con resultados (o una nota de "0 resultados").
2. Avísame. Con las exportaciones yo:
   - elimino duplicados entre bases;
   - compruebo si reaparecen Rivera 2009, Bombois 2006, Machado 2023 y Mechhoud 2024 (requisito R12);
   - hago el primer cribado por título y resumen, con D1a, D1b, D2, D3 y D4;
   - te propongo la clasificación en N1, N2 y excluidos.
3. Tú confirmas las inclusiones. Después viene la lectura completa de los N1 (≈ 4 h).

## Lista de control

- [ ] La sesión es del 2026-11-04 o posterior.
- [ ] Usé Scopus, WoS, IEEE Xplore y Google Scholar (Publish or Perish).
- [ ] Cada cadena quedó registrada tal cual, o como variante con su error.
- [ ] En S1–S3 verifiqué el filtro de años antes de exportar.
- [ ] Anoté total, filtros y archivo de cada una de las 20 ejecuciones.
- [ ] Anoté hora de inicio y fin.
