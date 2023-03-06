i=1
while i<=9:
        j=1
        while j<=9:
                print(i*j,end="\t")
                # là khi j chạy tới hết = 9 thì không thõa mãn đk j<=9 nên tăng 1 i lên để chạy tiếp vòng lặp cho đến khi i >9 thì dừng lại
                j=j+1        
        print()
        i=i+1