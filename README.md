# 🚀 Quality Demo Web - Gestión de Usuarios

Este es un **mini-sistema de gestión de usuarios en Python** con interfaz web (Flask) y base de datos SQLite.  
Se utiliza como ejemplo para enseñar **Gestión de Calidad de Software**, en particular **Complejidad Ciclomatica** y análisis con **SonarQube**.  

---

## ✨ Características
- 🗄️ Base de datos SQLite integrada (no requiere instalación adicional).  
- 🧑‍💻 Registro de usuarios con validaciones.  
- ✅ Tests unitarios con `pytest`.  
- 🧮 Funciones con **alta y baja complejidad ciclomatica** para comparación.
- 📊 Integración con **SonarQube** para análisis de calidad.  

---

## ⚙️ Instalación y uso

### 1. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate.ps1  # Windows
````

### 2. Instalar dependencias

````
pip install -r requirements.txt
````

### 3. Iniciar BBDD
````
python -c "from db import init_db; init_db()"
````

### 4. Ejecutar app
````
python app.py
````

La aplicación estará disponible en 👉 http://127.0.0.1:5000 🎉
