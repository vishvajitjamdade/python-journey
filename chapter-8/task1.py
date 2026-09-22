def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = int(input("Enter value of number1 : "))
b = int(input("Enter value of number2 : "))
c = int(input("Enter value of number3 : "))
print(f"Greatest of {a},{b},{c} is {greatest(a,b,c)}")