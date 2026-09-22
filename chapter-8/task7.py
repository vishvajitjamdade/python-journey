def rem(l,word):
    l.remove(word)
    return l

l = ["Suhas","Karan","Virag","Priya","John"]
word = input("Enter word to remove from list : ")
print(rem(l,word))