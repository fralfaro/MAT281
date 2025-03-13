# Markdown

<img src="https://downloads.marketplace.jetbrains.com/files/18897/166369/icon/pluginIcon.png" width="200" align="center"/>

## Introducción

[Markdown](https://www.markdownguide.org/) es un lenguaje de marcado ligero que facilita el formato de texto de manera sencilla y legible. Fue creado en 2004 por John Gruber y Aaron Swartz. Su principal ventaja es que es fácil de escribir y leer, y se convierte fácilmente a HTML y otros formatos. Es ampliamente utilizado en documentación, blogs, y plataformas como GitHub para archivos README.

## Elementos Básicos de Markdown

### 1. Encabezados

Crea encabezados con el símbolo `#`. Más `#` indican un encabezado de nivel inferior.

#### Ejemplo:
```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Sub-subtítulo (H3)
```

---

### 2. Párrafos

Escribe texto seguido de una línea en blanco para crear un nuevo párrafo.

#### Ejemplo:
```markdown
Este es un párrafo simple.

Este es otro párrafo, separado del anterior por una línea en blanco.
```

---

### 3. Negrita y Cursiva

Destaca el texto usando negrita o cursiva:

- **Negrita:** Usa `**texto**` o `__texto__`.
- *Cursiva:* Usa `*texto*` o `_texto_`.

#### Ejemplo:
```markdown
**Texto en negrita**
*Texto en cursiva*
```

---

### 4. Listas

Crea listas ordenadas y no ordenadas fácilmente.

- **No ordenadas:** Usa `*`, `-`, o `+`.
- **Ordenadas:** Usa números seguidos de un punto.

#### Ejemplo:
```markdown
- Manzanas
- Naranjas
  - Valencia
  - Navel
```

```markdown
1. Primer paso
2. Segundo paso
3. Tercer paso
```

---

### 5. Enlaces

Inserta enlaces con la siguiente sintaxis:

#### Ejemplo:
```markdown
[Visita Google](https://www.google.com)
```

---

### 6. Imágenes

Inserta imágenes de manera similar a los enlaces, pero precede con `!`.

#### Ejemplo:
```markdown
![Logo de Markdown](https://downloads.marketplace.jetbrains.com/files/18897/166369/icon/pluginIcon.png)
```

---

### 7. Citas

Destaca texto con citas utilizando `>` al principio de la línea.

#### Ejemplo:
```markdown
> Esto es una cita importante.
```

---

### 8. Código en Python

Markdown permite resaltar código en línea y en bloques. Es ideal para compartir scripts de Python.

#### Ejemplo de código en línea:

```markdown
El comando `print("Hola, mundo")` se utiliza para mostrar texto en Python.
```

#### Ejemplo de bloque de código:


```python
def saludar(nombre):
    return f"Hola, {nombre}!"

nombre = "John"
print(saludar(nombre))
```


---

### 9. Fórmulas Matemáticas

Incorpora expresiones matemáticas utilizando LaTeX con *MathJax*.

#### Ejemplo de fórmula en línea:
```markdown
La ecuación de Einstein es $E = mc^2$.
```

#### Ejemplo de fórmula en bloque:
```markdown
$$
\int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}
$$
```

---
