mylist = ["Rohan","Sudhir","Anmol","karan","Om"]
name = input("Enter name you want to search : ")
if(name in mylist):
    print("Your name is in the list")
else:
    print("Your name is not in the list")
    
print(mylist.__contains__(name))