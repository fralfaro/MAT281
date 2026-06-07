# Proyecto Final

## Introducción

El proyecto final es la **instancia integradora** del curso: aquí pondrás en
práctica, de forma articulada, todo lo aprendido en los **laboratorios** y
**tareas** —manipulación de datos con `pandas`, visualización y, sobre todo,
**Machine Learning**— para resolver un problema real de principio a fin.

A diferencia de las tareas, donde cada habilidad se evaluó por separado, el
proyecto exige **conectar todas las etapas** de un flujo de ciencia de datos en un
producto coherente y bien comunicado. El foco está puesto en el **modelamiento
predictivo (Machine Learning)**: la calidad del modelado, su evaluación rigurosa y
la interpretación de los resultados son el corazón de la evaluación.

> **Nota:** La *inferencia estadística* (pruebas de hipótesis, intervalos de
> confianza) se trabajó en la **Tarea 2**. En el proyecto puedes apoyarte en ella
> para justificar decisiones del análisis exploratorio, pero el énfasis debe estar
> en el **aprendizaje automático**.

> 🖼️ **Sugerencia de imagen — Pipeline de ML:** busca *"machine learning workflow
> pipeline diagram"* y pégala aquí para ilustrar el flujo completo del proyecto
> (`![Pipeline de ML](images/ml_pipeline.png)`).

## Descripción del Problema

En el competitivo mundo de las telecomunicaciones, **retener clientes** es tan
importante como atraer nuevos: adquirir un cliente nuevo puede costar varias veces
más que retener uno existente. Utilizando datos de una empresa de
telecomunicaciones, deberás construir un sistema predictivo que anticipe qué
clientes están en riesgo de cancelar su contrato (**churn**) y traducir esos
hallazgos en **recomendaciones de negocio**.

El problema es de **clasificación binaria**: para cada cliente, predecir si se
fugará (`Churn = Yes`) o permanecerá (`Churn = No`). Es un caso clásico y muy
demandado en la industria, lo que lo hace ideal para tu portafolio profesional.

