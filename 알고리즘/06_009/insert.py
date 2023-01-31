import sortMod as sm
nums = [5, 10, 2, 1, 0]

# ascending 오름차순
# for i1 in range(1, len(nums)):
#     i2 = i1 - 1
#     cNum = nums[i1]
#
#     while nums[i2] > cNum and i2 >= 0:
#         nums[i2 + 1] = nums[i2]
#         i2 -= 1
#
#     nums[i2+1] = cNum
#
#     print(f'nums: {nums}')

# nums = [0, 5, 2, 10, 1]

# descending 내림차순
# for i1 in range(1, len(nums)):
#     i2 = i1 - 1
#     cNum = nums[i1]
#
#     while nums[i2] < cNum and i2 >= 0:
#         nums[i2 + 1] = nums[i2]
#         i2 -= 1
#
#     nums[i2+1] = cNum
#
#     print(f'nums: {nums}')


# sortMod 모듈
result = sm.sortNumber(nums, asc=False)
print(f'result: {result}')