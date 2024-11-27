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

**itertools.permutations**:
用于生成给定input的排列（permutations）。是所有可能的顺序组合，组合不考虑顺序。
会return一个迭代器（里面的内容为tuple），包含所有可能的排列。如果想查看，可以用list()转换为list。

```Python
Syntax: itertools.permutations(iterable, r=None)
# iterable: 一个可迭代对象，例如list、tuple、string等。
# r: 一个整数，表示生成的排列的长度。如果不指定，默认为 len(iterable)，生成所有可能的排列。

from itertools import permutations

data = 'ABC'
result = permutations(data)

# 转为列表查看结果
print(list(result))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

result = permutations(data, 2)
print(list(result))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
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

**formatted string literals & format()**

在python的格式化字符串中（f-string）和format() method中，可以使用大括号 {} 来插入变量。在大括号中，可以包含表达式，变量名，甚至函数调用。还有许多选项可以自定义数字和字符串的显示方式。

```Python
# 对齐选项
# <: 左对齐 (default for strings)
# >: 右对齐 (default for numbers)
# ^: 居中对齐
# =: 在符号后填充，例如在正数前加上符号

value = 42

# 左对齐 (默认为字符串)
print(f'{value:<5}')  # Output: "42   "

# 右对齐 (默认为数字)
print(f'{value:>5}')  # Output: "   42"

# 居中对齐
print(f'{value:^5}')  # Output: " 42  "

# 在符号后填充
value = -42
print(f'{value:=5}')  # Output: "-  42"


# 符号选项
# +: 显示正数和负数的符号
# -: 只显示负数的符号
# 空格: 正数前加空格，负数前加负号

value = 42

# 显示正数和负数的符号
print(f'{value:+}')  # Output: "+42"
print(f'{-value:+}') # Output: "-42"

# 只显示负数的符号
print(f'{value:-}')  # Output: "42"
print(f'{-value:-}') # Output: "-42"

# 正数前加空格，负数前加负号
print(f'{value: }')  # Output: " 42"
print(f'{-value: }') # Output: "-42"


# 宽度和填充
# width 是该值占用的总字符数，fillchar 是用于填充的字符

value = 42

# 宽度为 5，填充为 0
print(f'{value:05}')  # Output: "00042"

# 宽度为 5，填充为 *
print(f'{value:*<5}')  # Output: "42***"

# 宽度为 5，填充为 *
print(f'{value:*>5}')  # Output: "***42"

# 宽度为 5，填充为 *
print(f'{value:*^5}')  # Output: "*42**"



# 类型转换：
# d: Integer十进制整数
# o: Octal八进制整数
# X: Hexadecimal十六进制整数（大写）
# x: Hexadecimal十六进制整数（小写）
# b: Binary二进制整数
# e: Scientific notation科学计数法（小写）
# E: Scientific notation科学计数法（大写）
# f: Float浮点数
# F: Float浮点数
# g: General format一般格式（小写）
# G: General format一般格式（大写）
# %: Percentage百分比

value = 42

# Decimal
print(f'{value:d}')  # Output: "42"

# Octal
print(f'{value:o}')  # Output: "52"

# Hexadecimal (uppercase and lowercase)
print(f'{value:X}')  # Output: "2A"
print(f'{value:x}')  # Output: "2a"

# Binary
print(f'{value:b}')  # Output: "101010"

# Exponential notation
print(f'{value:e}')  # Output: "4.200000e+01"
print(f'{value:E}')  # Output: "4.200000E+01"

# Fixed-point notation
print(f'{value:f}')  # Output: "42.000000"



# Precision精度
# 用于控制浮点数的小数位数
# .n: n 是要显示的小数位数
value = 3.141592653589793

# Default floating-point precision (6 digits)
print(f'{value:f}')   # Output: "3.141593"

# Limit to 2 decimal places
print(f'{value:.2f}') # Output: "3.14"

# Scientific notation with 3 decimal places
print(f'{value:.3e}') # Output: "3.142e+00"


```

**str.split()**

用于根据指定的分隔符将String拆分为a list of substrings，如果没有指定分隔符，则默认使用whitespace (spaces, tabs, or newlines)。
It returns a list of substrings.

```Python
Syntax: string.split(separator, maxsplit)
# separator (可选): 用于拆分字符串的分隔符，默认为whitespace
# maxsplit (可选): 所需的最大拆分数。如果未提供，则进行所有可能的拆分。

