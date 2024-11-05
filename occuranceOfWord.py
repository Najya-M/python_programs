string=input("enter the string")
n=string.split(" ")
count=0
for i in range(0,len(n)):
        if n[i]=="is":
            count=count+1
print(count)
