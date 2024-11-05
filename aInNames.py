list=[]
name=input("enter first name")
list.append(name)
print("list of first names:",list)
count=sum(name.upper().count('A')for name in list)
print("occuranceof 'A':",count)
