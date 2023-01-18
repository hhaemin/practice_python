def divideNumber(n):

    if n % 2 == 0:
        result = '짝수'
    else:
        result = '홀수'

    return result

    # if n % 2 == 0:
    #     return '짝수'
    # else:
    #     return '홀수'

returnValue = divideNumber(8)
print(f'returnValue: {returnValue}')