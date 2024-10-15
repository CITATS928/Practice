# Python

在for循环的时候，如果使用了全局变量作为循环内部的变量，那么在循环结束后，全局变量的值会被修改。这是因为在for循环中，全局变量和局部变量是同一个变量，只是在for循环中，全局变量被当做局部变量使用。所以在循环结束后，全局变量的值会被修改。

```python
x = 5
# 传统 for 循环
for x in range(3):
    print(x)  # 打印 0, 1, 2
print(x)  # 打印 2，for 循环覆盖了外部 x 的值

# 列表生成式
x = 5
[x for x in range(3)]
print(x)  # 打印 2，列表生成式内部的 x 覆盖了外部 x 的值
```

**list append**
list的append是引用（指向内存地址），而非复制。
当你将一个对象 append 到列表中时，实际上是将该对象的引用添加到列表中，而不是将对象本身的内容复制一份。
所以可以使用list2.append(list1.copy())   # 添加 list1 的副本

```python
list1 = [1, 2, 3]
list2 = []

for _ in range(3):
    list2.append(list1)

print(list2)  # 输出 [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

list1.append(4)  # 修改 list1
print(list2)  # 输出 [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
```

---

迭代器（iterator）是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。字符串、列表或元组对象都可用于创建迭代器：

它可以逐一返回其中的元素，但它的元素只能被访问一次。换句话说，当你用过迭代器获取元素的时候，它会被消耗掉，并且你无法再次访问已经消耗的元素，除非重新生成迭代器。

```python
# 创建一个简单的迭代器
numbers = iter([1, 2, 3, 4])

# 第一次迭代
for num in numbers:
    print(num)

# Output: 1 2 3 4

# 再次迭代同一个迭代器
for num in numbers:
    print(num)

# Output: 无输出
```

**itertools groupby**:
itertools.groupby(iterable, key=None)

用于将连续的相同元素分组。它对于按某个键对数据进行分组非常有用，尤其在对已经排序的序列进行分组时表现良好。

注意事项：

1. groupby 只对相邻的相同元素进行分组，因此通常需要先对数据进行排序。
2. groupby 返回的是一个迭代器，它生成 (key, group) 的元组，其中 key 是分组的键，group 是分组的元素。

**itertools.product**:

return一个itertor, 包含所有可能的组合

```Python
itertools.product(*iterables, repeat=1)
# *iterables: 一个或多个可迭代对象(lists, tuples, sets, etc.)
# repeat: 一个整数，表示重复生成元素的次数, 默认为 1
```

Example:

```Python
import itertools

list1 = [1, 2]
list2 = ['a', 'b']
list3 = [True, False]

# Compute the Cartesian product
result = itertools.product(list1, list2, list3)

# Print each combination
for item in result:
    print(item)

"""
(1, 'a', True)
(1, 'a', False)
(1, 'b', True)
(1, 'b', False)
(2, 'a', True)
(2, 'a', False)
(2, 'b', True)
(2, 'b', False)
"""

lists = [[1, 2], ['a', 'b'], [True, False]]

# Compute the Cartesian product
result = itertools.product(*lists)

# Print each combination
for item in result:
    print(item)

"""
(1, 'a', True)
(1, 'a', False)
(1, 'b', True)
(1, 'b', False)
(2, 'a', True)
(2, 'a', False)
(2, 'b', True)
(2, 'b', False)
"""
```

***lists**

unpacking operator (*) 用于解包可迭代对象，它允许我们将可迭代对象作为参数传递给函数或构造函数。

```Python
# Unpack a list
numbers = [1, 2, 3]
print(*numbers)  # Output: 1 2 3

###

def my_function(a, b, c):
    print(a, b, c)

# Example with lists
my_list = [1, 2, 3]

# Using * to unpack
my_function(*my_list)

# Output: 1 2 3
# *my_list将list[1, 2, 3]解包成了my_function的参数a=1, b=2, c=3。如果没有*，my_function（my_list）会将整个列表作为单个参数传递，则会报错。
```

**map()**

map() 函数接收一个函数和一个可迭代对象，它会对可迭代对象中的每个元素应用函数，并返回一个包含所有函数调用结果的迭代器。
这是一种在一行代码中处理集合元素（如转换或修改它们）的方法，而无需编写 for 循环。

```Python
map(function, iterable, ...)
# function: 想要应用于iterable中每个元素的函数
# iterable: 一个或多个iterable
# It returns an iterator

# Example 1: map() with int() to convert strings to integers
numbers = ['1', '2', '3']
result = map(int, numbers)
print(list(result))  # Output: [1, 2, 3]

# Example 2: map() with lambda function
numbers = [1, 2, 3]
result = map(lambda x: x * x, numbers)
print(list(result))  # Output: [1, 4, 9]

# Example 3: map() with custom function
def square(x):
    return x * x

numbers = [1, 2, 3]
result = map(square, numbers)
print(list(result))  # Output: [1, 4, 9]
```

**str.join()**

jion is a string method. 允许你将iterable combine or concatenate into a single string. 在每个字符串之间使用指定的分隔符。

```Python
Syntax: separator.join(iterable)
# separator: 用于分隔每个元素的字符串，例如空格‘ ’、逗号‘，’，换行符‘\n’等。
# iterable: 要链接的字符串列表、元组、集合等。
# It returns a new string，结合了iterable的所有元素，由指定的separator分隔

# Example 1: Joining a list of words with spaces
words = ['Python', 'is', 'fun']

# Joining with space separator
result = ' '.join(words)
print(result)  # Output: Python is fun



# Example 2: Joining with newlines (\n)
words = ['Python', 'is', 'fun']

# Joining with newline separator
result = '\n'.join(words)
print(result)
"""
Output:
Python
is
fun
"""

# Example 4: Using join() with characters
characters = ['P', 'y', 't', 'h', 'o', 'n']

# Joining with empty separator
result = ''.join(characters)
print(result)  # Output: Python




# Example 5: Joining non-string elements    
numbers = [1, 2, 3]

# Joining with a comma separator
result = ', '.join(map(str, numbers))
print(result)  # Output: 1, 2, 3
```

**str.center()**

center() 方法用于将字符串居中，并使用指定的填充字符（默认为空格）填充空格。

```Python
Syntax: string.center(width, fillchar=‘ ‘)
# width: the total width of the result string (包括填充字符)
# fillchar（可选）: 用于填充的字符，默认为空格。
# It returns a string

# Example 1: Basic
string = 'Hello'
centered_string = string.center(11)
print(centered_string)  # Output: '   Hello   '
# Hello字长5，总共11个字符，所以两边各有3个空格



# Example 2: With custom fillchar
string = 'Hello'
centered_string = string.center(11, '-')
print(centered_string)  # Output: '---Hello---'



# Example 3: With odd width
string = 'Hello'
centered_string = string.center(10, '*')
print(centered_string)  # Output: '**Hello***'
#当填充所需的额外空格或字符为奇数时，Python 会在右侧添加更多字符以平衡它。
```
