### XML（可扩展标记语言）和HTML（超文本标记语言）都是用于描述和组织文档结构的标记语言，但它们有不同的用途和设计重点。

**XML（可扩展标记语言）：**

> XML是一种通用的标记语言，旨在用于表示和传输结构化数据。它的设计目标是将数据从其内容中分离出来，并将其描述为标签、元素和属性的层次结构。XML并不定义特定的标签或元素，而是提供了一种方法来创建自定义的标记以表示特定领域的数据。XML被广泛用于数据交换、配置文件、文档表示和许多其他领域。

XML示例：
```xml
<person>
    <name>John Doe</name>
    <age>30</age>
    <email>john@example.com</email>
</person>
```

**HTML（超文本标记语言）：**

> HTML是一种用于创建网页的标记语言。它具有预定义的标签和元素，用于定义网页的结构、内容和呈现方式。HTML中的标签描述了文档的结构、段落、标题、链接、图像等。浏览器可以解析HTML并将其渲染为可视化的网页。HTML通常与CSS（层叠样式表）一起使用，以控制网页的外观和样式。

HTML示例：
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This is a paragraph of text.</p>
    <a href="https://www.example.com">Visit Example</a>
    <img src="image.jpg" alt="An image">
</body>
</html>
```

**CSS（层叠样式表，Cascading Style Sheets）:**

> CSS是一种用于定义文档（如HTML和XML）外观和样式的标记语言。它与HTML和XML结合使用，以控制网页的布局、字体、颜色、间距、背景等外观方面的属性。通过将样式从文档内容中分离出来，CSS使得在多个页面中应用相同的样式变得更加简便，并提供了更大的灵活性和一致性。

CSS通过选择器（Selectors）和属性-值对（Property-Value Pairs）的规则来定义文档的样式。选择器指定了应用样式的元素，而属性-值对定义了应用于这些元素的具体样式。

以下是一个简单的CSS示例，展示如何使用CSS来设置HTML元素的样式：

```css
/* CSS样式规则 */
p {
    color: blue;        /* 设置文本颜色为蓝色 */
    font-size: 16px;    /* 设置字体大小为16像素 */
    margin: 10px;       /* 设置外边距为10像素 */
}
```

与上述CSS样式规则配合使用的HTML示例：

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Stylish Page</title>
    <link rel="stylesheet"type="text/css"href="styles.css">     <!-- 引入CSS文件 -->
</head>
<body>
    <p>This is a paragraph with styled text.</p>
</body>
</html>
```

在这个示例中，CSS文件（styles.css）中的规则会应用于HTML中的段落（`<p>`）元素，从而使段落文本变为蓝色、字体大小为16像素，并添加外边距为10像素。

总之，CSS是一种用于控制文档外观和样式的标记语言，它与HTML和XML一起使用，通过样式规则来定义元素的呈现方式。