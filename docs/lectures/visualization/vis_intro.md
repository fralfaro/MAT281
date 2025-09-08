# Introducción

<img src="https://cdn-icons-png.flaticon.com/256/11232/11232292.png" width = "250" align="center"/>


La visualización de datos es una herramienta poderosa en el campo de la
ciencia de datos y el análisis de datos que permite representar información
de manera gráfica y comprensible. A través de gráficos, diagramas
y otras representaciones visuales, la visualización de datos ayuda a identificar patrones,
tendencias y relaciones en los datos, facilitando la interpretación y
la toma de decisiones basadas en evidencia.

## Motivación

Aprender sobre visualización es importante por varias razones:

**Comunicar información compleja de manera clara y efectiva**

Al presentar datos de una manera visual, es más fácil identificar patrones y tendencias, así como también hacer comparaciones y contrastes. Esto es especialmente importante cuando se trabaja con grandes conjuntos de datos o cuando se trata de presentar información a un público diverso.

**Descubrir información oculta o desconocida**

A menudo, los datos pueden contener patrones o relaciones que no son obvios a simple vista, pero que pueden ser descubiertos mediante la exploración y la visualización. La visualización también puede ayudar a identificar errores y anomalías en los datos, lo que puede ser importante para la toma de decisiones y la planificación.

**Mejorar la capacidad de análisis de datos**

Al comprender cómo presentar datos de manera efectiva, se puede desarrollar una mejor comprensión de los datos y las relaciones que existen entre ellos. Esto puede ayudar a tomar decisiones informadas basadas en datos y a identificar tendencias y oportunidades que de otra manera podrían haber pasado desapercibidas.

### Malos Gráficos

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Fox1.png" width = "500" align="center"/>


<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/male_height.jpg" width = "500" align="center"/>

### Buenos Gráficos

<img src="https://cdn.slingshotapp.io/wp-content/uploads/2021/12/1.slingshot-marketing-performance-data-visualization-example-768x485.png" width = "600" align="center"/>




### Primeras visualizaciones

**Campaña de Napoleón a Moscú (Charles Minard, 1889)**

Gráfico que muestra el número de las fuerzas francesas en su marcha hacia Moscú y durante la retirada, por Charles Minard. También contiene información ambiental como la temperatura por fecha.

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Napoleon.png" width = "600" align="center"/>

**Mapa del cólera (John Snow, 1855)**

Gráfico que muestra los casos de cólera durante la epidemia en Londres de 1854 y Las cruces la ubicación de las bombas de agua.

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Colera.png" width = "600" align="center"/>

## ¿Por qué utilizar gráficos?

* El 70 % de los receptores sensoriales del cuerpo humano está dedicado a la visión.
* Cerebro ha sido entrenado evolutivamente para interpretar la información visual de manera masiva.

    _“The eye and the visual cortex of the brain form a massively
    parallel processor that provides the highest bandwidth channel
    into human cognitive centers”
    — Colin Ware, Information Visualization, 2004._

### Cuarteto de ANSCOMBE

El **Cuarteto de Anscombe** es un conjunto de cuatro conjuntos de datos que tienen las mismas estadísticas descriptivas (medias, varianzas, correlaciones y regresiones), pero que se ven muy diferentes cuando se visualizan. Fueron presentados por el estadístico Francis Anscombe en 1973 para demostrar la importancia de la visualización en el análisis de datos.

Los cuatro conjuntos de datos consisten en pares de variables **x** e **y**, y cada conjunto representa un tipo diferente de relación entre las variables. A simple vista, los cuatro conjuntos parecen tener distribuciones y relaciones completamente diferentes entre sí, pero cuando se analizan las estadísticas descriptivas, todas son idénticas.

**Estadísticos**

<img src="https://matemelga.wordpress.com/wp-content/uploads/2018/11/canscombe.jpg" width = "400" align="center"/>


**Gráficos**

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Anscombe.svg/1200px-Anscombe.svg.png" width = "600" align="center"/>



## Teoría de visualización

La **teoría de visualización** se refiere a la investigación y el estudio de cómo las personas procesan, interpretan y comprenden información visual. La visualización puede involucrar cualquier tipo de información que pueda ser representada visualmente, incluyendo gráficos, diagramas, mapas, fotografías y videos.

Algunos de los conceptos y principios importantes en la teoría de visualización incluyen:

* **Percepción visual**: Cómo procesamos y entendemos la información visual a través de nuestros sentidos.


* **Cognición visual**: Cómo procesamos y entendemos la información visual a través de nuestros procesos mentales, como la atención, la memoria y la toma de decisiones.


* **Diseño visual**: Cómo se pueden crear visualizaciones efectivas y atractivas para comunicar información de manera clara y efectiva.


* **Interactividad visual**: Cómo las visualizaciones interactivas pueden ayudar a los usuarios a explorar y comprender mejor la información visual.


### Consejos generales

**Noah Iliinsky** es un experto en visualización de datos y ha identificado cuatro pilares fundamentales de la visualización.

Estos pilares son:

* **Contenido**: El contenido se refiere a la información que se está visualizando. Para que la visualización sea efectiva, es importante tener una comprensión clara del contenido y cómo se relaciona con el objetivo de la visualización.


* **Función**: La función se refiere al propósito de la visualización. ¿Qué se espera que haga la visualización? ¿Debe mostrar una tendencia, comparar datos o explorar patrones? Es importante tener en cuenta la función de la visualización para asegurarse de que se está diseñando de manera efectiva.


