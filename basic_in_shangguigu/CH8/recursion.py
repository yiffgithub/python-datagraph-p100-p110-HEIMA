def climb_stairs(n, path="",totalways=0):

    # 基本情况：当楼梯台阶数为 0 时，打印路径并返回
    if n == 0:
        #print(path)

        return 1


    ways=0
    # 递归情况：尝试爬一级台阶和两级台阶，并将每次的选择添加到路径中
    if n >= 1:
        ways+= climb_stairs(n-1, path + "1 ",totalways)
    if n >= 2:
       ways+= climb_stairs(n-2, path + "2 ",totalways)

    return ways




list=[0,1,2]
for i in range(3,11):
     list.append(list[i-1]+list[i-2])
     print('当有%d台阶的时候，一共有%d方式'%(i,list[i]))



# 测试
abc=climb_stairs(10)
print(abc)