> **Dataset oficial:** [Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
> (≈ 7.000 clientes, 21 variables: datos demográficos, servicios contratados,
> tipo de contrato, cargos mensuales y totales, etc.).
>
> *(Puedes proponer un dataset alternativo de clasificación o regresión de
> complejidad equivalente, previa autorización del equipo docente.)*

> 🖼️ **Sugerencia de imagen — Churn:** busca *"customer churn retention concept"*
> y pégala aquí para contextualizar el problema de negocio
> (`![Churn de clientes](images/churn.png)`).

## Objetivos

1. Aplicar un **flujo completo de Machine Learning**, desde el dato crudo hasta un
   modelo evaluado e interpretado.
2. Integrar las competencias de **todo el curso**: manipulación de datos,
   visualización efectiva y modelamiento predictivo.
3. Comparar y **optimizar** múltiples modelos de forma metodológicamente correcta,
   evitando fugas de información (*data leakage*) y sobreajuste.
4. **Interpretar** el modelo y traducir los resultados en recomendaciones de
   negocio accionables.
5. **Comunicar** el trabajo de forma profesional en un informe escrito y una
   presentación.

---

## Etapas del Proyecto (Parte Técnica)

El desarrollo técnico se entrega como un **Jupyter Notebook** ordenado, ejecutable
de inicio a fin (`Restart Kernel and Run All Cells`) y debidamente comentado. A
continuación se detalla **qué se espera en cada etapa** y algunas preguntas guía.

### 1. Definición del problema
Explica el problema de *churn* y su impacto económico. Define con claridad la
variable objetivo (`Churn`) y la(s) **métrica(s) de éxito** alineadas al negocio.

* *Pregunta clave:* ¿qué error es más costoso para la empresa, un **falso
  negativo** (no detectar a un cliente que se fuga) o un **falso positivo** (gastar
  en retener a alguien que igual se quedaba)? Esto determinará si priorizas
  **recall**, **precision** u otra métrica.

### 2. Análisis exploratorio (EDA)
Describe el dataset: dimensiones, tipos de variables, calidad de datos. Estudia las
distribuciones y las relaciones con la variable objetivo.

* Tasa global de *churn* y cómo varía por segmento (tipo de contrato, método de
  pago, antigüedad, servicios contratados).
* Detecta y documenta problemas de datos (p. ej. `TotalCharges` viene como texto y
  tiene espacios en blanco que hay que convertir/tratar).

> 🖼️ **Sugerencia de imagen — EDA:** busca *"exploratory data analysis dashboard
> seaborn"* y pégala aquí (`![EDA](images/eda.png)`).

### 3. Visualización descriptiva
Acompaña el EDA con gráficos pertinentes (barras, violín, dispersión, *heatmaps*).
**Cada gráfico debe incluir una lectura/interpretación**, no solo el código.

### 4. Preprocesamiento e ingeniería de características
* Tratamiento de nulos y codificación de categóricas (`OneHotEncoder` /
  `get_dummies`).
* Escalamiento/normalización cuando el modelo lo requiera.
* **Ingeniería de características** justificada (p. ej. agrupar antigüedad en
  tramos, contar número de servicios contratados).
* Maneja el **desbalance** de la clase (≈ 27% de *churn*): `class_weight`,
  *resampling* o `SMOTE`.
* **Evita el *data leakage*:** ajusta todo el preprocesamiento **solo con el
  conjunto de entrenamiento**, idealmente con un `Pipeline` de scikit-learn.

> 🖼️ **Sugerencia de imagen — Data leakage / Pipeline:** busca *"scikit-learn
> pipeline ColumnTransformer diagram"* y pégala aquí
> (`![Pipeline](images/pipeline.png)`).

### 5. Selección y comparación de modelos
* Compara **al menos cuatro modelos supervisados**.
* **Al menos tres** deben incorporar **ajuste de hiperparámetros**
  (`GridSearchCV` / `RandomizedSearchCV`).
* Usa **validación cruzada** para una estimación robusta y comparable.
* Modelos sugeridos: `Logistic Regression`, `Random Forest`, `Gradient Boosting` /
  `XGBoost`, `SVM`, `KNN`.
* Presenta una **tabla comparativa** de modelos vs métricas.

### 6. Evaluación de modelos
* Métricas adecuadas al desbalance: **Accuracy, Precision, Recall, F1-score,
  ROC-AUC**.
* **Curva ROC** y **matriz de confusión** del modelo final.
* Discute el **umbral de decisión** y su impacto en el negocio (mover el umbral
  cambia el equilibrio precision/recall).

> 🖼️ **Sugerencia de imagen — Evaluación:** busca *"confusion matrix and ROC curve
> explained"* y pégala aquí (`![Matriz de confusión y ROC](images/roc_cm.png)`).

### 7. Interpretación del modelo
Abre la "caja negra": ¿qué variables explican mejor el *churn*?

* Importancia de variables (*feature importance*, coeficientes) o técnicas
  interpretables como `SHAP` o `permutation_importance`.

> 🖼️ **Sugerencia de imagen — Interpretabilidad:** busca *"SHAP summary plot
> feature importance"* y pégala aquí (`![SHAP](images/shap.png)`).

### 8. Conclusiones y recomendaciones
* Principales hallazgos y patrones relevantes.
* **Recomendaciones accionables** para las áreas comercial y de retención
  (p. ej. "ofrecer contratos anuales a clientes mensuales con alta probabilidad de
  fuga").
* Limitaciones del análisis y posibles mejoras futuras.

> **Se valorará especialmente** la incorporación —correctamente justificada— de
> técnicas avanzadas: *ensembles*, redes neuronales, o aprendizaje **no
> supervisado** (p. ej. **segmentación de clientes** con *clustering* + PCA como
> análisis complementario).

---

## Ejemplos y recursos en Kaggle

Antes de empezar, **estudia cómo otros han abordado este mismo dataset**. En la
pestaña **Code** del dataset encontrarás cientos de notebooks públicos:

* 🔗 **Notebooks del dataset:** [Telco Churn — Code](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/code)
  (filtra por *"Most Votes"* para ver los mejores ejemplos).
* 🔗 **Discusión del dataset:** [Telco Churn — Discussion](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/discussion)

Qué observar en esos notebooks de referencia:

1. Cómo limpian `TotalCharges` y codifican las variables categóricas.
2. Qué gráficos usan para mostrar la relación de cada variable con el *churn*.
3. Cómo manejan el **desbalance** de clases y qué métricas reportan
   (ojo: muchos reportan solo *accuracy*, lo cual es **engañoso** con clases
   desbalanceadas → tú debes ir más allá).
4. Cómo estructuran la comparación de modelos y el *tuning* de hiperparámetros.

> **Importante:** puedes inspirarte en estos ejemplos, pero tu trabajo debe ser
> **original**. Copiar un notebook de Kaggle será evaluado como plagio.

> 🖼️ **Sugerencia de imagen — Kaggle:** busca *"kaggle notebook example data
> science"* y pégala aquí (`![Ejemplo Kaggle](images/kaggle.png)`).

---

## Entregables

La entrega del proyecto consta de **tres componentes obligatorios**:

| # | Entregable | Formato | Descripción |
|---|------------|---------|-------------|
| 1 | **Notebook** | `.ipynb` | Desarrollo técnico completo, ejecutable de inicio a fin y reproducible. |
| 2 | **Informe** | **PDF generado con LaTeX** | Documento narrativo que reporta el trabajo. |
| 3 | **Presentación** | **PDF generado con LaTeX (Beamer)** | Diapositivas para la exposición oral. |

### 1. Notebook (`.ipynb`)
* Contiene todas las etapas descritas arriba, con código limpio y comentado.
* **Reproducible:** al ejecutar `Kernel → Restart Kernel and Run All Cells` debe
  correr sin errores. Incluye junto al notebook todos los archivos necesarios
  (datos, scripts).

### 2. Informe en PDF (LaTeX)
Documento escrito (sugerido **8–15 páginas**), compilado con **LaTeX**, con al
menos:

* Portada (título, integrantes, rol USM, fecha).
* Introducción y definición del problema.
* Metodología (datos, preprocesamiento, modelos y validación).
* Resultados (tablas y figuras de métricas y comparaciones).
* Discusión, conclusiones y recomendaciones.
* Referencias.

> Puedes redactarlo en [Overleaf](https://www.overleaf.com/). El informe **no es**
> el notebook exportado: es un documento que comunica el trabajo a una audiencia
> técnica.

### 3. Presentación en PDF (LaTeX / Beamer)
* Diapositivas en **PDF**, elaboradas con **LaTeX/[Beamer](https://www.overleaf.com/learn/latex/Beamer)**
  ([tutorial de ejemplo](https://www.youtube.com/watch?v=rx7wwtmFlD8)).
* Exposición oral de **15–20 minutos** centrada en visualizaciones, resultados y
  conclusiones (evita llenar las láminas de código).
* La presentación debe alojarse, además, en tu **Portafolio Personal** del curso.

> 🖼️ **Sugerencia de imagen — Beamer:** busca *"LaTeX Beamer presentation example
> slides"* y pégala aquí (`![Presentación Beamer](images/beamer.png)`).

---

## Rúbrica de Evaluación (referencial)

| Componente | Aspecto evaluado | Ponderación |
|------------|------------------|:-----------:|
| Notebook | EDA y visualización | 15% |
| Notebook | Preprocesamiento e ingeniería de características | 15% |
| Notebook | Modelamiento, *tuning* y validación | 25% |
| Notebook | Evaluación e interpretación de modelos | 15% |
| Informe (PDF/LaTeX) | Claridad, estructura y rigor | 15% |
| Presentación (PDF/LaTeX) | Comunicación oral y visual | 15% |

> La **reproducibilidad** del notebook es un requisito: un notebook que no ejecuta
> de principio a fin será penalizado independientemente de su contenido.

## Información Importante

* **Modalidad:** individual o en grupos de hasta 2 personas (según indique el
  equipo docente).
* **Plazo de entrega:** _por definir por el equipo docente_ (fin del semestre).
* El problema corresponde a un desafío público de Kaggle
  ([link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)).
