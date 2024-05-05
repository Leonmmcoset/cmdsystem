#Calender appcation
def start():
    print('--Calender--')
    # 计算函数
    def calc(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2


    # 检查输入的运算符规范性函数
    def check_operator(operator):
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            return True
        else:
            return False


    # 录入运算符号的处理函数
    def input_operator():
        a = input('+ - * /:')
        while True:
            if check_operator(a):
                return a
            else:
                a = input('Math error:no such input.')


    # 输入的第二个数的处理函数
    def input_num2(operator):
        num2 = float(input('Num 2:'))
        while True:
            if operator == '/' and num2 == 0:
                num2 = float(input("Can't be 0!"))
            else:
                return num2


    Exit_Flag = 'N'
    while Exit_Flag == 'N':
        # 输入第一个数
        Input_num1 = float(input('Num 1:'))
        # 输入运算符
        Input_operator = input_operator()
        # 输入第二个数
        Input_num2 = input_num2(Input_operator)
        # 进行运算并打印出运算结果
        Result = calc(Input_num1, Input_num2, Input_operator)
        print('Result:', Result)
        Exit_Flag = input('Exit? Y/N:')

