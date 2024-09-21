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
