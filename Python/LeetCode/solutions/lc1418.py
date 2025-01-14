# 1418. Display Table of Food Orders in a Restaurant
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/description/?envType=problem-list-v2&envId=azgp9mnm

from collections import defaultdict
class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        set_table = set()
        set_food = set()
        for _, number, food in orders:
            set_table.add(int(number))
            set_food.add(food)
        ordered_table = sorted(set_table)
        ordered_food = sorted(set_food)
        # print(ordered_food)
        new_dict = {table:defaultdict(int) for table in ordered_table}

        for _, table, item in orders:
            new_dict[int(table)][item]+=1

        # print(new_dict)

        result = []
        result.append(['Table'] + ordered_food)

        for table in ordered_table:
            row=[str(table)]
            for food in ordered_food:
                row.append(str(new_dict[table][food]))
            result.append(row)

        # print(result)
        return result
    


# 优化：
# 省略set_table和set_food，直接使用ordered_table = sorted(set(int(number) for _, number, _ in orders)) 和 ordered_food = sorted(set(food for _, _, food in orders))

# 创建result的时候：result = [['Table'] + ordered_food]直接构成nested list，省略append
# 最后的loop里省略append，直接result.append([str(table)] + [str(new_dict[table][food]) for food in ordered_food])