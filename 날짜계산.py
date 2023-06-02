# 연도, 월, 일 입력받아서 그 날이 그 해의 몇 번째 날인지 맞추기
# 윤년: 4의 배수 이면서, 100의 배수가 되면 안되고, 400의 배수는 윤년
# 윤년의 경우 2월이 29일이 됨. 윤년 아니면 28일

year = int(input("연도: "))
month = int(input("월: "))
day = int(input("일: "))

each_month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0

if year%4 == 0 and year%100 != 0 or year%400 ==0: # 윤년
    each_month_day[1] = 29
for i in range(month-1):
    cnt += each_month_day[i]
print(cnt + day)