# Example 1: Splitting a string without a separator
string = 'Python is fun'
result = string.split()
print(result)  # Output: ['Python', 'is', 'fun']

# Example 2: Using maxsplit
string = "one two three four five"
result = string.split(' ', 2)
print(result)  # Output: ['one', 'two', 'three four five']

# Example 3: Splitting with Multiple Spaces
string = "   Python   is   fun   "
result = string.split()
print(result)  # Output: ['Python', 'is', 'fun']

result = string.split(' ')
print(result)  # Output: ['', '', '', 'Python', '', '', 'is', '', '', 'fun', '', '']
```

**ord() & chr()**

ord() 函数返回一个字符的ASCII or Unicode value.
ord()的作用
-按ASCII值比较字符
-将字符转换为整数，以遍历字母表
-对字符进行排序，对数据进行编码

chr() 函数返回ASCII or Unicode value对应的字符。
chr()的作用
-将ASCII值转换为字符
-将数据储存为ASCII，chr()将其转换回字符

```Python
ord() Syntax: ord(character)
chr() Syntax: chr(number)

# Example 1: Using ord()
print(ord('a'))  # Output: 97
print(ord('A'))  # Output: 65
print(ord('0'))  # Output: 48

# Example 2: Using chr()
print(chr(97))  # Output: 'a'
print(chr(65))  # Output: 'A'
print(chr(48))  # Output: '0'

# Example 3: Using ord() and chr() together
# 迭代字母表
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=" ")
ord('a')为97，ord('z')为122，使用 range（97， 123） 来迭代这些值。chr（i） 将每个值转换回其对应的字符

# Example 4: Using ord() and chr() 
# 小写字母转换为大写字母
char = 'b'
uppercase_char = chr(ord(char) - 32)
print(uppercase_char)  # Output: 'B'
大写字母和小写字母的 ASCII 值用 32 分隔，减去 32 会将小写字母转换为其大写字母。
```

常用的ASCII 表

| ASCII Code | Character |
|------------|-----------|
| 32         | (space)   |
| 33         | !         |
| 34         | "         |
| 35         | #         |
| 36         | $         |
| 37         | %         |
| 38         | &         |
| 39         | '         |
| 40         | (         |
| 41         | )         |
| 42         | *         |
| 43         | +         |
| 44         | ,         |
| 45         | -         |
| 46         | .         |
| 47         | /         |
| 48         | 0         |
| 49         | 1         |
| 50         | 2         |
| 51         | 3         |
| 52         | 4         |
| 53         | 5         |
| 54         | 6         |
| 55         | 7         |
| 56         | 8         |
| 57         | 9         |
| 58         | :         |
| 59         | ;         |
| 60         | <         |
| 61         | =         |
| 62         | >         |
| 63         | ?         |
| 64         | @         |
| 65         | A         |
| 66         | B         |
| 67         | C         |
| 68         | D         |
| 69         | E         |
| 70         | F         |
| 71         | G         |
| 72         | H         |
| 73         | I         |
| 74         | J         |
| 75         | K         |
| 76         | L         |
| 77         | M         |
| 78         | N         |
| 79         | O         |
| 80         | P         |
| 81         | Q         |
| 82         | R         |
| 83         | S         |
| 84         | T         |
| 85         | U         |
| 86         | V         |
| 87         | W         |
| 88         | X         |
| 89         | Y         |
| 90         | Z         |
| 91         | [         |
| 92         | \         |
| 93         | ]         |
| 94         | ^         |
| 95         | _         |
| 96         | `         |
| 97         | a         |
| 98         | b         |
| 99         | c         |
| 100        | d         |
| 101        | e         |
| 102        | f         |
| 103        | g         |
| 104        | h         |
| 105        | i         |
| 106        | j         |
| 107        | k         |
| 108        | l         |
| 109        | m         |
| 110        | n         |
| 111        | o         |
| 112        | p         |
| 113        | q         |
| 114        | r         |
| 115        | s         |
| 116        | t         |
| 117        | u         |
| 118        | v         |
| 119        | w         |
| 120        | x         |
| 121        | y         |
| 122        | z         |
| 123        | {         |
| 124        | \|         |
| 125        | }         |
| 126        | ~         |

**dict.fromkeys()**

fromkeys() 方法用于创建一个新字典，其中包含指定键的值。如果未提供值，则默认为 None。

