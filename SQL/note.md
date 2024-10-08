# TODO
窗口函数
CTE

‘is’ and ‘=’
‘is’通常用于null值和bool值的比较
’=‘用于字符串和数字的比较

#### MATH

##### **MOD(number, divisor)**

```sql
SELECT MOD(10, 2);  -- 返回 0，因为 10 除以 2 没有余数（10 是偶数）

SELECT * FROM my_table 
WHERE MOD(id, 2) = 0;
```

##### **POWER(base, exponent)**

```sql
SELECT POWER(2, 3);  -- 返回 8，因为 2 的 3 次幂等于 8

SELECT name, POWER(score, 2) AS squared_score 
FROM test_results;
-- 返回每个学生的名字及其成绩的平方
```

##### **SQRT(number)**

```sql
SELECT SQRT(16);  -- 返回 4，因为 4 是 16 的平方根

SELECT name, SQRT(score) AS sqrt_score 
FROM scores;
-- 返回每个学生的名字及其成绩的平方根
```

##### **LOG(number) & EXP(number)**

LOG(number) 返回 number 的自然对数（以 e 为底）。
EXP(number) 返回 e 的 number 次幂。

```sql
SELECT LOG(2.71828);  -- 返回约 1，因为 2.71828 是 e 的近似值，LOG(e) 为 1

SELECT EXP(1);  -- 返回 2.71828，因为 e 的 1 次幂是 e（自然对数的底）

SELECT name, LOG(salary) AS log_salary 
FROM employees;
-- 返回每个员工的名字及其工资的自然对数值
```

##### **ROUND(number, decimal)**

将 number 四舍五入到指定的小数位数 decimals。decimals 参数是可选的，如果不指定，默认四舍五入到整数。

```sql
SELECT ROUND(123.4567, 2);  -- 返回 123.46，保留两位小数

SELECT ROUND(123.4567);  -- 返回 123，四舍五入到最近的整数

SELECT product_name, ROUND(price, 1) AS rounded_price 
FROM products;
-- 返回每个产品的名字及其价格的四舍五入值（保留一位小数）
```

##### **CEIL(number) & FLOR(number)**

```sql
SELECT FLOOR(4.7);  -- 返回 4，因为 4 是小于 4.7 的最大整数

SELECT CEIL(4.2);   -- 返回 5，因为 5 是大于 4.2 的最小整数

SELECT CEILING(4.2);  -- 等同于 CEIL(4.2)，返回 5
```

##### **ABS(number)**

```sql
SELECT ABS(-15);  -- 返回 15，因为 -15 的绝对值是 15

SELECT product_name, ABS(profit_loss) AS abs_profit_loss 
FROM financials;
-- 返回每个产品的名字及其利润或亏损的绝对值
```

##### **ROUND(number, decimals)**

用于控制数值的精度并保留指定的小数位数
Example:

```sql  
SELECT ROUND(value, 4) 
FROM table_name;
```

##### **TRUNCATE(number, decimals)**

用于截断数值并保留指定的小数位数，会删除多余的小数位，而不是四舍五入
Example:

```sql
SELECT TRUNCATE(value, 4)
FROM table_name;
```

##### **FORMAT(number, decimals)**

用于格式化数值并保留指定的小数位数, returns a string
Example:

```sql
SELECT FORMAT(value, 4)
FROM table_name;
```

#### STRING operation

##### **REPLACE(string, substring, new_substring)**

- string: 原始的string
- substring: 要查找的并替换的substring
- new_substring: 要替换substring的

```sql
SELECT REPLACE('Hello World', 'World', 'SQL');  -- return 'Hello SQL'


SELECT REPLACE('100200', '0', '');  -- return '12'
```

##### CONCAT()

##### SUBSTRING()

#### CONVERT function

##### **CAST(expression AS data_type)**

