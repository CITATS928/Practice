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
