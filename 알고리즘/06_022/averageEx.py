'''
평균을 구하고 순위를 정하는 알고리즘
'''

import near

scores = (8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7)
top5PlayerScores = [9.12, 8.95, 8.12, 7.90, 7.88]

print(f'Current scores: {top5PlayerScores}')

total = 0
average = 0

for n in scores:
    total += n

average = round(total / len(scores), 2)

print(f'total: {total}')
print(f'average: {average}')

tp = near.Top5Players(top5PlayerScores, average)
tp.setAlignScore()
top5PlayerScores = tp.getFinalTop5Scores()
print(f'Final scores: {top5PlayerScores}')
