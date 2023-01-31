'''
순위 : 수의 크고 작음을 이용해서 수의 순서를 정하는 것을 순위라고 한다.
'''

import random

scores = random.sample(range(50, 101), 20)
ranks = [0 for i in range(20)]
# 길이가 20이고, 아이템이 0인 리스트
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# 연속된 두 수의 크기를 비교해서 인덱스의 값 1씩 추가
for idx, sco1 in enumerate(scores):
    for sco2 in scores:
        if sco1 < sco2:
            ranks[idx] += 1

print(scores)
print(ranks)

for i, s in enumerate(scores):
    print(f'score:{s} \t rank:{ranks[i] + 1}')
    # 순위가 0등이 되면 안되므로 ranks에 +1 해준다.