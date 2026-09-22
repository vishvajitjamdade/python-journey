def sum(num):
    if(num == 1):
        return 1
    return num+sum(num-1)

n = int(input("Enter the number : "))
print(sum(n))