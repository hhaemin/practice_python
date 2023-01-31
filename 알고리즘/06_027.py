def mSort(ns):
    if len(ns) < 2:
        return ns

    # 분할 단계
    # 중간 값
    midIdx = len(ns) // 2 
    # 처음부터 중간값까지
    leftNums = mSort(ns[0:midIdx])
    # 중간값부터 마지막값까지
    rightNums = mSort(ns[midIdx:len(ns)])

    # 병합 단계 
    mergedNums = []
    leftIdx = 0; rightIdx = 0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergedNums.append(leftNums[leftIdx])
            leftIdx += 1
        else:
            mergedNums.append(rightNums[rightIdx])
            rightIdx += 1

    mergedNums = mergedNums + leftNums[leftIdx:]
    mergedNums = mergedNums + rightNums[rightIdx:]
    print(f'mergedNums: {mergedNums}')
    return mergedNums


nums = [8, 1, 4, 3, 2, 5, 10, 6]
print(f'mergedNums: {mSort(nums)}')