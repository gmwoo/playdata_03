# ord("문자") -> 해당 문자에 대한 숫자로 변환
print(ord("A"))  # 65
print(ord("B"))  # 66
print(ord("C"))  # 67
print(ord("a"))  # 97
print(ord("b"))  # 98
print(ord("0"))  # 48
print(ord("1"))  # 49
print(ord("2"))  # 50

# chr: ord의 반대 역할, 숫자를 문자로 변환
print(chr(65))
print(chr(66))
print(chr(67))


# 문제. 알파벳을 for문 사용해서 대문자로 출력 26
for i in range(0, 26):
    k=1
    for j in range(0, 26):
        print(chr(k+65), end='')
        k+=1
        if k>25:
            k=0
    print()
