'''
1부터 100까지의 난수 10개를 생성하고, 다음의 요구 사항을 만족하는 모듈
요구사항1) 퀵정렬 알고리즘을 이용한 난수 정렬 모듈 구현
요구사항2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가
'''

# def qSort(ns):
#
#     if len(ns) < 2:
#         return ns
#
#     midIdx = len(ns) // 2
#     midVal = ns[midIdx]
#
#     smallNums = []
#     sameNums = []
#     bigNums = []
#
#
#     for n in ns:
#         if n < midVal:
#             smallNums.append(n)
#         elif n == midVal:
#             sameNums.append(n)
#         else:
#             bigNums.append(n)
#
#     return qSort(smallNums) + sameNums + qSort(bigNums)


def qSort(ns, asc=True):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallNums = []
    sameNums = []
    bigNums = []


    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)
    else:
        return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)


if __name__ == '__main__':
    nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
    print(f'quick sorted nums: {qSort(nums)}')
    print(f'quick sorted nums: {qSort(nums, asc=False)}')