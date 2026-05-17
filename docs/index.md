---
hide:
  - toc
---


# Bienvenidos al Curso!

## Descripción

Este curso entrega herramientas prácticas para el análisis de datos aplicado a negocios. El foco está en manipular, visualizar y modelar datos de forma reproducible, con énfasis en la toma de decisiones basada en evidencia.

Durante las sesiones se trabaja con las principales herramientas del ecosistema Python para ciencia de datos: **NumPy**, **Pandas**, **Matplotlib/Seaborn** y **Scikit-learn**, complementadas con **Google Colab**, **GitHub** e **Inteligencia Artificial** como apoyo al aprendizaje.



<div class="ai-tools-grid">

  <div class="notebooklm-card">
    <div class="card-content">
      <div class="notebooklm-header">
        <svg width="28" height="28" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M24 4C13 4 4 13 4 24s9 20 20 20 20-9 20-20S35 4 24 4z" fill="#1a73e8" opacity="0.15"/>
          <path d="M8 24c0-8.8 7.2-16 16-16" stroke="#1a73e8" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M13 24c0-6.1 4.9-11 11-11" stroke="#1a73e8" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M18 24c0-3.3 2.7-6 6-6" stroke="#1a73e8" stroke-width="3.5" stroke-linecap="round"/>
        </svg>
        <div>
          <span class="label-text">Recursos disponibles en</span>
          <strong class="brand-notebook">NotebookLM</strong>
        </div>
      </div>
      <p class="card-desc">
        Accede a los materiales del curso con inteligencia artificial. Puedes hacer preguntas, obtener resúmenes y profundizar los contenidos de Analítica para Negocios —desde Pandas hasta Machine Learning— a tu propio ritmo.
      </p>
    </div>
    <div class="card-footer">
      <div class="notebooklm-links">
        <a href="https://notebooklm.google.com/notebook/be0f2702-fb1c-439b-bbd7-ba9b59586aaa" target="_blank" class="notebooklm-btn">
          🔨 NotebookLLM
        </a>
      </div>
    </div>
  </div>

  <div class="github-card">
    <div class="card-content">
      <div class="github-header">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
        </svg>
        <div>
          <span class="label-text">Entregables del curso en</span>
          <strong class="brand-github">GitHub</strong>
        </div>
      </div>
      <p class="card-desc">
        Accede al repositorio del curso con todo el material, notebooks y recursos. Crea tu cuenta en GitHub para clonar y trabajar con los contenidos.
      </p>
      <div class="github-repo">
        <code>fralfaro/ICS40125-entregables</code>
      </div>
    </div>
    <div class="card-footer">
      <div class="github-links">
        <a href="https://github.com/signup" target="_blank" class="github-btn github-btn-outline">Crear cuenta</a>
        <a href="https://github.com/fralfaro/ICS40125-entregables" target="_blank" class="github-btn github-btn-green">Ver repositorio →</a>
      </div>
    </div>
  </div>

</div>

<style>
/* --- Layout General --- */
.ai-tools-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin: 1.5rem 0;
}

@media (max-width: 768px) {
  .ai-tools-grid { grid-template-columns: 1fr; }
}

/* --- Estructura de Tarjetas (Alineación) --- */
.notebooklm-card, .github-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1.5rem;
  border-radius: 12px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  height: 100%; /* Asegura que ambas tengan el mismo alto */
}

.card-content { flex-grow: 1; }
.card-footer { margin-top: 1.25rem; }

/* --- NotebookLM Style --- */
.notebooklm-card {
  background: linear-gradient(135deg, #f0f7ff 0%, #e8f0fe 100%);
  border: 1px solid #c5d8f7;
  border-left: 5px solid #1a73e8;
}
.brand-notebook { color: #1a73e8; font-size: 1.1rem; display: block; }

/* --- GitHub Style --- */
.github-card {
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-left: 5px solid #24292f;
}
.brand-github { color: #24292f; font-size: 1.1rem; display: block; }

/* --- Elementos Comunes --- */
.notebooklm-header, .github-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 1rem;
}
.label-text {
  display: block;
  font-size: 0.75rem;
  color: #5f6368;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.card-desc {
  font-size: 0.92rem;
  color: #3c4043;
  line-height: 1.5;
  margin: 0;
}

/* --- Repositorio Box --- */
.github-repo {
  background: white;
  border: 1px solid #d0d7de;
  border-radius: 6px;
  padding: 6px 10px;
  margin-top: 10px;
  display: inline-block;
}
.github-repo code { font-size: 0.85rem;  }

/* --- Botones --- */
.notebooklm-links, .github-links { display: flex; gap: 8px; flex-wrap: wrap; }

.notebooklm-btn {
  background: #1a73e8;
  color: white !important;
  padding: 0.6rem 1rem;
  border-radius: 8px;
  text-decoration: none !important;
  font-size: 0.85rem;
  font-weight: 500;
  transition: 0.2s;
}
.notebooklm-btn:hover { background: #1558b0; }

.github-btn {
  padding: 0.6rem 1rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  text-decoration: none !important;
  transition: 0.2s;
}
.github-btn-outline { background: white; color: #24292f !important; border: 1px solid #d0d7de; }
.github-btn-green { background: #2da44e; color: white !important; }
.github-btn:hover { opacity: 0.85; }
</style>






## Contenidos del Curso

::cards:: cols=3

- title: Toolkit del Curso
  content: Linux, Git/GitHub, Python
  image: images/icons/tools.png
  url: lectures/toolkit/bt_intro

- title: Manipulación de Datos
  content: NumPy, Pandas, EDA
  image: images/icons/data.png
  url: lectures/data_manipulation/data_intro

- title: Visualización de Datos
  content: Matplotlib, Seaborn
  image: images/icons/vis.png
  url: lectures/visualization/vis_intro




::/cards::


::cards:: cols=3

- title: Inferencia Estadística
  content: test hipótesis, regresión lineal
  image: images/icons/inf.png
  url: lectures/inference/a_inferencia

- title: Machine Learning
  content: Regresión, Clasificación, Clustering
  image: images/icons/ml.png
  url: lectures/machine_learning/01_intro

::/cards::

## Evaluaciones del Curso

::cards:: cols=3

- title: Laboratorios
  content: Labs del curso
  image: images/icons/lab.png
  url: labs/lab_01

- title: Proyectos
  content: Proyectos del curso
  image: images/icons/hw.png
  url: projects/project_01.ipynb



::/cards::
