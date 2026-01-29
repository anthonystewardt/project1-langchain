# Project1 - LangChain con OpenAI 🤖

Un proyecto básico que demuestra el uso de LangChain con OpenAI GPT-4o-mini, implementando LCEL (LangChain Expression Language) para crear cadenas de prompts modernas.

## 📋 Requisitos Previos

- Python 3.11 o superior
- Una cuenta de OpenAI con API Key
- Git instalado en tu sistema

## 🚀 Instalación y Configuración (Windows)

### Paso 1: Instalar Python

1. Ve a [python.org](https://www.python.org/downloads/windows/)
2. Descarga Python 3.11 o superior
3. Durante la instalación, **marca la casilla "Add Python to PATH"**
4. Verifica la instalación abriendo CMD y ejecutando:

   ```cmd
   python --version
   ```

### Paso 2: Instalar uv (Gestor de dependencias)

Abre **PowerShell como Administrador** y ejecuta:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

O alternativamente con pip:

```cmd
pip install uv
```

Verifica la instalación:

```cmd
uv --version
```

### Paso 3: Clonar el Repositorio

```cmd
git clone https://github.com/anthonystewardt/project1-langchain.git
cd project1-langchain
```

### Paso 4: Configurar Variables de Entorno

1. Crea un archivo llamado `.env` en la raíz del proyecto:

   ```cmd
   echo. > .env
   ```

2. Abre el archivo `.env` con tu editor favorito (Notepad, VS Code, etc.) y añade:

   ```env
   OPENAI_KEY=tu_api_key_de_openai_aquí
   ```

**📝 Nota:** Para obtener tu API Key de OpenAI:

- Ve a [platform.openai.com](https://platform.openai.com/)
- Inicia sesión o crea una cuenta
- Ve a "API Keys" y genera una nueva clave
- Copia la clave y pégala en tu archivo `.env`

### Paso 5: Instalar Dependencias

```cmd
uv sync
```

Este comando instalará automáticamente todas las dependencias necesarias:

- `langchain`
- `langchain-core`
- `langchain-openai`
- `python-dotenv`

### Paso 6: Ejecutar el Proyecto

```cmd
uv run main.py
```

## 🔧 Estructura del Proyecto

```
project1-langchain/
│
├── main.py              # Archivo principal con el código LangChain
├── pyproject.toml       # Configuración de dependencias
├── .env                 # Variables de entorno (crear manualmente)
└── README.md           # Este archivo
```

## 💡 ¿Qué hace este proyecto?

El proyecto demuestra:

1. **Configuración de OpenAI GPT-4o-mini** con LangChain
2. **Uso de PromptTemplate** para crear prompts dinámicos
3. **LCEL (LangChain Expression Language)** para cadenas modernas
4. **Manejo de variables de entorno** para la seguridad de API Keys

### Ejemplo de salida

```
Question: What is the capital of France?
Answer: Hello, Anthony! The capital of France is Paris. If you have any more questions, feel free to ask!
Hello from initialsproj1!
```

## 🐛 Solución de Problemas

### Error: "python no se reconoce como comando"

- Reinstala Python y asegúrate de marcar "Add Python to PATH"
- Reinicia tu terminal/PowerShell

### Error: "OPENAI_KEY not found"

- Verifica que el archivo `.env` existe en la raíz del proyecto
- Asegúrate de que la clave API es válida y no tiene espacios extras

### Error: "uv no se reconoce como comando"

- Reinstala uv siguiendo las instrucciones del Paso 2
- Reinicia tu terminal

### Error: "ModuleNotFoundError"

- Ejecuta `uv sync` nuevamente para instalar las dependencias
- Verifica que estás en la carpeta correcta del proyecto

## 🔑 Configuración Adicional

Para usar tu propio nombre en el saludo, puedes modificar la variable `name` en [main.py](main.py):

```python
name = "Tu Nombre Aquí"  # Línea 25
```

## 📚 Recursos Adicionales

- [Documentación oficial de LangChain](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [uv Documentation](https://docs.astral.sh/uv/)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

---

⭐ **¡No olvides dar una estrella si te fue útil!** ⭐
