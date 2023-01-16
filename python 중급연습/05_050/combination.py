def getCombinationCnt(n, r):
    
    resultP = 1
    resultR = 1
    resultC = 1
    
    for n in range(n, (n-r), -1):
        resultP = resultP * n
        
    for n in range(r, 0, -1):
        resultR = resultR * n
        
    resultC = int(resultP / resultR)
    
    return resultC