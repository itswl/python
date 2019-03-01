
#闭包
def curve_pre():
    def curve():
        print('This is a function')
    return curve

f = curve_pre()
f()


def curve_pre1():
    a = 25
    def curve1(x):
        return a*x**2
    return curve1

#闭包 = 函数 + 环境变量(函数定义的时候)
a = 20     #不受外部变量影响
f1 = curve_pre1()
print(f1.__closure__)   #(<cell at 0x00000216457D06D8: int object at 0x00007FFEF75AD720>,)实质返回了一个闭包
print(f1.__closure__[0].cell_contents)  #25  取出环境变量
f1(2)   
print(f1(2))  #100

def f2():
    a = 10
    def f3():
        #a(=20)被python 认为是一个局部变量,没有引用上面的a(=10)(环境变量)就不是闭包了
        a = 20
        print(a)
    print(a)
    f3()
    print(a)

f2()

# 这是一个闭包
def f4():
    a = 10
    def f5():
        c = 20 * a
    return f5

f = f4()
print(f)
print(f.__closure__)


#闭包 只是一种思维方式，函数式编程
#例题，origin 最初为0，累加计算

#非闭包
origin = 0
def go(step):
    global origin   #定义一个全局变量
    new_pos = origin + step
    origin = new_pos
    return origin

print(go(2))#2
print(origin)#2  #改变了全局变量的值
print(go(3))#5
print(origin)#5
print(go(5))#10
print(origin)#10

#闭包
#闭包可以记忆上次调用的状态
# origin = 0

# def factory(pos):
#     def go(step):
#         nonlocal pos #pos不是本地局部变量
#         new_pos = pos +step
#         pos = new_pos
#         return new_pos
#     return go

# tourist = factory(origin)   #初始化为 0
# print(tourist(2))    #即step为2
# print(tourist.__closure__[0].cell_contents)#取环境变量#2记住了调用的值
# print(tourist(3))
# print(tourist.__closure__[0].cell_contents)#5
# print(tourist(5))
# print(tourist.__closure__[0].cell_contents)#10
# print(origin)  #0  使用闭包，并没有改变全局变量,所有操作都在函数内部

#面向对象编程
class Tourist():
    origin = 0
    def pos(self,new_pos):
        self.origin += new_pos
tourist=Tourist()
print(tourist.origin)
tourist.pos(2)
print(tourist.origin)
tourist.pos(3)
print(tourist.origin)
tourist.pos(5)
print(tourist.origin)
