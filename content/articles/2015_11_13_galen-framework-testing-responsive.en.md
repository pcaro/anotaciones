Title: Galen Framework: Automated Testing for Responsive Design
Date: 2015-11-13 18:20
Tags: galen, testing, responsive, layout, selenium
Lang: en
Category: Testing
Slug: galen-framework-testing-responsive
Summary: Galen Framework simplifies automated testing of responsive layouts by verifying the position and appearance of elements across different devices

**Galen Framework** is an automated testing tool designed specifically to **test responsive web designs**. Its main purpose is to simplify layout testing by verifying the positioning and appearance of web elements on different device sizes.

## Key Features

### Intelligent Layout Testing
> "Layout testing seemed always a complex task. Galen Framework offers a simple solution: test location of objects relatively to each other on page."

### Full Responsive Support
- **Automatic resizing** of the browser to defined sizes
- **Cross-device testing** in multiple resolutions
- **Rule verification** specific per screen

### Human and Flexible Syntax
```galen
header
    width: 100% of screen/width
    height: 50px
    
sidebar
    below: header
    width: 200px
    left-of: content 10px
```

### Advanced Capabilities
- **Selenium Grid compatibility**
- **Visual testing** with image comparison
- **Color scheme verification**
- **Detailed HTML reports** with highlighted errors

## Multi-Language Support

Tests written in:
- **JavaScript**
- **Java**
- Other languages with integrated parameterization

## Why Galen?

Before Galen, layout testing was **complex and error-prone**. Galen introduces:

1. **Declarative syntax** easy to read
2. **Relational verification** between elements
3. **Native responsive testing**
4. **Visual reports** understandable

## Typical Use Case

```javascript
// Open browser, resize and test
test("Homepage on mobile", function() {
    var driver = createDriver();
    driver.get("http://example.com");
    driver.manage().window().setSize(375, 667);
    checkLayout(driver, "homepage-mobile.spec");
});
```

Galen democratizes responsive design testing, making **layout testing as easy as functional testing**.

*Open source framework*: [Galen Framework](http://galenframework.com/) (Apache License 2.0)
