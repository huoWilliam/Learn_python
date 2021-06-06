# 高级特性

## 切片

Python提供了**切片（Slice）操作符，能大大简化取可迭代对象的部分元素的操作。**

可以使用切片复制一个新的可迭代对象。做法是`L = l[:]`，便可以复制l的元素到L中。

---

参考代码： [slice.py](slice.py) 

## 迭代

在Python中，迭代是通过`for ... in`来完成的。**只要是可迭代对象，无论有无下标，都可以迭代，比如`dict`就可以迭代**。

> 🔑如何判断一个对象是可迭代对象呢？
>
> 方法是通过`collections.abc`模块的`Iterable`类型判断
>
> ```python
> >>> from collections.abc import Iterable
> >>> isinstance('abc', Iterable) # str是否可迭代
> True
> ```

如果要**对`list`实现类似Java那样的下标循环**：Python内置的`enumerate`函数可以把一个`list`变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身。

---

参考代码： [iterate.py](iterate.py) 

## 列表生成式

如果要生成`[1x1, 2x2, 3x3, ..., 10x10]`，可以使用列表生成式：

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来。**for循环后面还可以加上if判断**，这样我们就可以筛选出仅偶数的平方。

> 🔑跟在`for`后面的`if`是一个筛选条件，不能带`else`

**在一个列表生成式中，`for`前面的`if ... else`是表达式，而`for`后面的`if`是过滤条件，不能带`else`。**

---

 参考代码：[list_generator.py](list_generator.py) 

## 生成器

在Python中，有种**一边循环一边计算的机制，称为生成器：generator。**这样就不必创建完整的list，从而节省大量的空间。

创建生成器的方法：

1. 只要把一个列表生成式的`[]`改成`()`，就创建了一个generator
2. 如果一个函数定义中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator

如果要把元素一个一个打印出来，正确的方法是使用`for`循环，因为**generator也是可迭代对象**。

**generator和函数的执行流程不一样。**函数是顺序执行，遇到`return`语句或者最后一行函数语句就返回。**而变成generator的函数，在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行**。

---

参考代码： [generator.py](generator.py) 

## 迭代器

可以直接作用于`for`循环的数据类型有以下几种：

一类是集合数据类型，如`list`、`tuple`、`dict`、`set`、`str`等；

一类是`generator`，包括生成器和带`yield`的generator function。

这些可以直接作用于`for`循环的对象统称为**可迭代对象**：`Iterable`。

而可以被`next()`函数调用并不断返回下一个值的对象称为**迭代器**：`Iterator`。

生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：

