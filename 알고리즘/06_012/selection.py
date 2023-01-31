import random
import sortMod as sm
import copy

scores = random.sample(range(50, 101), 20)
print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

# ascending
# result = sm.sortNumber(scores)
result = sm.sortNumber(copy.deepcopy(scores))
print(f'result(ASC): {result}')

# descending
# result = sm.sortNumber(scores, asc=False)
result = sm.sortNumber(copy.deepcopy(scores), asc=False)
print(f'result(DESC): {result}')
