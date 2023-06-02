# for문 안에 또 for문이 있다
"""
for i in range(1, 6):           i=1 j=1,2,3,4,5
    for j in range(1, 6):       i=2 j=1,2,3,4,5
        코드                    i=3 j=1,2,3,4,5
                                i=4 j=1,2,3,4,5
                                i=5 j=1,2,3,4,5
"""
# for i in range(1,6):
#     print("i = ", i, " j = ",end=' ')
#     for j in range(1,6):
#         print(j, end = ' ') # 옆으로 출력하기
#     print() # 줄바꿈
    
# 이중 for문을 사용해서 도형 만들 수 있음
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()
    
# num = 4
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         # if j
#         print(' ' * (num-i), '*'*j, end='') 
#         print()
#     # print()

num = 7
for i in range(1,num+1):
    print(' ' * (num-i+1), '*'*(2*i-1), end='') 
    print()
for j in range(num+1, 0,-1):
    print(' ' * (num-j+1), '*'*(2*j-1), end='')
    print()
    

line = 7
for i in range(0,line):
    # 공백 출력
    for j in range(0,line-i):
        print(' ', end='')
    # 별그리기
    for j in range(0,2*i-1):
        print('*', end='')
    print()
    
# 역으로 그리기
for i in range(0,line):
    # 공백 출력
    for j in range(0,i):
        print(' ', end='')
    # 별그리기
    for j in range(0,(line-i)*2-1):
        print('*', end='')
    print()