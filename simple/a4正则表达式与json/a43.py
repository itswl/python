# #字符集
# import re

# s = 'abc,acc,adc,aec,adfc,ahc,afc'
# r = re.findall('a[cf]c',s)  #提取afc 或acc,普通字符a,c定界，元字符c，f
# #[]里表示或。[cf] c或f.[cdf] c或d或f  [^cfd]取反，不是c和d和f。[c-f]取c到f。
                        
# print(r) 

# 概括字符集
# 只能匹配单一的字符（单个字母，数字）
# \d即 [0-9] \D 
#  \w单词字符 '[A-Za-z0-9]和_ \W 非单词字符   
# \s 空白字符  \S 非空白字符
# . 匹配除换行符之外其他所有的字符
# import re
# a = 'C0C++7Java12C#9Python67Javascript8\n\r &^'

# # r = re.findall('.',a) 
# # print(r)
# # # #数量词

# r = re.findall('\w{3}',a)
# s = re.findall('[A-Za-z]{3}',a)
# t = re.findall('[A-Za-z]{3,7}',a)

# #贪婪 与 非贪婪
# #python默认使用贪婪  按最大的匹配
# u = re.findall('[A-Za-z]{3,7}?',a)#非贪婪  按最小的匹配
# print(r)
# print(s)
# print(t)
# print(u)   

# #  *  对*前的字符匹配0次或无限多次
# #  +  对+前的字符匹配1次或无限多次
# #  ?  对?前的字符匹配0次或1次    与贪婪中的?是不同的
# import re
# a = 'pytho0python1pythonn2'

# r =  re.findall('python*',a)
# s =  re.findall('python+',a)
# t =  re.findall('python?',a)
# print(r)
# print(s)
# print(t)

# #边界匹配
# import re 
# qq = '100000000001'
# #4-10位数
# r =  re.findall('^\d{4,10}$',qq)  #^从字符串开头匹配  $从字符串末尾匹配
# print(r)


# #组
# import re
# a = 'PythonPythonPythonPythonPythonPython'
# r =  re.findall('(Python){2}',a)
# print(r)

#匹配模式   #函数中的第三个参数
#re.I 忽略匹配中的大小写
#re.S 匹配所有的字符，包括换行符
import re
a = 'C0C++7Java12C#\n9Python67Javascript#8'
r =  re.findall('c#',a,re.I)
r1 =  re.findall('c#.{1}',a,re.I|re.S)   #  |  且
print(r)
print(r1)

# #
#re.sub     
import re
a = 'C0C++C#7Java12C#\n9Python6C#7JavascriptC#8'
r =  re.sub('C#','GO',a,0)  #无限次替换
s =  re.sub('C#','GO',a,1)  #只替换一次
t =  a.replace('C#','GO')    #python内置函数
print(r)
print(s)
print(t)