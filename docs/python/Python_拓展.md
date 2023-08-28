## 1.python中的i++



```python1
i = 0
i += 1  # 自增操作，等同于 i = i + 1
print(i)  # 输出 1
```

##  2.如何理解下方一段代码（关于读和写）

~~~python
IN:with open('demo.html','w', encoding='utf-8') as f:
IN:f.write(html_doc)
~~~

`open(文件的路径，访问模式)`

这段代码使用了 Python 中的文件操作来创建或覆盖一个名为 `demo.html` 的 HTML 文件，并将一个名为 `html_doc` 的字符串写入该文件中。让我们逐步解释这段代码的作用：

1. `with open('demo.html', 'w', encoding='utf-8') as f:`:
   - `with open(...) as f:` 是一个上下文管理器（context manager）的语法，用于在代码块执行完毕后自动关闭文件。
   - `open('demo.html', 'w', encoding='utf-8')` 打开一个文件叫做 `demo.html`，使用写入模式 `'w'`，并使用 UTF-8 编码（用于支持中文等非英文字符）。
   - `as f` 将打开的文件对象赋值给变量 `f`，这样我们可以通过 `f` 来操作文件。

2. `f.write(html_doc)`:
   - `f` 是文件对象，它表示已打开的 `demo.html` 文件。
   - `write(html_doc)` 调用了文件对象的 `write` 方法，将变量 `html_doc` 中的内容写入文件。
   - 这段代码的作用是将 `html_doc` 中的字符串写入到打开的文件中，即将 HTML 内容写入到 `demo.html` 文件中。



> 如果文件存在，会先清空原来的数据 ，然后在写
>
> 如果想在每一次执行之后追加数据时，用"a"
>
> ~~~python
> IN:with open('demo.html','w', encoding='utf-8') as f:
> IN:f.write(html_doc)
> ~~~



这段代码的目的是打开名为 `example.txt` 的文件，并在上下文管理器的环境中使用文件对象 `f` 来读取文件的内容，然后将文件的全部内容打印出来。让我们一步步理解这段代码：

```python
with open('example.txt', 'r') as f:
    print(f.read())
```

1. `with open('example.txt', 'r') as f:`:
   
- 这部分与前面的解释一样，使用上下文管理器 `with` 打开 `example.txt` 文件，以读取模式 `'r'`，并将文件对象赋值给变量 `f`。
  
2. `print(f.read())`:
   - `f` 是文件对象，表示已打开的 `example.txt` 文件。
   - `f.read()` 调用了文件对象的 `read()` 方法，这会读取整个文件的内容，并返回一个包含文件内容的字符串。
   - `print(...)` 打印出从 `f.read()` 返回的文件内容字符串。
   
   >拓展:
   >
   >f.read()也可以写成f.readlines(),可以按照行来读取    但是会将所有数据都读取到，并且以一个列表的形式返回

整体上，这段代码的作用是打开文件 `example.txt`，读取文件的全部内容，然后通过 `print` 函数将读取到的内容输出到终端或控制台上。这种模式常用于查看文件的内容，测试文件读取操作以及进行基本的文本处理。在上下文管理器的环境中，文件会在操作结束后自动关闭，避免了手动关闭文件的繁琐。



## 3.python中print(f"XXX{YYY}")是什么意思

