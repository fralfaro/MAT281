# LaTeX
> Escribe documentos académicos profesionales desde el navegador

---

## ¿Qué es LaTeX?

LaTeX es un sistema para crear documentos académicos y científicos con formato profesional. A diferencia de Word, tú escribes el contenido y LaTeX se encarga del diseño — sin que las tablas se desplacen solas ni las ecuaciones queden mal formateadas.

**Ventajas frente a Word:**

- Automatiza referencias, citas y ecuaciones.
- Control total sobre formato y estructura.
- Ideal para documentos extensos: informes, tesis, artículos.

![Curva de esfuerzo: LaTeX vs Word según complejidad del documento](latexword2.jpg)

> A mayor complejidad del documento, LaTeX requiere menos esfuerzo relativo que Word.

---

## ¿Cómo empezar?

La forma más sencilla es usar **Overleaf**, un editor en línea que no requiere instalar nada.

- 🌐 [Overleaf](https://www.overleaf.com/) — editor recomendado, gratuito, en el navegador.
- Si prefieres trabajar localmente: [TeX Live](https://www.tug.org/texlive/) (Linux/Windows), [MacTeX](https://tug.org/mactex/) (macOS), [MiKTeX](https://miktex.org/) (Windows).
- Editores locales: [TeXstudio](https://www.texstudio.org/) o [VSCode + LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).

---

## Overleaf: LaTeX en línea

![Logo de Overleaf](overleaf.png)

Overleaf es una plataforma en línea para escribir y compilar documentos LaTeX sin instalar nada.

**¿Por qué usarlo?**

- Edición colaborativa en tiempo real.
- Vista previa del PDF instantánea al compilar.
- Integración con GitHub y almacenamiento en la nube.
- Acceso desde cualquier navegador.

Crea tu cuenta gratuita en [overleaf.com](https://www.overleaf.com/).

### Interfaz de Overleaf

El editor muestra el código LaTeX a la izquierda y el PDF compilado a la derecha en la misma pestaña. Puedes cambiar el diseño desde el menú **Layout**.

![Interfaz del editor Overleaf con código y previsualización PDF](ovealeaf2.png)

![Lista de proyectos en Overleaf](overleaf1.jpg)

---

## Plantillas en Overleaf Gallery

No es necesario empezar desde cero. Overleaf ofrece cientos de plantillas listas para usar.

**Tipos disponibles:** artículos de journal, tesis, CV/Résumé, pósters, presentaciones Beamer, cartas formales, informes y más.

![Galería de plantillas de Overleaf por categoría](templates1.png)

Para explorar: [overleaf.com/gallery](https://www.overleaf.com/gallery).

### Ejemplo: plantilla de journal académico

![Plantilla OSA Express Journals en Overleaf](templates2.png)

Muchas revistas científicas y conferencias tienen su propia plantilla oficial en Overleaf. Abrirla y estudiar su código es una de las mejores formas de aprender LaTeX.

---

## Estructura básica de un documento

```latex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}

\title{Mi Informe}
\author{Nombre Apellido}
\date{\today}

\begin{document}

\maketitle

\section{Introducción}
Texto de la introducción.

\section{Metodología}
Una ecuación importante:
\begin{equation}
    f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\end{equation}

\end{document}
```

---

## Herramientas útiles

- 📊 [Tables Generator](https://www.tablesgenerator.com/) — crea tablas LaTeX visualmente y copia el código.
- 🔢 [LaTeX Equation Editor](https://editor.codecogs.com/) — genera ecuaciones en tiempo real.
- 🧾 [BibTeX Editor](https://truben.no/latex/bibtex/) — gestiona referencias bibliográficas.
- 🔍 [Detexify](https://detexify.kirelabs.org/classify.html) — dibuja un símbolo y obtén su comando LaTeX.

---

## LaTeX con Inteligencia Artificial

Los asistentes IA (ChatGPT, Gemini, Claude) pueden ayudarte a escribir en LaTeX mucho más rápido:

- Generan y corrigen código LaTeX.
- Crean ecuaciones, tablas y bibliografía.
- Explican comandos y paquetes.
- Detectan errores de compilación.

### Ejemplos de prompts útiles

**Ecuaciones:**
> "Escríbeme en LaTeX la fórmula de la distribución normal estándar, con una breve explicación de cada parámetro."

**Tablas:**
> "Crea una tabla en LaTeX con booktabs que compare Python, R y Julia según velocidad, facilidad de uso y comunidad."

**Corrección de errores:**
> "Este código LaTeX no compila, ¿qué está mal? [pega tu código]"

**Bibliografía:**
> "Genera la entrada BibTeX para el libro *The Elements of Statistical Learning* de Hastie, Tibshirani y Friedman (2009, Springer)."

---

## Recursos adicionales

- 📖 [Documentación oficial de Overleaf](https://www.overleaf.com/learn)
- 🎓 [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- 🖼️ [Overleaf Gallery de plantillas](https://www.overleaf.com/gallery)
- ✨ [Awesome LaTeX (GitHub)](https://github.com/egeerardyn/awesome-LaTeX)
