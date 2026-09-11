num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))
num4 = int(input("Enter num4 : "))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1,"is greater")
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2,"is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3,"is greater")
else:
    print(num4,"is greater")