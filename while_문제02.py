# 문제: 정수를 음수가 입력될 때까지 입력을 받아서
# 각각 짝수와 홀수를 구분해서 짝수의 합계와 홀수의 합계 출력
# 각각 짝수와 홀수를 구분해서 다른 리스트에 담아 한 번에 출력

nums = []
lst_even = []
lst_odd = []
sum_even = 0
sum_odd = 0

# 음수가 나올 때 까지 nums 리스트에 정수 입력
num = int(input("정수 입력: "))
while num>=0:
    nums.append(num)
    num = int(input("정수 입력: "))
print(nums)

# 리스트 내 짝수와 홀수 구분해서 합계, 리스트 생성
for x in nums:
    if x%2 == 0:
        sum_even += x  # 짝수의 합계
        lst_even.append(x)  # 짝수 리스트 
    else: 
        sum_odd += x  # 홀수의 합계
        lst_odd.append(x)   # 홀수 리스트
        
print(f"짝수의 합계: {sum_even}, 홀수의 합계: {sum_odd}")
print(f"짝수 리스트: {lst_even}, 홀수 리스트: {lst_odd}")
