num=int(input("Enter A Number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    print(temp)
if num==sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")
