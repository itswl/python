#列表推导式
#集合字典也可
#元组也可
# a = [1,2,3,4,5,6,7,8,9]
# b = [i**3 for i in a if i <=4]
# print(b)

# a = (1,2,3,4,5,6,7,8,9)
# b = [i**3 for i in a if i <=5]#
# #b = (i**3 for i in a if i <=5)#
# print(b)
#也可以map filter
# list_a=[1,2,3,4,5,6,7,8,9]
# r=filter(lambda x:x if x<=5 else 0,list_a)
# s=map(lambda x:x**3,filter(lambda x:x if x<=5 else 0,list_a))
# print(list(s))

# students ={
#     'wei':18,
#     'lai':19,
#     'wan':20
# }
# b = (key for key,value in students.items())
# print(b)#['wei', 'lai', 'wan']
# for x in b:
#     print(x)#wei#lai#wan

# students ={
#     'wei':18,
#     'lai':19,
#     'wan':20
# }

# b ={value:key for key,value in students.items()}
# print(b)

'''
None 表示空  不同于
空字符串 空的列表 0 False

类型不同，值不同
print(type(None)) <class 'NoneType'>None是None类
'''
# print(type(None))
# def fun():
#     return None

# a = []
# if not a:
#     print('S')
# else:
#     print('F')

# if a is None:
#     print('S')
# else:
#     print('F')

class Test():

    def __len__(self):
        print('len called')
        return True #(只能为int类型)

    def __bool__(self):
        print('bool called')
        return True


print(bool(Test()))