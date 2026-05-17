https://github.com/fralfaro/RocheBot.git# Onboarding Técnico

> **🎯 Objetivo General**:  Guiar a nuevos integrantes en la configuración inicial de su entorno técnico y en la integración con las herramientas y flujos de trabajo del equipo, asegurando una incorporación fluida y productiva.


## 1. Introducción

<img src="https://cdn-icons-png.flaticon.com/512/4862/4862651.png" width = "200" align="center"/>

| Tema                                     | Descripción                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Importancia de un onboarding** | - Garantizar entornos consistentes y configuraciones compatibles<br>- Permite que los nuevos integrantes sean más productivos<br>- Transmite buenas prácticas y estándares del equipo<br>- Facilita el soporte y resolución de problemas                                                              |
| **Qué suele fallar cuando no se hace**   | - Instalaciones incompletas o dependencias rotas.<br>- Falta de permisos en repositorios o plataformas.<br>- Desorden en el uso de Git y estructuras de proyecto.<br>- Desconocimiento de herramientas clave o flujos de trabajo                                                                                 |
| **Qué aprenderás hoy**                   | - Configurar herramientas locales  (Git, Python, VS Code, ...)<br>- Comprender el flujo de trabajo con Git y Azure DevOps.<br>- Conocer herramientas de apoyo como Copilot, ChatGPT, ...<br>- Buenas prácticas para mantener un entorno limpio |





## 2. Instalación y Configuración de Herramientas

### 2.1 Terminales y gestores de paquetes

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/GNOME_Terminal_icon_2019.svg/1024px-GNOME_Terminal_icon_2019.svg.png" width = "200" align="center"/>

Configurar una terminal adecuada es el primer paso para poder instalar y ejecutar herramientas de desarrollo.

- **Windows:**
    - Instalar **Git Bash** para tener una terminal compatible con comandos Unix.
    - Usar **PowerShell** para comandos del sistema y scripts.
    - Activar **WSL2 (Windows Subsystem for Linux)** para trabajar con entornos Linux reales.
    - Opcional: instalar **Windows Terminal** para gestionar varias sesiones en un mismo entorno.

- **macOS:**
    - Instalar **Homebrew** (`brew`), el gestor de paquetes estándar de macOS.
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/  install/HEAD/install.sh)"
      ```
    - Permite instalar fácilmente herramientas como Python, Git, Node, y más.

- **Linux (Ubuntu/Debian/RHEL):**
    - Usar el gestor de paquetes del sistema (`apt` o `yum`) para instalar software.
      ```bash
      sudo apt update && sudo apt install git python3-pip
      ```


### 2.2 Git y control de versiones

<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Git-logo-orange.svg" width = "250" align="center"/>

<br>

Controlar versiones del código y colaborar en proyectos compartidos es esencial.

- Instalar Git desde [git-scm.com](https://git-scm.com/).
- Configurar credenciales:
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu.email@empresa.cl"
    ```

* Generar y registrar una **SSH key**:

    ```bash
    ssh-keygen -t ed25519 -C "tu.email@empresa.cl"
    ```

  Luego agregar la clave pública en **GitHub**, **GitLab** o **Azure DevOps**.
* Comandos básicos de uso:

     ```bash
     git clone <url>
     git checkout -b feature/nueva-funcionalidad
     git add .
     git commit -m "Agrega nueva funcionalidad"
     git push origin feature/nueva-funcionalidad
     ```
* Mantener la sincronización entre ramas (`git pull origin develop`).



### 2.3 Python y entornos virtuales

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png" width = "400" align="center"/>


Python es la base para la mayoría de los proyectos de análisis, automatización y machine learning.

