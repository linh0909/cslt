a=int(input("Tieu thu="))
if a<100:
    gia=a*550
elif a<=150:
    gia=100*550+(a-100)*750
elif a<=200:
    gia=100*550+50*750+(a-150)*950
elif 201<=a:
    gia=100*550+50*750+50*950+(a-200)*1350
VAT=gia*(10/100)
print('Phai tra=',gia+VAT,sep="")
