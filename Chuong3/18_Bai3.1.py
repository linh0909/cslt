import math 
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if ((a+b)<=c or (a+c)<=b or (b+c)<=a):
    print("Khong hop le")
else: 
    p=(a+b+c)/2
    dientich=math.sqrt((p*(p-a)*(p-b)*(p-c)))
    print("Dien tich=",round(dientich,3),sep="")
    