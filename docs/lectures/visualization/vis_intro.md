# Introducción

<img src="https://cdn.thenewstack.io/media/2023/01/285d68dd-charts-e1674846251395.jpg" width = "600" align="center"/>


La visualización de datos permite representar información de manera gráfica para identificar
patrones, tendencias y relaciones que serían difíciles de detectar en tablas o resúmenes numéricos.

## Motivación

| Razón | Idea clave |
|---|---|
| **Comunicar información compleja** | Un gráfico bien hecho transmite en segundos lo que una tabla tarda minutos en revelar. |
| **Descubrir información oculta** | La exploración visual expone patrones, outliers y errores que las estadísticas agregadas ocultan. |
| **Mejorar el análisis** | Visualizar obliga a entender la estructura del dato antes de modelarlo. |

##  Malos y buenos gráficos

### Malos gráficos

Gráficos que distorsionan o confunden: ejes truncados, gráficos 3D innecesarios,
colores sin significado o demasiada información en una sola figura.

![Mal gráfico — Fox News](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Fox1.png)

![Mal gráfico — alturas](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/male_height.jpg)

### Buenos gráficos

Gráficos que cuentan una historia clara: una sola idea central, jerarquía visual,
y título que guía la lectura.

![Buen gráfico — marketing performance](https://cdn.slingshotapp.io/wp-content/uploads/2021/12/1.slingshot-marketing-performance-data-visualization-example-768x485.png)


### Primeras visualizaciones históricas

**Campaña de Napoleón a Moscú** *(Charles Minard, 1869)*
Muestra simultáneamente la ruta, el tamaño del ejército, la dirección del avance/retirada
y la temperatura. Considerado uno de los mejores gráficos estadísticos de la historia.

![Minard](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Napoleon.png)

**Mapa del cólera** *(John Snow, 1855)*
Mapeó los casos de cólera en Londres vinculándolos geográficamente a una sola bomba de agua,
inaugurando la epidemiología moderna.

![Snow](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Colera.png)


##  ¿Por qué utilizar gráficos?

> *"The eye and the visual cortex of the brain form a massively parallel processor
> that provides the highest bandwidth channel into human cognitive centers."*
> — Colin Ware, *Information Visualization*, 2004

El 70 % de los receptores sensoriales del cuerpo humano están dedicados a la visión.
El cerebro procesa información visual de forma masiva y paralela, lo que hace del gráfico
el canal más eficiente para transmitir datos.

### Cuarteto de ANSCOMBE

Cuatro datasets con **estadísticas descriptivas idénticas** pero **distribuciones completamente distintas**.
Presentado por Francis Anscombe en 1973 para demostrar que los números solos no bastan.

<img src="https://matemelga.wordpress.com/wp-content/uploads/2018/11/canscombe.jpg" width = "400" align="center"/>

Sin visualización, los cuatro datasets parecen iguales. Con visualización, son radicalmente distintos:


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Anscombe.svg/1280px-Anscombe.svg.png" width = "600" align="center"/>



## Teoría de visualización

### Conceptos fundamentales

<img src="https://www.kdnuggets.com/wp-content/uploads/ferrer_data_visualization_theory_techniques_8.png" width = "600" align="center"/>


| Concepto | Descripción |
|---|---|
| **Percepción visual** | Cómo los sentidos procesan la información gráfica. |
| **Cognición visual** | Cómo la atención, memoria y razonamiento interpretan lo que vemos. |
| **Diseño visual** | Principios para construir visualizaciones claras y atractivas. |
| **Interactividad** | Cómo las visualizaciones dinámicas permiten explorar los datos. |

### Los 4 pilares de Iliinsky

<img src="https://static.thenounproject.com/png/1034113-200.png" width = "300" align="center"/>

Noah Iliinsky identifica cuatro preguntas que toda buena visualización debe responder:

- **Contenido** — ¿qué dato se representa?
- **Función** — ¿cuál es el objetivo (comparar, mostrar tendencia, explorar)?
- **Forma** — ¿qué tipo de gráfico y codificación visual es más adecuada?
- **Audiencia** — ¿quién lo va a leer y qué nivel de detalle necesita?

> 🔑 Ver [video de referencia](https://www.youtube.com/watch?v=nC92wIzpQFE) para profundizar estos conceptos.




## Python Landscape

Referencia general: [PyViz](https://pyviz.org/) — sitio que ayuda a elegir la librería correcta según la necesidad.

![Landscape](https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/landscape.png)

### Librerías para gráficos estáticos

| Librería | Descripción |
|---|---|
| `matplotlib` | Base del ecosistema; inspirada en MATLAB. Control total sobre el gráfico. |
| `seaborn` | Construida sobre matplotlib; orientada a visualizaciones estadísticas. |
| `pandas.plot` | Wrapper rápido de matplotlib integrado en DataFrames. |
| `networkx` | Visualización de grafos y redes. |

### Librerías para gráficos interactivos

| Librería | Descripción |
|---|---|
| `plotly` | Interactivo y con soporte para dashboards via `Dash`. |
| `bokeh` | Alta performance con datasets grandes y streaming de datos. |
| `D3.js` | Basado en JavaScript; permite visualizaciones totalmente personalizadas. |

> La clave no es dominar una sola librería, sino **saber elegir** la más adecuada para cada problema.
