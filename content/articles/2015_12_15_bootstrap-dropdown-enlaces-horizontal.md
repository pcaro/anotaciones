Title: Bootstrap: Dos enlaces en la misma fila en dropdown
Date: 2015-12-15 10:40
Tags: bootstrap, css, dropdown, flexbox, html
Lang: es
Category: Frontend
Slug: bootstrap-dropdown-enlaces-horizontal
Summary: Técnica CSS para colocar dos enlaces en la misma fila horizontal dentro de un menú dropdown de Bootstrap usando flexbox

A veces necesitas **colocar dos enlaces lado a lado** en la misma fila dentro de un dropdown de Bootstrap. La solución combina HTML estructurado y CSS con flexbox.

## El problema

Por defecto, Bootstrap renderiza los enlaces de dropdown como elementos de bloque, ocupando toda la fila:

```html
<!-- Comportamiento por defecto: cada enlace en su fila -->
<li><a href="#">Enlace 1</a></li>
<li><a href="#">Enlace 2</a></li>
```

## La solución

### HTML estructurado
```html
<li class="hz">
    <a href="#">En la tercera fila</a>
    <a href="#">También en la tercera fila</a>
</li>
```

**Clave**: Múltiples enlaces `<a>` dentro del mismo `<li>` con clase personalizada.

### CSS con flexbox
```css
.open > ul > li.hz {
    display: inline-flex !important;
}
```

**Clave**: `inline-flex` override el display block por defecto de Bootstrap.

## Implementación completa

```html
<div class="dropdown">
    <button class="btn btn-default dropdown-toggle" data-toggle="dropdown">
        Menú <span class="caret"></span>
    </button>
    <ul class="dropdown-menu">
        <li><a href="#">Primera opción</a></li>
        <li><a href="#">Segunda opción</a></li>
        <li class="hz">
            <a href="#">Opción A</a>
            <a href="#">Opción B</a>
        </li>
        <li><a href="#">Última opción</a></li>
    </ul>
</div>
```

## Consideraciones adicionales

### Espaciado entre enlaces
```css
.hz a {
    margin-right: 10px;
}
.hz a:last-child {
    margin-right: 0;
}
```

### Responsive
```css
@media (max-width: 768px) {
    .open > ul > li.hz {
        display: block !important;
    }
}
```

## ¿Cuándo usarlo?

- **Acciones relacionadas** (Editar/Eliminar)
- **Opciones binarias** (Sí/No, Activar/Desactivar)
- **Navegación compacta** en espacios reducidos

Esta técnica mantiene la **semántica HTML correcta** mientras aprovecha la flexibilidad de flexbox para layouts más complejos.

*Fuente original*: [Stack Overflow](http://stackoverflow.com/questions/15844533/bootstrap-dropdown-menu-two-links-on-same-horizontal-row)