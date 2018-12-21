a=[1,2,3,4,5]
for x in a:
    if x==3:
    #     break 
    # print(x)

        continue
    print(x)

a = [['apple','orange','banana'],(1,2,3)]
for x in a:
    for y in x: 
        print(y)
    print(x)


for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x)

# 注意事项：
#         1)break和continue区别：break到3就停止，continue跳过3继续
#         2）注意print()函数的位置，对结果的影响
#         3）递归用while，遍历用for
