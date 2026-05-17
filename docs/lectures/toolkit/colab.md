# Colab (Teoría)
> Ejecuta código Python y R desde el navegador, sin instalar nada

---

## ¿Qué es Google Colab?

Google Colab es un entorno de notebooks Jupyter en la nube, gratuito y sin instalación. Solo necesitas una cuenta de Google para empezar en [colab.research.google.com](https://colab.research.google.com).

**¿Para qué sirve?**

- Ejecutar código Python (y R) directamente desde el navegador.
- Compartir análisis, tareas y proyectos con un simple enlace.
- Acceder a GPU/TPU gratuita para proyectos de datos e IA.

![Logo de Google Colab](colab.png)

### Ejemplos de notebooks en uso

Notebook de clasificación supervisada con el dataset Iris (Python):

![Notebook Python: clasificación supervisada con Iris](example_01.png)

Notebook de regresión lineal (R):

![Notebook R: modelo de regresión de salarios](example_02.png)

---

## Celdas: el corazón de Colab

Un notebook tiene dos tipos de celdas:

**Celdas de texto (Markdown)** — para explicar, titular y estructurar el trabajo:

```markdown
# Mi Análisis

Este notebook explora los datos de estudiantes
de la UTFSM durante el semestre 2026.

## Objetivos
- Explorar distribuciones
- Visualizar tendencias
- Ajustar un modelo
```

**Celdas de código Python** — para ejecutar análisis y generar visualizaciones:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv")
df["nota"].hist(bins=20, color="#0F2044")
plt.title("Distribución de notas")
plt.show()
```

**Celdas de código R** — activa R desde el menú: `Runtime → Change runtime type → R`:

```r
library(ggplot2)
df <- read.csv("datos.csv")
ggplot(df, aes(x = nota)) +
  geom_histogram(fill = "#0F2044", bins = 20) +
  labs(title = "Distribución de notas")
```

> 💡 No necesitas instalar R en tu computador — Colab lo tiene listo.

---

## Recursos de la máquina virtual

Cada sesión de Colab asigna una máquina virtual con los siguientes recursos (cuenta gratuita):

- **CPU**: ~2 núcleos Intel Xeon.
- **RAM**: ~12 GB — suficiente para datasets medianos.
- **Disco**: ~100 GB temporales — se borran al cerrar la sesión.
- **GPU T4** *(disponible bajo demanda)*: para modelos de ML/DL.

![Menú para cambiar el tipo de runtime y acelerador de hardware](vm.png)

> ⚠️ **Sesiones temporales**: si la sesión se desconecta, los archivos locales se pierden. Guarda siempre en Drive.

Puedes verificar los recursos disponibles con estas celdas:

```python
# RAM y CPU
import psutil, platform
print(f"CPU: {psutil.cpu_count()} núcleos")
print(f"RAM total:     {psutil.virtual_memory().total / 1e9:.1f} GB")
print(f"RAM disponible:{psutil.virtual_memory().available / 1e9:.1f} GB")

# GPU asignada
!nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

# Disco disponible
!df -h /
```

---

## Cambiar el Kernel (Runtime)

Ve a **Runtime → Change runtime type** para elegir el entorno:

![Diálogo para cambiar el tipo de runtime en Colab](runtime.png)

- **CPU**: para análisis de datos y scripts generales.
- **GPU T4**: para entrenamiento de modelos de ML/DL.
- **TPU**: para modelos muy grandes con TensorFlow.
- **R**: para cambiar completamente el lenguaje del entorno.

> ⚠️ Cambiar el runtime **reinicia la sesión** — guarda tu trabajo antes.

---

## Librerías disponibles

Las siguientes librerías vienen preinstaladas en Python:

| Librería | Para qué sirve |
|---|---|
| `pandas` | Datos tabulares |
| `numpy` | Álgebra numérica |
| `matplotlib` | Gráficos básicos |
| `scikit-learn` | Machine Learning |
| `tensorflow` | Deep Learning |
| `seaborn` | Visualización estadística |

Para instalar librerías adicionales:

```python
# Python
!pip install polars lightgbm

# R (con kernel R activo)
install.packages("tidymodels")
```

> ⚠️ Las librerías instaladas con `!pip` se pierden al reiniciar la sesión.

---

## Subir y acceder a datos

**Subida directa** — para archivos pequeños de uso puntual:

```python
from google.colab import files
uploaded = files.upload()
# → abre un selector de archivos
```

**Desde URL** — la opción más reproducible:

```python
import pandas as pd

# Desde GitHub (raw)
url = "https://raw.githubusercontent.com/usuario/repo/main/datos.csv"
df = pd.read_csv(url)

# Desde Google Sheets publicado como CSV
sheet_url = "https://docs.google.com/spreadsheets/d/ID/export?format=csv"
df = pd.read_csv(sheet_url)
```

**Google Drive** — la forma más estable para datos persistentes:

```python
from google.colab import drive
drive.mount("/content/drive")

import pandas as pd
ruta = "/content/drive/MyDrive/datos/notas.csv"
df = pd.read_csv(ruta)
```

> 💡 Con Drive, los archivos persisten aunque se reinicie la sesión.

---

## Credenciales seguras (Secrets)

Nunca escribas claves o tokens directamente en el código:

```python
# ❌ Mal — expone tu clave en el notebook
API_KEY = "sk-abc123supersecreta"
```

Usa el panel de **Secrets** de Colab:

```
🔑 Ícono de llave (panel izquierdo)
  → "Add new secret"
  → Nombre: MI_API_KEY
  → Valor: tu clave real
  → Activar acceso al notebook
```

Luego accede a ella en el código:

```python
from google.colab import userdata
api_key = userdata.get("MI_API_KEY")
```

> 🔐 Nunca compartas un notebook con claves escritas directamente en el código.

---

## Gemini integrado en Colab

Colab incluye Gemini como asistente IA directamente en el entorno. El ícono ✨ aparece en cada celda de código.

**¿Qué puede hacer?**

- Generar celdas de código a partir de una descripción en lenguaje natural.
- Corregir errores y explicar qué falló.
- Sugerir análisis exploratorios y mejoras de estilo.

**Ejemplo — generar código:**
> *"Crea un gráfico de barras con matplotlib que muestre las notas promedio por carrera."*

**Ejemplo — corregir un error:**
> `AttributeError: 'SeriesGroupBy' object has no attribute 'means'`
> Gemini detecta que el método correcto es `mean()` (sin 's') y entrega el código corregido.

---

## Recursos adicionales

- 📖 [Documentación oficial de Colab](https://colab.research.google.com/notebooks/intro.ipynb)
- 🎓 [Tutorial: Welcome to Colab](https://colab.research.google.com/notebooks/welcome.ipynb)
- 📦 [seaborn-data — datasets de ejemplo](https://github.com/mwaskom/seaborn-data)
