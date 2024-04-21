def calculator():
    while True:
        try:
            num1 = float(input("请输入第一个数字: "))
            operator = input("请输入运算符 (+, -, *, /)，或者输入 'exit' 退出: ")

            if operator.lower() == 'exit':
                print("退出计算器。")
                break

            num2 = float(input("请输入第二个数字: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("除数不能为零")
                result = num1 / num2
            elif operator == '^':
                raise Exception("bu neng yong ^, mei zhi chi ne")
            elif operator == 'x':
                raise Exception("bu neng yong x")
            else:
                raise ValueError("无效的运算符")

            print("结果:", result)

        except ValueError as ve:
            print("错误:", ve)
        except ZeroDivisionError as zde:
            print("错误:", zde)
        except Exception as e:
            print(e)
        finally:
            print("程序结束")

calculator()
