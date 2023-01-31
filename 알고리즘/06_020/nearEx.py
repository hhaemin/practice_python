'''
근삿값 알고리즘을 이용해서 시험점수를 입력하면 학점이 출력되는 프로그램
평균점수에 따른 학점 기준 점수는 다음과 같다.
95 -> A
85 -> B
75 -> C
65 -> D
55 -> F
'''

import near

scores = []

kor = int(input('input kor score: '))
scores.append(kor)
eng = int(input('input eng score: '))
scores.append(eng)
mat = int(input('input mat score: '))
scores.append(mat)
sci = int(input('input sci score: '))
scores.append(sci)
his = int(input('input his score: '))
scores.append(his)

totalScore = sum(scores)
print(f'totalScore: {totalScore}')

avgScore = totalScore / len(scores)
print(f'avgScore: {avgScore}')

grade = near.getNearNum(avgScore)
print(f'grade: {grade}')
