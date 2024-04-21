try:
    pwd=input('Enter your password(must greater than 8 number): ')
    if len(pwd) < 8:
      raise Exception('太短了’')
except Exception as e:
    print(e)
except TypeError as e:
    print(e)
finally:
    print('程序结束')