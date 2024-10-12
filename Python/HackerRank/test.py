import itertools

# 三个列表
list=[[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]
list1 = [5, 4]
list2 = [7, 8, 9]
list3 = [5, 7, 8, 9, 10]

# 生成笛卡尔积（所有可能的组合）
combinations = itertools.product(*list)

# 计算每个组合的平方和
for combo in combinations:
    total = sum(x**2 for x in combo)
    result = total
    print(result)