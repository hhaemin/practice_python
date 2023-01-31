nums = [10, 2, 7, 21, 0]
print(f'not sorted nums: {nums}')

length = len(nums) - 1
for i in range(length):
    # 맨 끝까지 돌 필요가 없으므로 length-i까지만 비교
    for j in range(length-i):
        if nums[j] > nums[j+1]:
            # temp = nums[j]
            # nums[j] = nums[j+1]
            # nums[j+1] = temp
            # 같은 방법이다. 
            nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
    print()

print(f'sorted nums: {nums}')

# import copy
#
# def bubbleSort(ns):
#     cns = copy.copy(ns)
#     length = len(cns) - 1
#     for i in range(length):
#         for j in range(length - i):
#             if cns[j] > cns[j + 1]:
#                 cns[j], cns[j + 1] = cns[j + 1], cns[j]
#
#     return cns
#
# nums = [10, 2, 7, 21, 0]
# sortedNums = bubbleSort(nums)
#
# print(f'nums: {nums}')
# print(f'sortedNums: {sortedNums}')