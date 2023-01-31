'''
1부터 100까지의 난수 10개를 생성하고, 다음의 요구 사항을 만족하는 모듈
요구사항1) 병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
요구사항2) 위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션 추가
'''

# def mSort(ns):
#     if len(ns) < 2:
#         return ns
#
#     midIdx = len(ns) // 2
#     leftNums = mSort(ns[0:midIdx])
#     rightNums = mSort(ns[midIdx:len(ns)])
#
#     mergedNums = []
#     leftIdx = 0; rightIdx = 0
#     while leftIdx < len(leftNums) and rightIdx < len(rightNums):
#         if leftNums[leftIdx] < rightNums[rightIdx]:
#             mergedNums.append(leftNums[leftIdx])
#             leftIdx += 1
#         else:
#             mergedNums.append(rightNums[rightIdx])
#             rightIdx += 1
#
#     mergedNums = mergedNums + leftNums[leftIdx:]
#     mergedNums = mergedNums + rightNums[rightIdx:]
#     return mergedNums


def mSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

    mergedNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if asc:

            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

        else:

            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergedNums.append(leftNums[leftIdx])
                leftIdx += 1
            else:
                mergedNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergedNums = mergedNums + leftNums[leftIdx:]
    mergedNums = mergedNums + rightNums[rightIdx:]
    return mergedNums


if __name__ == '__main__':
    nums = [8, 1, 4, 3, 2, 5, 10, 6]
    print(f'merge sorted nums: {mSort(nums)}')
    print(f'merge sorted nums: {mSort(nums, asc=False)}')