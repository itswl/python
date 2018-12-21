#更进一步
#要利用好正则表达式啊
# import re
# a = 'C0C++C#7Java12C#\n9Python6C#7JavascriptC#8'

# def convert(value):
#     print(value)
#     matched = value.group()
#     return '!!' + matched +'!!'

# r =  re.sub('C#',convert,a)
# print(r)

#把函数作为传递参数

#正则表达式只能操作字符串
# import re
# s = 'A1b2c3d4e5f6g7h8i9'

# def convert1(value):
#     print(value)
#     matched1 = value.group()
#     if int(matched1) >=6:
#         return '9'
#     else:
#         return '0'

# s =  re.sub( r'\d',convert1,s)
# print(s)

# #re.match   第一个匹配就匹配，第一个不匹配就不匹配
# #re.search  有匹配的就匹配
# #均只找一个
# import re
# s = 'A1b2c3d4e5f6g7h8i9'
# r = re.match(r'\d',s)    
# r1 = re.search(r'\d',s)

# print(r)
# print(r1)

#group()
# import re

# s = 'life is short,i use python'
# r = re.search('life.*python',s)
# r1 = re.search(('life.*python'),s) #与上行一样
# r2 = re.search('life(.*)python',s)
# print(r.group())
# print(r1.group())
# print(r2.group(0))  #全文匹配
# print(r2.group(1))  #括号内匹配
# r = re.findall('life(.*)python',s)
# print(r)

import re

s = 'life is short,i use python,I love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(0,1,2))   #用元组的方式表达出来
print(r.groups())  #只会表示出（.*）的内容