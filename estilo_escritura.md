# Estilo de Escritura del Blog

## 1. Tono y Enfoque

- **Directo y pragmático**: Los artículos van directos al grano, sin introducciones largas ni reflexiones filosóficas extensas.
- **"Notas para mí mismo"**: El tono es personal pero técnico, pensado como un bloc de notas o referencia rápida para el futuro.
- **Enfoque en código**: Muchos artículos empiezan con código directamente si ese es el contenido principal.
- **Evitar frases**: NO empezar con "Nota mental:", "Nota para recordar:", "Otra nota recordatoria:", etc. Solo dive into the content.

## 2. Estructura

### Párrafo introductorio breve (opcional)
- Solo 1-2 líneas para situar el contexto o el problema.
- Algunas veces no hay intro en absoluto (artículos código-first).
- Siempre mantenerlo breve y personal.

### Cuerpo del artículo
- **Código como protagonista**: Bloques de código (bash, python, nginx, SQL, etc.) son centrales y aparecen frecuentemente.
- **Listas con viñetas**: Para resumir características, limitaciones, usos o casos.
- **Negritas**: Para destacar conceptos clave dentro de los párrafos.
- **Encabezados funcionales** (opcional): "El problema", "La solución", "Configuración", "Ejemplo de uso", "¿Cuándo usar?".

### Cierre
- Breve consideración final o resumen (1-2 líneas).
- Incluir "*Fuente original*:" cuando la información se basó en otro artículo o documentación.

## 3. Formato de Código

- Usar bloques de código con el lenguaje apropiado:
  ```python
  # Python
  ```
  ```bash
  # Bash/shell
  ```
  ```sql
  # SQL
  ```
  ```nginx
  # Nginx config
  ```
  ```javascript
  # JavaScript
  ```

- Para código inline, usar ``:code:`nombre` `` (reStructuredText) o `` `nombre` `` (Markdown).

## 4. Enlaces y Referencias

- **Documentación oficial**: Incluir enlace a la documentación cuando sea relevante.
- **Fuente original**: Usar el formato:
  ```
  *Fuente original*: [nombre](url)
  ```
- **Enlaces internos**: linking a otras anotaciones relevantes del blog (versión correcta del idioma).

## 5. Imágenes y Visuales

- Incluir capturas de pantalla cuando ilustren el contenido (herramientas CLI, interfaces).
- Guardar imágenes en `content/images/`.
- Añadir la imagen en el artículo y como `featured_image` en los metadatos para que aparezca en la homepage.


## 6. Anti-patrones a Evitar

❌ **NO hacer**:
- No empezar con "Nota mental:" o "Nota para recordar:"
- No empezar con "Otra nota recordatoria:"

