Title: Galen Framework: Testing automatizado para diseño responsive
Date: 2015-11-13 18:20
Tags: galen, testing, responsive, layout, selenium
Lang: es
Category: Testing
Slug: galen-framework-testing-responsive
Summary: Galen Framework simplifica el testing automatizado de layouts responsivos verificando la posición y apariencia de elementos across different dispositivos

**Galen Framework** es una herramienta de testing automatizado diseñada específicamente para **probar diseños web responsivos**. Su propósito principal es simplificar las pruebas de layout verificando el posicionamiento y apariencia de elementos web en diferentes tamaños de dispositivo.

## Características principales

### Testing de layout inteligente
> "Layout testing seemed always a complex task. Galen Framework offers a simple solution: test location of objects relatively to each other on page."

### Soporte responsive completo
- **Redimensionado automático** del navegador a tamaños definidos
- **Testing cross-device** en múltiples resoluciones
- **Verificación de reglas** específicas por pantalla

### Sintaxis humana y flexible
```galen
header
    width: 100% of screen/width
    height: 50px
    
sidebar
    below: header
    width: 200px
    left-of: content 10px
```

### Capacidades avanzadas
- **Compatibilidad con Selenium Grid**
- **Testing visual** con comparación de imágenes
- **Verificación de esquemas de color**
- **Reportes HTML detallados** con errores destacados

## Soporte multi-lenguaje

Tests escritos en:
- **JavaScript**
- **Java**
- Otros lenguajes con parametrización integrada

## ¿Por qué Galen?

Antes de Galen, el testing de layouts era **complejo y propenso a errores**. Galen introduce:

1. **Sintaxis declarativa** fácil de leer
2. **Verificación relacional** entre elementos
3. **Testing responsive nativo**
4. **Reportes visuales** comprensibles

## Caso de uso típico

```javascript
// Abrir navegador, redimensionar y probar
test("Homepage on mobile", function() {
    var driver = createDriver();
    driver.get("http://example.com");
    driver.manage().window().setSize(375, 667);
    checkLayout(driver, "homepage-mobile.spec");
});
```

Galen democratiza el testing de diseño responsive, haciendo que las **pruebas de layout sean tan fáciles como las pruebas funcionales**.

*Framework open source*: [Galen Framework](http://galenframework.com/) (Apache License 2.0)