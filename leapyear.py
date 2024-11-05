a=2024
b=int(input("enter the year"))
for i in range(a,b):
      if (i%4==0 or i%400==0) and i%100!=0:
          print("leap year",i)
      
