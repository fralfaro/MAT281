# DIPLOMADO EN IA PARA EDUCACIÓN  
### MÓDULO 1: METODOLOGÍAS PARA INTEGRACIÓN DE MACHINE LEARNING EN EDUCACIÓN  

## TAREA 2: Arquitectura  

**Docente:** Leonardo Hernández Vera  
**Tutora:**  
**Alumno:**  
**Institución elegida:** Pontificia Universidad Católica de Valparaíso (PUCV)  

---

## 1. EJEMPLOS DE VALORES QUE TOMA EL KPI  

### KPI #1: Tasa de Retención Estudiantil  

**Fórmula:**  
$$
\text{Tasa de retención} = \frac{\text{Número de estudiantes que continúan}}{\text{Total de estudiantes inscritos}} \times 100
$$

**Objetivo Estratégico Asociado:** Excelencia Académica  

**Explicación y Análisis:**  
Este KPI mide el porcentaje de estudiantes que permanecen en la universidad en distintos períodos. Una alta tasa de retención indica efectividad en la experiencia estudiantil y apoyo académico.  

| Año   | Valor (%) |
|-------|----------|
| 2022  | 85       |
| 2023  | 88       |
| 2024  | 90       |
| **Meta 2025** | 92 |

---

### KPI #2: Cantidad de Cursos con Tecnología Integrada  

**Fórmula:**  
$$
\text{Porcentaje de cursos con tecnología} = \frac{\text{Cursos con integración tecnológica}}{\text{Total de cursos}} \times 100
$$

**Objetivo Estratégico Asociado:** Integración de Tecnologías en el Aprendizaje  

**Explicación y Análisis:**  
Este KPI mide el porcentaje de cursos que han adoptado tecnologías educativas para mejorar el aprendizaje, como aulas virtuales o herramientas interactivas.  

| Año   | Valor (%) |
|-------|----------|
| 2022  | 30       |
| 2023  | 50       |
| 2024  | 75       |
| **Meta 2025** | 85 |

---

### KPI #3: Nivel de Satisfacción Estudiantil en Innovación Pedagógica  

**Fórmula:**  
$$
\text{Puntaje promedio de encuestas de satisfacción (1-10)}
$$

**Objetivo Estratégico Asociado:** Mejora Continua de Programas Académicos  

**Explicación y Análisis:**  
Mide la percepción de los estudiantes sobre la efectividad de la innovación pedagógica en la universidad.  

| Año   | Valor (Escala 1-10) |
|-------|----------------------|
| 2022  | 7.5                  |
| 2023  | 8.2                  |
| 2024  | 9.0                  |
| **Meta 2025** | 9.5          |

---

## 2. ARQUITECTURA  

### **Arquitectura basada en el ciclo de vida de los datos**  

- **Fuentes de Datos:**  
  - Sistemas OLTP de la universidad  
  - Plataformas LMS como Blackboard o Moodle  

- **Cargas de Datos:**  
  - **Batch:** Datos históricos de cursos y retención estudiantil  
  - **Tiempo real:** Encuestas y actividad en plataformas LMS  

- **Servicios en la Nube:**  
  - **Almacenamiento:** Data Lake (Azure Data Lake, Google Cloud Storage, AWS S3)  
  - **Procesamiento:** Azure Synapse, BigQuery, Redshift  
  - **Visualización:** Power BI, Google Looker, Tableau  
  - **Machine Learning:** Azure ML, Vertex AI, SageMaker  

- **Procesamiento:**  
  - ETL/ELT para limpieza y consolidación de datos  

- **Uso y Visualización:**  
  - Dashboards en Power BI/Looker para análisis  

- **Aplicación de ML:**  
  - Modelos predictivos para estimar retención estudiantil  
  - Análisis de sentimiento en comentarios de encuestas  

---

## 3. REFLEXIÓN Y CONCLUSIÓN  

Esta arquitectura permite analizar la evolución de los KPIs estratégicos de la **PUCV**, facilitando la toma de decisiones basada en datos.  

La combinación de almacenamiento **on-premise** y en la **nube** proporciona **flexibilidad y escalabilidad**.  

Además, la integración de **Machine Learning** ayuda a predecir tendencias y optimizar la experiencia estudiantil, alineándose con la visión de **excelencia e innovación** de la universidad.  
