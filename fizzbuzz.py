


# write num 1 - 100
# for mult of 3: print "Fizz"
# for mult of 5: print "Buzz"
# mult of both print "FizzBuzz"

for i in range(100):
	result = ""
	num = i+1;

	if num % 3 == 0:
		result = result + "Fizz"
	if num % 5 == 0:
		result = result + "Buzz"
	if not(num % 3 == 0) and not(num % 5 == 0):
		result = result + str(num)
	print(result)


print("yatta!")