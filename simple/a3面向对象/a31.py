
# 有意义的面向对象的代码
# 类  是面向对象最核心的观念
# 类、对象
# 实例化
# 类最基本的作用：封装
# 一定要用self,引用 self.
# 类只负责定义，不会去运行
# 类和对象。
# 数据成员
# 构造函数可以让模板生成不同的对象

class Student():
    name = ''   #在class内部定义变量    类变量 （和类相关联在一起的）
    age = 0   
    #行为 与  特征   
         
    def __init__(self,name,age):        #构造函数(实例化后，会自动调用)
        #初始化对象属性
        self.name = name 
        self.age = age        #定义实例变量，实例变量只和对象相关 self.

    #     print('student')     
    #    #return NONE (构造函数只能返回NONE)  (补充知识)

    def print_files(self):        #在class内部定义函数
        print('name:'+ self.name)
        print('age:'+ str(self.age))

student = Student('weilai',19)  #类的实例化
student.print_files()  #类下面方法的调用
#  建议 类的实例化以及类下面方法的调用 与类的定义放在不同的模块。
  




# 定义实例时需要self，调用实例不需要给self赋参 