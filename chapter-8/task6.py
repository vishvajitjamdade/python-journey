def converter(inch):
    return inch*2.54

inch = int(input("Enter the inch : "))
print(f"{inch} inch means {converter(inch)}cm")