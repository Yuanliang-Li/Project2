import time  # 引入time模块
from mypacage.runoob1 import *



# 时间函数学习=====================================================

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Mon Oct 29 20:46:30 2018"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 将格式字符串转换为时间戳
a = "2018-10-29 20:46:30"
print(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))

# 时间函数学习=====================================================


# for x循环
for i in range(0,10,3):
    print(i, end=" ")
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 类学习==========================================================
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)


    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


li=Employee("liyuanliang",5000)
li.displayCount()
li.displayEmployee()

wang=Employee("wangbadan",7000)
wang.displayCount()
wang.displayEmployee()

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# 类学习==========================================================

runoob1()
runoob2()

# I/O文件操作
fo = open("foo.txt", "w")# 打开并穿件一个文件，方式为：打开一个文件只用于写入。
fo.write("www.runoob.com!\nVery good site!\n")
fo.close()# 关闭打开的文件

fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()
