while True:
    print("options")
    print("enter '+' to add two numbers")
    print("enter '-' to substract two numbers")
    print("enter '//' to multiply two numbers")
    print("enter '*' to multiply two numbers")
    print("enter '**' to multiply two numbers")
    print("enter 'quit' to quit two numbers")
    user_name = input(':')

    if user_name == "quit":
        print('HELLO WORLD!!!')
        break
    elif user_name == "+":
        num1=float(input('enter a number'))
        num2=float(input('enter another number'))
        result = str(num1+num2)
        print('the answer is '+result)

    elif user_name == "*":
        num1=float(input('enter a number'))
        num2=float(input('enter another number'))
        result = str(num1*num2)
        print('the answer is '+result)
        
    elif user_name == "**":
       num1=float(input('enter a number'))
       num2=float(input('enter another number'))
       result = str(num1**num2)
       print('the answer is '+result)
    
    elif user_name == "-":
        num1=float(input('enter a number'))
        num2=float(input('enter another number'))
        result = str(num1-num2)
        print('the answer is '+result)

    elif user_name == "//":
        num1=float(input('enter a number'))
        num2=float(input('enter another number'))
        result = str(num1//num2)
        print('the answer is '+result)
