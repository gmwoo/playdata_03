# 동전 거스르기
# 거스름돈: 78760원    
    
num = int(input("처음 돈: "))
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(len(money)):
    count = num // money[i]
    num %= money[i]
    print(f"{money[i]} 원: {count} 장(개)")