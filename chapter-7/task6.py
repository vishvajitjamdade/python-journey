fact = 1
print("Enter the number...")
num = int(input())

for i in range(1,num+1,1):
    fact = fact*i

print(f"Factorial of {num} is {fact}")