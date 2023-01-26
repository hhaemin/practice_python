'''
튜플에 요구사항에 맞춰 아이템 슬라이싱
- index 0부터 3까지
- index 2부터 4까지
- index 3부터 끝까지
- index 2부터 뒤에서 -2까지
- index 0부터 끝까지 3단계
'''

# numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)
# #index: 0 ~ 3
# print(f'numbers[:4] : {numbers[0:4]}')
#
# #index: 2 ~ 4
# print(f'numbers[2:5] : {numbers[2:5]}')
#
# #index: 3 ~ end
# print(f'numbers[3:] : {numbers[3:]}')
#
# #index: 2 ~ end-2
# print(f'numbers[2:-1] : {numbers[2:-1]}')
#
# #index: 0 ~ end, step = 3
# print(f'numbers[::3] : {numbers[::3]}')
#
#
# # 최솟값
# print(f'최솟값 : {min(numbers)}')
# print(f'최솟값 인덱스 : {numbers.index(min(numbers))}')
#
# # 최댓값
# print(f'최댓값 : {max(numbers)}')
# print(f'최댓값 인덱스 : {numbers.index(max(numbers))}')

'''
시험 점수를 입력한 후 튜플에 저장하고 과목별 학점을 출력
'''

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))
sciScore = int(input('과학 점수 입력: '))
hisScore = int(input('국사 점수 입력: '))

scores = ({'kor':korScore},
          {'eng':engScore},
          {'mat':matScore},
          {'sci':sciScore},
          {'his':hisScore})

print(f'scores: {scores}')

for item in scores:
    for key in item.keys():
        if item[key] >= 90:
            item[key] = 'A'
        elif item[key] >= 80:
            item[key] = 'B'
        elif item[key] >= 70:
            item[key] = 'C'
        elif item[key] >= 60:
            item[key] = 'D'
        else:
            item[key] = 'F'

print(f'scores: {scores}')