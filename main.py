#Simple calculator logic app with out UI
#we are also using try and except for good coding practice

try:
    num1 = int(input('Enter your First Number: '))
    num2 = int(input('Enter your Second Number: '))
    op = input('Enter Operator: ')
    if op == '+':
        print('Your Resul is: ',num1+num2)
    elif op == '-':
        print('Your Result is: ', num1 - num2)
    elif op == '*':
        print('Your Result is: ', num1 * num2)
    elif op == '/':
        print('Your Result is: ', num1 / num2)
    else:
        print('Invalid Operator, Please enter valid operator: like + _ / or * for basic math calculation') 
    
except:
    print('Unkown Error acuur')

