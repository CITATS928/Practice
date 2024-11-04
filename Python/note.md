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
