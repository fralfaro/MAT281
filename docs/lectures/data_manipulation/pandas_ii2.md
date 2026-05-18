# 🗂️ Pandas II

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fralfaro/MAT281/blob/main/docs/lectures/data_manipulation/pd_01b.ipynb)

> *"Groupby, merge y pivot son las tres operaciones que separan a quien
> manipula datos de quien los padece."*

---

## Introducción

En Pandas I aprendiste a cargar, explorar, filtrar y limpiar datos.
En esta clase vas un paso más allá: **agregar, combinar y reshapear** DataFrames,
y terminas con una primera mirada a **Seaborn** para visualizar los resultados.

En este módulo aprenderás a:

- Agrupar y resumir datos con `groupby`
- Combinar tablas con `concat` y `merge`
- Cambiar la forma de una tabla con `pivot` y `melt`
- Visualizar datos estadísticos con **Seaborn básico**

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset NBA Players
path = "https://raw.githubusercontent.com/fralfaro/MAT281/main/docs/lectures/data_manipulation/data/player_info.csv"
df = pd.read_csv(path).dropna()
df["decade"] = df["year_start"].apply(lambda x: "2000s" if x >= 2000 else "1900s")
df.head()
```

---

## 1. Groupby

**Groupby** divide el DataFrame en grupos, aplica una función a cada grupo,
y combina los resultados. Es el equivalente a un `GROUP BY` en SQL.

```
dividir → aplicar → combinar
```

![Groupby esquema](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/data_manipulation/images/groupby.jpg)

### 1.1 Agrupar por una columna

```python
# Peso promedio por posición
df.groupby("position")["weight"].mean()
```

### 1.2 Agrupar por varias columnas

```python
# Peso promedio por década y posición
df.groupby(["decade", "position"])["weight"].mean().head(10)
```

### 1.3 Múltiples funciones con `.agg()`

```python
# Estadísticas de peso y año de inicio por grupo
df.groupby(["decade", "position"]).agg({
    "weight":     ["min", "max", "mean"],
    "year_start": ["min", "max"]
}).head()
```

### 1.4 Función personalizada con `.apply()`

```python
def promedio_armonico(serie):
    return len(serie) / sum(1 / x for x in serie)

df.groupby(["decade", "position"])["weight"].apply(promedio_armonico).head()
```

### 1.5 `transform` — agregar resultado al DataFrame original

```python
# Agrega la media del grupo como nueva columna (mantiene el índice original)
df["mean_weight_group"] = df.groupby(["decade", "position"])["weight"].transform("mean")
df[["name", "position", "decade", "weight", "mean_weight_group"]].head()
```

> 💡 `transform` es útil para comparar cada registro contra su grupo,
> por ejemplo: `df["peso_vs_media"] = df["weight"] - df["mean_weight_group"]`

### 1.6 `filter` — conservar grupos que cumplen una condición

```python
# Solo posiciones cuyo peso promedio supera 220 lbs
df.groupby("position").filter(lambda x: x["weight"].mean() > 220).head()
```

---

## 2. Concat — unir tablas verticalmente u horizontalmente

`pd.concat()` apila DataFrames.

```python
df_antes_2000  = df.loc[df["year_start"] < 2000]
df_desde_2000  = df.loc[df["year_start"] >= 2000]

# Mismas columnas → apila filas
result = pd.concat([df_antes_2000, df_desde_2000])
print(result.shape)   # misma cantidad de columnas
```

Si las columnas no coinciden exactamente, pandas rellena con `NaN`:

```python
df_desde_2000_mod = df_desde_2000.rename(columns={"birth_date": "birth"})
result = pd.concat([df_antes_2000, df_desde_2000_mod])
result.columns   # aparecen birth_date Y birth como columnas separadas
```

> ⚠️ Usa `ignore_index=True` si quieres resetear el índice después de concatenar:
> `pd.concat([df1, df2], ignore_index=True)`

---

## 3. Merge — unir tablas por columnas clave

`pd.merge()` combina dos DataFrames por una o más columnas comunes.
Es el equivalente a un `JOIN` en SQL.

```python
df_info    = df[["name", "year_start", "year_end", "position"]]
df_fisico  = df[["name", "height", "weight", "college"]]

# Inner join por nombre
result = pd.merge(df_info, df_fisico, on="name")
result.head()
```

### Tipos de merge

| Tipo    | Descripción                              | SQL equivalente |
|---------|------------------------------------------|-----------------|
| `inner` | Solo filas con coincidencia en ambas tablas | `INNER JOIN`  |
| `left`  | Todas las filas de la izquierda          | `LEFT JOIN`     |
| `right` | Todas las filas de la derecha            | `RIGHT JOIN`    |
| `outer` | Unión de ambas tablas                    | `FULL OUTER JOIN` |

```python
cols_key = ["name", "year_start", "year_end"]
pd.merge(df_info, df_fisico_v2, on=cols_key, how="inner")
pd.merge(df_info, df_fisico_v2, on=cols_key, how="left")
pd.merge(df_info, df_fisico_v2, on=cols_key, how="outer")
```

### Columnas duplicadas

Cuando ambas tablas tienen una columna con el mismo nombre que **no** es la clave,
pandas la renombra automáticamente con sufijos `_x` e `_y`:

```python
df_a = df[["name", "year_start", "year_end", "position"]]
df_b = df[["name", "year_start", "year_end", "height"]]

