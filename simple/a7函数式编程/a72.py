# 函数式编程
# map reduce filter 
# lambda

#命令式编程
#def 
#if else 
#for

#计算1+2+3+...+100
from functools import reduce
a = range(0,101)
r = reduce(lambda x,y:x+y,a,50)
print(r) 

