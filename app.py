from flask import Flask, request, jsonify
import os
import sys
import traceback
import json

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
# No tocar Arriba
# ----------------------------------

@app.route("/nuevo")
def nuevo():
    """
    Endpoint nuevo sirve para crear un nuevo perfil de personaje
    utilizar el formato de /plantilla/perfil.json, cada perfil tiene un id,
    el id tambien es normbre de archivo. ej. id: 0 -> 0.json
    1. Leer Plantilla
    2. Recibir datos
    3. Cargar Plantilla
    4. Escribir pefirl nuevo
    5. Devolver ID de perfil y Exito, sino ERROR!

    ARG: ?Nombre=""&Edad=""&Foto=""&Creador=""&Sexo=""&Colores=["","",""]&Tecnicas:""&Raza:""&Vivo:true
    """

    # abrir plantilla y convertirla en diccionario
    with open('plantilla/perfil.json', 'r') as file:
        plantilla = json.load(file)
    
    # Leer arguentos y asignarlos a variables
    nombre = request.args.get("Nombre")
    edad = request.args.get("Edad")
    foto = request.args.get("Foto")
    creador = request.args.get("Creador")
    sexo = request.args.get("Sexo")
    colores = request.args.get("Colores")
    tecnicas = request.args.get("Tecnicas")
    raza = request.args.get("Raza")
    vivo = request.args.get("Vivo")

    # completamos la plantilla

    plantilla["Nombre"] = nombre
    plantilla["Edad"] = edad
    plantilla["Sexo"] = sexo
    plantilla["Foto"] = foto
    plantilla["Creador"] = creador
    plantilla["Detalles"]["Tecnicas"] = tecnicas
    plantilla["Detalles"]["Raza"] = raza
    plantilla["Detalles"]["Vivo"] = vivo

    # encontrar si existe algun perfil y cual es el ultimo
    ultimo_perfil=0
    for perfil in os.listdir('perfiles'):
        if perfil.endswith(".json"):
            try:
                numero = int(perfil[:-5]) # removemos extension .json
                ultimo_perfil = max(ultimo_perfil,perfil)
            except ValueError:
                pass # Ignorar si no hay archivo
    ultimo_perfil = ultimo_perfil + 1
    
    plantilla["id"] = ultimo_perfil
    
    # demostramos que encontramos los datos
    print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}")

    # grabar la plantilla como el nuevo perfil 
    nuevo_perfil = os.path.join('perfiles',f"{ultimo_perfil}.json") # armamos el nombre del archivo

    with open(nuevo_perfil, "w", encoding="utf-8") as perfil_json:
        json.dump(plantilla, perfil_json, indent=4, ensure_ascii=False) #Lo guardamos

    # avisamos! 

    return f"Perfil ID: {ultimo_perfil} fue creado exitosamente!"


# ----------------------------------
# No tocar abajo
if __name__ == "__main__":
    print("Escaneando código antes de iniciar la aplicación...")
    scan_code()
    print("Iniciando aplicación...")
    app.run(host="0.0.0.0", port=5000, debug=True)
