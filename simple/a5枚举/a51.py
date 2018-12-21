#类型
#绿钻、黄钻、红钻、黑钻
# 1 绿钻
# 2 黄钻
# 3 红钻
# 4 黑钻

#字典   枚举
#表示类型的三种方式

yellow = 1
green =2      #模块里全局变量方式

{'yellow':1,'green':2}  #字典

a = {'yellow':1,'green':2}
a['yellow'] = 3  #可变
{'yellow':1,'green':1}  #相同值

class TypeDiamond():     #类
    yellow = 1
    green = 2

#都是可变的
#没有防止相同标签的功能