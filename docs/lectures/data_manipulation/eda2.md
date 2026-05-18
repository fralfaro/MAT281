# 🔍 Análisis Exploratorio de Datos (EDA)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fralfaro/MAT281/blob/main/docs/lectures/data_manipulation/eda_01.ipynb)

<img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=900&auto=format&fit=crop"
     width="100%"
     style="border-radius: 12px; margin-bottom: 1rem;"
     alt="EDA banner"/>

> *"El análisis exploratorio de datos nunca puede ser la historia completa,
> pero nada más puede servir como fundamento."*
> — John W. Tukey

---

## Introducción

El **Análisis Exploratorio de Datos** (EDA, por sus siglas en inglés) es el proceso
de examinar un dataset antes de aplicar cualquier modelo o técnica avanzada.
Su objetivo es simple pero crítico: **entender qué hay en los datos**.

Un buen EDA responde preguntas como:

- ¿Cómo están distribuidas las variables?
- ¿Hay valores atípicos o nulos?
- ¿Qué relaciones existen entre variables?
- ¿Los datos tienen la calidad suficiente para lo que quiero hacer?

En este módulo integrarás todo lo aprendido en Pandas I, Pandas II
y las visualizaciones con matplotlib y seaborn en un flujo de análisis completo.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted")

# Dataset: Indicadores socioeconómicos comunales de Chile (CASEN-like)
# Usaremos el dataset NBA como proxy para mantener consistencia con módulos anteriores
path = "https://raw.githubusercontent.com/fralfaro/MAT281/main/docs/lectures/data_manipulation/data/player_info.csv"
df = pd.read_csv(path)
df.head()
```

---

## 1. Perfil del dataset

El primer paso es siempre obtener una **radiografía** del dataset:
dimensiones, tipos de datos, completitud y primeras estadísticas.

### 1.1 Dimensiones y tipos

```python
print(f"Filas:    {df.shape[0]:,}")
print(f"Columnas: {df.shape[1]}")
print()
df.dtypes
```

### 1.2 Valores nulos

```python
nulos = df.isnull().sum().sort_values(ascending=False)
pct_nulos = (nulos / len(df) * 100).round(2)

resumen_nulos = pd.DataFrame({
    "nulos":      nulos,
    "% del total": pct_nulos
})
resumen_nulos[resumen_nulos["nulos"] > 0]
```

```python
# Visualizar el porcentaje de nulos
fig, ax = plt.subplots(figsize=(8, 4))
pct_nulos[pct_nulos > 0].sort_values().plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Porcentaje de valores nulos por columna")
ax.set_xlabel("% nulos")
ax.axvline(5, color="red", linestyle="--", alpha=0.5, label="umbral 5%")
ax.legend()
plt.tight_layout()
plt.show()
```

### 1.3 Duplicados

```python
n_dup = df.duplicated().sum()
print(f"Filas duplicadas: {n_dup} ({n_dup/len(df)*100:.2f}%)")
```

### 1.4 Estadísticas descriptivas

```python
df.describe(include="all").T   # include="all" incluye columnas categóricas
```

> 💡 `describe()` con `include="all"` es una de las formas más rápidas
> de detectar columnas con pocos valores únicos (potenciales categóricas),
> rangos sospechosos o conteos que no coinciden con el total de filas.

---

## 2. Análisis univariado

Estudia **cada variable por separado**. El objetivo es entender su distribución,
rango y posibles anomalías.

### 2.1 Variables numéricas

```python
# Preparar: convertir altura a cm y añadir duración
def height_to_cm(h):
    try:
        f, i = h.split("-")
        return int(f) * 30.48 + int(i) * 2.54
    except:
        return None

df["height_cm"] = df["height"].apply(height_to_cm)
df["duration"]  = df["year_end"] - df["year_start"]
df_num = df[["weight", "height_cm", "duration", "year_start"]].dropna()
```

```python
# Histogramas de todas las variables numéricas
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, col in zip(axes, df_num.columns):
    ax.hist(df_num[col].dropna(), bins=30, color="steelblue",
            edgecolor="white", alpha=0.8)
    ax.axvline(df_num[col].mean(),   color="red",    linestyle="--", label="media")
    ax.axvline(df_num[col].median(), color="orange", linestyle=":",  label="mediana")
    ax.set_title(col)
    ax.legend(fontsize=8)