```Python
Syntax: dict.fromkeys(keys, value)
# keys（必须）: 可作为新字典的key的可迭代对象
# value（可选）: 用于设置所有键的值。默认为 None。

# Example 1: Using fromkeys() with a list
keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys)
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}

# Example 2: Using fromkeys() with a tuple
keys = ('name', 'age', 'city')
new_dict = dict.fromkeys(keys)
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}

# Example 3: Using fromkeys() with a string
keys = 'name'
new_dict = dict.fromkeys(keys)
print(new_dict)  # Output: {'n': None, 'a': None, 'm': None, 'e': None}

# Example 4: Using fromkeys() with a string and value
keys = 'name'
new_dict = dict.fromkeys(keys, 1)
print(new_dict)  # Output: {'n': 1, 'a': 1, 'm': 1, 'e': 1}
```

**zip()**

zip() 用于将多个iterables合并为一个元组列表。它返回一个元组的迭代器。每个 Tuples 都包含来自同一位置的每个提供的可迭代对象的元素。

\*是解包操作符，它允许您将可迭代对象解包为单独的元素。在 zip() 中使用\* 可以将元组列表解包为单独的列表。

```Python
Syntax: zip(iterable1, iterable2, ...)
# iterable1, iterable2, ...: 一个或多个可迭代对象，它们可以是列表、元组、字符串等。
# returns an iterator of tuples. You can convert it to a list or use it directly in a loop.

# Example 1: Using zip() with two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Example 2: Using zip() with three lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Los Angeles", "Chicago"]

zipped = zip(names, ages, cities)
print(list(zipped))
# Output: [('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]

# Example 3: Using zip() with different length lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]

zipped = zip(names, ages)
print(list(zipped))
# Output: [('Alice', 25), ('Bob', 30)]
# zip() 会在最短的可迭代对象结束时停止，因此在这种情况下，Charlie 不会包含在结果中。

# Example 4: Using zip() with strings
string1 = "abc"
string2 = "123"

zipped = zip(string1, string2)
print(list(zipped))
# Output: [('a', '1'), ('b', '2'), ('c', '3')]

# Example 5: Using zip() with a list and a string
names = ["Alice", "Bob", "Charlie"]
string = "123"

zipped = zip(names, string)
print(list(zipped))
# Output: [('Alice', '1'), ('Bob', '2'), ('Charlie', '3')]

# Example 6: Using zip() in a Loop
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# Output:
# Alice is 25 years old.
# Bob is 30 years old.

# Example 7: Unzipping with zip(*...)
zipped_list = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*zipped_list)
print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)
# zip（*zipped_list） 将每个元组的第一个元素分成一个列表 （names），将第二个元素分成另一个列表 （ages）。
```

**eval()**

eval() 函数用于执行一个字符串表达式，并返回表达式的值。
它可以执行动态代码并返回计算表达式的结果，但是它可能会有安全风险，因此应谨慎使用。

```Python
Syntax: eval(expression, globals=None, locals=None)
# expression: 要执行的表达式字符串
# globals（可选）: 全局变量的字典（用于控制 eval（） 可以访问的变量）。如果未提供，则默认为 globals（）。
# locals（可选）: 局部变量的字典（用于控制 eval（） 可以访问的变量）。如果未提供，则默认为 locals（）。

# Example 1: Using eval() with a simple expression
print(eval("3 + 5"))        # Output: 8
print(eval("10 * (2 + 3)")) # Output: 50

# Example 2: Using eval() with variables
x = 10
print(eval("x + 5"))  # Output: 15

# Example 3: Using eval() with built-in functions
print(eval("len([1, 2, 3, 4])"))  # Output: 4
print(eval("min(3, 5, 7, 2)"))    # Output: 2

# Example 4: Using eval() with a dictionary
x = 5
safe_dict = {"x": x, "max": max}

print(eval("max(10, x)", safe_dict))  # Output: 10

#在这种情况下，eval（） 只能访问 x 和 max，因此它不能执行任何其他函数或访问 safe_dict 之外的变量。
```

**lambda function**

lambda 函数是一种匿名函数，它可以接受任意数量的参数，但只能有一个表达式。

```Python
Syntax: lambda arguments: expression
# arguments: 传递给 lambda 函数的参数
# expression: lambda 函数的主体，它计算并返回结果

# Example 1: Using lambda function with one argument
square = lambda x: x * x
print(square(5))  # Output: 25


# Example 2: Using lambda function with multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


# Example 3: A function with a lambda function
def my_function(n):
    return lambda a: a * n

double = my_function(2)
triple = my_function(3)

print(double(11))  # Output: 22
print(triple(11))  # Output: 33
```

