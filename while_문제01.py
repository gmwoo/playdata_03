# 정수를 입력받는다.
# 음수가 입력될때까지 양의 정수나 0을 입력받아 합계와 평균을 구하자

nums = []

num = int(input("정수 입력: "))
while num>=0:
    nums.append(num)
    num = int(input("정수 입력: "))
print(nums)
sum = 0
for i in range(0, len(nums)):
    sum = sum + nums[i]
print(f"합계: {sum}, 평균: {sum/len(nums)}")
