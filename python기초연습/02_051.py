'''
국어, 영어, 수학, 과학, 국사 점수를 입력하면 
총점을 비롯한 각종 데이터가 출력되는 프로그램

과목별 점수를 입력하면 총점, 평균, 편차를 출력
평균 (국어 : 85, 영어: 82, 수학:89, 과학:75, 국사:94)
각종 편차 데이터는 막대 그래프로 시각화한다.
'''

korAvg = 85; engAvg = 82; matAvg = 89
sciAvg = 75; hisAvg = 94
totalAvg = korAvg + engAvg + matAvg + sciAvg + hisAvg
avgAvg = int(totalAvg / 5)

korScore = int(input('국어 점수: '))
engScore = int(input('영어 점수: '))
matScore = int(input('수학 점수: '))
sciScore = int(input('과학 점수: '))
hisScore = int(input('국사 점수: '))

totalScore = korScore + engScore + matScore + sciScore + hisScore
avgScore = int(totalScore / 5)

korGap = korScore - korAvg
engGap = engScore - engAvg
matGap = matScore - matAvg
sciGap = sciScore - sciAvg
hisGap = hisScore - hisAvg

totalGap = totalScore - totalAvg
avgGap = avgScore - avgAvg

print('-' * 70)
print('총점: {}({}), 평균:{}({})'.format(totalScore, totalGap, avgScore, avgGap) )
print('국어: {}({}), 영어: {}({}), 수학: {}({}), 과학:{}({}), 국사: {}({})'.format
      (korScore,korGap,engScore,engGap,matScore,matGap,sciScore,sciGap,hisScore,hisGap))
print('-' * 70)
str = '+' if korGap > 0 else '-'
print('국어 편차: {}({})'.format(str * abs(korGap), korGap)) # abs는 절대값을 나타내는 함수
str = '+' if engGap > 0 else '-'
print('영어 편차: {}({})'.format(str * abs(engGap), engGap))
str = '+' if matGap > 0 else '-'
print('수학 편차: {}({})'.format(str * abs(matGap), matGap))
str = '+' if sciGap > 0 else '-'
print('과학 편차: {}({})'.format(str * abs(sciGap), sciGap))
str = '+' if hisGap > 0 else '-'
print('국사 편차: {}({})'.format(str * abs(hisGap), hisGap))
str = '+' if totalGap > 0 else '-'
print('총점 편차: {}({})'.format(str * abs(totalGap), totalGap))
str = '+' if avgGap > 0 else '-'
print('평균 편차: {}({})'.format(str * abs(avgGap), avgGap))