**Any() & All()**

Any() : 如果可迭代对象中至少有一个元素为 True，则 any()函数返回 True。如果所有元素均为 False，则返回 False。如果可迭代对象为空，则 any()返回 False。

All() : 如果可迭代对象中所有元素均为 True，则 all()函数返回 True。如果有一个元素为 False，则返回 False。如果可迭代对象为空，则 all()返回 True。

```Python
any() Syntax: any(iterable)
any将会遍历 iterable 的每个元素，一旦找到 True 值，它就会停止检查并返回 True。如果未找到任何 True 值，则返回 False。

# Example 1: With a list of booleans
print(any([False, False, True, False]))  # Output: True (because there’s at least one `True` value)

# Example 2: Checking for positive numbers
numbers = [-1, -2, -3, 4]
print(any(num > 0 for num in numbers))  # Output: True (4 is positive)

# Example 3: Empty list
print(any([]))  # Output: False (no elements to check)

# Example 4: With a list of booleans
# Check if there’s any even number in the list
numbers = [1, 3, 5, 7, 8]
has_even = any(num % 2 == 0 for num in numbers)
print(has_even)  # Output: True (because 8 is even)


##############################

all() Syntax: all(iterable)
all() 将遍历 iterable 的每个元素，一旦找到 False 值，它就会停止检查并返回 False。如果未找到任何 False 值，则返回 True。

# Example 1: With a list of booleans
print(all([True, True, True]))  # Output: True (all elements are `True`)
print(all([True, False, True])) # Output: False (because there’s a `False` value)

# Example 2: Checking if all numbers are positive
numbers = [1, 2, 3, 4]
print(all(num > 0 for num in numbers))  # Output: True (all numbers are positive)

# Example 3: Empty list
print(all([]))  # Output: True (no elements to check, so it defaults to True)

# Example 4: With a list of booleans
# Check if all numbers in a list are even
numbers = [2, 4, 6, 8]
all_even = all(num % 2 == 0 for num in numbers)
print(all_even)  # Output: True (all numbers are even)
```

**Collections.Counter**
是一个字典的子类，用于计数可哈希对象。旨在计算可迭代对象中项目的出现次数。当你想快速获取列表、元组或任何可迭代对象中每个元素的计数时，它非常有用。

```Python
from collections import Counter

# Example 1: Counting a list of numbers
numbers = [1, 2, 3, 1, 2, 3, 4, 1]
counter = Counter(numbers)
print(counter)  # Output: Counter({1: 3, 2: 2, 3: 2, 4: 1})

# Example 2: Counting a list of strings
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Use Counter to count occurrences
item_counts = Counter(items)
print(item_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

#Counter.most_common（n））：以元组列表的形式返回 n 个最常见的元素。
print(item_counts.most_common(2))  # [('apple', 3), ('banana', 2)]

#访问项目的计数，例如字典。
print(item_counts['apple'])  # Output: 3

#更新计数：可以添加或减去计数
item_counts['apple'] += 1
print(item_counts['apple'])  # Output: 4

item_counts.update(['apple', 'orange'])
print(item_counts)  # Output: Counter({'apple': 5, 'banana': 2, 'orange': 2})
```

**Collections.defaultdict**

它和普通的dict差不多，区别是它会为不存在的键提供一个默认值。这样，当你访问不存在的键时，它不会引发 KeyError，而是返回指定的默认值。

当创建一个 defaultdict 时，你需要指定一个默认工厂函数，它将用于为不存在的键提供默认值。这个函数可以是 int、list、set 等。

```Python
from collections import defaultdict

# 使用 int 作为默认工厂
count_dict = defaultdict(int)
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for item in items:
    count_dict[item] += 1

print(count_dict)
# 输出: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})

# 在这里，count_dict[item] += 1 自动将不存在的 item 初始化为 0（因为 int() 默认返回 0），然后再执行加一操作。

# 自动初始化列表

# 使用 list 作为默认工厂
position_dict = defaultdict(list)
words = ['a', 'b', 'a', 'a', 'b']
for index, word in enumerate(words):
    position_dict[word].append(index)

print(position_dict)
# 输出: defaultdict(<class 'list'>, {'a': [0, 2, 3], 'b': [1, 4]})
```