plt.suptitle("Distribución de variables numéricas", y=1.01, fontsize=13)
plt.tight_layout()
plt.show()
```

```python
# Boxplots para detectar outliers
fig, axes = plt.subplots(1, 4, figsize=(14, 5))
for ax, col in zip(axes, df_num.columns):
    ax.boxplot(df_num[col].dropna(), vert=True, patch_artist=True,
               boxprops=dict(facecolor="steelblue", alpha=0.6))
    ax.set_title(col)
plt.suptitle("Boxplots — detección de valores atípicos", fontsize=13)
plt.tight_layout()
plt.show()
```

### 2.2 Variables categóricas

```python
# Frecuencia de posiciones
fig, ax = plt.subplots(figsize=(8, 4))
df["position"].value_counts().plot(kind="bar", ax=ax, color="steelblue",
                                    edgecolor="white")
ax.set_title("Frecuencia de posiciones NBA")
ax.set_xlabel("Posición")
ax.set_ylabel("Cantidad de jugadores")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

```python
# Top 10 universidades
top_colleges = df["college"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(9, 4))
top_colleges.sort_values().plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Top 10 universidades de origen")
ax.set_xlabel("Número de jugadores")
plt.tight_layout()
plt.show()
```

---

## 3. Análisis bivariado

Estudia la **relación entre dos variables**. Es el paso donde empiezan
a aparecer las preguntas interesantes.

### 3.1 Numérica vs numérica: scatter + correlación

```python
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df["height_cm"], df["weight"], alpha=0.3, color="steelblue", s=15)
ax.set_title("Altura vs Peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (lbs)")
plt.tight_layout()
plt.show()
```

```python
# Matriz de correlación
cols_num = ["weight", "height_cm", "duration", "year_start"]
corr = df[cols_num].corr()

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, ax=ax, linewidths=0.5)
ax.set_title("Correlaciones entre variables numéricas")
plt.tight_layout()
plt.show()
```

> 💡 Correlación alta no implica causalidad. Altura y peso correlacionan
> porque los datos provienen de una población específica (atletas de élite),
> no porque una cause la otra.

### 3.2 Categórica vs numérica: boxplot por grupo

```python
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df.dropna(subset=["weight", "position"]),
            x="position", y="weight",
            palette="Set2", ax=ax)
ax.set_title("Distribución del peso por posición")
ax.set_xlabel("Posición")
ax.set_ylabel("Peso (lbs)")
plt.tight_layout()
plt.show()
```

```python
# Violinplot — más detalle que el boxplot
fig, ax = plt.subplots(figsize=(10, 5))
sns.violinplot(data=df.dropna(subset=["weight", "position"]),
               x="position", y="weight",
               palette="muted", inner="quartile", ax=ax)
ax.set_title("Distribución del peso por posición (violinplot)")
plt.tight_layout()
plt.show()
```

### 3.3 Categórica vs categórica: tabla de contingencia

```python
# Crear variable decade
df["decade"] = df["year_start"].apply(lambda x: "2000s" if x >= 2000 else "1900s")

# Tabla de contingencia: posición × década
tabla = pd.crosstab(df["position"], df["decade"], normalize="index") * 100
tabla.round(1)
```

```python
# Visualizar como heatmap
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(tabla, annot=True, fmt=".1f", cmap="Blues",
            linewidths=0.5, ax=ax)
ax.set_title("Distribución de décadas por posición (%)")
plt.tight_layout()
plt.show()
```

---

## 4. Análisis temporal

Cuando los datos tienen una dimensión temporal, es clave explorar
cómo evolucionan las variables en el tiempo.

```python
# Evolución del peso promedio por año de inicio
peso_por_año = (
    df.dropna(subset=["weight"])
    .groupby("year_start")["weight"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(peso_por_año["year_start"], peso_por_año["weight"],
        color="steelblue", linewidth=2)
ax.fill_between(peso_por_año["year_start"], peso_por_año["weight"],
                alpha=0.15, color="steelblue")
ax.set_title("Evolución del peso promedio de jugadores NBA (1947–2018)")
ax.set_xlabel("Año de inicio")
ax.set_ylabel("Peso promedio (lbs)")
ax.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()
```

