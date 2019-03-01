def add(x,y):
    result=x+y
    return result
    
def print_code(code):
    print(code)
    return

a=add(1,2)
print_code('python')
print(a)
 
def add1(x,y):
    result = x + y
    print(result)

add1(1,2)

def add2(x,y):
    print('%d + %d = %d'%(x,y,x+y))

add2(1,2)

def add3(x,y):
    print('{} + {} = {}'.format(x,y,x+y))

add3(1,2)


def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
# num 为 1
# args 为 (2,3,4,5)
# **kwargs 为 {'name': '小明', 'age': 18, 'gender': True}


# print("-"*20)   # 分割线,哈哈哈

# 后文解释为什么变元组
demo(1,(2,3,4,5),{"name":"小明", "age":18, "gender":True})
# 1
# ((2, 3, 4, 5), {'name': '小明', 'age': 18, 'gender': True})
# {}

# print("-"*20)
demo(1,(2,3,4,5), name="小明", age=18, gender=True)
# 1
# ((2, 3, 4, 5),)
# {'name': '小明', 'age': 18, 'gender': True}

def demo1(*args, **kwargs):

    print(args)
    print(kwargs)

# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
demo1(gl_nums, gl_xiaoming)
# ((1, 2, 3), {'name': '小明', 'age': 18})
# {}

demo1(*gl_nums, **gl_xiaoming)
# (1, 2, 3)
# {'name': '小明', 'age': 18}



