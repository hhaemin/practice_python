'''
학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서
각각의 순위를 구하고, 중간고사 대비 기말고사 순위 변화(편차)를 출력하는 프로그램
(시험 성적은 난수를 이용)
'''

import rankMod as rm
import random

midStuScos = random.sample(range(50, 101), 20)
endStuScos = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(midStuScos, endStuScos)

rd.setMidRank()
print(f'midStuScos: {midStuScos}')
print(f'mid_rank: {rd.getMidRank()}')

rd.setEndRank()
print(f'endStuScos: {endStuScos}')
print(f'end_rank: {rd.getEndRank()}')

rd.printRankDeviation()