def searchNumberByLineAlgorithm(ns, sn):

    searchResultIdx = -1

    print(f'Numbers: {ns}')
    print(f'Search Numbers: {sn}')

    n = 0
    while True:

        # 만약 인덱스가 끝까지 갔음에도 없다 -> 찾기 실패!
        if n == len(ns):
            print('Search FAIL!!')
            break

        # 인덱스의 숫자가 찾는 숫자일 경우
        if ns[n] == sn:
            searchResultIdx = n
            print('Search SUCCESS!!')
            print(f'Search result INDEX: {searchResultIdx}')
            break

        n += 1

    return searchResultIdx