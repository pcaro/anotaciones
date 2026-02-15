Title: Bootstrap: Two Links in the Same Row in Dropdown
Date: 2015-12-15 10:40
Tags: bootstrap, css, dropdown, flexbox, html
Lang: en
Category: Frontend
Slug: bootstrap-dropdown-enlaces-horizontal
Summary: CSS technique to place two links on the same horizontal row within a Bootstrap dropdown menu using flexbox

Sometimes you need to **place two links side by side** in the same row within a Bootstrap dropdown. The solution combines structured HTML and CSS with flexbox.

## The Problem

By default, Bootstrap renders dropdown links as block elements, occupying the entire row:

```html
<!-- Default behavior: each link on its row -->
<li><a href="#">Link 1</a></li>
<li><a href="#">Link 2</a></li>
```

## The Solution

### Structured HTML
```html
<li class="hz">
    <a href="#">On the third row</a>
    <a href="#">Also on the third row</a>
</li>
```

**Key**: Multiple `<a>` links within the same `<li>` with a custom class.

### CSS with Flexbox
```css
.open > ul > li.hz {
    display: inline-flex !important;
}
```

**Key**: `inline-flex` overrides Bootstrap's default block display.

## Complete Implementation

```html
<div class="dropdown">
    <button class="btn btn-default dropdown-toggle" data-toggle="dropdown">
        Menu <span class="caret"></span>
    </button>
    <ul class="dropdown-menu">
        <li><a href="#">First option</a></li>
        <li><a href="#">Second option</a></li>
        <li class="hz">
            <a href="#">Option A</a>
            <a href="#">Option B</a>
        </li>
        <li><a href="#">Last option</a></li>
    </ul>
</div>
```

## Additional Considerations

### Spacing between links
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

## When to use it?

- **Related actions** (Edit/Delete)
- **Binary options** (Yes/No, Enable/Disable)
- **Compact navigation** in tight spaces

This technique maintains **correct HTML semantics** while leveraging the flexibility of flexbox for more complex layouts.

*Original source*: [Stack Overflow](http://stackoverflow.com/questions/15844533/bootstrap-dropdown-menu-two-links-on-same-horizontal-row)
