# a=[1,2,3,4,5]
# for x in a:
#     if x==3:
#         break 
#     print(x)

#     #     continue
#     # print(x)

# a = [['apple','orange','banana'],(1,2,3)]
# for x in a:
#     for y in x: 
#         print(y)
#     print(x)


# for x in range(0,10):
#     print(x)
# for x in range(0,10,2):
#     print(x)

# for x in range(1,10):
#     print('=')
#     continue   # 遇到continue就不再执行循环体后面的内容，直接进入下一次循环的判断
#     print(x)  ## 所有的print(x)都不执行

# # 注意事项：
# #         1)break和continue区别：break到3就停止，continue跳过3继续
# #         2）注意print()函数的位置，对结果的影响
# #         3）递归用while，遍历用for
# #         4）python 中只有 for循环只有 for  in 


n=5
for x in range(1,n+1):   # 控制行数
    for b in range(1,x+1):  # 控制当前行的数值
        print(b,end='')
    print()   # 一行结束换行