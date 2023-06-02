# 1부터 100까지 한 줄에 10개 씩, 이중 for문 사용
        
num = 10
cnt = 0
for i in range(1, num+1):
    for j in range(1, num+1):
        cnt += 1
        print(cnt, end=' ')
    print()