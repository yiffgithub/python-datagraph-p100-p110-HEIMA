import random


range1 = range(ord('A'), ord('Z'))
range2 = range(ord('a'), ord('z'))
a = []
n = 5
for i in range(20):
    s = ''
    for j in range(n):
        chooserange = random.choice([range1, range2])  # 随机选择一个范围
        t = random.randint(chooserange.start, chooserange.stop-1)  # 从范围中随机选择一个数
        s += chr(t)
    a.append(s)

print(a)
