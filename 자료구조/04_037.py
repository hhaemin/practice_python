scores = {'score1':8.9, 'score2':8.1, 'score3':8.5, 'score4':9.8, 'score5':8.8}
minScore = 10; minScoreKey = ''
maxScore = 0; maxScoreKey = ''

for key in scores.keys():
    if scores[key] < minScore:
        minScore = scores[key]
        minScoreKey = key

    if scores[key] > maxScore:
        maxScore = scores[key]
        maxScoreKey = key

print('minScore : {}'.format(minScore))
print('minScoreKey : {}'.format(minScoreKey))

print('maxScore : {}'.format(maxScore))
print('maxScoreKey : {}'.format(maxScoreKey))

del scores[minScoreKey]
del scores[maxScoreKey]

print('scores : {}'.format(scores))