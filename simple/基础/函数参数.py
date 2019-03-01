def print_student_files(name, gender,age,adress):
    print("I'm "+name)
    print("I'm "+age+' years old')
    print("I'm a "+ gender)
    print("I'm living in "+adress)

print_student_files('weilai','man','18','hubei')

def print_student_files1(name, gender='man',age=18,adress='hubei'):
    print("I'm "+name)
    print("I'm "+str(age)+ ' years old')
    print("I'm a "+gender)
    print("I'm living in "+adress)

print_student_files1('weilai','woman',18,'hubei')
# 重点：
# 1）必须参数  :形参(例如name)，实参('weilai','man',18,'hubei')
# 2）关键字参数：例如 line4
# 3)默认参数：大多数情况下，函数的参数选取的的是一种默认值，
#  可选用默认参数，eg: line9

# 注意事项:1、形参没有给默认值的，函数调用时得给一个实参
#         2、非默认参数不能放在默认参数之后（调用时，同理）
#         3、参数顺序得与默认参数顺序相同（关键字参数有时，可不遵守顺序）
#         4、给了默认参数，函数调用时优先使用实参