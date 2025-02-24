from flask import Flask, request, jsonify
import os
import sys
import traceback

app = Flask(__name__)

def scan_code():
    """
    Función para escanear cambios en el código y detectar errores antes de lanzar la aplicación.
    """
    errors = []
    
    # Verificar errores de sintaxis en archivos .py
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        source_code = f.read()
                    compile(source_code, file_path, "exec")
                except SyntaxError as e:
                    errors.append(f"Error de sintaxis en {file_path}: {e}")
                except Exception as e:
                    errors.append(f"Error en {file_path}: {e}")
    
    if errors:
        print("\n\033[91mErrores detectados antes de iniciar la aplicación:\033[0m")
        for error in errors:
            print(f"- {error}")
        print("\nCorrige los errores antes de continuar.")
        sys.exit(1)

@app.route("/app")
def sumar():
    """
    Endpoint para sumar dos números recibidos como parámetros en la URL.
    Uso: /app?a=12&b=10
    Retorna: "El Resultado es 22"
    """
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return f"El Resultado es {a + b}"
    except ValueError:
        return "Error: Parámetros inválidos. Asegúrate de enviar números.", 400

@app.route("/health")
def health():
    """
    Endpoint de salud para verificar que el API está funcionando correctamente.
    Retorna: "HTTP 200 - OK | Estoy Funcionando"
    """
    return "HTTP 200 - OK | Estoy Funcionando"

if __name__ == "__main__":
    print("Escaneando código antes de iniciar la aplicación...")
    scan_code()
    print("Iniciando aplicación...")
    app.run(host="0.0.0.0", port=5000, debug=True)
