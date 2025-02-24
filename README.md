# 📌 API en Python con Flask

Este proyecto proporciona una API simple con Flask que permite sumar dos números y verificar el estado de la aplicación. Además, al iniciar, escanea los archivos en busca de errores de sintaxis antes de ejecutarse.

---

## 🚀 Cómo iniciar la aplicación

1. **Instalar dependencias**
   Asegúrate de tener Python instalado en tu sistema. Luego, instala Flask si aún no lo tienes:
   ```bash
   pip install flask
   ```

2. **Ejecutar la API**
   Inicia la aplicación con el siguiente comando:
   ```bash
   python app.py
   ```
   Esto primero escaneará el código en busca de errores y luego iniciará el servidor.

3. **Probar la API**
   - Para probar la suma de dos números, abre un navegador o usa `curl`:
     ```bash
     curl "http://localhost:5000/app?a=12&b=10"
     ```
     Respuesta esperada:
     ```
     El Resultado es 22
     ```
   - Para verificar el estado de la API:
     ```bash
     curl "http://localhost:5000/health"
     ```
     Respuesta esperada:
     ```
     HTTP 200 - OK | Estoy Funcionando
     ```

---

## 🔄 Cómo agregar nuevos endpoints

Si deseas añadir más funcionalidades a la API, sigue estos pasos:

1. **Editar `app.py`**
   - Abre el archivo `app.py` con tu editor de código favorito.
   - Agrega una nueva función y decórala con `@app.route("/nuevo_endpoint")`.

2. **Ejemplo de un nuevo endpoint**
   ```python
   @app.route("/multiplicar")
   def multiplicar():
       a = int(request.args.get("a", 1))
       b = int(request.args.get("b", 1))
       return f"El Resultado es {a * b}"
   ```

3. **Reiniciar la aplicación**
   Después de agregar un nuevo endpoint, reinicia la aplicación:
   ```bash
   python app.py
   ```

---

## 📌 Notas adicionales

- El escaneo de errores solo ocurre al iniciar la aplicación, por lo que si hay un problema en el código, será detectado antes de ejecutarse.
- Todos los mensajes de error están en español para facilitar su comprensión.

Si tienes dudas o mejoras, ¡siéntete libre de contribuir! 🚀

