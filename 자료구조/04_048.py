'''
학급별 학생 수를 나타낸 튜플을 이용해서, 요구 사항에 맞는 데이터를 출력하는 프로그램

전체 학생 수; 평균 학생 수; 학생 수가 가장 적은 학급;
학생 수가 가장 많은 학급; 학급별 학생 편차
'''

studentCnt = ({'cls01':18},
              {'cls02':21},
              {'cls03':20},
              {'cls04':19},
              {'cls05':22},
              {'cls06':20},
              {'cls07':23},
              {'cls08':17})

totalCnt = 0
minStdCnt = 0; minCls = ''
maxStdCnt = 0; maxCls = ''
deviation = []

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        totalCnt += v

        if idx == 0 or minStdCnt > v:
            minStdCnt = v
            minCls = k

        if maxStdCnt < v:
            maxStdCnt = v
            maxCls = k

print(f'전체 학생 수: {totalCnt}명')

avgCnt = totalCnt/len(studentCnt)
print(f'평균 학생 수: {round(avgCnt, 2)}명')

print(f'학생 수가 가장 적은 학급: {minCls}({minStdCnt}명)')
print(f'학생 수가 가장 많은 학급: {maxCls}({maxStdCnt}명)')

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        deviation.append({k:round(v-avgCnt, 2)})

print(f'학급별 학생 편차: {deviation}')