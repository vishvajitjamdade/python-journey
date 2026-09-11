sub1 = int(input("Subject1 mark : "))
sub2 = int(input("Subject2 mark : "))
sub3 = int(input("Subject3 mark : "))
sub4 = int(input("Subject4 mark : "))

total = ((sub1+sub2+sub3+sub4)/400)*100

if(total>=40 and sub1>=33 and sub2>=33 and sub3>=33 and sub4>=33):
    print("PASS")
else:
    print("Fail")
