a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
min=c
max=a
if b>max:
    max=b
if c>max:
    max=c
print("SLN=",max,sep="")
if b<min:
    min=b
if a<min:
     min=a
print("SNN=",min,sep="")