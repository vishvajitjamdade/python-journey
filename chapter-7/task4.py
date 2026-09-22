import math

print("Enter number...")
num = int(input())
flag = True
for i in range(2,int(math.sqrt(num))+1,1):
    if(num%i == 0):
        flag = False
        break

if(flag):
    print(num,"Prime Number")
else:
    print(num,"Not Prime Number")