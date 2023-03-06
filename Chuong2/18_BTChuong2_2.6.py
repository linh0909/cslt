ten=input("Ho ten: ")
songaycong = int(input("So ngay cong: "))
dongiangaycong = int(input("Don gia ngay cong: "))
hesophucap = float(input("He so phu cap: "))
tamung = int(input("Tam ung: "))
luong = dongiangaycong *songaycong*hesophucap
thuclinh=luong - tamung
print("Nhan vien",ten, end=", ")
print("Co tien luong=",luong,sep="",end=", ")
print("Tam ung=",tamung,sep="",end=" va ")
print("Thuc linh=",thuclinh,sep="")
