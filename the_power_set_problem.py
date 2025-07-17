# python: power set problem
# input: an array of ints
# output: print all possible permutations from a given array

# ex: [1,2,3]
# []
# [1]
# [1,2]
# [1,3]
# [2,3]
# [1,2,3]

def power_set(int_arr):
	result = []

	# create and add the permutations sets
	for i in range(len(int_arr)):
		current_num = int_arr[i]
		# add just this num in a set
		result.append([current_num])
		# add all values up to this index
		result.append(int_arr[0:i])

		for j in range(i):
			new_num = int_arr[j]

			# add set with just new num & current num
			temp_arr = [current_num]
			temp_arr.append(new_num)
			result.append(temp_arr)

			# add set with all nums up to current num minus new num
			temp_arr = int_arr[0:i]
			temp_arr.remove(new_num)
			if (temp_arr):
				result.append(temp_arr)

	result.append(int_arr)
	return result


test_set = [1,2,3]
print(power_set(test_set))


