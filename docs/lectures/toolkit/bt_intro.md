# Introducción

## Sistema Operativo

<img src="https://miro.medium.com/v2/resize:fit:1400/0*qlEu4VFyhV-PU1YJ" width = "600" align="center"/>

Los **sistemas operativos** son programas de software que gestionan los recursos de hardware y
proporcionan servicios comunes para otros programas que se ejecutan en una computadora.

Básicamente, actúan como intermediarios entre el hardware de la computadora y
el software de aplicación. Los sistemas operativos realizan tareas como la gestión de memoria,
la gestión de archivos, el control de dispositivos, la administración de procesos y la interfaz de usuario.

Algunos ejemplos comunes de sistemas operativos son Windows, macOS, Linux, Android e iOS.


💡 **Recomendaciones**

* Personalmente recomiendo **Linux**, en particular distribuciones como Ubuntu, Mint o Fedora por su facilidad a la hora de instalar.
* En ocasiones las implementaciones en **Windows** no están completamente integradas e inclusive en ocasiones no están disponibles.
    - Una alternativa es [**Windows Subsystem for Linux**](https://docs.microsoft.com/en-us/windows/wsl/about), pero lamentablemente no se asegura un 100% de compatibilidad.
* En el caso que poseas un equipo con **macOS** no debería haber problema.

**Interfaz de Línea de Comandos (*Command Line Interface* / CLI)**

La **Interfaz de Línea de Comandos** es un tipo de interfaz de usuario que permite
a los usuarios interactuar con un sistema informático mediante comandos de texto introducidos
a través de una línea de comando. En lugar de utilizar elementos gráficos como ventanas,
botones y menús, los usuarios ingresan comandos específicos en un símbolo del sistema o terminal.

En una CLI, los usuarios escriben comandos y argumentos de texto plano para
ejecutar diversas tareas, como administrar archivos, manipular configuraciones del
sistema, ejecutar programas y realizar diversas operaciones informáticas.

Esto proporciona un nivel de control y flexibilidad avanzado para usuarios experimentados,
aunque puede tener una curva de aprendizaje más pronunciada en comparación con
las interfaces gráficas de usuario (GUI).

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Linux_command-line._Bash._GNOME_Terminal._screenshot.png/450px-Linux_command-line._Bash._GNOME_Terminal._screenshot.png" width = "600" align="center"/>


## Python

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width = "200" align="center"/>

[Python](https://www.python.org/) es un lenguaje de programación interpretado que destaca por su claridad y legibilidad en el código. Es multiparadigma, lo que significa que admite diferentes estilos de programación, incluyendo orientación a objetos, programación imperativa y, en menor medida, programación funcional. Además, es dinámico y multiplataforma, lo que lo hace versátil y ampliamente utilizado en diversos entornos de desarrollo.

En el ámbito científico y de análisis de datos, Python cuenta con una variedad de bibliotecas especializadas. Algunas de las más importantes son:

- [Numpy](http://www.numpy.org/): para computación científica.
- [Pandas](https://pandas.pydata.org/): ideal para el análisis de datos.
- [Matplotlib](https://matplotlib.org/): proporciona herramientas para visualización de datos.
- [Scikit-Learn](http://scikit-learn.org/stable/): una biblioteca esencial para machine learning.

Además, durante el curso se explorarán otras bibliotecas complementarias, como scipy, seaborn y statsmodels, entre otras. Estas herramientas amplían las capacidades de Python en áreas específicas, como estadísticas, visualización avanzada y análisis científico.

### Entorno Virtual

<img src="https://miro.medium.com/v2/resize:fit:1400/1*iXJ9E_k62m9Kd8cU3aufOg.png" width = "500" align="center"/>

**Problemas recurrentes:**
- Incompatibilidad entre dependencias de librerías (*packages*).
- Dificultad para compartir y reproducir resultados debido a la falta de conocimiento sobre las versiones de las librerías instaladas.
- Tedioso y costoso tener que usar una máquina virtual diferente para cada desarrollo.
- Temor constante a la interrupción del funcionamiento del script al instalar nuevas herramientas o librerías.

**Solución:**
Aislar el desarrollo para mejorar la compatibilidad y la reproducibilidad de los resultados.

**Para el curso (recomendado):**

![Conda](https://i0.wp.com/exitcondition.com/wp-content/uploads/2019/02/Conda-2.png?fit=1000%2C402&ssl=1)

> *Gestión de paquetes, dependencias y entornos para cualquier lenguaje: Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN.*

**¿Por qué Conda?**
- Es de código abierto.
- Permite gestionar tanto librerías como entornos virtuales.
- Compatible con Linux, Windows y macOS.
- No está limitado a un solo lenguaje de programación (aunque se desarrolló inicialmente para Python).
- Fácil de instalar y utilizar.

**Otras alternativas:**
- `pip + virtualenv`: Pip es el gestor de librerías preferido en Python, mientras que Virtualenv es un gestor de entornos virtuales. Sin embargo, esta combinación es exclusiva de Python.
- `Pipenv` o `Poetry`: Librerías especializadas en la gestión de dependencias (altamente recomendadas).


> 🔑 **Nota**: Las sugerencias anteriores están orientadas principalmente al
> trabajo en entornos locales. Sin embargo, dado que todo el curso está diseñado
> para trabajar en **Google Colab**.

## Project Jupyter

[Project Jupyter](https://jupyter.org/index.html) exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.*

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1767px-Jupyter_logo.svg.png" width = "200" align="center"/>

### Jupyter Notebook

Es una aplicación web que permite crear y compartir documentos que contienen código, ecuaciones, visualizaciones y texto. Entre sus usos se encuentra:

* Limpieza de datos
* Transformación de datos
* Simulaciones numéricas
* Modelamiendo Estadístico
* Visualización de Datos
* Machine Learning
* Mucho más.

### Jupyter Lab

<img src="https://user-images.githubusercontent.com/7244206/224844987-30e9b7c5-abb1-416d-9e3d-63dc8ce9d532.png" width = "200" align="center"/>

* Es la siguiente generación de la interfaz de usuario de *Project Jupyter*.
* Similar a Jupyter Notebook cuenta con la facilidad de editar archivos .ipynb (notebooks) y heramientas como una terminal, editor de texto, explorador de archivos, etc.
* Eventualmente Jupyter Lab reemplazará a Jupyter Notebok (aunque la versión estable fue liberada hace algunos meses).
* Cuenta con una serie de extensiones que puedes instalar (y desarrollar inclurisve.
* Más información en: https://github.com/jupyterlab/jupyterlab-demo

### Otros Proyectos

Entre los más conocidos se encuentran:

* [JupyterHub](https://jupyterhub.readthedocs.io/): Distribuir Jupyter Noterbooks a múltiples usuarios.
* [nbviewer](https://nbviewer.jupyter.org/): Compartir Jupyter Notebooks.
* [Jupyter Book](https://jupyterbook.org/): Construir y publicar libros de tópicos computacionales.
* [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/): Imágenes de Jupyter para utilizar en Docker.

## Versionamiento de Código

<img src="https://miro.medium.com/v2/resize:fit:700/1*1Irij2OQitp_DnqXoGJDeQ.png" width = "400" align="center"/>

* Permite compartir el código fuente de nuestros desarrollos y a la vez mantener un registro de los cambios por los que va pasando.

* Herramienta más importante y fundamental dentro del desarrollo.
* Tipos de versionadores de código:
 * [Sistemas Centralizados](https://sites.google.com/site/practicadesarrollosoft/temario/sistemas-de-versionado-de-cdigo/sistemas-de-versionado-de-cdigo-centralizados): Son los más "tradicionales", por ejemplo SVN, CVS, etc.
 * [Sistemas Distribuidos](https://sites.google.com/site/practicadesarrollosoft/temario/sistemas-de-versionado-de-cdigo/sistemas-de-versionado-de-cdigo-distribuidos): son los que están en auge actualmente como: Git, Mercurial, Bazaar, etc.

### Git

<img src="https://1000logos.net/wp-content/uploads/2023/04/Git-logo.png" width = "400" align="center"/>

> [__Git__](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.


Es importante comprender que _Git_ es la herramienta que permite versionar tus proyectos, sin embargo, a la hora de querer aprovechar más funcionalidades, como compartir o sincronizar tus trabajos se hace necesario utilizar servicios externos. Los más famosos son:

* GitHub
* GitLab
* Bitbucket

Piensa lo siguiente, cualquiera podría implementar un correo electrónico entre dos computadoras conectadas entre ellas por LAN pero no conectadas a Internet. Sin embargo la gente utiliza servicios como Gmail, Outlook, etc. con tal de aprovechar de mejor manera las funcionalidades que ofrece la tecnología del correo electrónico. Esta es una analogía perfecta entre las diferencias de Git y los servicios como GitHub o GitLab.

### GitHub

<img src="https://icones.pro/wp-content/uploads/2021/06/icone-github-rouge.png" width = "200" align="center"/>

> [GitHub](https://github.com/) is a development platform inspired by the way you work. From open source to business, you can host and review code, manage projects, and build software alongside 30 million developers.M


## Configuraciones

* **GitHub**: Crear una cuenta directamente en el [sitio oficial](https://github.com/).
* **Google Colab**: Herrramienta de trabajo oficial. Cada clase con *código* tendrá el siguiente logo (donde deben hacer click): <a href="" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
* **Portafolio Personal**: Para los entregables del curso, utilizaremos la plantilla de [MAT281-Portfolio](https://github.com/fralfaro/MAT281-Portfolio).

> 🔑 **Nota**: Las instrucciones de uso se encuentran en el [siguiente archivo](https://github.com/fralfaro/MAT281-Portfolio/blob/master/docs/setup.md).
