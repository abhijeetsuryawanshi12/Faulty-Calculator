# faulty calculator
print("Enter your first number")
num1 = int(input())
print("Enter your second number")
num2 = int(input())
print("Enter operation" "+,-,/,%.*,**")
num3 = input()
if num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("660")
elif num3 == '**':
    num4 = num1**num2
    print(num4)
elif num3 == '/':
    num5 = num1/num2
    print(num5)
elif num3 == '%':
    num6 = num1%num2
    print(num6)
elif num3 == '+':
    num7 = num1+num2
    print(num7)
elif num3 == '*':
    num8 = num1*num2
    print(num8)
