e = set() # empty set
# Don't use s = {} as it will create an empty dictionary

s = {1,5,32,54,5,5,5,"Vishvajit"}

print(s, type(s))

s.add(544)
print(s, type(s))
s.remove(1)
print(s, type(s))