def getPermutationCnt(n,r):
    
    result = 1
    for n in range(n, (n-r), -1):
        result = result * n
        
    return result

'''
python에서 제공하는 순열 함수 사용시

from itertools import permutations

def getPermutations(ns, r):
    
    pList = list(permutations(ns, r))
    print(f'{len(ns)}P{r} 개수: {len(pList)}')
    
    for n in permutations(ns, r):
        print(n, end='')     
'''