# year_end aparece en ambas pero no es la clave → year_end_x, year_end_y
pd.merge(df_a, df_b, on=["name", "year_start"]).head()
```

---

## 4. Formatos wide y long

Los datos tabulares pueden presentarse en dos formatos:

| Formato | Descripción | Cuándo usarlo |
|---------|-------------|---------------|
| **Wide** | Cada variable tiene su propia columna | Análisis, ML |
| **Long**  | Una columna de variable + una de valor | Visualización, groupby |

### 4.1 Long → Wide: `pivot_table`

```python
# Peso promedio por década (filas) y posición (columnas)
pivot = df.pivot_table(
    index="decade",
    columns="position",
    values="weight",
    aggfunc="mean"
)
pivot
```

```python
# Pivot con múltiples índices
pivot_multi = df.pivot_table(
    index=["decade", "height"],
    columns="position",
    values="weight",
    aggfunc="mean"
).fillna(0)
pivot_multi.head()
```

### 4.2 Wide → Long: `melt`

```python
# Tenemos tabla wide
df_wide = df.pivot_table(
    index=["name", "year_start", "year_end"],
    columns="position",
    values="weight",
    aggfunc="mean"
).fillna(0).reset_index()
df_wide.columns.name = None

# Volver a long
df_long = df_wide.melt(
    id_vars=["name", "year_start", "year_end"],
    var_name="position",
    value_name="weight"
)
df_long.head()
```

> 💡 La mayoría de las funciones de Seaborn esperan datos en **formato long**.
> Si tienes datos en wide, usa `melt` antes de graficar.

---

## 5. Visualización básica con Seaborn

Seaborn está construido sobre pandas DataFrames: le pasas un DataFrame
y el nombre de las columnas. Mucho más simple que matplotlib para gráficos estadísticos.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
```

### 5.1 Distribución de una variable numérica

```python
plt.figure(figsize=(8, 4))
sns.histplot(data=df, x="weight", bins=30, kde=True, color="steelblue")
plt.title("Distribución del peso de jugadores NBA")
plt.xlabel("Peso (lbs)")
plt.tight_layout()
plt.show()
```

### 5.2 Comparar distribuciones por grupo: boxplot

```python
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="position", y="weight", palette="Set2")
plt.title("Peso por posición en la NBA")
plt.xlabel("Posición")
plt.ylabel("Peso (lbs)")
plt.tight_layout()
plt.show()
```

### 5.3 Comparar promedios: barplot

```python
plt.figure(figsize=(9, 4))
sns.barplot(data=df, x="position", y="weight", hue="decade",
            palette="muted", errorbar="sd")
plt.title("Peso promedio por posición y década")
plt.xlabel("Posición")
plt.ylabel("Peso promedio (lbs)")
plt.legend(title="Década")
plt.tight_layout()
plt.show()
```

### 5.4 Relación entre dos variables: scatterplot

```python
# Primero convertimos height de "6-9" a centímetros para graficarlo
def height_to_cm(h):
    try:
        feet, inches = h.split("-")
        return int(feet) * 30.48 + int(inches) * 2.54
    except:
        return None

df["height_cm"] = df["height"].apply(height_to_cm)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="height_cm", y="weight",
                hue="position", alpha=0.5, palette="tab10")
plt.title("Relación altura vs peso por posición")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (lbs)")
plt.tight_layout()
plt.show()
```

### 5.5 Heatmap de correlaciones

```python
cols_num = ["year_start", "year_end", "weight", "height_cm"]
corr = df[cols_num].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Matriz de correlación")
plt.tight_layout()
plt.show()
```

> 💡 En el módulo de **Visualización** verás estos mismos gráficos
> en versiones interactivas (Plotly), geoespaciales (GeoPandas)
> y de redes (NetworkX). Lo que aprendiste aquí es la base.

---

## Resumen

| Operación       | Función / método                                           |
|-----------------|------------------------------------------------------------|
| Agrupar         | `.groupby()` + `.mean()`, `.agg()`, `.apply()`             |
| Agregar al df   | `.groupby().transform()`                                   |
| Filtrar grupos  | `.groupby().filter(lambda x: ...)`                         |
| Unir filas      | `pd.concat([df1, df2])`                                    |
| Unir columnas   | `pd.merge(df1, df2, on=..., how=...)`                      |
| Wide → Long     | `.melt(id_vars=..., var_name=..., value_name=...)`         |
| Long → Wide     | `.pivot_table(index=..., columns=..., values=..., aggfunc=...)` |
| Distribución    | `sns.histplot`, `sns.boxplot`                              |
| Comparar grupos | `sns.barplot`, `sns.scatterplot`                           |
| Correlaciones   | `sns.heatmap(df.corr())`                                   |

---

## Referencias

1. [Pandas Groupby](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
2. [Pandas Merging](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
3. [Pandas Reshaping](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)
4. [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
5. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly.
