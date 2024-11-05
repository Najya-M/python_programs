vowels="AEIOUaeiou"
a=input("Enter a word")
b=[]
for i in a:
    if i in vowels:
        b.append(i)
print(b)
