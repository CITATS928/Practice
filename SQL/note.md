

‘is’ and ‘=’
‘is’通常用于null值和bool值的比较
’=‘用于字符串和数字的比较

### 数学运算相关函数

#### 取余

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

