num1,num2,num3=input("Enter The numbers")

if num1>=num2 and num1>=num3:
    largest=num1
elif num2>num3:
    largest=num2
else :
    largest=num3
print("Largest is ",largest)
