names=[]
new_list_names=[]
for i in range(5):
    name=input("enter the name:")
    names.append(name)
print(names)
for i in names[:]:
    if i.startswith('a'):
        new_list_names.append(i)
        names.remove(i)
print(new_list_names)
print(names)
