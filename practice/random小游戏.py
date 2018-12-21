# num2 = 100
# sum1 = lambda num1 : num1 + num2 
# num2 = 10000
# sum2 = lambda num1 : num1 + num2 

# print( sum1( 1 ) )#10001
# print( sum2( 1 ) )#10001
# # lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。

# for m in range(1, 10):
#     for n in range(1, m+1):
#         print('%d*%d=%d\t'%(n,m,n*m), end='')
 
#     print()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(i, j, i*j), end='')
#     print()


# import random

# # 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# player = int(input("请输入您要出的拳 石头（1）／剪刀（2）／布（3）："))

# # 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# computer = random.randint(1, 3)

# print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))

# # 比较胜负
# # 1 石头 胜 剪刀
# # 2 剪刀 胜 布
# # 3 布 胜 石头
# # if (()
# #        or ()
# #        or ()):
# if ((player == 1 and computer == 2)
#         or (player == 2 and computer == 3)
#         or (player == 3 and computer == 1)):

#     print("欧耶，电脑弱爆了！")
# # 平局
# elif player == computer:
#     print("真是心有灵犀啊，再来一盘")
# # 其他的情况就是电脑获胜
# else:
#     print("不服气，我们决战到天明！")

import random
guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        continue
    elif computer == people:
        print ("平手，再玩一次！")
    elif [computer, people] in win_combination:
        print ("电脑获胜，再玩，人获胜才能退出！")
    else:
        print ("人获胜！")
        break
