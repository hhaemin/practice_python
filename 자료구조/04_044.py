'''
대학생 길동이의 1,2,3학년의 성적은 다음과같다. 졸업할 때 4.0이상의 학점을
받기 위해 길동이가 받아야하는 4학년 1,2학기의 최소 학점을 구해보자
scores = ((3.7,4.2),(2.9,4.3),(4.1,4.2))
'''

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))
total = 0

for s1 in scores:
    for s2 in s1:
        total += s2

total = round(total, 1)
avg = round((total / 6), 1)
print(f'3학년 총학점: {total}')
print(f'3학년 평균: {avg}')

print('-'*60)

grade4TagetScore = round((4.0 * 8 - total), 1)
print(f'4학년 목표 총학점: {grade4TagetScore}')

minScore = round(grade4TagetScore / 2, 1)
print(f'4학년 한학기 최소학점: {minScore}')

scores = list(scores)               # 튜플은 변경이 불가능하므로, list로 바꿔서 추가해야 한다.
scores.append((minScore, minScore))

print('-'*60)

scores = tuple(scores)              # 점수는 중요한 것이기 때문에 변경불가능한 튜플로 다시 변경
print(f'scores: {scores}')