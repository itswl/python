
## 生成器

**在Python中，有一边循环一边计算的机制，称为生成器：generator**

**python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器**

**生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器**

```
#列表生成式
lis = [x*x for x in range(10)]
print(lis)
#生成器
generator_ex = (x*x for x in range(10))
print(generator_ex)
for i in generator_ex:
    print(i)
    
```

   **生成器函数：也是用def定义的，利用关键字yield一次性返回一个结果，阻塞，重新开始**

   **生成器表达式：返回一个对象，这个对象只有在需要的时候才产生结果**
   
   ```
   def create_counter(n):
    print("create_counter")
    while True:
        yield n
        print("increment n")
        n +=1

gen = create_counter(2)
print(gen)
print(next(gen))
print(next(gen)
   
   ```
   
   