​	python的print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样. ![img](https://pic1.zhimg.com/v2-71e6954227b76fe2ef88195593be7a40_r.jpg)

## 4.Python zfill()方法

* 描述：Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
* 语法：zfill()方法语法：str.zfill(width)

 ## 5.list转换为str

* 使用join方法
  **基本使用**
  <str> = <separator>.join(<list>)
  <separator>: 分隔符，为str类型，如','
  <list>: 需要进行合并的list对象，其中每个元素必须为str类型
  <str>: 返回一个str对象，是将<list>中每个元素按顺序用分隔符<separator>用什么拼接而成

## 6.lambda函数的定义

​	公式：<函数名>=lambda<参数>:<表达式>

​	说明：冒号后面的表达式的计算结果即为该lambda函数的返回值

* *lambda函数等价于：*

  ~~~python
  def <函数名> (<参数>):
      <函数体>
      return <返回值>
  ~~~

## 7.**enumerate()**

​	`	enumerate()` 是Python中的一个内置函数，它用于将一个可迭代对象（如列表、元组、字符串等）组合成一个索引序号和对应的元素的迭代器。这对于遍历列表（或其他可迭代对象）并且需要同时获取元素和索引的情况非常有用。

​	`enumerate()` 函数的基本语法如下：

```python
enumerate(iterable, start=0)
```

- `iterable`：需要迭代的可迭代对象，如列表、元组、字符串等。
- `start`（可选参数）：表示索引起始值，默认为0，你可以通过设置它来改变起始值。

下面是一个使用 `enumerate()` 函数的示例：

```python
fruits = ['apple', 'banana', 'orange', 'grape']
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")
```

输出：

```python
Index 1: apple
Index 2: banana
Index 3: orange
Index 4: grape
```

在这个示例中，`enumerate()` 函数将列表 `fruits` 中的元素与它们的索引一一配对，并返回一个迭代器。通过在循环中使用这个迭代器，我们可以同时获得元素和索引。设置 `start` 参数为 1，所以索引从 1 开始。

这使得在遍历时能够方便地获取元素和对应的索引，从而简化代码。

## 8.**copy.copy()和copy.deepcopy()**

* `copy.copy()` 和 `copy.deepcopy()` 都是 Python 中用于复制对象的函数，但它们在复制对象时的方式和效果有所不同。让我们逐个说明它们并加以比较：

  1. **`copy.copy()`**：
     `copy.copy()` 函数是 Python 标准库中 `copy` 模块中的一部分。它用于创建一个浅拷贝（shallow copy）的对象。浅拷贝意味着外层对象（如列表、字典等）会被复制，但内部嵌套的对象只是引用。换句话说，新对象的内部嵌套对象与原对象的内部嵌套对象是同一个，这可能会导致某些修改影响到原对象和新对象。

     示例：

     ```python
     import copy
     
     original_list = [1, [2, 3]]
     copied_list = copy.copy(original_list)
     
     original_list[1][0] = 99
     print(original_list)  # 输出: [1, [99, 3]]
     print(copied_list)    # 输出: [1, [99, 3]]
     ```

     在上面的示例中，修改了 `original_list` 的嵌套列表，但是由于浅拷贝，`copied_list` 的嵌套列表也受到了影响。

  2. **`copy.deepcopy()`**：
     `copy.deepcopy()` 也是 `copy` 模块中的函数，它用于创建一个深拷贝（deep copy）的对象。深拷贝会递归地复制所有嵌套的对象，包括内部嵌套对象，因此新对象与原对象的所有内容都是相互独立的。

     示例：

     ```python
     import copy
     
     original_list = [1, [2, 3]]
     deep_copied_list = copy.deepcopy(original_list)
     
     original_list[1][0] = 99
     print(original_list)       # 输出: [1, [99, 3]]
     print(deep_copied_list)    # 输出: [1, [2, 3]]
     ```

     在这个示例中，即使修改了 `original_list` 的嵌套列表，`deep_copied_list` 的嵌套列表仍然保持不变，因为它是通过深拷贝创建的。

     总结：

  - 使用 `copy.copy()` 进行浅拷贝，内部嵌套对象可能会共享引用，修改其中一个会影响另一个。
  - 使用 `copy.deepcopy()` 进行深拷贝，内部嵌套对象会被递归地复制，创建一个完全独立的新对象。

  在选择使用哪种方法时，取决于你对复制对象的需求。如果你需要一个独立的、与原对象完全无关的副本，那么使用 `copy.deepcopy()` 是更好的选择。如果你只需要外部对象的副本，而不关心内部对象的变化，那么使用 `copy.copy()` 可能更合适。

## 9.**if\_\_name\_\_=="\_\_main\_\_"**

>深入了解：[if\_\_name\_\_=="\_\_main\_\_"](https://www.bilibili.com/video/BV1rA41137mj/?spm_id_from=333.337.search-card.all.click&vd_source=2a411562cb1015d46811fc2c5f78baef )

## 10.搞懂Python 中的 import 与 from import 

​	**一个模块里面可以包含多个函数。**

>"from import"通常是指Python中的导入（import）语句，它用于将其他模块（或模块中的特定成员）引入到当前的Python脚本中，以便在当前脚本中使用这些模块或成员。
>
>在Python中，有几种不同的导入方式，其中包括：
>
>1. **import**：这是最常见的导入语句，它用于导入一个完整的模块。例如：
>
>```python
>import math
>```
>
>这样就将Python标准库中的`math`模块引入到当前脚本中，然后你可以使用`math`模块中的函数和变量。
>
>2. **from ... import**：这个导入方式可以从一个模块中选择性地导入特定的成员（函数、类、常量等）。例如：
>
>```python
>from math import sqrt, pi
>```
>
>这样只会将`math`模块中的`sqrt()`函数和`pi`常量引入到当前脚本中，而其他`math`模块的成员将不会被引入。
>
>3. **from ... import \***：这个导入方式允许导入模块中的所有成员。例如：
>
>```python
>from math import *
>```
>
>这样会将`math`模块中的所有成员都引入到当前脚本中。但是，不推荐使用这种方式，因为它可能导致命名冲突，特别是当导入的模块有许多成员时。
>
>4. **import ... as**：这个导入方式可以为导入的模块或成员设置别名，以便在代码中更方便地使用。例如：
>
>```python
>import numpy as np
>```
>
>这样将`numpy`模块导入，并给它设置了一个别名`np`，这样你可以使用`np`来代替`numpy`。
>
>导入语句在Python中是非常重要的，因为它允许你利用其他开发者编写的模块和库，以及Python标准库的功能，从而更加高效地开发复杂的应用程序。
>
>

 