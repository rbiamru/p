# # Brute Force:Function to return the maximum water that can be stored 
# def maxWater(arr, n): 
# 	res = 0
# 	for i in range(1, n):

# 		# Find maximum element on the left
# 		left = arr[i]
# 		for j in range(0, i):
# 			left = max(left, arr[j])

# 		# Find maximum element on the right
# 		right = arr[i]
# 		for j in range(i+1, n):
# 			right = max(right, arr[j])
# 		# Update the maximum water
# 		res += (min(left, right) - arr[i])
# 	return res
# # Method Precalculation
# def maxWater(arr, n):
# 	water = 0
# 	left = [0] * n
# 	right = [0] * n
# 	#Find maximum left 
# 	left[0] = arr[0]
# 	for i in range(1, n):
# 		left[i] = max(arr[i], left[i-1])
# 	#Find maximum right
# 	right[n-1] = arr[n-1]
# 	for i in range(n-2, -1, -1):
# 		right[i] = max(right[i+1], arr[i])
# 	# Check water between buildings
# 	for i in range(0, n):
# 			water += min(left[i], right[i]) - arr[i]
# 	return water
# Stack Method
# def maxWater(arr, n):
# 	# stores the indices of the bars
# 	stack = []
# 	# stores the final result
# 	ans = 0
# 	# loop through each bar
# 	for i in range(n):
# 		# Remove bars from the stack until a condition holds
# 		while(len(stack) != 0 and (arr[stack[-1]] < arr[i])):
# 			# store the height of the top and pop it
# 			pop_height = arr[stack[-1]]
# 			stack.pop()
# 		# If the stack does not have any bars or the popped bar has no left boundary
# 			if len(stack) == 0:
# 				break
# 			# Get the effective distance between left and right boundary of popped bar
# 			distance = i - stack[-1] - 1
# 			# Calculate the min_height
# 			min_height = min(arr[stack[-1]], arr[i]) - pop_height
# 			ans += distance * min_height
# 		# If the stack is either empty or height of the current bar is <= to the top bar of stack
# 		stack.append(i)
# 	return ans
# Horizontal scan method-> error 
# def maxWater(arr, n):
# 	num_blocks = 0
# 	max_height = float('-inf')
# 	# Find total of the blocks, max height and length of array
# 	for height in arr:
# 		num_blocks += height
# 		#n += 1
# 		max_height = max(max_height, height)
# 	# Total water is initialised to 0, left and right pointer initialised to 0 and n-1
# 	total = 0
# 	left = 0
# 	right = n-1
# 	for i in range(1, max_height + 1):
# 		# Find the leftmost point greater than current row at i
# 		while arr[left] < i:
# 			left += 1
# 		# Find the rightmost point greater than current at i
# 		while arr[right] < i:
# 			right -= 1
# 		# Water in this row = right - left + 1
# 			total += (right - left + 1)
# 	total -= num_blocks
# 	return total
# # 2 pointer approach
# def maxWater(arr, n):
# 	# Indices to traverse the array
# 	left = 0
# 	right = n-1
# 	# To store left max and right max for two pointers left and right
# 	l_max = 0
# 	r_max = 0
# 	# To store the total amount of rainwater trapped
# 	result = 0
# 	while left <= right:
# 		# We need to check for minimum of left and right max for each element
# 		if r_max <= l_max:
# 			# Add the difference between current value and right max at index r
# 			result += max(0, r_max - arr[right])
# 			# Update the right max
# 			r_max = max(r_max, arr[right])
# 			# Update the right pointer
# 			right -= 1
# 		else:
# 			 #Add the difference between current value and left max at index l
# 			result += max(0, l_max - arr[left])
# 			# Update the left max
# 			l_max = max(l_max, arr[left])
# 			# Update the left pointer
# 			left += 1
# 	return result
# Using Linear Search
def maxWater(arr, n):
	size = n - 1
	# Let the first element be stored as previous, we shall loop from index 1
	prev = arr[0]
	# To store previous wall's index
	prev_index = 0
	water = 0
	# To store the water until a larger wall is found, if there are no larger walls found then delete temp value from water
	temp = 0
	for i in range(1, size+1):
		# If the current wall is taller than the previous wall then make current wall as the previous wall and its index as previous wall's index for the subsequent loops
		if arr[i] >= prev:
			prev = arr[i]
			prev_index = i
			# Because larger or same height wall is found
			temp = 0
		else:
			# Since current wall is shorter than the previous, we subtract previous wall's height from the current wall's height and add it to the water
			water += prev - arr[i]
			# Store the same value in temp as well. If we don't find any larger wall then we will subtract temp from water
			temp += prev - arr[i]
	# If the last wall was >= to the previous wall then prev_index would be equal to size of the array(last element). If we didn't find a wall greater than or equal to the previous wall from the left then prev_index must be less than the index of the last element
	if prev_index < size:
		# Temp would've stored the water collected from previous largest wall till the end of array. If no larger wall was found then it has excess water and remove that from water
		water -= temp
		# We start from the end of the array, so prev should be assigned to the last element
		prev = arr[size]
		# Loop from the end of array upto the 'previous index' which would contain the "largest wall from the left"
		for i in range(size, prev_index - 1, -1):
			# Right end wall will be definitely smaller than the 'previous index' wall
			if arr[i] >= prev:
				prev = arr[i]
			else:
				water += prev - arr[i]
	return water
# Driver code
if __name__ == "__main__": 

	arr = [0, 1, 0, 2, 1, 0, 
		1, 3, 2, 1, 2, 1] 
	n = len(arr) 
	print(maxWater(arr, n)) 

