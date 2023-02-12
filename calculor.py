num1 = int(input("enter you first number"))
num2 = int(input("enter your second number"))
operators = (input("enter the operator"))
if operators=="+":
    print(num1+num2)
elif operators=="-":
    print(num1-num2)
elif operators=="*":
    print(num1*num2)
elif operators=="%":
    print(num1%num2)
else:
    print("syntax error")