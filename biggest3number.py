n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
if n1>n2 and n1>n3:
    print("the greatest is",n1)
elif n2>n3:
    print("the greatest is",n2)
else:
    print("the greatest is",n3)
