# Python常考编程100题

## 目录

- [一、基础输入输出 & 变量](#一、基础输入输出 & 变量)
- [二、分支if判断](#二、分支if判断)
- [三、循环for/while](#三、循环for/while)
- [四、列表基础操作](#四、列表基础操作)
- [五、字典 & 字符串](#五、字典 & 字符串)
- [六、函数定义调用](#六、函数定义调用)
- [七、 面向对象编程 ](#第七部分 面向对象编程)
- [八、文件操作 & 综合编程](#八、文件操作 & 综合编程)

## 一、基础输入输出 & 变量

### 输入姓名，输出：你好，XXX

```python
name = input("请输入姓名：")
print(f"你好，{name}")
```

### 输入两个整数，求和、差、积、商

```python
a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
print("和：", a+b)
print("差：", a-b)
print("积：", a*b)
print("商：", a/b)
```

### 输入圆半径，计算周长和面积

```python
r = float(input("输入半径："))
pi = 3.14
print("周长：", 2*pi*r)
print("面积：", pi*r*r)
```

### 输入摄氏温度，转华氏温度

```python
c = float(input("输入摄氏温度："))
f = c * 9 / 5 + 32
print("华氏温度：", f)
```

### 输入三角形三边，求周长

```python
a = float(input("边长1："))
b = float(input("边长2："))
c = float(input("边长3："))
print("周长：", a+b+c)
```

### 输入一个数字，输出它的平方、立方

```python
n = int(input("输入数字："))
print("平方：", n**2)
print("立方：", n**3)
```

### 输入身高体重，计算BMI指数

```python
h = float(input("身高(m)："))
w = float(input("体重(kg)："))
bmi = w / h**2
print("BMI：", bmi)
```

### 输入秒数，换算成时分秒

```python
s = int(input("输入秒数："))
h = s // 3600
m = s % 3600 // 60
sec = s % 60
print(f"{h}时{m}分{sec}秒")
```

### 输入三位数，逆序输出

```python
n = input("输入三位数：")
print(n[::-1])
```

### 求一个数的最大公约数，最小公倍数

```python
# 求两个数最大公约数、最小公倍数
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))

x, y = a, b
# 辗转相除法求最大公约数
while y != 0:
    x, y = y, x % y
gcd = x

# 最小公倍数 = 两数乘积 ÷ 最大公约数
lcm = a * b // gcd

print("最大公约数：", gcd)
print("最小公倍数：", lcm)
```

## 二、分支if判断

### 输入一个数，判断是正数、负数还是0

```python
n = int(input())
if n > 0:
    print("正数")
elif n < 0:
    print("负数")
else:
    print("零")
```

### 输入一个整数，判断奇偶性

```python
n = int(input())
print("偶数" if n%2==0 else "奇数")
```

### 输入成绩，按优秀、良好、及格、不及格评级

```python
s = int(input("输入成绩："))
if s >= 90:
    print("优秀")
elif s >= 80:
    print("良好")
elif s >= 60:
    print("及格")
else:
    print("不及格")
```

### 输入三个整数，找出最大值

```python
a,b,c = map(int,input().split())
print(max(a,b,c))
```

### 输入年份，判断是否闰年

```python
y = int(input("输入年份："))
if (y%4==0 and y%100!=0) or y%400==0:
    print("闰年")
else:
    print("平年")
```

### 判断一个数能否同时被3和5整除

```python
n = int(input())
print("能同时整除" if n%3==0 and n%5==0 else "不能")
```

### 输入三条边长，判断能否构成三角形

```python
a,b,c = map(float,input().split())
if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
else:
    print("不能")
```

### 输入月份，判断所属季节

```python
m = int(input("月份："))
if m in [3,4,5]:
    print("春季")
elif m in [6,7,8]:
    print("夏季")
elif m in [9,10,11]:
    print("秋季")
else:
    print("冬季")
```

### 按重量分段计算快递运费

```python
w = float(input("重量kg："))
if w <= 1:
    print("运费10元")
else:
    print("运费", 10 + (w-1)*3)
```

### 输入两个数，按从小到大顺序输出

```python
a,b = map(int,input().split())
if a > b:
    a,b = b,a
print(a,b)
 
```

### 消费金额按满减打折计算

```python
price = float(input("金额："))
if price >= 200:
    print("折后：", price*0.8)
elif price >= 100:
    print("折后：", price*0.9)
else:
    print("原价：", price)
```

### 输入一个数，判断是否为素数

```python
n = int(input())
flag = True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
print("素数" if flag else "不是素数")
```

## 三、循环for/while

### 计算1到100累加和

```python
s = 0
for i in range(1,101):
    s += i
print(s)
```

### 输入n，计算1到n累加和

```python
n = int(input())
s = sum(range(1,n+1))
print(s)
```

### 计算1到100平方和

```python
s = 0
for i in range(1,101):
    s += i*i
print(s)
```

### 输出1~100内能被7整除的数

```python
for i in range(1,101):
    if i%7==0:
        print(i,end=" ")
```

### 打印正序九九乘法表

```python
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()
```

### 画菱形

```python
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(1,8,2):
    t = (7-i)//2
    print(' '*t + '*'*i)
for y in range(7-2,0,-2):
    x = (7-y)//2
    print(' '*x+y*'*')
```

### 输入行数，打印星号三角形

```python
n = int(input("行数："))
for i in range(1,n+1):
    print("*"*i)
```

### 计算n的阶乘

```python
n = int(input())
res = 1
for i in range(1,n+1):
    res *= i
print(res)
```

### 求1+2!+3!+…+20!的和

```python
total = 0
factorial = 1

for i in range(1, 21):
    factorial *= i      # 计算 i!
    total += factorial   # 累加

print("=" * 45)
print(f"总和 = {total}")

```

### 输出斐波那契数列前20项

```python
a,b = 1,1
print(a,b,end=" ")
for _ in range(18):
    c = a+b
    print(c,end=" ")
    a,b = b,c
```

### 输入多位数，逐位数字求和

```python
n = input()
s = 0
for ch in n:
    s += int(ch)
print(s)
```

### 判断101-200之间有多少个素数，并输出所有素数

```python
import math

total = 0  # 计数器

for i in range(100, 200):
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        total += 1  # 是素数，计数器+1
        print(i, end=' ')

print(f'\n\n100-200之间共有 {total} 个素数')

```

### 计算 1+1/2+1/3+…+1/n

```python
n = int(input())
s = 0
for i in range(1,n+1):
    s += 1/i
print(s)
```

### s=a+aa+aaa+aaaa+aa…a的值

```python
a = int(input("请输入数字a（0-9）："))
n = int(input("请输入项数n："))

res=0
for i in range(n):
    res+=int(a)
    a+=a[0]
print('结果是：',res)
```

### 输出所有三位数水仙花数

```python
for i in range(100,1000):
    a = i//100
    b = i//10%10
    c = i%10
    if a**3+b**3+c**3 == i:
        print(i)
```

### 找出1000以内的所有完数

```python
print("1000以内的完数：")

for num in range(2, 1001):
    factors_sum = 1
    factors = [1]
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors_sum += i
            factors.append(i)
            if i != num // i:
                factors_sum += num // i
                factors.append(num // i)
    
    if factors_sum == num:
        print(f"{num}  →  因数：{factors}")
```

### 将一个整数分解质因数

```python
num = int(input("请输入一个整数："))
n = num
i = 2

print(f"{num} = ", end="")

while i * i <= n:
    while n % i == 0:
        print(i, end="")
        n //= i
        if n > 1:
            print("*", end="")
    i += 1

if n > 1:
    print(n, end="")

print()

```

### 高空抛物问题

```python
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
Sn = 100.0
Hn = Sn / 2
for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2
print('这个球的总路线长度是： %f' % Sn)
print ('第10次反弹的高度是%f 米' % Hn)
```

### 猴子吃桃问题

```python
#猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半再加一个。到第10天早上再吃时，发现只剩下一个桃子。求第一天共摘了多少个桃子

total = 1  # 第10天桃子剩1个
for d in range(9, 0, -1):  # 逆着推算，每次减1
    total = (total + 1) * 2  # 前一天的桃子是当前桃子数加1的两倍
print(f'第{d}天的桃子数为：{total}')  # 打印出第1天共摘了多少桃子
```

### 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

```python
count = 0
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (x !=z ) and (y != z):
                print("%d%d%d" % (x, y, z), end='  ')
                count += 1
    print('')
print('最终结果为：%s个' % count)
```

## 四、列表基础操作

### 求列表最大值、最小值、平均值

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    num = int(input(f"请输入第{i+1}个数字："))
    lst.append(num)

print("最大值",max(lst))
print("最小值",min(lst))
print("平均值",sum(lst)/len(lst))
```

### 将列表元素逆序输出

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    num = int(input(f"请输入第{i+1}个数字："))
    lst.append(num)

print(lst[::-1])
```

### 实现列表元素去重

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    num = int(input(f"请输入第{i+1}个数字："))
    lst.append(num)

new_lst = list(set(lst))
print(new_lst)
```

### 合并两个列表

```python
n1 = int(input("第一个列表个数："))
lst1 = []
for i in range(n1):
    lst1.append(int(input()))

n2 = int(input("第二个列表个数："))
lst2 = []
for i in range(n2):
    lst2.append(int(input()))

print(lst1+lst2)
```

### 统计列表中某个元素出现次数

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

x = int(input("请输入要查找的数字："))
print(lst.count(x))
```

### 对10个数进行排序（冒泡）

```python
# 获取用户输入的10个数字
raw = []
for i in range(10):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

# 冒泡排序算法
n = len(raw)
for i in range(n):
    # 最后i个元素已经排好序，不需要再比较
    for j in range(0, n-i-1):
        # 如果当前元素大于下一个元素，则交换它们
        if raw[j] > raw[j+1]:
            raw[j], raw[j+1] = raw[j+1], raw[j]

# 输出排序后的结果
print("排序后的结果:", raw)
```

### 对10个数进行排序（选择）

```python
raw=[]
for i in range(10):
    x=int(input('int%d: '%(i)))
    raw.append(x)
 
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)
```

### 筛选出列表中所有偶数

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

res = [x for x in lst if x%2==0]
print(res)
```

### 删除列表指定下标元素

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

idx = int(input("请输入要删除的下标："))
del lst[idx]
print(lst)
```

### 在列表指定位置插入元素

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

pos = int(input("插入位置："))
num = int(input("插入数字："))
lst.insert(pos,num)
print(lst)
```

### 生成 10 个随机整数存入列表

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    num = int(input(f"第{i+1}个数："))
    lst.append(num)
print(lst)
```

### 对列表进行切片取前 3 个、后 3 个

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

print("前3个",lst[:3])
print("后3个",lst[-3:])
```

### 遍历打印二维列表所有元素

```python
row = int(input("输入行数："))
col = int(input("输入列数："))
arr = []
for i in range(row):
    line = list(map(int,input(f"第{i+1}行：").split()))
    arr.append(line)

for r in arr:
    for x in r:
        print(x,end=" ")
    print()
```

### 计算列表所有元素总和

```python
n = int(input("请输入数字个数："))
lst = []
for i in range(n):
    lst.append(int(input()))

print(sum(lst))
```

### 列表转字符串

```python
# 示例列表
my_list = ['Hello', 'World', 'Python']

# 1. 使用空格作为分隔符
result_with_space = " ".join(my_list)
print(result_with_space)  # 输出: Hello World Python

# 2. 使用逗号和空格作为分隔符
result_with_comma = ", ".join(my_list)
print(result_with_comma)  # 输出: Hello, World, Python

# 3. 使用连字符作为分隔符
result_with_dash = "-".join(my_list)
print(result_with_dash)   # 输出: Hello-World-Python

# 4. 不使用任何分隔符（直接拼接）
result_no_separator = "".join(my_list)
print(result_no_separator) # 输出: HelloWorldPython

```

### 矩阵对角线之和

```python
mat=[[1,2,3],[3,4,5],[4,5,6]]
res=0
for i in range(len(mat)):    
  res+=mat[i][i]
  
print(res)
```

### 矩阵相加

```python
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
 
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(res)):
    for j in range(len(res[0])):
        res[i][j]=X[i][j]+Y[i][j]
print(res)
```

### 有序列表插入元素

```python
lis=[1,5,10,20,30,40]
n=int(input('insert a number: '))
lis.append(n)
for i in range(len(lis)-1):
    if lis[i]>=n:
        for j in range(i,len(lis)):
            lis[j],lis[-1]=lis[-1],lis[j]
        break
print(lis)
```

### 旋转数列

```python
# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
from collections import deque

nums = [1, 2, 3, 4, 5, 6, 7]
m = int(input("请输入移动位数 m: "))

d = deque(nums)
d.rotate(m)
print(list(d))

```

## 五、字典 & 字符串

### 字典增删改查基础操作

```python
d = {}
n = int(input("请输入键值对数量："))
for i in range(n):
    k = input("键：")
    v = input("值：")
    d[k] = v

print(d)
del d[list(d.keys())[0]]
print(d)
```

### 分别遍历字典的键、值、键值对

```python
d = {}
n = int(input("请输入键值对数量："))
for i in range(n):
    k = input("键：")
    v = input("值：")
    d[k] = v

for k,v in d.items():
    print(k,v)
```

### 学生成绩字典，求出最高分

```python
score = {}
n = int(input("学生人数："))
for i in range(n):
    name = input("姓名：")
    s = int(input("成绩："))
    score[name] = s

print("最高分：",max(score.values()))
```

### 字符串长度

```Python
s='hello world'
print(len(s))
```

### 实现字符串反转

```python
s = input("请输入字符串：")
print(s[::-1])
```

### 统计字符串中字母、数字、空格个数

```python
s = input("请输入字符串：")
letter = digit = space = 0
for ch in s:
    if ch.isalpha():
        letter +=1
    elif ch.isdigit():
        digit +=1
    elif ch==" ":
        space +=1
print(letter,digit,space)
```

### 判断是否为回文字符串

```python
s = input("请输入字符串：").strip()
print("回文" if s==s[::-1] else "不是回文")
```

### 字符串大小写互相转换

```python
s = input("请输入字符串：")
print(s.upper())
print(s.lower())
```

### 按分隔符把字符串分割成列表

```python
s = input("请输入字符串：")
lst = s.split(",")
print(lst)
```

### 替换字符串中指定内容

```python
s = input("原字符串：")
old = input("要替换内容：")
new = input("替换成：")
print(s.replace(old,new))
```

### 查找字符在字符串中首次出现位置

```python
s = input("请输入字符串：")
ch = input("查找字符：")
print(s.find(ch))
```

### 用字典实现简易通讯录

```python
book = {}
n = int(input("联系人个数："))
for i in range(n):
    name = input("姓名：")
    tel = input("电话：")
    book[name] = tel

print(book.get(input("查询姓名："),"无此人"))
```

### 去除字符串首尾空格

```python
s = input("请输入字符串：")
print(s.strip())
```

### 拼接多个字符串

```python
a = input("字符串1：")
b = input("字符串2：")
print(a+" "+b)
```

### 判断字符串是否全部由数字组成

```python
s = input("请输入字符串：")
print(s.isdigit())
```

### 统计一句话中每个单词出现次数

```python
s = input("请输入一句话：")
word_list = s.split()
d = {}
for w in word_list:
    d[w] = d.get(w,0)+1
print(d)
```

## 六、函数定义调用

### 定义函数求两个数之和

```python
def add(a,b):
    return a+b
print(add(3,5))
```

### 定义函数交换数字

```python
def swap_numbers(a, b):
    """交换两个数字的值"""
    return b, a

# 使用示例
x, y = 5, 10
x, y = swap_numbers(x, y)
print(x, y)  # 输出: 10 5

```

### 定义函数判断一个数奇偶

```python
def is_odd(n):
    return n%2==1
print(is_odd(6))
```

### 定义函数计算阶乘

```python
def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
print(fact(5))
```

### 定义函数计算阶乘(递归)

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"{num} 的阶乘是: {result}")

```

### 定义函数求三个数最大值

```python
def max3(a,b,c):
    return max(a,b,c)
print(max3(12,45,23))
```

### 定义函数判断闰年

```python
def leap(y):
    return (y%4==0 and y%100!=0) or y%400==0
print(leap(2024))
```

### 定义函数求列表平均值

```python
def avg(lst):
    return sum(lst)/len(lst)
print(avg([1,2,3,4]))
```

### 定义函数判断素数

```python
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(17))
```

### 定义函数打印星号三角形

```python
def tri(n):
    for i in range(1,n+1):
        print("*"*i)
tri(5)
```

### 演示函数默认参数用法

```python
def info(name,age=18):
    print(name,age)
info("小明")
info("小红",20)
```

### 用递归实现求阶乘

```python
def fact_rec(n):
    if n==1:
        return 1
    return n*fact_rec(n-1)
print(fact_rec(5))
```

## 第七部分 面向对象编程

###  图形类继承多态

```python
# 父类：圆 封装私有半径
class Circle:
    def __init__(self):
        self.__r = 0

    def set_r(self, r):
        self.__r = r

    def get_area(self):
        return 3.14 * self.__r ** 2

# 子类继承父类，重写方法实现多态
class Ball(Circle):
    def get_area(self):
        return 4 * 3.14 * self._Circle__r ** 2

    def get_volume(self):
        return 4 / 3 * 3.14 * self._Circle__r ** 3

r = float(input("请输入半径："))
b = Ball()
b.set_r(r)
print("球表面积：", b.get_area())
print("球体积：", b.get_volume())
```

### 人员信息类 封装 + 继承 + 多态展示

```python
class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_info(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        return f"姓名：{self.__name}，年龄：{self.__age}"

# 学生类继承人类
class Student(Person):
    def __init__(self):
        super().__init__()
        self.__score = 0

    def set_score(self, s):
        self.__score = s

    def show(self):
        # 方法重写 = 多态
        return super().show() + f"，成绩：{self.__score}"

# 统一多态调用函数
def print_info(obj):
    print(obj.show())

stu = Student()
stu.set_info(input("姓名："), int(input("年龄：")))
stu.set_score(int(input("成绩：")))
print_info(stu)
```

### 员工薪资类 封装继承 + 工资多态计算

```python
class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, s):
        self.__salary = s

    def get_total(self):
        return self.__salary

# 经理子类继承，重写薪资算法
class Manager(Employee):
    def get_total(self):
        return super().get_total() + 1500

def count_wage(obj):
    print("本月总收入：", obj.get_total())

m = Manager()
m.set_salary(float(input("请输入基本工资：")))
count_wage(m)
```

### 抽象图形父类 矩形 & 三角形多态求面积

```python
# 抽象父类
class Shape:
    def area(self):
        pass

# 矩形子类
class Rectangle(Shape):
    def __init__(self):
        self.__w = 0
        self.__h = 0

    def set_wh(self, w, h):
        self.__w = w
        self.__h = h

    def area(self):
        return self.__w * self.__h

# 三角形子类
class Triangle(Shape):
    def __init__(self):
        self.__a = 0
        self.__h = 0

    def set_ah(self, a, h):
        self.__a = a
        self.__h = h

    def area(self):
        return self.__a * self.__h / 2

# 多态统一调用
r = Rectangle()
t = Triangle()
r.set_wh(float(input("矩形宽：")), float(input("矩形高：")))
t.set_ah(float(input("三角形底：")), float(input("三角形高：")))
print("矩形面积：", r.area())
print("三角形面积：", t.area())
```

### 动物发声经典多态大题

```python
class Animal:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("小狗：汪汪汪")

class Cat(Animal):
    def speak(self):
        print("小猫：喵喵喵")

# 多态函数
def animal_sound(obj):
    obj.speak()

d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)
```

## 八、文件操作 & 综合编程

### 向txt文件写入内容

```python
with open("test.txt","w",encoding="utf-8") as f:
    f.write("Python期末题库\n")
```

### 逐行读取txt文件并打印

```python
with open("test.txt","r",encoding="utf-8") as f:
    print(f.read())
```

### 把列表内容逐行写入文件

```python
lst = ["第1题","第2题","第3题"]
with open("list.txt","w",encoding="utf-8") as f:
    for x in lst:
        f.write(x+"\n")
```

### 统计文本文件一共有多少行

```python
cnt = 0
with open("list.txt","r",encoding="utf-8") as f:
    for _ in f:
        cnt +=1
print("行数：",cnt)
```

### 简易学生成绩录入与查询

```python
stu = {}
name = input("姓名：")
score = int(input("成绩："))
stu[name] = score
print(stu.get(name))
```

### 简单手机号格式合法性校验

```python
phone = input("手机号：")
if len(phone)==11 and phone.isdigit():
    print("格式正确")
else:
    print("格式错误")
```

### 判断身份证号位数是否合法

```python
id_card = input("身份证号：")
if len(id_card) in [15,18]:
    print("位数合法")
else:
    print("位数不合法")
```

### 随机生成6位数字验证码

```python
import random
code = ""
for _ in range(6):
    code += str(random.randint(0,9))
print(code)
```

### 批量生成自定义用户名

```python
user = ["user"+str(i) for i in range(1,11)]
print(user)
```

### 简易购物车商品总价结算

```python
cart = {"苹果":5,"香蕉":3}
total = sum(cart.values())
print("总价：",total)
```

### 统计成绩中优秀、良好、及格、不及格人数

```python
scores = [88,92,56,77,66,95]
excellent = good = pass_ = fail = 0
for s in scores:
    if s>=90:
        excellent +=1
    elif s>=80:
        good +=1
    elif s>=60:
        pass_ +=1
    else:
        fail +=1
print(excellent,good,pass_,fail)
```

### 用冒泡排序实现列表升序

```python
def bubble(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
lst = [5,2,9,1]
bubble(lst)
print(lst)
```

### 用二分查找查找列表指定元素

```python
def binary_search(lst,target):
    left,right = 0,len(lst)-1
    while left<=right:
        mid = (left+right)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1
lst = [1,2,3,4,5,6]
print(binary_search(lst,4))
```

### 学生信息录入、保存到文件并支持查询

```python
name = input("姓名：")
age = input("年龄：")
with open("stu_info.txt","a",encoding="utf-8") as f:
    f.write(f"{name},{age}\n")

find_name = input("查询姓名：")
with open("stu_info.txt","r",encoding="utf-8") as f:
    for line in f:
        if find_name in line:
            print(line.strip())
```

 