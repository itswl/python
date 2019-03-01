# # 模块
# c = 50

# def add(x, y):
#     c= x+y 
#     print(c)

# add(1,2)       #3   函数中局部变量的值
# print(c)       #50  全局变量的值
 
# # 两个print(c)的区别 
# # 局部变量不会改变全局变量的值


# #类和模块要区别对待

# #  '类变量'     和 类  关联在一起的
# # '实例变量'    和 对象 关联在一起的 

# # class Student():        
# #     sum = 0    #   类变量   和类相关
# #     name = 'weilai'   #在class内部定义变量    类变量
# #     age = 0           # 类中赋值没有意义的。   #21 ，22 其实是与对象相关，不应出现在这
# #     # 行为 与  特征   
         
# #     def __init__(self,name,age,sum):     #构造函数(实例化后，会自动调用),是一个特殊的方法
# #         #主要是被用来初始化对象属性
# #         self.name = name            #实例方法操控实例变量
# #         self.age = age
# #         print(self.__class__.sum)   
# #         print(Student.sum)
# #         self.__class__.sum +=1      #实例方法访问类变量中的sum
# #         print(Student.sum)

    
# #     def marking(self,sorce):         #内部访问
# #         if sorce < 0:                #建议通过方法 对 类变量赋值
# #             # sorce =0
# #             return '不能给同学打负分'
# #         self.__sorce = sorce
# #         print(self.name + '同学本次的考试分数为：' + str(self.__sorce))
# #         return 'hello'
        

#     # 类方法主要操作和类相关的变量
#     # @classmethod                  #让其成为类方法     
#     # def plus_sum(cls):             #sum每运行一次就+1
#     #     cls.sum+=1
#     #     print(cls.sum)


#     # @staticmethod                #静态方法
#     # def add(x,y):
#     #     print(Student.sum)
#     #     print('this is a static method')

# #静态方法 能用的地方 基本可以用  类方法替代(最好用类方法)
# #当和类和对象没多大关系的时候,可以使用静态方法
# #静态方法和类方法  均不能访问  实例变量



# # student1 = Student('wang',18)
# # student1.plus_sum()
# # studentt = Student('li',19)
# # student.plus_sum()
# # student1.marking(-8)

# # result =  student1.marking(80)
# # print(result)

# # Student.plus_sum()     #用类调用类方法
# # student1.plus_sum()    #用对象调用类方法(最好不用)
# # student1.add(1,2)      #用对象调用静态方法
# # Student.add(1,2)       #用类调用静态方法
# # student2 = Student('li',19)
# # print(student1.name)
# # print(student2.name)
# # print(Student.name)
# # print(student1.age)
# # print(student2.age)
# # print(Student.age)

# # 类中赋值没有意义的。

# class Studenta():
#     name = 'weilai'
#     age = 0

#     def __init__(self,name,age): 
#         name = name 
#         age = age    

# student1 = Studenta('wang',18)
# print(student1.name)
# print(student1.age)
# print(student1.__dict__)  #__dict__显示student1下所有的变量，即没有变量
# # python  会先在  实列变量上寻找 ，寻找不到就会到类变量里寻找，（然后再到父类里寻找）
# # 所以即使student1为空，也显示了类变量下的值
# #公开的 public    私有的（外部不能访问）private  在方法或变量前加__ 表示私有的
# #__init__ 构造函数是python特有的，可以从外部访问
# #print(student2._Student__sorce)    表明python中私有只是改了一个名字



class Studentb():        
    sum=0    #   类变量   和类相关
    name = 'weilai'   #在class内部定义变量    类变量
    age = 0           # 类中赋值没有意义的。   #21 ，22 其实是与对象相关，不应出现在这
    # 行为 与  特征   

#实例方法操控实例变量
    def __init__(self,name,age):     #构造函数(实例化后，会自动调用),是一个特殊的方法
        #主要是被用来初始化对象属性
        self.name = name            
        self.age = age
        print(self.__class__.sum)   
        print(Student.sum)
        self.__class__.sum +=1      #实例方法访问类变量中的sum
        print(Studentb.sum)
student1 = Studentb('wang',18)
student2 = Studentb('li',19)