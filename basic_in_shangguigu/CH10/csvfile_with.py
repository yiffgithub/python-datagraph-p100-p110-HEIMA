import csv
with   open('xxx.csv', mode='r', encoding='utf-8') as f:
    context=csv.reader(f)
    print(context)
    print('-'*20)
    head=next(context)
    score=[]
    for i in context:
        # print(type(i))
        # print(i[0])

        #print(i)
        score.append(int(i[2]))
    print(score)
    print(sum(score)/len(score))

with open('xxx.csv', mode='a', encoding='utf-8') as f:

    cf = csv.writer(f)

    # 使用 writerow 方法写入单行数据
    cf.writerow(['tom', 'c', '50'])

    # 准备多行数据
    lista = [
        ['lily', 'c', '70'],
        ['lily', 'python', '57'],
        ['lily', 'java', '90']
    ]

    # 使用 writerows 方法写入多行数据
    cf.writerows(lista)

print('CSV文件写入完成。')

