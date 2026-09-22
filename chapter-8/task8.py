def table(n,i = 1):
    if(i > 10):
        return
    print(f"{n} x {i} = {n*i}")
    table(n,i+1)

n = int(input("Enter the number : "))
table(n)