- expression: 要转换的表达式
- data_type: 要转换的数据类型
  - CHAR(n)
  - DECIMAL(n)
  - SIGNED(n)
  - UNSIGNED(n)
  - DATE
  - DATETIME
  - TIME
  - BINARY(n)
  - JSON

```sql
-- 将一个整数转换为字符串
SELECT CAST(my_column AS CHAR) FROM my_table;

SELECT CAST(123.45 AS INT);  -- return 123
SELECT CAST('123' AS INT);  -- return 123
```

##### CONVERT()

##### TO_CHAR()

##### TO_DATE()

#### JOIN

##### **INNER JOIN**

```sql
SELECT column_name(s)
FROM table1
<JOIN_TYPE> JOIN table2
ON table1.column_name = table2.column_name
WHERE <condition>;
```

- INNER JOIN：只返回两个表中匹配的行。
- LEFT JOIN：返回左表的所有行，即使右表没有匹配。
- RIGHT JOIN：返回右表的所有行，即使左表没有匹配。
- FULL JOIN：返回两个表中的所有行，没有匹配的地方用 NULL 填充。
- CROSS JOIN：
- SELF JOIN：

#### CASE

在 SQL 查询中执行 if-then-else 逻辑
可以在SQL查询的不同部分使用 CASE 语句，如 SELECT、WHERE 和 ORDER BY 子句。

Basic Syntax Example:

```sql
SELECT
  CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE resultN  -- Optional
  END
FROM table_name;
```

##### **CASE IN SELECT (Example)**

Table:

| Employee | Salary |
|----------|--------|
| Charlie  | 1000   |
| Alice    | 5000   |
| Bob      | 3000   |
| David    | 7000   |

- If the salary is greater than 5000, return "High salary".
- If the salary is between 3000 and 5000, return "Average salary".
- Otherwise, return "Low salary".

```sql
SELECT Employee,
       Salary,
       CASE
         WHEN Salary > 5000 THEN 'High salary'
         WHEN Salary BETWEEN 3000 AND 5000 THEN 'Average salary'
         ELSE 'Low salary'
       END AS Salary_Category
FROM Employees;
```

Result:

| Employee | Salary | Salary_Category |
|----------|--------|-----------------|
| Charlie  | 1000   | Low salary      |
| Alice    | 5000   | Average salary  |
| Bob      | 3000   | Average salary  |
| David    | 7000   | High salary     |

##### **CASE IN WHERE (Example)**

```sql
SELECT *
FROM Employees
WHERE 
  CASE
    WHEN Salary > 5000 THEN Salary
    ELSE NULL
  END IS NOT NULL;
```

Return all employees with a salary greater than 5000.

##### **CASE IN ORDER BY (Example)**

```sql
SELECT Employee, Salary
FROM Employees
ORDER BY
  CASE
    WHEN Salary > 5000 THEN 1  -- High salary comes first
    WHEN Salary BETWEEN 3000 AND 5000 THEN 2  -- Average salary comes second
    ELSE 3  -- Low salary comes last
  END;
```

Result:

| Employee | Salary |
|----------|--------|
| David    | 7000   |
| Alice    | 5000   |
| Bob      | 3000   |
| Charlie  | 1000   |

##### **CASE IN JOIN (Example)**

假设有2个表，Order和Costumer。希望根据订单类型的不同把他们join起来。比如订单类型是‘Online’，则join on email，如果是‘InStore’，则join on costomer_id。

```sql
SELECT o.order_id, c.customer_name
FROM Orders o
JOIN Customers c
ON 
  CASE 
    WHEN o.order_type = 'Online' THEN o.email = c.email
    WHEN o.order_type = 'In-Store' THEN o.customer_id = c.customer_id
  END;
```

##### **CASE with Aggregate Functions (Example)**

Return the total amount of shipped orders.

```sql
SELECT 
  SUM(
    CASE
      WHEN status = 'Shipped' THEN amount
      ELSE 0
    END
  ) AS Shipped_Amount
FROM Orders;
```
