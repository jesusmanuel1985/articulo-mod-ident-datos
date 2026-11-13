# P5 — Diagrama de flujo (BORRADOR)

Borrador de apoyo, no forma parte del diseño congelado. Resume `P5_Diseno.md` v1.2. Si hay diferencias, manda `P5_Diseno.md`.

## Flujo general

Son tres etapas seguidas. Cada corrida pasa además por el control de la sección siguiente.

### 1. Preparación y corridas iniciales

```mermaid
flowchart TD
  A["P5 v1.2"] --> FZ{"¿Autor congela P5 v1.2?"}
  FZ -- "no" --> A
  FZ -- "sí" --> SC["Script con semilla: señal suave, PRBS, máscaras A, B, C"]
  SC --> C2{"C2 en el archivo de comando: tasa ≤ 2 L/h·s, saltos ≥ 100 L/h, máx ≤ 400 L/h"}
  C2 -- "no cumple" --> SC
  C2 -- "cumple" --> K["K: V·I por resistencia → P_nom"]
  K --> PS["PS: PI en lazo cerrado → secuencia de caudal"]
  PS --> P["Piloto: 2 repeticiones de 2500 s → σ_T4"]
  P --> NR{"σ_T4 > 0.25 °C"}
  NR -- "sí" --> N5["n_rep = 5 por máscara"]
  NR -- "no" --> N3["n_rep = 3 por máscara"]
  N5 --> NL["Corrida NL: 200, 300, 400 L/h; 4 resistencias 0 → 100 → 0 %"]
  N3 --> NL
  NL --> C7["C7: K(200)/K(400) ≥ 1.5 y K decreciente"]
  NL --> SIG["Sigue en la etapa 2"]
```

### 2. Identificación y congelación de modelos

```mermaid
flowchart TD
  ID["IS: señal suave + máscara A · IP: PRBS + máscara A; mismo día, orden sorteado"] --> V3I{"V3: IS vs IP, ΔT amb ≤ 3 °C, ΔT0 ≤ 1 °C, muestras ≤ 1 %"}
  V3I -- "falla" --> RID["Repetir identificación (N = 1)"]
  RID --> ID
  V3I -- "cumple" --> EST["Estimar bilineal-suave, bilineal-PRBS y FOPDT-PRBS; retardo global en grilla 0–200 s; 10 multiarranques"]
  EST --> C3["C3: intervalos bootstrap de C_i, suave vs PRBS"]
  EST --> CONG["Congelar modelos: parámetros, código, hash, fecha"]
  CONG --> SIG["Sigue en la etapa 3"]
```

### 3. Validación y análisis

```mermaid
flowchart TD
  VAL["Validación: máscaras B y C alternadas, n_rep por máscara"] --> V3V{"V3: T amb media dentro de ± 5 °C de IS e IP"}
  V3V -- "falla" --> RVAL["Repetir esa corrida (N = 1)"]
  RVAL --> VAL
  V3V -- "cumple" --> OPEN["Abrir datos de validación"]
  OPEN --> V5{"V5: bilineal-PRBS a 1000 s, FIT ≥ 50 % y mejor que persistencia"}
  V5 -- "no" --> INVID["Identificación INV: volver a la etapa 2"]
  V5 -- "sí" --> MET["RMSE_H a 1000 s por réplica y por modelo"]
  MET --> C0["C0: regla de desenlace (detalle abajo)"]
  MET --> C1["C1: bilineal vs FOPDT"]
  MET --> C4["C4: RMSE por tramo de caudal"]
  C0 --> P6["P6, junto con C3 y C7"]
  C1 --> P6
  C4 --> P6
```

## Control de cada corrida (se aplica a K, PS, P, NL, IS, IP y validación)

```mermaid
flowchart TD
  R0["Banco a 300 L/h, resistencias en el estado inicial de la máscara"] --> V2{"V2: pendiente de T4 en 300 s < 0.05 °C/min"}
  V2 -- "no" --> R0
  V2 -- "sí" --> RUN["Ejecutar la corrida; guardar datos crudos"]
  RUN --> DESC["Descartar primeros 900 s, fallos de sensor y saturación"]
  DESC --> GATE{"V1: pérdida ≤ 2 %, sin PT100 fuera de rango, comando igual al archivo · V4: descarte ≤ 5 %"}
  GATE -- "cumple" --> OK["Corrida válida"]
  GATE -- "falla" --> INV["INV"]
  INV --> NR{"¿Reintento disponible? (N = 1)"}
  NR -- "sí" --> R0
  NR -- "no" --> NOB["NOB: retorno a P4"]
```

## Regla de desenlace de C0

```mermaid
flowchart TD
  S["Por máscara (B y C): R_p, R_s, M = máx(1.5·R_p, R_p + 0.5 °C), m = M − R_p"] --> SD{"σ_d > m/2"}
  SD -- "sí" --> NC["No concluyente"]
  SD -- "no" --> RS{"R_s ≤ M"}
  RS -- "sí" --> SOS["Sostenido"]
  RS -- "no" --> NEG["Refutado (NEG)"]
  NC --> COMB
  SOS --> COMB
  NEG --> COMB
  COMB{"Combinar B y C"} --> F1["Ambas sostenido → C0 sostenido"]
  COMB --> F2["Ambas NEG → C0 NEG"]
  COMB --> F3["Una sostenido y otra NEG → PAR"]
  COMB --> F4["Alguna no concluyente → no concluyente"]
```