* **Forma**: La forma se refiere a la apariencia visual de la visualización. Esto incluye cosas como el tipo de gráfico o diagrama utilizado, la paleta de colores y la tipografía. La forma debe ser coherente y legible para que la visualización sea fácil de entender.


* **Audiencia**: La audiencia se refiere a las personas que verán la visualización. La comprensión de la audiencia es esencial para determinar el nivel de detalle y complejidad adecuados para la visualización. La visualización debe ser accesible y comprensible para su audiencia objetivo.

> 🔑 **Nota**: Se recomienda ver el siguiente [video](https://www.youtube.com/watch?v=nC92wIzpQFE&ab_channel=StarsConf) para profundizar estos conceptos


### Honestidad

El ojo humano no tiene la misma precisión al estimar distintas atribuciones:

* **Largo**: Bien estimado y sin sesgo, con un factor multiplicativo de 0.9 a 1.1.
* **Área**: Subestimado y con sesgo, con un factor multiplicativo de 0.6 a 0.9.
* **Volumen**: Muy subestimado y con sesgo, con un factor multiplicativo de 0.5 a 0.8.

Resulta inadecuado realizar gráficos de datos utilizando áreas o volúmenes si no queda claro la atribución utilizada.

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/Honestidad2.png" width = "500" align="center"/>


Una pseudo-excepción la constituyen los _pie-chart_ o gráficos circulares,
porque el ojo humano distingue bien ángulos y segmentos de círculo,
y porque es posible indicar los porcentajes respectivos.



<img src="https://graphworkflow.com/wp-content/uploads/2019/08/pie.png" width = "500" align="center"/>



### Percepción

No todos los elementos tienen la misma percepción a
nivel del sistema visual. En particular, el color y la
forma son elementos preatentivos: un color distinto o una forma distinta
se reconocen de manera no conciente.


<img src="https://miro.medium.com/v2/resize:fit:1400/1*dcO-I9tiwbFvH2i_oSb6zA.png" alt="" width="600" align="middle"/>

El sistema visual humano puede estimar con precisión siguientes atributos visuales:

1. Posición
2. Largo
3. Pendiente
4. Ángulo
5. Área
6. Volumen
7. Color

### Colormaps

Puesto que la percepción del color tiene muy baja precisión, resulta ***inadecuado*** tratar de representar un valor numérico con colores.
* ¿Qué diferencia numérica existe entre el verde y el rojo?
* ¿Que asociación preexistente posee el color rojo, el amarillo y el verde?
* ¿Con cuánta precisión podemos distinguir valores en una escala de grises?

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/colormap.png" width = "300" align="center"/>




## Python Landscape

Para empezar, [PyViz](https://pyviz.org/) es un sitio web que se dedica a ayudar a los usuarios a decidir dentro de las mejores herramientas de visualización open-source implementadas en Python, dependiendo de sus necesidades y objetivos. Mucho de lo que se menciona en esta sección está en detalle en la página web del proyecto PyViz.

Algunas de las librerías de visualización de Python más conocidas son:

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/data_manipulation/visualization/images/landscape.png" width = "700" align="center"/>


Este esquema es una adaptación de uno presentado en la charla [_The Python Visualization Landscape_](https://us.pycon.org/2017/schedule/presentation/616/) realizada por [Jake VanderPlas](http://vanderplas.com/) en la PyCon 2017.

Cada una de estas librerías fue creada para satisfacer diferentes necesidades, algunas han ganado más adeptos que otras por uno u otro motivo. Tal como avanza la tecnología, estas librerías se actualizan o se crean nuevas, la importancia no recae en ser un experto en una, si no en saber adaptarse a las situaciones, tomar la mejor decicisión y escoger según nuestras necesidades y preferencias. Por ejemplo, `matplotlib` nació como una solución para imitar los gráficos de `MATLAB` (puedes ver la historia completa [aquí](https://matplotlib.org/users/history.html)), manteniendo una sintaxis similar y con ello poder crear gráficos __estáticos__ de muy buen nivel.

Debido al éxito de `matplotlib` en la comunidad, nacen librerías basadas ella. Algunos ejemplos son:

- `seaborn` se basa en `matpĺotlib` pero su nicho corresponde a las visualizaciones estadísticas.
- `ggpy` una suerte de copia a `ggplot2` perteneciente al lenguaje de programación `R`.
- `networkx` visualizaciones de grafos.
- `pandas` no es una librería de visualización propiamente tal, pero utiliza a `matplotplib` como _bakcned_ en los métodos con tal de crear gráficos de manera muy rápida, e.g. `pandas.DataFrame.plot.bar()`

Por otro lado, con tal de crear visualizaciones __interactivas__ aparecen librerías basadas en `javascript`, algunas de las más conocidas en Python son:

- `bokeh` tiene como objetivo proporcionar gráficos versátiles, elegantes e incluso interactivos, teniendo una gran performance con grandes datasets o incluso streaming de datos.
- `plotly` visualizaciones interactivas que en conjunto a `Dash` (de la misma empresa) permite crear aplicaciones webs, similar a `shiny` de `R`.
- `D3.js` a pesar de estar basado en `javascript` se ha ganado un lugar en el corazón de toda la comunidad, debido a la ilimitada cantidad de visualizaciones que son posibles de hacer, por ejemplo, la [malla interactiva](https://mallas.labcomp.cl/) que hizo un estudiante de la UTFSM está hecha en `D3.js`.
