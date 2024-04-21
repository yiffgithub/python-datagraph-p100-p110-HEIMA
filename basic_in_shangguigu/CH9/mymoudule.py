def add(x, y):
    return x + y


def total(*args):
    totalnum = 0
    for i in args:

        totalnum=totalnum+i

    return totalnum

name='dddd'
# 这部分代码只有在模块被直接运行时才会执行
if __name__ == "__main__":
    print(total(2, 3, 4, 8))
    print(name)