**collection.namedtuple**
用来表示不可变的对象（类似于元组）。它的主要特点是：

- 更具可读性：你可以通过属性名称（如 .name、.age）而不是index（如 [0]、[1]）访问值。
- 节省内存：与dict相比，namedtuple 的存储效率更高。
- 不可变性：它的字段值不能被更改，类似于tuple。

```
Syntax: TypeName = namedtuple('TypeName', [field1, field2, ...])
# TypeName: 类的名字。
# [field1, field2, ...]: 字段名称列表。可以是字符串列表或单个用空格分隔的字符串。

# 两种定义字段的方式
Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', 'width height')

p = Point(10, 20)
print(p.x, p.y)  # 输出: 10 20

r = Rectangle(15, 25)
print(r.width, r.height)  # 输出: 15 25



from collections import namedtuple

# 创建一个 namedtuple 类型
Person = namedtuple('Person', ['name', 'age', 'city'])

# 创建 Person 实例
person1 = Person(name='Alice', age=30, city='New York')

# 访问字段
print(person1.name)  # 输出: Alice
print(person1.age)   # 输出: 30

# 像tuple一样访问字段
print(person1[0])  # 输出: Alice
print(person1[1])  # 输出: 30

# 使用 _fields 查看字段名称
print(person1._fields)  # 输出: ('name', 'age', 'city')

# 将一个dict转换为 namedtuple
data = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
person2 = Person(**data)
print(person2)  # 输出: Person(name='Bob', age=25, city='Los Angeles')


# Example: 
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# _fields: 查看所有字段的名称
print(p._fields)  # 输出: ('x', 'y')

# _asdict: 将namedtuple转换成dict
print(p._asdict())  # 输出: {'x': 1, 'y': 2}

# _replace: 返回一个新的 namedtuple，修改指定字段。
new_p = p._replace(x=10)
print(new_p)  # 输出: Point(x=10, y=2)

# _make: 从一个可迭代对象创建namedtuple
data = [10, 20]
p = Point._make(data)
print(p)  # 输出: Point(x=10, y=20)
```


**Dictionary**

```Python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with initial values
student = {'name': 'Alice', 'age': 25, 'courses': ['Math', 'Science']}

# Accessing Dictionary Items
print(student['name'])  # Output: Alice

# 如果访问的key不存在，会引发key Error。可以使用get()方法，它会返回None或指定的默认值。
print(student.get('name'))         # Output: Alice
print(student.get('GPA', 'N/A'))   # Output: N/A (default if key doesn't exist)

# Adding or Modifying Items
student['GPA'] = 3.8           # Adding new key-value pair
student['age'] = 26            # Updating existing key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26, 'courses': ['Math', 'Science'], 'GPA': 3.8}

student['courses'].append('History')  # Adding an item to a list
print(student['courses'])  # Output: ['Math', 'Science', 'History']

# Removing Items
age = student.pop('age') # Removing a key-value pair
print(age)            # Output: 26
del student['GPA']  # Deleting a key-value pair
print(student)        # Output: {'name': 'Alice', 'courses': ['Math', 'Science']}
student.clear()      # Clearing the dictionary
print(student)        # Output: {}
```

**Dictionary Comprehension**

```Python
# Example 1: Creating a dictionary with a loop
squares = {}
for num in range(1, 6):
    squares[num] = num * num
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Using dictionary comprehension
squares = {num: num * num for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 3: Using dictionary comprehension with if condition
even_squares = {num: num * num for num in range(1, 6) if num % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16}
```

**enumerate()**

用于在遍历iterable时，同时获取元素的index和value。它返回一个包含index和value的元组。可以让代码更清晰简洁，避免手动管理index。

```Python
# Basic Usage
my_list = ['a', 'b', 'c', 'd']
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c
# 3 d

# Specifying the start index
# enumerate() 默认从 0 开始，但可以通过指定 start 参数来更改起始index。
for index, value in enumerate(my_list, start=1):
    print(index, value)
# Output:
# 1 a
# 2 b
# 3 c
# 4 d
```

**filter()**

filter() 函数用于过滤可迭代对象中的元素。它接收一个函数和一个可迭代对象，然后返回一个迭代器，其中包含仅满足函数条件的元素。

```Python
Syntax: filter(function, iterable)
# function: 用于过滤元素的函数
# iterable: 要过滤的可迭代对象
# returns an iterator

# Example 1: Using filter() with a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
```
