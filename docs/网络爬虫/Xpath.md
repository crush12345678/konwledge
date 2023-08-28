## 1.Xpath

XPath（XML Path Language）是一种用于在XML和HTML文档中进行导航和定位的查询语言。它广泛应用于Web爬虫、数据抽取、XML处理以及各种语境中。以下是XPath的完整知识点概述：

* **Xpath**

> 1.解析本地文件【etree.parse()】：
>
> ​	html_tree=etree.parse('xx.html')
>
> 2.解析服务器响应文件【etree.HTML()】
>
> ​	html_tree = etree.HTML(response.read().decode("utf-8"))
>
> 3.用html_tree.xpath(删选条件)进行删选
>
> 4.Xpath利用规则查找的返回值是列表

1. **节点（Nodes）**：
   - 元素节点：XML或HTML中的标签。
   - 属性节点：元素的属性。
   - 文本节点：元素内的文本内容。
   - 注释节点：XML或HTML中的注释。
   - 命名空间节点：元素的命名空间。

2. **路径表达式（Path Expressions）**：
   - 绝对路径：从根节点开始的路径。
   - 相对路径：相对于当前节点的路径。
   - `//`：匹配任何位置的节点。
   - `.`：表示当前节点。
   - `..`：表示当前节点的父节点。

3. **选择节点**：
   - `nodename`：选择具有指定名称的元素节点。
   - `*`：选择所有子元素。
   - `@attribute`：选择指定属性名的属性节点。
   - `text()`：选择当前元素的文本内容。
   - `node()`：选择当前元素的所有子节点。

4. **谓语（Predicates）**：
   - 在方括号内添加条件来过滤节点。
   - `[]` 中可以使用运算符、函数、逻辑操作等。

5. **运算符**：
   - 比较运算符：`=`, `!=`, `<`, `>`, `<=`, `>=`
   - 逻辑运算符：`and`, `or`, `not`

6. **轴（Axes）**：
   - 定义相对于当前节点的节点集合。
   - 常用轴：`ancestor`, `descendant`, `parent`, `child`, `following`, `preceding`.

7. **函数**：
   
   - `name()`: 获取节点名称。
   - `text()`: 获取节点文本内容。
   - `count()`: 计算节点数量。
   - `concat()`: 合并字符串。
- `substring()`: 提取子字符串。
  
8. **示例用法**：

   - 定位元素：`//div`

   - 定位具有特定属性的元素：`//a[@href]`

   - 使用索引定位：`(//a)[1]`

   - 选择父节点：`../`

   - 选择属性值：`//img/@src`

   - 使用逻辑操作：`//h2[text()='Title' or text()='Header']`

   - 使用谓语：`//table/tr[position() < 5] 

9. **补充**

   * last()表示最后一个，是一个数值。

10. **XPath在Python中的应用**：

   - 使用解析库（如lxml、xml.etree.ElementTree）解析文档并应用XPath表达式。
   - 通过`xpath()`方法获取匹配的节点。
   - 提取文本、属性等信息。

   ~~~举列子
   想要选择所有<div>元素，但不包括某些具有特定属性的<div>元素
   //div[not(@class='exclude')]
   ~~~

   ~~~
   想要排除多个属性值
   //div[not(@class='exclude' or @id='exclude')]
   ~~~

   ~~~
   想要选择所有包含特定文本 "example" 的<p>元素
   //p[contains(text(), 'example')]
   ~~~

   ~~~
   选择所有具有包含 "important" 的 class 属性值的<div>元素
   //div[contains(@class, 'important')]
   ~~~

   ~~~
   想要选择所有同时具有 class 属性为 "important" 或 id 属性为 "special" 的<div>元素
   //div[@class='important' or @id='special']
   ~~~

   ~~~
   使用 | 运算符在XPath中选择同时匹配 <div> 和 <a> 元素的节点
   //div | //a
   ~~~

~~~
|运算的多条使用规则
((//div[contains(@class,"main_page")]//li) |(//div[@class="title"]))//@href
~~~

~~~
不要下面class中包含tags的节点
//*[not(contains(@class,"tags"))]
~~~

~~~
匹配所有div下面的所有text，但是不包括style标签和script标签中的text（）。
//div[@class="box_statem"]//*[not(self::styple) and not(self::script)]/txet()
~~~

```
匹配最后一个
book[last()]
```

~~~python
查询id的值以l开头的li标签
li_list= tree.xpath("//li[start-with(@id,"l")]/text()")
~~~



   下面这个同时获取比较容易出错，谨慎使用。

   ```
   选择所有同时满足是 <div> 元素或 <a> 元素的节点
   //*[self::div or self::a]
   ```

   





## 2.position的使用方法

在XPath中，`position()` 是一个函数，用于返回当前节点在其父节点中的位置。这个函数通常用于谓词（predicate）中，以便在路径表达式中选择特定位置的节点。

在XPath中，节点的位置从1开始计数。例如，如果有一个父节点包含多个相同类型的子节点，你可以使用 `position()` 函数来选择特定位置的子节点。

以下是一个示例，假设有一个XML文档结构如下：

```xml
<fruits>
    <fruit>Apple</fruit>
    <fruit>Banana</fruit>
    <fruit>Orange</fruit>
</fruits>
```

如果想选择第二个 `<fruit>` 元素（即 `<fruit>` 内容为 "Banana" 的元素），可以使用以下XPath表达式：

```xpath
//fruit[position() = 2]
```

这个表达式会选择具有位置为2的 `<fruit>` 元素，即 "Banana"。

