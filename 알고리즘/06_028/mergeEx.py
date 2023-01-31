import random as rd
import sortMod as sm

rNums = rd.sample(range(1, 101), 10)
print(f'not sorted rNums: {sm.mSort(rNums)}')
print(f'merge sorted rNums by ASC: {sm.mSort(rNums)}')
print(f'merge sorted rNums by DESC: {sm.mSort(rNums, asc=False)}')