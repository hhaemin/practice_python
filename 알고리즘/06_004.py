'''
이진검색 : 정렬되어 있는 자료구조에서 중앙값과 크고 작음을 이용해서 데이터를 검색한다.

리스트를 오름차순으로 정렬한 후 '7'을 검색하고 위치(인덱스)를 출력하자
[4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
'''

nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
print(f'nums: {nums}')

# 오름차순으로 정리
nums.sort()
print(f'nums: {nums}')

searchData = int(input('찾으려는 숫자 입력: '))

# 존재하지 않는 index -1로 초기화
searchResultIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx +  endIdx) // 2
midVal = nums[midIdx]

# nums가 0보다 작거나 88보다 크면 안되므로 범위 설정
while searchData <= nums[len(nums)-1] and searchData >= nums[0]:

    # 끝에 있는 data와 동일하다면
    if searchData == nums[len(nums)-1]:
        searchResultIdx = len(nums)-1
        break

    # searchData가 midVal보다 큰 경우
    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx +  endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    # searchData가 midVal보다 작은 경우
    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    # searchData가 midVal와 같은 경우
    elif searchData == midVal:
        searchResultIdx = midIdx
        break

print(f'searchResultIdx: [{searchResultIdx}]')