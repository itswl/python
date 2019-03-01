# #函数式编程是一种思维，闭包只是其一种体现

# #匿名函数
# def add(x,y):
#     return x+y

# add(1,2)
# print(add(1,2))

# lambda x,y:x+y #定义一个匿名函数   lambda 表达式
add = lambda x,y:x+y   #这给匿名函数取了名字
add(1,2)
print(add(1,2))


#三元表达式
#x,y  x大于y，取x 否则，取y
#x > y ? x:y  (其他语言中)

#条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果   (python中)
x = 1
y = 4
#x if x > y else y   # python中
r = x if x > y else y  
print(r)

#map类  #将集合里每个元素传到square里去，并且映射到新的集合中
list_a = [1,2,3,4,5,6,7,8]
#list_y = [1, 4, 9, 16, 25, 36, 49, 64]


square = lambda x:x**2

r = map(square,list_a)
print(r)  #<map object at 0x0000026BCECDE9E8>
print(list(r)) #[1, 4, 9, 16, 25, 36, 49, 64]

square1 = lambda x:x**2
for x in list_a:
    x = square1(x)
    print(x)


#map常用方法

r = map(lambda x:x * x,list_a)
print(list(r))

list_b = [1, 4, 9, 16, 25, 36, 49]

s = map(lambda x,y:x * x + y,list_a,list_b)  #map中传入多个list
print(list(s))  #[2, 8, 18, 32, 50, 72, 98] 长度取决于列表少的那个

#reduce  #连续计算，连续调用lambda
from functools import reduce
list_a = [1,2,3,4,5,6,7,8]
r = reduce(lambda x,y:x + y,list_a,10)  #10+1,得到11，11+2,得到13.....等一系列计算
print(r)

# #(x,y)
#(0,0)
list_b = [(1,3),(2,-2),(-2,3),(1,2)]
r = reduce(lambda x,y:(x) +(y),list_b) 
print(r)


# map/reduce编程模型 映射 归纳 
# 并行计算
# 函数式编程

#filter  过滤
list_a = [1,1,0,0,1,1,0,1,0]
r = filter(lambda x: True if x==1 else False, list_a)
s = filter(lambda x:x,list_a) #因为0代表False
print(list(r))
print(list(s))
