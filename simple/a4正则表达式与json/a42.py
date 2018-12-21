
# a = 'C|C++|Java|C#|Python|Javascript'

# print(a.index('Python')>-1)
# print('Python' in a)             #优先使用内置函数

#用正则表达式
# import re                      #   引入re 模块 

# a = 'C|C++|Java|C#|Python|Javascript'

# r = re.findall('Python',a)           #findall 方法  
# print(r)
# if len(r) > 0:
#     print('字符串中包含Python')
# else:
#     print('No')                    
      
# #正则表达式的灵魂：  规则

# import re                       

# a = 'C0C++7Java12C#9Python\n67Javascript8'
# #来提取a中的数字
# r = re.findall('\d',a)      #\d 来表示数字
# print(r)

# s = re.findall('\D',a)      #\D 来表示非数字
# print(s)

# #   'Python'  普通字符 。 '\d'，'\D'， 元字符
# # 正则表达式就是由普通字符和元字符等组合在一起的。