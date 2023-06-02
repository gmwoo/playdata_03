"""
홍길동, 90, 80, 70
장길산, 100 100, 90
임꺽정, 80, 70, 60

list안에 dict으로 넣고 총점, 평균 구해서 출력    
"""

lst = [
    {"name": "홍길동", "eng": 90, "math": 80, "kor": 70},
    {"name": "장길산", "eng": 100, "math": 100, "kor": 90},
    {"name": "임꺽정", "eng": 80, "math": 70, "kor": 60}
]
print(lst)

for score in lst:
    score['total'] = score['eng'] + score['math'] + score['kor']
    score['avg'] = score['total'] / 3
    
for x in lst:
    print(f"{x['name']} 의 총점은 {x['total']} 이고 평균은 {x['avg']} 이다")
