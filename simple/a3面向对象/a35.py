from a36 import Human

class Student(Human):     #Human是Student的父类，Student是Human的子类
    # sum=0
    def __init__(self,school,name,age):
        self.school = school 

        super(Student,self).__init__(name,age)  #建议以此方式调用父类
        #super 不仅仅可用于构造函数，也可以用于普通的实例方法

        # Human.__init__(self,name,age)   #子类里调用父类构造函数
        #self   用类调用实例方法没意义，所以加self

    #     self.age = age 
    #     self.__sorce = 0
    #     self.__class__.sum +=1

    def do_homework(self):      #子类和父类同名的话，不会报错，先使用子类
        # super(Student,self).do_homework()
        print('English homework')
        
student1 = Student('jinan university','wei',18)
student1.do_homework()
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)
#继承   a35.py a36.py 


