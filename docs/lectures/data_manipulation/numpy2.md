# 🔢 NumPy

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fralfaro/MAT281/blob/main/docs/lectures/data_manipulation/sc_01.ipynb)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/2560px-NumPy_logo_2020.svg.png" width="400"/>

> *"NumPy es al cómputo científico en Python lo que el álgebra lineal
> es a las matemáticas: el lenguaje base sobre el que todo lo demás se construye."*

---

## Introducción

[NumPy](https://numpy.org/) es la biblioteca fundamental para el cómputo numérico
en Python. Su objeto central — el **array multidimensional** (`ndarray`) —
permite operar sobre vectores y matrices de forma eficiente, con una sintaxis
mucho más limpia que las listas nativas de Python.

En este módulo aprenderás a:

- Crear y manipular arrays de una y múltiples dimensiones
- Realizar operaciones aritméticas, estadísticas y de álgebra lineal
- Visualizar datos numéricos con **matplotlib** de forma básica

> 💡 **¿Por qué importa?** Pandas, Scikit-Learn, y prácticamente toda
> la cadena de herramientas de ciencia de datos operan internamente
> sobre arrays NumPy. Entender NumPy es entender el fundamento.

---

## 1. Python Lists vs NumPy Arrays

Antes de crear arrays, vale la pena entender por qué no basta con las listas de Python.

```python
import numpy as np
import time
import sys

def tiempo_lista(n):
    t1 = time.time()
    X, Y = range(n), range(n)
    Z = [X[i] + Y[i] for i in range(n)]
    return time.time() - t1, sys.getsizeof(Z)

def tiempo_numpy(n):
    t1 = time.time()
    X, Y = np.arange(n), np.arange(n)
    Z = X + Y
    return time.time() - t1, sys.getsizeof(Z)

for n in [1_000, 100_000, 1_000_000]:
    t1, s1 = tiempo_lista(n)
    t2, s2 = tiempo_numpy(n)
    print(f"n={n:>10,} | lista: {t1:.5f}s {s1:>10} bytes | numpy: {t2:.5f}s {s2:>9} bytes")
```

**Resultado típico:**

| n         | Lista (tiempo) | Lista (memoria) | NumPy (tiempo) | NumPy (memoria) |
|-----------|---------------|-----------------|----------------|-----------------|
| 1.000     | 0.00000s      | 9.016 bytes     | 0.00000s       | 4.112 bytes     |
| 100.000   | 0.01600s      | 824.456 bytes   | 0.00000s       | 400.112 bytes   |
| 1.000.000 | 0.14600s      | 8.697.456 bytes | 0.00261s       | 4.000.112 bytes |

> ✅ NumPy es ~2x más eficiente en memoria y hasta **50x más rápido**
> para operaciones numéricas a gran escala.

---

## 2. Objetos en NumPy

El objeto principal es el `ndarray`. Puede ser 1D (vector), 2D (matriz) o nD (tensor).

```python
import numpy as np

# Vector (1D)
v = np.array([1, 2, 3])

# Matriz (2D)
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Tensor (3D)
T = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(f"vector: shape={v.shape}, ndim={v.ndim}, dtype={v.dtype}")
print(f"matriz: shape={M.shape}, ndim={M.ndim}, dtype={M.dtype}")
print(f"tensor: shape={T.shape}, ndim={T.ndim}, dtype={T.dtype}")
```

### Atributos clave de un ndarray

| Atributo     | Descripción                              | Ejemplo         |
|--------------|------------------------------------------|-----------------|
| `.shape`     | Dimensiones del array                    | `(3,)`, `(2,3)` |
| `.ndim`      | Número de dimensiones                    | `1`, `2`, `3`   |
| `.size`      | Total de elementos                       | `6`             |
| `.dtype`     | Tipo de datos                            | `int64`, `float64` |

### Arrays especiales

```python
np.zeros((3, 3))        # matriz de ceros
np.ones((2, 4))         # matriz de unos
np.eye(3)               # matriz identidad
np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)    # [0.0, 0.25, 0.5, 0.75, 1.0]

np.random.seed(42)
np.random.uniform(0, 10, size=6)   # valores aleatorios reproducibles
```

---

## 3. Operaciones

### 3.1 Aritméticas (element-wise)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4  0.5]
print(a ** 2)  # [1 4 9]
```

> ⚠️ `a * b` es multiplicación **elemento a elemento**, no producto matricial.
> Para producto matricial usa `np.dot(A, B)` o el operador `@`.

### 3.2 Comparación

```python
a = np.array([1, 2, 3])
b = np.array([2, 2, 4])

print(a == b)   # [False  True False]
print(a > b)    # [False False False]
print(a <= b)   # [ True  True  True]
```

Los resultados son arrays booleanos — útiles para **filtrar** datos:

```python
# Seleccionar elementos mayores a 2
print(a[a > 2])   # [3]
```

### 3.3 Estadísticas

```python
a = np.array([2, 4, 4, 4, 5, 5, 7, 9])

print(f"suma:    {np.sum(a)}")
print(f"media:   {np.mean(a):.2f}")
print(f"std:     {np.std(a):.2f}")
print(f"mínimo:  {np.min(a)}")
print(f"máximo:  {np.max(a)}")
print(f"mediana: {np.median(a)}")
```

---

## 4. Indexación y Slicing

```python
a = np.array([10, 20, 30, 40, 50])

a[0]     # 10  — primer elemento
a[-1]    # 50  — último elemento
a[1:4]   # [20 30 40]
a[::2]   # [10 30 50] — saltando de dos en dos
```

Para arrays 2D:

```python
M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

M[0, :]    # primera fila:    [1 2 3]
M[:, 1]    # segunda columna: [2 5 8]
M[1, 2]    # elemento (fila 1, col 2): 6
M[:2, :]   # primeras dos filas
M.diagonal()  # [1 5 9]
```

---

## 5. Álgebra Lineal

NumPy cubre las operaciones fundamentales del curso vía `np.linalg`:

```python
A = np.array([[1, 2],
              [3, 4]])

# Operaciones básicas
print(A.T)                    # transpuesta
print(np.linalg.det(A))       # determinante: -2.0
print(np.linalg.inv(A))       # inversa
print(np.trace(A))            # traza: 5

# Valores y vectores propios
vals, vecs = np.linalg.eig(A)
print(f"eigenvalues:  {vals}")
print(f"eigenvectors:\n{vecs}")

# Sistema de ecuaciones: Ax = b
b = np.array([5., 7.])
x = np.linalg.solve(A, b)
print(f"solución x: {x}")     # [-3.  4.]
```

---

## 6. Broadcasting

Broadcasting permite operar entre arrays de **distinta forma** sin copiar datos.
La regla básica: NumPy "expande" el array más pequeño para que las formas sean compatibles.

```python
# Escalar + vector
np.arange(3) + 5           # [5 6 7]

# Matriz + vector (por filas)
np.ones((3, 3)) + np.arange(3)
# [[1. 2. 3.]
#  [1. 2. 3.]
#  [1. 2. 3.]]

# Vector columna + vector fila → matriz
np.arange(3).reshape((3, 1)) + np.arange(3)
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]
```

![Broadcasting](https://numpy.org/doc/stable/_images/broadcasting_4.png)

---

## 7. Visualización básica con Matplotlib

NumPy y Matplotlib trabajan de forma natural juntos: matplotlib opera
directamente sobre arrays. Aquí los gráficos más útiles para explorar datos numéricos.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### 7.1 Gráfico de línea

```python
x = np.linspace(0, 2 * np.pi, 100)

plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)", linestyle="--")
plt.title("Funciones trigonométricas")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

### 7.2 Gráfico de dispersión

```python
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(6, 5))
plt.scatter(x, y, alpha=0.6, color="steelblue", edgecolors="white")
plt.title("Dispersión: relación lineal con ruido")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.tight_layout()
plt.show()
```

### 7.3 Histograma

```python
np.random.seed(42)
datos = np.random.normal(loc=170, scale=10, size=500)  # alturas simuladas (cm)

plt.figure(figsize=(7, 4))
plt.hist(datos, bins=30, color="steelblue", edgecolor="white", alpha=0.8)
plt.axvline(np.mean(datos), color="red", linestyle="--", label=f"media = {np.mean(datos):.1f}")
plt.title("Distribución de alturas simuladas")
plt.xlabel("Altura (cm)")
plt.ylabel("Frecuencia")
plt.legend()
plt.tight_layout()
plt.show()
```

### 7.4 Visualizar una matriz (heatmap simple)

```python
np.random.seed(0)
M = np.random.randint(0, 100, size=(5, 5))

plt.figure(figsize=(5, 4))
plt.imshow(M, cmap="Blues")
plt.colorbar(label="Valor")
plt.title("Heatmap de una matriz")
plt.tight_layout()
plt.show()
```

> 💡 En el módulo de **Pandas + Seaborn** verás cómo crear estos mismos
> gráficos directamente desde un DataFrame, con menos código y más contexto.

---

## Resumen

| Tema              | Función clave                                  |
|-------------------|------------------------------------------------|
| Crear arrays      | `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace` |
| Atributos         | `.shape`, `.ndim`, `.size`, `.dtype`           |
| Aritmética        | `+`, `-`, `*`, `/`, `**`, `np.dot`             |
| Estadísticas      | `np.sum`, `np.mean`, `np.std`, `np.min`, `np.max` |
| Álgebra lineal    | `np.linalg.inv`, `.det`, `.eig`, `.solve`      |
| Visualización     | `plt.plot`, `plt.scatter`, `plt.hist`, `plt.imshow` |

---

## Referencias

1. [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
2. [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
3. [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
4. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly.
