yrsOfService=int(input())
salary=int(input())
bonus = 0
if yrsOfService < 5:
    if salary < 500:
        bonus = 100
    else:
        bonus = 200
else:
    bonus = 700
print("Bonus amount: ", bonus)
 