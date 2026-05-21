# Machine Learning


<img src="https://cdn-icons-png.flaticon.com/512/8637/8637099.png" width="200"  align="center"/>

El **Machine Learning** (aprendizaje automático) es una rama de la inteligencia artificial que desarrolla algoritmos capaces de aprender patrones a partir de datos, sin necesidad de programar explícitamente cada regla. En lugar de escribir instrucciones para cada caso, entrenamos un modelo con ejemplos y esperamos que generalice a nuevas situaciones.


En esta sección trabajamos los tres grandes tipos de problemas: el **aprendizaje supervisado**, donde disponemos de una variable objetivo que queremos predecir; el **aprendizaje no supervisado**, donde buscamos estructura en los datos sin una respuesta definida; y los problemas de **generalización**, donde el foco está en construir modelos que funcionen bien más allá de los datos de entrenamiento. La librería principal es `scikit-learn`, que provee una interfaz uniforme para entrenar, evaluar y comparar modelos. <br>

<img src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/ml/introduccion_ml/images/sklearn.png" width="240"  align="center"/>

<br>

> Construir un modelo es relativamente sencillo; construir uno que sea confiable y útil requiere entender qué está midiendo cada métrica y qué puede salir mal.



**Conceptos clave**

<img alt="Machine Learning" title="Machine Learning" src="https://raw.githubusercontent.com/fralfaro/MAT281_2022/main/docs/lectures/ml/introduccion_ml/images/esquema.png" width = "700">

<br>

| Concepto | Descripción |
|---|---|
| **Aprendizaje supervisado** | El modelo aprende a partir de datos etiquetados, es decir, ejemplos donde se conoce la respuesta correcta. El objetivo es predecir la etiqueta de nuevas observaciones. |
| **Aprendizaje no supervisado** | No existe una variable objetivo. El modelo busca estructura en los datos: agrupaciones, patrones o representaciones compactas. |
| **Variable objetivo (target)** | La variable que queremos predecir. Si es continua, el problema es de regresión; si es categórica, es de clasificación. |
| **Features (características)** | Las variables que usamos como entrada del modelo para predecir la variable objetivo. |
| **Entrenamiento y evaluación** | El modelo se ajusta sobre un conjunto de datos de entrenamiento y se evalúa sobre datos que no vio durante ese proceso. |
| **Overfitting** | El modelo memoriza los datos de entrenamiento pero generaliza mal a datos nuevos. Es uno de los problemas más frecuentes en la práctica. |
| **Métricas de desempeño** | Medidas cuantitativas del rendimiento del modelo: RMSE y R² para regresión; accuracy, precisión, recall y AUC para clasificación. |
| **Scikit-learn** | Librería de referencia para Machine Learning en Python. Provee una API uniforme para preprocesamiento, entrenamiento, evaluación y selección de modelos. |
