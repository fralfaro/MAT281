# Proyecto Final

## Introducción

El propósito de este proyecto es que los estudiantes enfrenten un problema real de clasificación binaria en ciencia de datos, abarcando todas las etapas fundamentales de un flujo de trabajo de Machine Learning. El desafío se basa en identificar qué clientes de una empresa de telecomunicaciones están en riesgo de cancelar su contrato (churn), utilizando datos demográficos y de comportamiento.

## Descripción del Proyecto

En el competitivo mundo de las telecomunicaciones, **retener clientes** es tan importante como atraer nuevos. Utilizando un conjunto de datos proporcionado por una empresa ficticia de telecomunicaciones, los estudiantes deberán construir un modelo predictivo que permita anticipar qué clientes podrían dejar la empresa, y generar recomendaciones basadas en los patrones detectados.

Este proyecto no solo mide la capacidad técnica de implementar modelos, sino también la habilidad de explorar, interpretar y comunicar hallazgos relevantes para la toma de decisiones comerciales.

> Dataset oficial: [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Evaluación

El proyecto final consta de dos componentes:

* **Parte Técnica**: Desarrollo completo del proyecto en Jupyter Notebook.
* **Presentación de Resultados**: Exposición oral de 10 a 20 minutos basada en visualizaciones y conclusiones.



### Parte Técnica

Debe incluir las siguientes secciones:

1. **Definición del problema**

     * Justificación del problema de churn en contextos reales.
     * Objetivo del análisis y definición de la variable objetivo (`Churn`).

2. **Análisis exploratorio**

     * Estadísticas descriptivas generales.
     * Distribuciones, correlaciones, y relaciones entre variables clave.

3. **Visualización descriptiva**

     * Gráficos de barras, violín, dispersión, heatmaps, etc.
     * Comparaciones entre clientes que se mantienen y los que abandonan.

4. **Preprocesamiento**

     * Tratamiento de valores nulos, codificación de variables categóricas, transformación de datos.
     * Detección de desbalanceo en la variable objetivo y posible uso de técnicas como `SMOTE`.

5. **Selección y comparación de modelos**

     * Comparación de al menos **cuatro modelos supervisados**.
     * Al menos **tres de ellos deben incorporar ajuste de hiperparámetros** (ej. grid search o random search).
     * Modelos sugeridos: `Logistic Regression`, `Random Forest`, `XGBoost`, `SVM`, `KNN`.

6. **Evaluación de modelos**

     * Utilizar métricas como Accuracy, F1-score, Precision, Recall, ROC-AUC.
     * Curvas ROC y matriz de confusión.

7. **Interpretación del modelo**

     * Importancia de variables (feature importance) o uso de técnicas interpretables (`SHAP`, `eli5`).

8. **Conclusiones y recomendaciones**

     * Principales hallazgos y patrones relevantes.
     * Recomendaciones para áreas comerciales y de retención de clientes.

> **Nota**: Se valorará especialmente la incorporación de redes neuronales o técnicas avanzadas si son correctamente justificadas.



### Presentación de Resultados

* Duración: 15–20 minutos.
* Utilizar diapositivas con [BEAMER](https://www.dropbox.com/s/ol38qwzacgwzud7/Beamer.rar). Se deja el siguiente [tutorial](https://www.youtube.com/watch?v=rx7wwtmFlD8&t=792s&ab_channel=Dr.TreforBazett) a modo de ejemplo.
* La presentación debe alojarse en su **Portafolio Personal** del curso (`.pdf`).


## Información Importante

* **Plazo**: 28 de Noviembre de 2025.
* Esto corresponde a un desafío de Kaggle ([link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)).
* Como inspiración, pueden revisar notebooks de Kaggle en la sección [Kaggle Code](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/code).
