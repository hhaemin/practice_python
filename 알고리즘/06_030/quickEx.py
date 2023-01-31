import random as rd
import sortMod as sm

rNums = rd.sample(range(1, 101), 10)
print(f'not sorted rNums: {sm.qSort(rNums)}')
print(f'merge sorted rNums by ASC: {sm.qSort(rNums)}')
print(f'merge sorted rNums by DESC: {sm.qSort(rNums, asc=False)}')