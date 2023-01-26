'''
튜플의 과일 개수에 대해서 오름차순 및 내림차순으로 정렬

(두개를 비교하면서 자리바꿈)
'''

fruits = ({'수박':8}, {'포도':13}, {'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits)

cIdx = 0; nIdx = 1                  # cIdx : 현재 인덱스값; nIdx : 다음 인덱스값
eIdx = len(fruits) - 1              # eIdx : 마지막 인덱스값

flag = True
while flag:
    curDic = fruits[cIdx]
    nextDic = fruits[nIdx]

    curDicCnt = list(curDic.values())[0]
    nextDicCnt = list(nextDic.values())[0]

    if nextDicCnt < curDicCnt:                      # 다음 과일이 그 전 과일보다 개수가 적으면
    #if nextDicCnt > curDicCnt
        fruits.insert(cIdx, fruits.pop(nIdx))       # 그자리에서 없애고(pop), 그 전자리에 삽입(insert)
        nIdx = cIdx + 1                             # 항상 nIdx는 cIdx보다 1이 커야 한다.
        continue

    nIdx += 1
    if nIdx > eIdx:
        cIdx += 1
        nIdx = cIdx + 1

        if cIdx == 5:
            flag = False

print(tuple(fruits))