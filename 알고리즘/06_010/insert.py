import random
import sortMod as sm

nums = random.sample(range(1, 1000), 100)
print(f'not sortedNumber: {nums}')

# 객체 생성
sn = sm.SortNumbers(nums)

# ascending
sn.setSort()
sortedNumber = sn.getSortedNumbers()
print(f'sortedNumber by ASC: {sortedNumber}')

# descending
sn.isAscending(False)
sn.setSort()
sortedNumber = sn.getSortedNumbers()
print(f'sortedNumber by DESC: {sortedNumber}')

# min & max
print(f'MinNumber : {sn.getMinNumber()}')
print(f'MaxNumber : {sn.getMaxNumber()}')