* Descargar desde [python.org](https://www.python.org/downloads/) o instalar con `brew install python` o `apt install python3`.
* Verificar versión:

     ```bash
     python --version
     ```
* Instalar herramientas de gestión de entornos y dependencias:

     ```bash
     pip install poetry
     ```
* Crear y activar un entorno:

     ```bash
     poetry init
     poetry add pandas numpy
     poetry shell
     ```
* Exportar dependencias:

     ```bash
     poetry export -f requirements.txt --output requirements.txt
     ```



### 2.4 Entorno de Desarrollo Integrado (IDE)


<img src="https://miro.medium.com/v2/1*c0qfWs8sKeyNY5naAl0X0w.png" width = "500" align="center"/>

<br>

Un **IDE** (*Integrated Development Environment*) es un programa que reúne en un solo lugar todas las herramientas que un desarrollador necesita para **crear, probar y depurar software**.

#### Visual Studio Code

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width = "100" align="center"/>

<br>

Editor versátil y extensible, ideal para Python, SQL y Markdown.

* Descargar desde [code.visualstudio.com](https://code.visualstudio.com/).
* Instalar extensiones esenciales:

    * Python
    * Jupyter
    * GitLens
    * Markdown Preview Enhanced
    * YAML
    * GitHub Copilot (requiere licencia o cuenta habilitada)
* Configurar intérprete Python:
  `Ctrl + Shift + P → Python: Select Interpreter`
* Activar Copilot y probar sugerencias automáticas en código.

#### Cursor IDE

<img src="https://img.icons8.com/color/512/cursor-ai.png" width = "150" align="center"/>


Alternativa moderna a VS Code con IA integrada.

* Basado en VS Code, pero optimizado para asistencia de código, refactorización y documentación.
* Permite generar funciones, escribir tests, y depurar código con ayuda de modelos de lenguaje.
* Integración directa con Git y GitHub Copilot.
* Disponible en [cursor.com](https://www.cursor.com/).



#### Jupyter Notebooks

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" width = "150" align="center"/>


* Usado para análisis exploratorio y desarrollo incremental.
* Ejecutar localmente con:

    ```bash
    pip install notebook
    jupyter notebook
    ```



### 2.5 Herramientas de bases de datos


<img src="https://www.svgrepo.com/show/419127/big-data-data-database.svg" width = "150" align="center"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/1200px-DBeaver_logo.svg.png" width = "150" align="center"/>


Los proyectos de análisis y desarrollo suelen requerir conexión a distintas bases de datos.

#### DBeaver

* Cliente universal para conectar a múltiples motores (SQL Server, PostgreSQL, MySQL, Oracle, etc.).
* Permite explorar esquemas, ejecutar consultas, importar/exportar datos y generar diagramas ER.
* Soporta conexiones seguras mediante credenciales o autenticación Azure AD.
* Recomendado para entornos corporativos o trabajo con bases en Azure o AWS.
* Instalación rápida:

    ```bash
    brew install --cask dbeaver-community
    ```

### 3. Servicios, permisos y cuentas en la nube

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Permission_logo_2021.svg" width = "300" align="center"/>



Tener los accesos y permisos correctos es clave para trabajar sin interrupciones. Antes de iniciar, se debe verificar que todo el entorno esté autorizado y funcional.

#### Accesos y permisos
- Utiliza siempre tu cuenta institucional o corporativa para garantizar trazabilidad y seguridad en los proyectos.
- Solicita acceso a los repositorios de código (GitHub, GitLab u otras plataformas) según las necesidades del equipo.
- Verifica que tus credenciales permitan conectarte a las bases de datos, servicios compartidos y entornos en la nube utilizados por el proyecto.
- Asegúrate de tener acceso a las herramientas y espacios de trabajo requeridos (como Power BI, Tableau, Google Colab, o plataformas de almacenamiento).
- Mantén un registro actualizado de los accesos y revisa periódicamente los permisos otorgados.


#### Solicitudes de instalación o requerimientos
- En entornos donde no se puede instalar software directamente, solicitarlo al área de TI.
- Especificar en la solicitud:
    - Nombre y versión del programa (ej. Python, Git, VS Code, DBeaver, DB Browser).
    - Justificación del uso.
    - Usuario y equipo solicitante.
- Esperar confirmación o instalación asistida por un administrador.

#### Buenas prácticas
- No compartir contraseñas ni claves fuera de los canales oficiales.
- Documentar los accesos y procedimientos de solicitud para nuevos integrantes.
- Revisar periódicamente los permisos activos y eliminar los que ya no se utilizan.
