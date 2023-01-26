playerScore = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
print('playerScore: {}'.format(playerScore))
print(type(playerScore))

playerScore = list(playerScore)                 # 튜플을 리스트로 자료형 변환
print(type(playerScore))

playerScore.sort()
print('playerScore: {}'.format(playerScore))
playerScore.pop(0)
playerScore.pop(len(playerScore) - 1)

playerScore = tuple(playerScore)
print('playerScore: {}'.format(playerScore))
print(type(playerScore))

sum = 0
avg = 0
for score in playerScore:
    sum += score

avg = sum / len(playerScore)

print('총점: %.2f' % sum)
print('평점: %.2f' % avg)