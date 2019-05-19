import numpy as np
import pandas as pd

np.set_printoptions(precision=2) #指定精度为小数点后2位

'''
array1=np.array([[1,2,3,4],[4,5,6,7],[5,6,7,8]])
print("array1=\n",array1)
print("array1[:,1:3]\n",array1[:,1:3])

array2=np.ones((2,4))
array3=np.zeros((2,4))
array4=np.eye(3)
print("array2=\n",array2)
print("array3=\n",array3)
print("array4=\n",array4)

array5=np.empty((2,2),"f2") #
print("array5=\n",array5)

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
asqrt=np.sqrt(a)
print("Sum = \n", sum)
print("Difference = \n", difference)
print("Product = \n", product)
print("Quotient = \n", quotient)
print("Sqrt = \n", asqrt)


# sum 方法
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.sum(tang_array)
print("a=\n",a)
a=np.sum(tang_array,axis=0)
print("a=\n",a)
a=np.sum(tang_array,axis=1)
print("a=\n",a)
a=np.sum(tang_array,axis=-1)

# 乘积
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.prod(tang_array)
print("a=\n",a)
a=np.prod(tang_array,axis=0)
print("a=\n",a)

# min
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.min(tang_array)
print("a=\n",a)
a=np.min(tang_array,axis=0)
print("a=\n",a)

# max
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.max(tang_array)
print("a=\n",a)
a=np.max(tang_array,axis=0)
print("a=\n",a)

# 索引
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.argmin(tang_array,axis=0)
print("a=\n",a)

# 均值
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.mean(tang_array,axis=0)
print("a=\n",a)

#标准差
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.std(tang_array,axis=0)
print("a=\n",a)

#方差
tang_array=np.array([[1,2,3],[4,5,6]])
print(tang_array)
a=np.var(tang_array,axis=0)
print("a=\n",a)

#四舍五入
tang_array=np.array([[1.1,2.5,3],[4.7,5.1,6]])
print(tang_array)
a=np.round(tang_array)
print("a=\n",a)


tang_array=np.array([[1.5,1.3,7.5],[5.6,7.8,1.2]])
print("array=\n",tang_array)
a=np.sort(tang_array)
print("a=\n",a)


a=np.arange(10)
print("a=\n",a)

a=np.arange(2,20,2)
print("a=\n",a)

a=np.linspace(0,300,10)
print("a=\n",a)

a=np.eye(5)
print("a=\n",a)


x=np.array([5,5])
y=np.array([2,2])
z1=np.dot(x,y)
z2=np.multiply(x,y)
z3=x*y
print("z1=\n",z1)
print("z2=\n",z2)
print("z3=\n",z3)


# 随机模块
np.set_printoptions(precision=2) #指定精度为小数点后2位

a=np.random.rand(3,2)  #0-1的浮点数
print("a=\n",a)

a=np.random.rand()  #0-1的浮点数
print("a=\n",a)


a=np.random.randint(10,size=(5,4))  #10以内的随机整数，取不到10
print("a=\n",a)

a=np.random.randint(3,10,3)  #3到10的3个数，10取不到
print("a=\n",a)

mu, sigma=0,0.1
a=np.random.normal(mu,sigma,10) #正太分布
print("a=\n",a)



#洗牌
a=np.arange(10)
print("a=\n",a)
np.random.shuffle(a)  #打乱顺序

# 随机种子
np.random.seed(0)    #随机种子的作用就是不改变随机的模式，当调试过程中不希望随机产生影响是，可以采用随机种子
mu, sigma=0,0.1
a=np.random.normal(mu,sigma,10) #正太分布，结果将不变
print("a=\n",a)


'''

# 文件读取
data = np.loadtxt("./data/foo.txt", delimiter=',',usecols=(1,3), skiprows=1)
#数据导入，并指定一个分隔符为","（空格是默认的）,并使用第1,3列,并去掉第一行
print(data)

# 文件写
a=np.array([[1,2,3],[4,5,6]])
np.savetxt("./data/foo2.txt", a, fmt='%.2f', delimiter=',')


# 通过npy来保存数据，类似matlab的mat
a=np.array([[1,2,3],[4,5,6]])
np.save("./data/data.npy", a)
data=np.load("./data/data.npy")
print("data=\n",data)



# 通过npz来保存多个数据为一个压缩包，,并通过键值来索引，类似matlab的mat
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[5,6,7],[8,9,10]])
np.savez("./data/data.npz", a=a, b=b)
data=np.load("./data/data.npz")
print("data=\n", data['b'])




#########################################

