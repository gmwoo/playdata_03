count = int(input("몇 개? "))
nums = list() # nums = [] 와 같음

for i in range(1, count+1):
    n = int (input("숫자: "))
    nums.append(n)

print(nums)