```python
# Número de jugadores debutantes por año
debuts = df.groupby("year_start").size().reset_index(name="n_jugadores")

fig, ax = plt.subplots(figsize=(12, 4))
ax.bar(debuts["year_start"], debuts["n_jugadores"],
       color="steelblue", alpha=0.7, width=0.8)
ax.set_title("Jugadores debutantes por año en la NBA")
ax.set_xlabel("Año")
ax.set_ylabel("N° de jugadores")
plt.tight_layout()
plt.show()
```

---

## 5. Detección de anomalías

Una parte fundamental del EDA es identificar valores que podrían
ser errores, casos extremos o simplemente inusuales.

### 5.1 Método IQR

```python
def detectar_outliers_iqr(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = serie[(serie < lower) | (serie > upper)]
    return outliers, lower, upper

outliers_peso, lo, hi = detectar_outliers_iqr(df["weight"].dropna())
print(f"Rango normal: [{lo:.1f}, {hi:.1f}] lbs")
print(f"Outliers detectados: {len(outliers_peso)}")
print(outliers_peso.describe())
```

### 5.2 Método Z-score

```python
from scipy import stats

z_scores = np.abs(stats.zscore(df["weight"].dropna()))
outliers_z = df["weight"].dropna()[z_scores > 3]
print(f"Outliers (|z| > 3): {len(outliers_z)}")
print(outliers_z.sort_values(ascending=False).head(10))
```

```python
# Visualizar outliers en el contexto del dataset
fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(df["weight"].dropna(), bins=40, color="steelblue",
        edgecolor="white", alpha=0.8, label="distribución")
ax.axvline(lo, color="red",    linestyle="--", label=f"límite inferior IQR ({lo:.0f})")
ax.axvline(hi, color="orange", linestyle="--", label=f"límite superior IQR ({hi:.0f})")
ax.set_title("Distribución de peso con límites IQR")
ax.set_xlabel("Peso (lbs)")
ax.legend()
plt.tight_layout()
plt.show()
```

---

## 6. Reporte EDA — checklist

Un EDA bien hecho debería poder responder estas preguntas antes de
pasar al modelado:

| Pregunta | Herramienta |
|----------|-------------|
| ¿Cuántas filas y columnas tiene el dataset? | `.shape`, `.info()` |
| ¿Qué porcentaje de nulos tiene cada columna? | `.isnull().sum()` |
| ¿Hay filas duplicadas? | `.duplicated().sum()` |
| ¿Cómo se distribuye cada variable numérica? | histograma + boxplot |
| ¿Cuáles son las categorías más frecuentes? | `.value_counts()` + barplot |
| ¿Qué variables están correlacionadas? | heatmap de correlación |
| ¿Hay outliers? | IQR, Z-score, boxplot |
| ¿Cómo evolucionan las variables en el tiempo? | lineplot por año/fecha |
| ¿Hay diferencias entre grupos? | boxplot / violinplot por categoría |

> 💡 El EDA no termina con una respuesta definitiva — termina con
> **mejores preguntas**. Es un proceso iterativo: cada hallazgo
> abre nuevas líneas de exploración.

---

## Resumen

```
EDA = perfil + univariado + bivariado + temporal + anomalías
```

| Etapa          | Qué explorar                        | Herramientas                        |
|----------------|--------------------------------------|-------------------------------------|
| Perfil         | Dimensiones, tipos, nulos, duplicados | `.info()`, `.describe()`, `.isnull()` |
| Univariado     | Distribución de cada variable        | histograma, boxplot, barplot        |
| Bivariado      | Relaciones entre pares de variables  | scatter, heatmap, boxplot por grupo |
| Temporal       | Evolución en el tiempo               | lineplot, barplot por año           |
| Anomalías      | Outliers y valores sospechosos       | IQR, Z-score, boxplot               |

---

## Referencias

1. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
2. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.
3. [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
4. [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
