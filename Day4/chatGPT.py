
"계산기 코드를 사용하려면 먼저 해당 코드를 언어로 구현된 프로그램에서 실행할 수 있도록 컴파일이나 인터프리팅 해야 합니다. 그리고 실행 파일을 열거나 터미널에서 실행하면 계산기 프로그램이 실행되며 사용자는 원하는 연산을 입력하고 결과를 확인할 수 있습니다."
def calculator():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input('Please enter the first number: '))
    number_2 = float(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2), end='')
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), end='')
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), end='')
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2), end='')
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

calculator()
