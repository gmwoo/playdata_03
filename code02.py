# p214 2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number > 100:
        print("- 100 이상의 수: ", number)
        

# p214 3번
for number in numbers:
    if number % 2 == 0:
        print(f"{number} 은(는) 짝수입니다.")
    else:
        print(f"{number} 은(는) 홀수입니다.")
    print(f"{number} 은(는) {len(str(number))} 자릿수입니다.") 
    print()
