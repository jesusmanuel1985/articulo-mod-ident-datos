import os
from dotenv import load_dotenv
import re
import json
import argparse
from typing import Dict, Any, Tuple
from google import genai
from google.genai import types

# -------------------------------------------------------------------------
# Configuración global
# -------------------------------------------------------------------------
RUTA_METODOLOGIA = "inputs/metodologia.md"
RUTA_LATEX = "inputs/proyecto.tex"
RUTA_ESTADO = "estado.json"
#MODELO_LLM = "gemini-flash-latest"
MODELO_LLM = "gemini-pro-latest"
# Inicializa el cliente oficial de Gemini
load_dotenv()
client = genai.Client()

# -------------------------------------------------------------------------
# Parser dinámico de la Metodología
# -------------------------------------------------------------------------
def parsear_metodologia(ruta_md: str) -> Dict[str, Any]:
    """
    Extrae el marco transversal/preámbulo y segmenta cada fase detectando
    el patrón '## P<n> — <nombre>'.
    """
    if not os.path.exists(ruta_md):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_md}")

    with open(ruta_md, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Extrae el preámbulo (todo lo que está antes de la primera fase P0)
    primer_fase_match = re.search(r"(?m)^##\s+P0\s+—", contenido)
    corte_preambulo = primer_fase_match.start() if primer_fase_match else len(contenido)
    marco_transversal = contenido[:corte_preambulo].strip()

    # Detecta todas las fases presentes en el markdown
    patron_fases = r"(?m)^##\s+(P\d+)\s+—\s+(.+)$"
    matches = list(re.finditer(patron_fases, contenido))

    fases = {}
    for i, match in enumerate(matches):
        pid = match.group(1).strip()
        nombre = match.group(2).strip()

        inicio = match.end()
        fin = matches[i + 1].start() if i + 1 < len(matches) else len(contenido)
        cuerpo = contenido[inicio:fin].strip()

        fases[pid] = {
            "id": pid,
            "nombre": nombre,
            "especificacion": cuerpo
        }

    return {
        "transversal": marco_transversal,
        "fases": fases,
        "orden_fases": [m.group(1).strip() for m in matches]
    }

# -------------------------------------------------------------------------
# Persistencia y Contenedor Flexible (estado.json)
# -------------------------------------------------------------------------
def cargar_estado() -> Dict[str, Any]:
    """Carga el estado existente o inicializa el contenedor flexible."""
    if not os.path.exists(RUTA_ESTADO):
        return {
            "meta": {
                "fase_actual": "P0",
                "fases_completadas": []
            },
            "artefactos": {},
            "retornos_registrados": []
        }
    with open(RUTA_ESTADO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_estado(estado: Dict[str, Any]) -> None:
    with open(RUTA_ESTADO, "w", encoding="utf-8") as f:
        json.dump(estado, f, ensure_ascii=False, indent=2)
    print(f"\n[✓] Estado formal actualizado en '{RUTA_ESTADO}'")

# -------------------------------------------------------------------------
# Motor de Ejecución y Refinamiento Interactivo
# -------------------------------------------------------------------------
def iniciar_sesion_fase(pid: str, meta: Dict[str, Any], texto_latex: str, estado: Dict[str, Any]) -> Tuple[Any, str]:
    """
    Abre una sesión de chat efímera inyectando solo el marco transversal,
    la fase en curso, los artefactos previos consolidados y el LaTeX fuente.
    """
    fase_info = meta["fases"][pid]

    system_instruction = (
        "Eres un auditor científico y redactor riguroso operando bajo una metodología formal por fases.\n"
        "REGLAS METODOLÓGICAS INVIOLABLES:\n"
        "1. La respuesta principal DEBE ser estrictamente el formulario de la SALIDA CANÓNICA de la fase solicitada.\n"
        "2. Prohibido usar verbos aspiracionales (contribuir, explorar, avanzar, desarrollar, estudiar, investigar).\n"
        "3. Todo requisito binario debe verificarse y contrastarse contra el texto del LaTeX provisto.\n"
        "4. Si falta información en el LaTeX para satisfacer un campo obligatorio, declara el Modo de Fallo según la metodología.\n"
        "5. Sé conciso, exacto y rechaza adjetivos sin demostración."
    )

    prompt_inicial = f"""### MARCO TRANSVERSAL Y REGLAS DE CONSTRUCCIÓN:
{meta["transversal"]}

### ESPECIFICACIÓN FORMAL DE LA FASE: {fase_info['id']} — {fase_info['nombre']}
{fase_info['especificacion']}

### ARTEFACTOS PREVIOS CONSOLIDADOS Y VALIDADOS:
{json.dumps(estado.get("artefactos", {}), indent=2, ensure_ascii=False)}

### TEXTO DE INVESTIGACIÓN FUENTE (LATEX):
{texto_latex}

### INSTRUCCIÓN DE EJECUCIÓN:
Analiza el documento LaTeX a la luz de las reglas transversales y la especificación de {fase_info['id']}.
Completa la SALIDA CANÓNICA de forma exhaustiva y rigurosa.
"""

    chat = client.chats.create(
        model=MODELO_LLM,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.0  # Máxima rigidez y determinismo
        )
    )

    respuesta = chat.send_message(prompt_inicial)
    return chat, respuesta.text

def procesar_fase(pid: str, meta: Dict[str, Any], texto_latex: str, estado: Dict[str, Any]):
    fase_info = meta["fases"][pid]

    print(f"\n{'='*70}")
    print(f"  EJECUTANDO: {pid} — {fase_info['nombre']}")
    print(f"{'='*70}")
    print("→ Evaluando LaTeX contra la metodología con Gemini...")

    chat_sesion, propuesta_actual = iniciar_sesion_fase(pid, meta, texto_latex, estado)

    while True:
        print(f"\n{'─'*25} SALIDA PROPUESTA ({pid}) {'─'*25}")
        print(propuesta_actual)
        print("─" * 70)
        print("\nOpciones de control:")
        print("  [A] Aprobar y guardar en estado.json")
        print("  [F] Dar Feedback a la IA para afinar la propuesta")
        print("  [E] Editar el texto manualmente")
        print("  [C] Cancelar sin guardar")
        
        op = input("\nElige una opción [A/F/E/C]: ").strip().upper()

        if op == "A":
            # Guarda únicamente el artefacto limpio final
            estado["artefactos"][pid] = propuesta_actual
            
            if pid not in estado["meta"]["fases_completadas"]:
                estado["meta"]["fases_completadas"].append(pid)

            # Calcula la siguiente fase en la escalera
            orden = meta["orden_fases"]
            idx = orden.index(pid)
            if idx + 1 < len(orden):
                estado["meta"]["fase_actual"] = orden[idx + 1]
            
            guardar_estado(estado)
            print(f"[✓] Fase {pid} completada. Siguiente fase en la escalera: {estado['meta']['fase_actual']}")
            break

        elif op == "F":
            feedback = input("\nInstrucción de ajuste (ej. 'Corrige R3: el criterio debe ser latencia <= 100ms'): ")
            if feedback.strip():
                print("→ Ajustando formulario canónico...")
                instruccion_ajuste = (
                    f"Ajusta la salida canónica según esta observación del auditor: '{feedback}'. "
                    "Devuelve el formulario canónico completo actualizado respetando estrictamente la metodología."
                )
                res = chat_sesion.send_message(instruccion_ajuste)
                propuesta_actual = res.text

        elif op == "E":
            print("\nPega tu texto corregido (finaliza presionando Enter en una línea vacía):")
            lineas = []
            while True:
                linea = input()
                if not linea and lineas:
                    break
                lineas.append(linea)
            propuesta_actual = "\n".join(lineas)

        elif op == "C":
            print("\n[!] Operación cancelada. El estado permanece intacto.")
            break

# -------------------------------------------------------------------------
# Interfaz de Línea de Comandos (CLI)
# -------------------------------------------------------------------------
def mostrar_reporte():
    estado = cargar_estado()
    print("\n" + "="*50)
    print("      REPORTE DE ESTADO METODOLÓGICO")
    print("="*50)
    print(f"Fase pendiente: {estado['meta'].get('fase_actual', 'P0')}")
    print(f"Fases aprobadas: {estado['meta'].get('fases_completadas', [])}")
    
    if estado.get("artefactos"):
        print("\n--- Artefactos consolidados ---")
        for k, v in estado["artefactos"].items():
            print(f"\n[{k}]:")
            primeras_lineas = "\n".join(v.splitlines()[:6])
            print(primeras_lineas + ("\n..." if len(v.splitlines()) > 6 else ""))
    print("="*50 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Motor de escritura científica rigurosa con Gemini API.")
    subparsers = parser.add_subparsers(dest="comando")

    # Comando: run
    p_run = subparsers.add_parser("run", help="Ejecuta una fase de la metodología")
    p_run.add_argument("--fase", type=str, default=None, help="Código de fase (ej. P0, P1, P2)")
    p_run.add_argument("--forzar", action="store_true", help="Reejecutar una fase ya aprobada")

    # Comando: status
    subparsers.add_parser("status", help="Muestra los artefactos consolidados en estado.json")

    args = parser.parse_args()

    if args.comando == "status":
        mostrar_reporte()
        return

    # Flujo por defecto o comando 'run'
    meta = parsear_metodologia(RUTA_METODOLOGIA)
    estado = cargar_estado()

    if not os.path.exists(RUTA_LATEX):
        print(f"Error: No se encontró el archivo de proyecto en '{RUTA_LATEX}'.")
        return

    with open(RUTA_LATEX, "r", encoding="utf-8") as f:
        texto_latex = f.read()

    # Determinar qué fase procesar
    pid = args.fase.upper() if (hasattr(args, "fase") and args.fase) else estado["meta"].get("fase_actual", "P0")

    if pid not in meta["fases"]:
        print(f"Error: La fase '{pid}' no está definida en '{RUTA_METODOLOGIA}'.")
        return

    if pid in estado["meta"].get("fases_completadas", []) and not getattr(args, "forzar", False):
        print(f"[!] La fase {pid} ya está aprobada. Usa '--forzar' si deseas recalcularla.")
        return

    procesar_fase(pid, meta, texto_latex, estado)

if __name__ == "__main__":
    main()