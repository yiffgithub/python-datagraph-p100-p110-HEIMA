# 匿名函数，就是简单的函数的用法，只是不需要给函数命名，直接使用lambda关键字定义函数，然后返回函数的值。
# 语法：lambda 参数:表达式

def f(a,b):
    return a+b
print(f(1,2))

func = lambda a,b:a+b

print (func(1,5))

# 匿名函数的应用场景：
# map函数的使用
# map函数的定义：map(function, iterable（通常是列表）, ...)
a=[1,2,3,4,5]
result = map(lambda x:x**3,a)
print(list(result))

#reduce 函数的使用
# reduce函数的定义：reduce(function, iterable[, initializer]) 通常情况就是累计，累加雷减少，累计乘法，累计除法
from functools import reduce

result = reduce(lambda x,y:x/y,a)

print(result)

result =1
for i in a:
    result = result / i

print(result)

#filter函数的使用
# filter函数的定义：filter(function, iterable) 通常是过滤
resultodd = filter(lambda x:x%2,a)
resulteven =filter(lambda x:x%2==0,a)

print(list(resultodd))
print(list(resulteven))

list1 = [1,2,3,40,5,4,6,0,0,45,645,7]
r=filter(lambda x:x!=0,list1)
list2 = list(r)

print('--------')
print(list2)





mul =1
num=0

for i in list2[::-1]:

    # print(i)
    num = num +i*mul 
    mul = mul*10**len(str(i))
    print(num)

print(num)


