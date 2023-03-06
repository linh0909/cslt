gianiemyet = int(input("nhap gia niem yet: "))
chietkhau = int(input("nhap gia chiet khau: "))
VAT = (gianiemyet - chietkhau) * 0.01
Giaban = gianiemyet - chietkhau + VAT
print("Gia ban:",Giaban)