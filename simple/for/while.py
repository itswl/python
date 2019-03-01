import random
num=random.randint(0,100)   # 产生一个0到100的随机数
print(num)
n=0
while True:
    num1=int(input("请输入你猜的数字："))
    n=n+1
    if num1>num:
        print('大了')
    elif num1<num:
        print('小了')
    else:
        print('恭喜你，猜对了！')       
        print('一共猜了：%d次'%(n),end='  ')
        if n<=5:
            print('你太棒了，只猜了%d次就猜对了'%(n))
        else:
            print('下次加油！')
        break

