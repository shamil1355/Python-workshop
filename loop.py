a=int(input("Enter Num"))
if a<0:
    print("Does Not Exist")
elif a==0:
    print("THE Fractional is 1")
else:
    fact=1
    for i in range(1,a+1):
        fact=i*fact
    print(fact)
