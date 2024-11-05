x=[1,2,3,7,9,10]
print("the greatest number is:",max(x))
c=max(x)
f='prime'
print("position :",(x.index(max(x))+1))
for i in range(2,c):
    if(c%i==0):
        f="not prime"
        break
print(f)
