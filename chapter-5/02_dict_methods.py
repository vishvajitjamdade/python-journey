marks={
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan":23,
    1:"vishvajit"
}

# print(marks, type(marks))
# print(marks["Shubham"])

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99})
# marks.update({"Shubham":99,"Karan":89})

print(marks)

print(marks.get("Harry2"))  #If key does not exists then it print "None"
print(marks["Harry2"]) #If key does not exists then it return an error
