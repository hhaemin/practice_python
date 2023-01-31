nums = [4, 2, 5, 1, 3]

for i in range(len(nums)-1):
	minIdx = i

	for j in range(i+1, len(nums)):
		if nums[minIdx] > nums[j]:
			minIdx = j

	tempNum = nums[i]
	nums[i] = nums[minIdx]
	nums[minIdx] = tempNum
	# nums[i], nums[minIdx] = nums[minIdx], nums[i]

print(f'nums: {nums}')