def range_letter_lenth_ul(lenth,upper=True):
    import random

    range1 = range(ord('A'), ord('Z'))
    range2 = range(ord('a'), ord('z'))
    a = [      ]
    if upper:
        chooserange = range1

    else:
       chooserange = range2
    for i in range(1):
        s = ''
        for j in range(lenth):
            t = random.randint(chooserange.start, chooserange.stop-1)  # 从范围中随机选择一个数
            s += chr(t)
        a.append(s)

    return a

def randommixedletter(lenth):
    import random

    range1 = range(ord('A'), ord('Z'))
    range2 = range(ord('a'), ord('z'))
    a = []
    for i in range(1):
        s = ''
        for j in range(lenth):
            chooserange = random.choice([range1, range2])  # 随机选择一个范围
            t = random.randint(chooserange.start, chooserange.stop-1)  # 从范围中随机选择一个数
            s += chr(t)
        a.append(s)

    return a

# mytimepackage/timemodule.py

from datetime import datetime

def get_current_time():
    # 获取当前时间
    now = datetime.now()
    # 格式化时间格式
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time


print(get_current_time())

print(range_letter_lenth_ul(5,upper=False))
print(range_letter_lenth_ul(5,upper=True))
print(randommixedletter(44545))
print(randommixedletter(4))

