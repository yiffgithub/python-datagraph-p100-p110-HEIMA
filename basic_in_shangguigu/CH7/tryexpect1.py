try:
    d = int(input('给出你的除数: '))
    result = 10 / d
    print(result)
except ZeroDivisionError as e:
    print('除数不能为0')
    print('你的错误类型是', ZeroDivisionError)
    print('你的错误类型是', e)

except:
    print('未知错误')

else:
    print('没有错误')
finally:
    print('程无论如何都会打印并且程序结束')
