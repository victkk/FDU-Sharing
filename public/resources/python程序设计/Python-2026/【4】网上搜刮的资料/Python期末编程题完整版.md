# Python期末高频编程题（完整版）

## 目录

1. [基础变量+判断](#一、基础变量判断)
2. [循环计算](#二、循环计算)
3. [列表与元组](#三、列表与元组)
4. [字符串处理](#四、字符串处理)
5. [字典操作](#五、字典操作)
6. [集合操作](#六、集合操作)
7. [函数与递归](#七、函数与递归)
8. [面向对象综合题](#八、面向对象综合题)
9. [文件操作](#九、文件操作)

---

## 一、基础变量+判断

### 1. 分段函数求值
**题目描述**：根据输入的x值，计算分段函数y的值。
```
y = x + 1        (x < 0)
y = x^2          (0 ≤ x < 5)
y = 2x - 1       (5 ≤ x < 10)
y = x/2          (x ≥ 10)
```

**输入**：一个整数x

**输出**：对应的y值

**示例输入**：`6`

**示例输出**：`11.0`

```python
x = int(input())
if x < 0:
    y = x + 1
elif 0 <= x < 5:
    y = x ** 2
elif 5 <= x < 10:
    y = 2 * x - 1
else:
    y = x / 2
print(y)
```

### 2. 判断水仙花数
**题目描述**：输入一个三位数，判断是否为水仙花数。

**输入**：一个三位数

**输出**："水仙花数"或"不是水仙花数"

**示例输入**：`153`

**示例输出**：`水仙花数`

```python
n = int(input())
a, b, c = n//100, n//10%10, n%10
if a**3 + b**3 + c**3 == n:
    print("水仙花数")
else:
    print("不是水仙花数")
```

### 3. 判断回文数
**题目描述**：输入一个整数，判断是否为回文数。

**输入**：一个整数

**输出**："回文数"或"不是回文数"

**示例输入**：`12321`

**示例输出**：`回文数`

```python
n = input()
print("回文数" if n == n[::-1] else "不是回文数")
```

### 4. 判断完数
**题目描述**：输入一个正整数，判断是否为完数。

**输入**：一个正整数

**输出**："完数"或"不是完数"

**示例输入**：`6`

**示例输出**：`完数`

```python
n = int(input())
sum_factor = sum(i for i in range(1, n) if n % i == 0)
print("完数" if sum_factor == n else "不是完数")
```

### 5. 判断闰年
**题目描述**：输入一个年份，判断是否为闰年。

**输入**：一个年份

**输出**："闰年"或"平年"

**示例输入**：`2024`

**示例输出**：`闰年`

```python
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("平年")
```

### 6. 输入两个整数，求和、差、积、商
**题目描述**：输入两个整数，输出它们的和、差、积、商。

**输入**：两个整数，用空格分隔

**输出**：和 差 积 商（商保留两位小数）

**示例输入**：`10 5`

**示例输出**：`15 5 50 2.00`

```python
a, b = map(int, input().split())
print(f"{a + b} {a - b} {a * b} {a / b:.2f}")
```

### 7. 摄氏温度转华氏温度
**题目描述**：输入摄氏温度，输出华氏温度。

**输入**：一个整数表示摄氏温度

**输出**：华氏温度（保留两位小数）

**公式**：F = C × 9/5 + 32

**示例输入**：`100`

**示例输出**：`212.00`

```python
c = int(input())
f = c * 9 / 5 + 32
print(f"{f:.2f}")
```

### 8. 判断三条边能否构成三角形
**题目描述**：输入三条边长，判断能否构成三角形。

**输入**：三个整数，用空格分隔

**输出**："能构成三角形"或"不能构成三角形"

**示例输入**：`3 4 5`

**示例输出**：`能构成三角形`

```python
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("能构成三角形")
else:
    print("不能构成三角形")
```

### 9. 成绩等级判断（Switch-Case）
**题目描述**：输入成绩（0-100），使用if-elif模拟switch-case输出等级。

**输入**：一个整数成绩

**输出**：等级A/B/C/D/E

**示例输入**：`85`

**示例输出**：`B`

```python
score = int(input())
level = score // 10
if level == 10 or level == 9:
    grade = 'A'
elif level == 8:
    grade = 'B'
elif level == 7:
    grade = 'C'
elif level == 6:
    grade = 'D'
else:
    grade = 'E'
print(grade)
```

### 10. 月份天数判断（Switch-Case）
**题目描述**：输入月份和年份，输出该月的天数。

**输入**：月份和年份，用空格分隔

**输出**：天数

**示例输入**：`2 2024`

**示例输出**：`29`

```python
month = int(input())
year = int(input())
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
elif month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
else:
    days = 30
print(days)
```

---

## 二、循环计算

### 11. 打印九九乘法表
**题目描述**：打印九九乘法表。

**输入**：无

**输出**：九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={i*j}", end='\t')
    print()
```

### 12. 计算1+2+3+...+n
**题目描述**：输入n，计算1到n的和。

**输入**：一个正整数n

**输出**：和

**示例输入**：`10`

**示例输出**：`55`

```python
n = int(input())
print(sum(range(1, n+1)))
```

### 13. 计算1+1/2+1/3+...+1/n
**题目描述**：输入n，计算调和级数的和。

**输入**：一个正整数n

**输出**：和（保留两位小数）

**示例输入**：`5`

**示例输出**：`2.28`

```python
n = int(input())
print("{0:.2f}".format(sum(1/i for i in range(1, n+1))))
```

### 14. 计算n的阶乘
**题目描述**：输入n，计算n!。

**输入**：一个非负整数n

**输出**：n的阶乘

**示例输入**：`5`

**示例输出**：`120`

```python
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)
```

### 15. 计算1!+2!+3!+...+n!
**题目描述**：输入n，计算阶乘的和。

**输入**：一个正整数n

**输出**：阶乘的和

**示例输入**：`5`

**示例输出**：`153`

```python
n = int(input())
total = 0
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    total += fact
print(total)
```

### 16. 最大公约数与最小公倍数
**题目描述**：输入两个正整数，计算GCD和LCM。

**输入**：两个正整数，用空格分隔

**输出**：GCD和LCM，用空格分隔

**示例输入**：`12 18`

**示例输出**：`6 36`

```python
a, b = map(int, input().split())
x, y = a, b
while y:
    x, y = y, x % y
print(x, a*b//x)
```

### 17. 斐波那契数列第n项
**题目描述**：输入n，输出斐波那契数列第n项。

**输入**：一个正整数n

**输出**：斐波那契数列第n项

**示例输入**：`10`

**示例输出**：`55`

```python
n = int(input())
if n <= 2:
    print(1)
else:
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b
    print(b)
```

### 18. 输出斐波那契数列前20项
**题目描述**：输出斐波那契数列前20项。

**输入**：无

**输出**：前20项，每行一个

```python
a, b = 1, 1
for i in range(20):
    print(a)
    a, b = b, a + b
```

### 19. 猴子吃桃问题
**题目描述**：猴子每天吃一半多一个桃子，第n天剩1个，求最初桃子数。

**输入**：一个正整数n

**输出**：最初桃子数

**示例输入**：`3`

**示例输出**：`10`

```python
n = int(input())
peach = 1
for _ in range(n-1):
    peach = (peach + 1) * 2
print(peach)
```

### 20. 高空坠球问题
**题目描述**：球从h米落下，每次反弹一半，求第n次落地时总路程。

**输入**：h和n，用空格分隔

**输出**：总路程（保留两位小数）

**示例输入**：`100 5`

**示例输出**：`287.50`

```python
h, n = map(float, input().split())
total = h
for _ in range(int(n)-1):
    h /= 2
    total += 2 * h
print("{0:.2f}".format(total))
```

### 21. 打印菱形
**题目描述**：输入n，打印n行菱形。

**输入**：一个正整数n

**输出**：n行菱形

**示例输入**：`5`

**示例输出**：
```
  *
 ***
*****
 ***
  *
```

```python
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
```

### 22. 数字反转
**题目描述**：输入一个整数，输出反转后的数。

**输入**：一个整数

**输出**：反转后的整数

**示例输入**：`12345`

**示例输出**：`54321`

```python
print(int(input()[::-1]))
```

### 23. 输出所有水仙花数
**题目描述**：输出所有三位水仙花数。

**输入**：无

**输出**：所有水仙花数，每行一个

```python
for n in range(100, 1000):
    a, b, c = n//100, n//10%10, n%10
    if a**3 + b**3 + c**3 == n:
        print(n)
```

### 24. 输出所有完数
**题目描述**：输出1000以内所有完数。

**输入**：无

**输出**：所有完数，每行一个

```python
for n in range(1, 1001):
    if sum(i for i in range(1, n) if n % i == 0) == n:
        print(n)
```

### 25. s=a+aa+aaa+aaaa+aa…a的值
**题目描述**：输入a和n，计算s=a+aa+aaa+aaaa+...+aa...a的值。

**输入**：a和n，用空格分隔

**输出**：s的值

**示例输入**：`2 5`

**示例输出**：`24690`

```python
a, n = map(int, input().split())
s = 0
for i in range(1, n+1):
    s += int(str(a) * i)
print(s)
```

### 26. 输出素数及统计个数
**题目描述**：输入范围[a,b]，输出该范围内所有素数及素数个数。

**输入**：两个整数a和b，用空格分隔

**输出**：先输出所有素数（空格分隔），再输出素数个数

**示例输入**：`1 20`

**示例输出**：
```
2 3 5 7 11 13 17 19
共8个素数
```

```python
a, b = map(int, input().split())
primes = []
for num in range(a, b+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(str(num))
print(' '.join(primes))
print(f"共{len(primes)}个素数")
```

### 27. 用1,2,3,4组成不重复的三位数
**题目描述**：有1,2,3,4四个数字，能组成多少个互不相同且无重复数字的三位数？输出所有可能的数及个数。

**输入**：无

**输出**：所有可能的三位数，每行一个，最后一行输出总数

```python
count = 0
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        for k in [1,2,3,4]:
            if i != j != k != i:
                print(i*100 + j*10 + k)
                count += 1
print(f"共{count}个")
```

### 28. 输出回文数及统计个数
**题目描述**：输入范围[a,b]，输出该范围内所有回文数及回文数个数。

**输入**：两个整数a和b，用空格分隔

**输出**：先输出所有回文数（空格分隔），再输出回文数个数

**示例输入**：`1 100`

**示例输出**：
```
1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99
共18个回文数
```

```python
a, b = map(int, input().split())
palindromes = []
for n in range(a, b+1):
    s = str(n)
    if s == s[::-1]:
        palindromes.append(str(n))
print(' '.join(palindromes))
print(f"共{len(palindromes)}个回文数")
```

### 29. 输出闰年及统计个数
**题目描述**：输入范围[a,b]，输出该范围内所有闰年及闰年个数。

**输入**：两个整数a和b，用空格分隔

**输出**：先输出所有闰年（空格分隔），再输出闰年个数

**示例输入**：`2000 2024`

**示例输出**：
```
2000 2004 2008 2012 2016 2020 2024
共7个闰年
```

```python
a, b = map(int, input().split())
leaps = []
for year in range(a, b+1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leaps.append(str(year))
print(' '.join(leaps))
print(f"共{len(leaps)}个闰年")
```

---

## 三、列表与元组

### 30. 列表求和
**题目描述**：输入n个数，求和。

**输入**：一行整数，用空格分隔

**输出**：和

**示例输入**：`1 2 3 4 5`

**示例输出**：`15`

```python
print(sum(list(map(int, input().split()))))
```

### 31. 列表平均值
**题目描述**：输入n个数，求平均值。

**输入**：一行整数，用空格分隔

**输出**：平均值（保留两位小数）

**示例输入**：`1 2 3 4 5`

**示例输出**：`3.00`

```python
nums = list(map(int, input().split()))
print("{0:.2f}".format(sum(nums)/len(nums)))
```

### 32. 列表最大最小值及其下标
**题目描述**：输入n个数，输出最大值、最小值及其下标。

**输入**：一行整数，用空格分隔

**输出**：最大值 最大值下标 最小值 最小值下标

**示例输入**：`1 3 5 2 4`

**示例输出**：`5 2 1 0`

```python
nums = list(map(int, input().split()))
max_val, min_val = max(nums), min(nums)
print(max_val, nums.index(max_val), min_val, nums.index(min_val))
```

### 33. 列表排序
**题目描述**：输入n个数，升序排序输出。

**输入**：一行整数，用空格分隔

**输出**：排序后的列表

**示例输入**：`5 2 9 1 5 6`

**示例输出**：`[1, 2, 5, 5, 6, 9]`

```python
nums = list(map(int, input().split()))
nums.sort()
print(nums)
```

### 34. 列表逆序
**题目描述**：输入n个数，逆序输出。

**输入**：一行整数，用空格分隔

**输出**：逆序后的列表

**示例输入**：`1 2 3 4 5`

**示例输出**：`[5, 4, 3, 2, 1]`

```python
print(list(map(int, input().split()))[::-1])
```

### 35. 列表去重
**题目描述**：输入n个数，去除重复元素输出（保持原顺序）。

**输入**：一行整数，用空格分隔

**输出**：去重后的列表

**示例输入**：`3 1 4 1 5 9 2 6`

**示例输出**：`[3, 1, 4, 5, 9, 2, 6]`

```python
nums = list(map(int, input().split()))
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print(unique)
```

### 36. 列表元素查找
**题目描述**：输入列表和目标值，查找目标值是否存在及位置。

**输入**：第一行是整数列表，第二行是目标值

**输出**：存在则输出所有位置（空格分隔），否则输出"不存在"

**示例输入**：
```
1 3 5 3 7 9
3
```

**示例输出**：`1 3`

```python
nums = list(map(int, input().split()))
target = int(input())
positions = [str(i) for i, v in enumerate(nums) if v == target]
print(' '.join(positions) if positions else "不存在")
```

### 37. 列表元素插入
**题目描述**：输入有序列表、值和位置，在指定位置插入值。

**输入**：第一行是整数列表，第二行是值，第三行是位置

**输出**：插入后的列表

**示例输入**：
```
1 3 5 7 9
4
2
```

**示例输出**：`[1, 3, 4, 5, 7, 9]`

```python
nums = list(map(int, input().split()))
nums.insert(int(input()), int(input()))
print(nums)
```

### 38. 数组合并
**题目描述**：输入两个列表，合并输出。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：合并后的列表

**示例输入**：
```
1 2 3
4 5 6
```

**示例输出**：`[1, 2, 3, 4, 5, 6]`

```python
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(list1 + list2)
```

### 39. 列表第二大的数
**题目描述**：输入列表，输出第二大的数。

**输入**：一行整数，用空格分隔

**输出**：第二大的数，不存在则输出"不存在"

**示例输入**：`1 3 5 7 9 5`

**示例输出**：`7`

```python
nums = list(map(int, input().split()))
unique = sorted(set(nums), reverse=True)
print(unique[1] if len(unique) >= 2 else "不存在")
```

### 40. 列表旋转
**题目描述**：输入列表和步数k，实现列表左旋转k步。

**输入**：第一行是整数列表，用空格分隔；第二行是k

**输出**：旋转后的列表

**示例输入**：
```
1 2 3 4 5 6 7
3
```

**示例输出**：`[4, 5, 6, 7, 1, 2, 3]`

```python
nums = list(map(int, input().split()))
k = int(input()) % len(nums)
print(nums[k:] + nums[:k])
```

### 41. 列表分组
**题目描述**：输入列表，按奇偶分组。

**输入**：一行整数，用空格分隔

**输出**：两行，第一行奇数列表，第二行偶数列表

**示例输入**：`1 2 3 4 5 6 7 8 9`

**示例输出**：
```
[1, 3, 5, 7, 9]
[2, 4, 6, 8]
```

```python
nums = list(map(int, input().split()))
odds = [x for x in nums if x % 2 == 1]
evens = [x for x in nums if x % 2 == 0]
print(odds)
print(evens)
```

### 42. 矩阵转置
**题目描述**：输入n行m列矩阵，输出转置矩阵。

**输入**：第一行是n和m，接下来n行是矩阵元素

**输出**：转置后的矩阵，每行用空格分隔

**示例输入**：
```
2 3
1 2 3
4 5 6
```

**示例输出**：
```
1 4
2 5
3 6
```

```python
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for j in range(m):
    print(' '.join(str(matrix[i][j]) for i in range(n)))
```

### 43. 杨辉三角
**题目描述**：输入n，输出n行杨辉三角。

**输入**：一个正整数n

**输出**：n行杨辉三角，每行用空格分隔

**示例输入**：`5`

**示例输出**：
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

```python
n = int(input())
triangle = []
for i in range(n):
    row = [1]
    if i > 0:
        prev = triangle[i-1]
        row.extend([prev[j-1]+prev[j] for j in range(1, i)])
        row.append(1)
    triangle.append(row)
    print(' '.join(map(str, row)))
```

### 44. 元组创建与访问
**题目描述**：输入多个整数，创建元组并访问指定位置元素。

**输入**：第一行是整数列表，第二行是索引

**输出**：指定索引的元素

**示例输入**：
```
1 2 3 4 5
2
```

**示例输出**：`3`

```python
t = tuple(map(int, input().split()))
index = int(input())
print(t[index])
```

### 45. 元组拆包
**题目描述**：输入三个整数，创建元组并拆包输出。

**输入**：三个整数，用空格分隔

**输出**：三个变量的值，每行一个

**示例输入**：`10 20 30`

**示例输出**：
```
10
20
30
```

```python
a, b, c = map(int, input().split())
print(a)
print(b)
print(c)
```

### 46. 元组拼接
**题目描述**：输入两个元组，拼接后输出。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：拼接后的元组

**示例输入**：
```
1 2 3
4 5 6
```

**示例输出**：`(1, 2, 3, 4, 5, 6)`

```python
t1 = tuple(map(int, input().split()))
t2 = tuple(map(int, input().split()))
print(t1 + t2)
```

### 47. 元组与列表转换
**题目描述**：输入列表，转换为元组输出。

**输入**：一行整数，用空格分隔

**输出**：转换后的元组

**示例输入**：`1 2 3 4 5`

**示例输出**：`(1, 2, 3, 4, 5)`

```python
lst = list(map(int, input().split()))
print(tuple(lst))
```

### 48. 列表生成式
**题目描述**：输入n，用列表生成式生成1到n的平方列表。

**输入**：一个正整数n

**输出**：平方列表

**示例输入**：`5`

**示例输出**：`[1, 4, 9, 16, 25]`

```python
n = int(input())
print([i*i for i in range(1, n+1)])
```

### 49. 二维列表创建
**题目描述**：输入n和m，创建n行m列的零矩阵。

**输入**：两个正整数n和m

**输出**：n行m列的零矩阵

**示例输入**：`3 4`

**示例输出**：`[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

```python
n, m = map(int, input().split())
print([[0]*m for _ in range(n)])
```

### 50. 对10个数进行排序（冒泡排序）
**题目描述**：使用冒泡排序对10个数进行升序排序。

**参考运行结果**：
```
排序前: [64, 34, 25, 12, 22, 11, 90, 5, 45, 18]
排序后: [5, 11, 12, 18, 22, 25, 34, 45, 64, 90]
```

```python
nums = [64, 34, 25, 12, 22, 11, 90, 5, 45, 18]
print(f"排序前: {nums}")
n = len(nums)
for i in range(n):
    for j in range(0, n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(f"排序后: {nums}")
```

### 51. 对10个数进行排序（选择排序）
**题目描述**：使用选择排序对10个数进行升序排序。

**参考运行结果**：
```
排序前: [64, 34, 25, 12, 22, 11, 90, 5, 45, 18]
排序后: [5, 11, 12, 18, 22, 25, 34, 45, 64, 90]
```

```python
nums = [64, 34, 25, 12, 22, 11, 90, 5, 45, 18]
print(f"排序前: {nums}")
n = len(nums)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
print(f"排序后: {nums}")
```

### 52. 矩阵对角线之和
**题目描述**：计算3×3矩阵的主对角线元素之和。

**参考运行结果**：
```
矩阵:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
主对角线之和: 15
```

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("矩阵:")
for row in matrix:
    print(row)
total = 0
for i in range(len(matrix)):
    total += matrix[i][i]
print(f"主对角线之和: {total}")
```

### 53. 矩阵相加
**题目描述**：计算两个2×2矩阵的和。

**参考运行结果**：
```
矩阵1:
[[1, 2],
 [3, 4]]
矩阵2:
[[5, 6],
 [7, 8]]
矩阵和:
[[6, 8],
 [10, 12]]
```

```python
matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]
print("矩阵1:")
for row in matrix1:
    print(row)
print("矩阵2:")
for row in matrix2:
    print(row)
result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("矩阵和:")
for row in result:
    print(row)
```

---

## 四、字符串处理

### 50. 字符串长度
**题目描述**：输入字符串，输出长度。

**输入**：一个字符串

**输出**：长度

**示例输入**：`Hello World`

**示例输出**：`11`

```python
print(len(input()))
```

### 51. 字符串反转
**题目描述**：输入字符串，输出反转后的字符串。

**输入**：一个字符串

**输出**：反转后的字符串

**示例输入**：`Hello World`

**示例输出**：`dlroW olleH`

```python
print(input()[::-1])
```

### 52. 字符串统计字母、数字、空格个数
**题目描述**：输入字符串，统计字母、数字、空格的个数。

**输入**：一个字符串

**输出**：字母个数 数字个数 空格个数

**示例输入**：`Hello World 123!`

**示例输出**：`10 3 2`

```python
s = input()
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
spaces = s.count(' ')
print(letters, digits, spaces)
```

### 53. 字符串回文判断
**题目描述**：输入字符串，判断是否为回文。

**输入**：一个字符串

**输出**："是回文"或"不是回文"

**示例输入**：`abba`

**示例输出**：`是回文`

```python
s = input()
print("是回文" if s == s[::-1] else "不是回文")
```

### 54. 字符串加密（凯撒密码）
**题目描述**：输入字符串和偏移量，输出加密结果（只加密字母）。

**输入**：第一行是字符串，第二行是偏移量

**输出**：加密后的字符串

**示例输入**：
```
Hello World
3
```

**示例输出**：`Khoor Zruog`

```python
s = input()
offset = int(input())
result = ''
for c in s:
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        result += chr((ord(c)-base+offset) % 26 + base)
    else:
        result += c
print(result)
```

### 55. 字符串切片
**题目描述**：输入字符串和起始、结束位置，输出切片结果。

**输入**：第一行是字符串，第二行是起始位置，第三行是结束位置

**输出**：切片结果

**示例输入**：
```
Hello World
0
5
```

**示例输出**：`Hello`

```python
s = input()
print(s[int(input()):int(input())])
```

### 56. 字符串重复
**题目描述**：输入字符串和次数n，将字符串重复n次输出。

**输入**：第一行是字符串，第二行是n

**输出**：重复后的字符串

**示例输入**：
```
Hello
3
```

**示例输出**：`HelloHelloHello`

```python
print(input() * int(input()))
```

### 57. 字符串方法练习
**题目描述**：输入字符串，练习字符串的常用方法。

**输入**：一个字符串

**输出**：输出字符串的大写、小写、去空格、长度

**示例输入**：`  Hello World  `

**示例输出**：
```
HELLO WORLD
hello world
Hello World
11
```

```python
s = input()
print(s.upper())
print(s.lower())
print(s.strip())
print(len(s))
```

### 58. 字符串查找与替换
**题目描述**：输入字符串、旧子串、新子串，查找位置并替换。

**输入**：三行，分别是原字符串、旧子串、新子串

**输出**：替换后的字符串及位置

**示例输入**：
```
Hello World
World
Python
```

**示例输出**：
```
Hello Python
6
```

```python
s = input()
old = input()
new = input()
print(s.replace(old, new))
print(s.find(old))
```

### 59. 字符串分割与统计
**题目描述**：输入字符串，统计单词个数。

**输入**：一个字符串

**输出**：单词个数及单词列表

**示例输入**：`Hello World Python Java`

**示例输出**：
```
4
['Hello', 'World', 'Python', 'Java']
```

```python
s = input()
words = s.split()
print(len(words))
print(words)
```

### 60. 字符串判断
**题目描述**：输入字符串，判断是否为数字、是否全为字母。

**输入**：一个字符串

**输出**：是否数字 是否字母

**示例输入**：`Hello123`

**示例输出**：`否 是`

```python
s = input()
print("是" if s.isdigit() else "否", end=" ")
print("是" if s.isalpha() else "否")
```

---

## 五、字典操作

### 61. 字典基本操作
**题目描述**：输入键值对，创建字典并输出。

**输入**：第一行是n，接下来n行是键和值

**输出**：字典

**示例输入**：
```
2
a 1
b 2
```

**示例输出**：`{'a': 1, 'b': 2}`

```python
n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
print(d)
```

### 62. 字典键值对查找
**题目描述**：输入字典和键，查找对应的值。

**输入**：第一行是字典，第二行是键

**输出**：对应的值，不存在则输出"不存在"

**示例输入**：
```
{'name': 'Tom', 'age': 20}
name
```

**示例输出**：`Tom`

```python
d = eval(input())
key = input()
print(d.get(key, "不存在"))
```

### 63. 字典遍历（遍历键）
**题目描述**：输入字典，遍历并输出所有键。

**输入**：一个字典

**输出**：所有键，空格分隔

**示例输入**：`{'a': 1, 'b': 2, 'c': 3}`

**示例输出**：`a b c`

```python
d = eval(input())
print(' '.join(d.keys()))
```

### 64. 字典遍历（遍历值）
**题目描述**：输入字典，遍历并输出所有值。

**输入**：一个字典

**输出**：所有值，空格分隔

**示例输入**：`{'a': 1, 'b': 2, 'c': 3}`

**示例输出**：`1 2 3`

```python
d = eval(input())
print(' '.join(map(str, d.values())))
```

### 65. 字典遍历（遍历键值对）
**题目描述**：输入字典，遍历并输出所有键值对。

**输入**：一个字典

**输出**：每行一个键值对，格式为"key: value"

**示例输入**：`{'name': 'Tom', 'age': 20}`

**示例输出**：
```
name: Tom
age: 20
```

```python
d = eval(input())
for k, v in d.items():
    print(f"{k}: {v}")
```

### 66. 字典统计单词频率
**题目描述**：输入文本，统计每个单词出现次数。

**输入**：一行文本

**输出**：单词频率字典

**示例输入**：`hello world hello python`

**示例输出**：`{'hello': 2, 'world': 1, 'python': 1}`

```python
freq = {}
for word in input().split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
```

### 67. 字典合并
**题目描述**：输入两个字典，合并后输出。

**输入**：两行，每行是一串键值对，格式为"键1:值1 键2:值2"

**输出**：合并后的字典

**示例输入**：
```
a:1 b:2
b:3 c:4
```

**示例输出**：`{'a': 1, 'b': 3, 'c': 4}`

```python
d1 = {}
for item in input().split():
    k, v = item.split(':')
    d1[k] = int(v)
d2 = {}
for item in input().split():
    k, v = item.split(':')
    d2[k] = int(v)
d1.update(d2)
print(d1)
```

### 68. 字典键值对删除
**题目描述**：输入字典和键，删除该键值对。

**输入**：第一行是一串键值对，格式为"键1:值1 键2:值2"，第二行是键

**输出**：删除后的字典

**示例输入**：
```
a:1 b:2 c:3
b
```

**示例输出**：`{'a': 1, 'c': 3}`

```python
d = {}
for item in input().split():
    k, v = item.split(':')
    d[k] = int(v)
key = input()
if key in d:
    del d[key]
print(d)
```

---

## 六、集合操作

### 65. 集合创建与去重
**题目描述**：输入列表，转换为集合去重后输出。

**输入**：一行整数，用空格分隔

**输出**：去重后的集合

**示例输入**：`1 2 2 3 3 3 4 5`

**示例输出**：`{1, 2, 3, 4, 5}`

```python
nums = list(map(int, input().split()))
print(set(nums))
```

### 70. 集合添加元素
**题目描述**：输入集合和元素，添加元素后输出。

**输入**：第一行是一串整数，用空格分隔，第二行是元素

**输出**：添加后的集合

**示例输入**：
```
1 2 3
4
```

**示例输出**：`{1, 2, 3, 4}`

```python
nums = list(map(int, input().split()))
s = set(nums)
s.add(int(input()))
print(s)
```

### 71. 集合删除元素
**题目描述**：输入集合和元素，删除元素后输出。

**输入**：第一行是一串整数，用空格分隔，第二行是元素

**输出**：删除后的集合

**示例输入**：
```
1 2 3 4
3
```

**示例输出**：`{1, 2, 4}`

```python
nums = list(map(int, input().split()))
s = set(nums)
s.discard(int(input()))
print(s)
```

### 72. 集合交集
**题目描述**：输入两个集合，输出交集。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：交集

**示例输入**：
```
1 2 3 4
3 4 5 6
```

**示例输出**：`{3, 4}`

```python
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 & s2)
```

### 73. 集合并集
**题目描述**：输入两个集合，输出并集。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：并集

**示例输入**：
```
1 2 3 4
3 4 5 6
```

**示例输出**：`{1, 2, 3, 4, 5, 6}`

```python
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 | s2)
```

### 74. 集合差集
**题目描述**：输入两个集合，输出差集（s1 - s2）。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：差集

**示例输入**：
```
{1, 2, 3, 4}
{3, 4, 5, 6}
```

**示例输出**：`{1, 2}`

```python
s1 = eval(input())
s2 = eval(input())
print(s1 - s2)
```

### 75. 集合对称差集
**题目描述**：输入两个集合，输出对称差集。

**输入**：两行，每行是一串整数，用空格分隔

**输出**：对称差集

**示例输入**：
```
1 2 3 4
3 4 5 6
```

**示例输出**：`{1, 2, 5, 6}`

```python
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(s1 ^ s2)
```

### 76. 集合子集判断
**题目描述**：输入两个集合，判断第一个是否是第二个的子集。

**输入**：两行，每行是一串整数，用空格分隔

**输出**："是子集"或"不是子集"

**示例输入**：
```
1 2
1 2 3 4
```

**示例输出**：`是子集`

```python
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print("是子集" if s1 <= s2 else "不是子集")
```

---

## 七、函数与递归

### 77. 函数交换两个数字
**题目描述**：编写函数交换两个数字的值。

**输入**：两个整数，用空格分隔

**输出**：交换后的两个整数

**示例输入**：`10 20`

**示例输出**：`20 10`

```python
def swap(a, b):
    return b, a

a, b = map(int, input().split())
a, b = swap(a, b)
print(a, b)
```

### 78. 函数递归求阶乘
**题目描述**：编写递归函数计算n的阶乘。

**输入**：一个非负整数n

**输出**：n的阶乘

**示例输入**：`5`

**示例输出**：`120`

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(int(input())))
```

### 79. 函数求阶乘（循环）
**题目描述**：编写循环函数计算n的阶乘。

**参考运行结果**：
```
5的阶乘: 120
```

```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = 5
print(f"{n}的阶乘: {factorial(n)}")
```

### 80. 函数判断闰年
**题目描述**：编写函数判断是否为闰年。

**输入**：一个年份

**输出**："闰年"或"平年"

**示例输入**：`2024`

**示例输出**：`闰年`

```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

year = int(input())
print("闰年" if is_leap(year) else "平年")
```

### 81. 函数求斐波那契数列（循环）
**题目描述**：编写函数求斐波那契数列第n项。

**输入**：一个正整数n

**输出**：斐波那契数列第n项

**示例输入**：`10`

**示例输出**：`55`

```python
def fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

print(fib(int(input())))
```

### 82. 函数求斐波那契数列（递归）
**题目描述**：编写递归函数求斐波那契数列第n项。

**输入**：一个正整数n

**输出**：斐波那契数列第n项

**示例输入**：`10`

**示例输出**：`55`

```python
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(int(input())))
```

### 83. 函数判断素数
**题目描述**：编写函数判断素数。

**输入**：一个正整数n

**输出**：True或False

**示例输入**：`17`

**示例输出**：`True`

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(int(input())))
```

### 84. 函数求最大公约数和最小公倍数
**题目描述**：编写函数求最大公约数和最小公倍数。

**输入**：两个正整数a和b，用空格分隔

**输出**：GCD和LCM，用空格分隔

**示例输入**：`12 18`

**示例输出**：`6 36`

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b), lcm(a, b))
```

### 84. 函数冒泡排序
**题目描述**：编写函数实现冒泡排序。

**输入**：一行整数，用空格分隔

**输出**：排序后的列表

**示例输入**：`5 2 9 1 5 6`

**示例输出**：`[1, 2, 5, 5, 6, 9]`

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(list(map(int, input().split()))))
```

### 86. 函数二分查找
**题目描述**：编写函数实现二分查找。

**输入**：第一行是有序列表，第二行是目标值

**输出**：目标值位置，不存在输出-1

**示例输入**：
```
1 3 5 7 9 11
7
```

**示例输出**：`3`

```python
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = list(map(int, input().split()))
print(binary_search(nums, int(input())))
```

---

## 八、面向对象综合题

### 87. 学生信息类
**题目描述**：定义Student类，包含姓名、年龄、专业属性，以及显示信息的方法。

**要求**：
- 类名为Student
- __init__方法初始化name、age、major属性
- show_info()方法打印学生信息

**参考运行结果**：
```
姓名: 张三, 年龄: 18, 专业: 软件技术
姓名: 李四, 年龄: 19, 专业: 大数据技术
```

```python
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def show_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 专业: {self.major}")

stu1 = Student("张三", 18, "软件技术")
stu2 = Student("李四", 19, "大数据技术")
stu1.show_info()
stu2.show_info()
```

### 88. 银行账户类
**题目描述**：定义BankAccount类，实现存款和取款功能。

**要求**：
- 类名为BankAccount
- __init__方法初始化账户名name和余额balance（默认0）
- deposit(money)方法实现存款，存款金额必须大于0
- withdraw(money)方法实现取款，余额不足时提示失败

**参考运行结果**：
```
张三存款成功，当前余额: 1500元
张三取款成功，当前余额: 1000元
余额不足，取款失败
```

```python
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"{self.name}存款成功，当前余额: {self.balance}元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, money):
        if self.balance < money:
            print("余额不足，取款失败")
            return
        self.balance -= money
        print(f"{self.name}取款成功，当前余额: {self.balance}元")

account = BankAccount("张三", 1000)
account.deposit(500)
account.withdraw(500)
account.withdraw(600)
```

### 89. 图形类继承与多态
**题目描述**：定义Shape基类和Circle、Rectangle子类，计算面积。

**要求**：
- Shape为基类，包含area()方法
- Circle类继承Shape，计算圆面积
- Rectangle类继承Shape，计算矩形面积
- 演示多态特性

**参考运行结果**：
```
圆的面积: 78.54
矩形的面积: 24
```

```python
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    if isinstance(shape, Circle):
        print(f"圆的面积: {shape.area():.2f}")
    elif isinstance(shape, Rectangle):
        print(f"矩形的面积: {shape.area()}")
```

### 90. 房屋物品类
**题目描述**：定义HouseItem类，表示房间里的物品。

**要求**：
- 类名为HouseItem
- __init__方法初始化名称name、面积area、位置location
- show_info()方法输出物品信息

**参考运行结果**：
```
物品: 床, 占地面积: 4.0, 放置位置: 卧室
物品: 桌子, 占地面积: 1.5, 放置位置: 书房
物品: 沙发, 占地面积: 3.0, 放置位置: 客厅
```

```python
class HouseItem:
    def __init__(self, name, area, location):
        self.name = name
        self.area = area
        self.location = location
    
    def show_info(self):
        print(f"物品: {self.name}, 占地面积: {self.area}, 放置位置: {self.location}")

bed = HouseItem("床", 4.0, "卧室")
table = HouseItem("桌子", 1.5, "书房")
sofa = HouseItem("沙发", 3.0, "客厅")
bed.show_info()
table.show_info()
sofa.show_info()
```

### 91. 动物叫声模拟器（多态）
**题目描述**：定义Animal基类和Dog、Cat、Bird子类，体现多态特性。

**要求**：
- Animal为基类，包含speak()方法
- Dog、Cat、Bird子类重写speak()方法
- 创建动物列表，遍历调用speak()方法

**参考运行结果**：
```
狗: 汪汪汪
猫: 喵喵喵
鸟: 叽叽叽
```

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

class Bird(Animal):
    def speak(self):
        return "叽叽叽"

animals = [Dog(), Cat(), Bird()]
names = ["狗", "猫", "鸟"]
for name, animal in zip(names, animals):
    print(f"{name}: {animal.speak()}")
```

### 92. 汽车类
**题目描述**：定义Car类，实现汽车的基本功能。

**要求**：
- 类名为Car
- __init__方法初始化品牌brand、颜色color、速度speed（默认0）
- accelerate()方法加速，每次增加10
- brake()方法减速，每次减少10，速度不能小于0
- show_speed()方法显示当前速度

**参考运行结果**：
```
宝马汽车当前速度: 0 km/h
加速后速度: 10 km/h
加速后速度: 20 km/h
刹车后速度: 10 km/h
刹车后速度: 0 km/h
```

```python
class Car:
    def __init__(self, brand, color, speed=0):
        self.brand = brand
        self.color = color
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
        print(f"加速后速度: {self.speed} km/h")
    
    def brake(self):
        self.speed = max(0, self.speed - 10)
        print(f"刹车后速度: {self.speed} km/h")
    
    def show_speed(self):
        print(f"{self.brand}汽车当前速度: {self.speed} km/h")

my_car = Car("宝马", "黑色")
my_car.show_speed()
my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_car.brake()
```

---

## 九、文件操作

### 93. 文件内容读取
**题目描述**：读取文件内容并输出。

**参考运行结果**：
```
文件内容:
Hello World
Python Programming
```

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World\nPython Programming')
with open('test.txt', 'r', encoding='utf-8') as f:
    print("文件内容:")
    print(f.read())
```

### 94. 文件内容写入
**题目描述**：将内容写入文件。

**参考运行结果**：
```
写入成功
```

```python
content = "Hello Python"
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("写入成功")
```

### 95. 文件内容追加
**题目描述**：将内容追加到文件末尾。

**参考运行结果**：
```
追加成功
```

```python
content = " is great!"
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write(content)
print("追加成功")
```

### 96. 文件行数统计
**题目描述**：统计文件的行数。

**参考运行结果**：
```
文件行数: 3
```

```python
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Line 1\nLine 2\nLine 3')
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f"文件行数: {len(f.readlines())}")
```

### 97. 检查文件是否存在
**题目描述**：检查指定文件是否存在。

**参考运行结果**：
```
test.txt 存在
not_exist.txt 不存在
```

```python
import os
print(f"test.txt {'存在' if os.path.exists('test.txt') else '不存在'}")
print(f"not_exist.txt {'存在' if os.path.exists('not_exist.txt') else '不存在'}")
```

### 98. 文件单词统计
**题目描述**：统计文件中的单词个数（空格分隔）。

**参考运行结果**：
```
文件中的单词个数: 6
```

```python
with open('words.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World Python Programming is fun')
with open('words.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    print(f"文件中的单词个数: {len(words)}")
```

### 99. 文件复制
**题目描述**：复制一个文件到指定位置。

**参考运行结果**：
```
文件复制成功
```

```python
import shutil
with open('source.txt', 'w', encoding='utf-8') as f:
    f.write('This is the source file content')
shutil.copy('source.txt', 'target.txt')
print("文件复制成功")
```

### 100. 文件重命名
**题目描述**：重命名文件。

**参考运行结果**：
```
文件重命名成功
```

```python
import os
with open('old_name.txt', 'w', encoding='utf-8') as f:
    f.write('Rename me')
os.rename('old_name.txt', 'new_name.txt')
print("文件重命名成功")
```

---

## 题目分类总结

| 类型 | 题目数量 |
|------|----------|
| 基础变量+判断 | 10题 |
| 循环计算 | 19题 |
| 列表与元组 | 24题 |
| 字符串处理 | 11题 |
| 字典操作 | 8题 |
| 集合操作 | 4题 |
| 函数与递归 | 10题 |
| 面向对象 | 6题 |
| 文件操作 | 8题 |
| **总计** | **100题** |