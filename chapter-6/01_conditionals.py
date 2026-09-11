age = int(input("Enter your age : "))

if(age >= 18):
    print("Your are above the age of concent")
    print("Good For You")
elif(age<0):
    print("You are entering invalid negative age")
elif(age == 0):
    print("You are entering age = 0 which is invalid")
else:
    print("Your are below the age of concent")

print("--------End of the program----------")