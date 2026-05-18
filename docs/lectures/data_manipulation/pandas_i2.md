# 🗂️ Pandas I

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fralfaro/MAT281/blob/main/docs/lectures/data_manipulation/pd_01a.ipynb)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" width="400"/>

> *"Pandas es a los datos tabulares lo que NumPy es a los arreglos numéricos:
> la herramienta que hace que todo lo demás tenga sentido."*

---

## Introducción

[Pandas](https://pandas.pydata.org/) es la biblioteca de referencia para manipulación
de datos tabulares en Python. Su objeto central — el **DataFrame** — es esencialmente
una tabla con etiquetas en filas y columnas, lo que lo hace mucho más expresivo
que un array NumPy para datos del mundo real.

En este módulo aprenderás a:

- Crear y cargar DataFrames desde distintas fuentes
- Explorar, filtrar y transformar datos
- Manejar valores nulos, duplicados y fechas

> 💡 Si ya sabes R, `pandas` es el equivalente a `dplyr + tidyr`.
> Los conceptos son los mismos, solo cambia la sintaxis.

---

## 1. Estructuras principales: Series y DataFrame

Pandas tiene dos objetos fundamentales:

- **Series** — array 1D con etiquetas (como un diccionario ordenado)
- **DataFrame** — tabla 2D con etiquetas en filas y columnas (como una hoja de cálculo)

```python
import pandas as pd
import numpy as np

# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# DataFrame desde diccionario
df = pd.DataFrame({
    "nombre":   ["Ana", "Luis", "María"],
    "edad":     [28, 34, 22],
    "ciudad":   ["Santiago", "Valparaíso", "Concepción"]
})
df
```

| Atributo    | Descripción                          |
|-------------|--------------------------------------|
| `.values`   | Datos como array NumPy               |
| `.index`    | Etiquetas de filas                   |
| `.columns`  | Etiquetas de columnas                |
| `.dtypes`   | Tipos de datos por columna           |
| `.shape`    | Dimensiones (filas, columnas)        |

---

## 2. Carga de datos

En la práctica los datos vienen de archivos externos. Pandas soporta múltiples formatos:

```python
# CSV (el más común)
df = pd.read_csv("datos.csv")

# CSV desde URL
url = "https://raw.githubusercontent.com/fralfaro/MAT281/main/docs/lectures/data_manipulation/data/player_info.csv"
df = pd.read_csv(url, sep=",")

# Excel
df = pd.read_excel("datos.xlsx", sheet_name="Hoja1")

# JSON
df = pd.read_json("datos.json")
```

> 💡 Para este módulo usaremos el dataset **NBA Players (1947–2018)**,
> que contiene información biográfica y de carrera de jugadores de la NBA.

### 🏀 Dataset: NBA Players

```python
path = "https://raw.githubusercontent.com/fralfaro/MAT281/main/docs/lectures/data_manipulation/data/player_info.csv"
df = pd.read_csv(path)
df.head()
```

| Columna      | Descripción                                      |
|--------------|--------------------------------------------------|
| `name`       | Nombre completo del jugador                      |
| `year_start` | Año de inicio de carrera en la NBA               |
| `year_end`   | Año de fin de carrera en la NBA                  |
| `position`   | Posición en cancha (G, F, C, etc.)               |
| `height`     | Altura en pulgadas                               |
| `weight`     | Peso en libras                                   |
| `birth_date` | Fecha de nacimiento                              |
| `college`    | Universidad de origen                            |

---

## 3. Exploración básica

Lo primero siempre es entender la estructura del dataset:

```python
df.head()          # primeras 5 filas
df.tail()          # últimas 5 filas
df.shape           # (4551, 8) → filas × columnas
df.dtypes          # tipo de dato por columna
df.info()          # resumen compacto: tipos + nulos
df.describe()      # estadísticas descriptivas de columnas numéricas
```

### Exploración por columna

```python
df["position"].nunique()        # cuántos valores únicos
df["position"].unique()         # qué valores únicos hay
df["position"].value_counts()   # frecuencia de cada valor

df.sort_values("year_start", ascending=True).head()   # ordenar
df.sort_values("weight", ascending=False).head()
```

---

## 4. Transformación de columnas

### Crear y eliminar columnas

```python
# Columna constante
df["liga"] = "NBA"

# Columna derivada
df["duration"] = df["year_end"] - df["year_start"]

# Eliminar columna
df = df.drop("liga", axis=1)

# Eliminar varias columnas
df = df.drop(["col1", "col2"], axis=1)
```

### Transformar con `apply`

```python
# Clasificar duración de carrera
df["carrera_larga"] = df["duration"].apply(lambda x: 1 if x > 10 else 0)
df["carrera_larga"].value_counts()
```

### Funciones útiles para series temporales de filas

```python
df["duration_shift"]   = df["duration"].shift()        # valor de la fila anterior
df["duration_cumsum"]  = df["duration"].cumsum()        # suma acumulada
df["duration_pct"]     = df["duration"].pct_change()    # cambio porcentual
df["duration_rank"]    = df["duration"].rank()          # ranking
```

> ⚠️ `shift()`, `cumsum()` y `pct_change()` asumen que el orden de las filas
> tiene sentido. Si no ordenaste el DataFrame antes, los resultados pueden
> ser incorrectos.

---

## 5. Filtrar datos

Pandas filtra con condiciones booleanas vía `.loc[]`:

```python
# Jugadores que empezaron desde 2000
df.loc[df["year_start"] >= 2000]

# Rango de años
df.loc[df["year_start"].between(2005, 2015)]

# Valor exacto
df.loc[df["year_start"] == 2000]

# Múltiples condiciones (& = AND, | = OR)
df.loc[(df["year_start"] == 2000) & (df["duration"] > 5)]

# Filtrar por texto
df.loc[df["name"].str.contains("Michael")]
```

> 💡 Siempre usa `.loc[]` para filtrar por condición lógica.
> Usa `.iloc[]` solo cuando necesites filtrar por posición numérica (fila 3, columna 2, etc.).

---

## 6. Valores nulos y duplicados

### Valores nulos

```python
# ¿Cuántos nulos por columna?
df.isnull().sum()

# Eliminar filas con algún nulo
df_clean = df.dropna()

# Eliminar filas donde cierta columna es nula
df_clean = df.dropna(subset=["weight"])

# Rellenar nulos con un valor específico
df_filled = df.fillna({"weight": df["weight"].mean(), "college": "Desconocido"})
```

> ⚠️ `dropna()` sin argumentos puede eliminar muchas filas si hay columnas
> con muchos nulos (como `college` con 304 nulos en este dataset).
> Siempre evalúa qué columnas importan antes de eliminar filas.

### Duplicados

```python
# ¿Hay filas duplicadas?
df.duplicated().sum()

# Eliminar duplicados
df_unique = df.drop_duplicates()

# Verificar
df_unique.duplicated().sum()   # → 0
```

---

## 7. Manipulación de fechas

Pandas tiene soporte nativo para fechas con `pd.to_datetime()` y el accesorio `.dt`:

```python
import datetime

# Convertir columna de texto a datetime
df["birth_date_parsed"] = pd.to_datetime(df["birth_date"])
df.dtypes   # birth_date_parsed → datetime64[ns]

# Extraer componentes
df["birth_year"]  = df["birth_date_parsed"].dt.year
df["birth_month"] = df["birth_date_parsed"].dt.month
df["birth_day"]   = df["birth_date_parsed"].dt.day

# Calcular edad aproximada (si tuviéramos una fecha de referencia)
hoy = pd.Timestamp("2025-01-01")
df["edad_aprox"] = (hoy - df["birth_date_parsed"]).dt.days // 365

df[["name", "birth_date_parsed", "birth_year", "birth_month", "edad_aprox"]].head()
```

---

## Resumen

| Operación              | Función / método                                     |
|------------------------|------------------------------------------------------|
| Cargar datos           | `pd.read_csv`, `pd.read_excel`, `pd.read_json`       |
| Explorar               | `.head()`, `.info()`, `.describe()`, `.shape`        |
| Crear columna          | `df["nueva"] = ...`                                  |
| Transformar            | `.apply(lambda x: ...)`, `.shift()`, `.cumsum()`     |
| Filtrar                | `.loc[condición]`, `.between()`, `.str.contains()`   |
| Nulos                  | `.isnull()`, `.dropna()`, `.fillna()`                |
| Duplicados             | `.duplicated()`, `.drop_duplicates()`                |
| Fechas                 | `pd.to_datetime()`, `.dt.year`, `.dt.month`          |

> 💡 En **Pandas II** verás cómo agrupar, combinar y reshapear
> DataFrames — y cómo visualizarlos con **Seaborn**.

---

## Referencias

1. [Pandas Documentation](https://pandas.pydata.org/docs/)
2. [Python Pandas Tutorial – LearnDataSci](https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/)
3. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly.
