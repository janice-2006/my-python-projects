num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))
op=input("Enter operators[+,-,*,/,%]:")
if(op=='+'):
    print("The sum is:",num1+num2)
elif(op=='-'):
    if(num1>num2):
        print("The difference is:",num1-num2)
    else:
        print("The difference is:",num2-num1)
elif(op=='*'):
    print("The product is:",num1*num2)
elif(op=='/'):
    print("The quotient is:",num1/num2)
elif(op=='%'):
    print("The remainder is:",num1%num2)
else:
    print("Invalid operator","\n please retry")
