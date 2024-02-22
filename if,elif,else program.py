operations=input("enter the operation(+for addition,-for substraction):")
if operations=='+':
    num1=int(input("enter the first no:"))
    num2=int(input("enter the second no:"))
    result=num1+num2
    print("result:",result)
elif operations=='-':
    num1 = int(input("enter the first no:"))
    num2 = int(input("enter the second no:"))
    result = num1 - num2
    print("result:", result)
else:
    print("invalid operation")


a=int(input("enter the side a:"))
b=int(input("enter the side b:"))
c=int(input("enter the side c:"))
if a==b==c:
    print("triangle is equilateral:")
elif a==b or b==c or c==a:
    print("triangle is isoscalene")
else:
    print("scalene triangle")