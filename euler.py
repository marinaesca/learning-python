#marinaescalante

# check long lilne 19 

import math

print("~~~~~")
print("goal: what is the 10001st prime?")
print("ex: 1st 6 primes: 2,3,5,7,11,13 -> 6th prime is 13")
print("~~~~~")


# make a multiple method
# will return how many multiples a number has
# start at 2, will always be divisible by 1
def multiples(num):
	count = 0

	for i in range(2, int(math.sqrt(num))):
	#for i in range(2, num):
		if num % (i) == 0:
			count += 1

	return count

# make a prime method
# will return true or false for prime
def prime(num):
	if multiples(num) > 1:
		return False
	return True


# go through and count up primes
# take in goal number prime
# have a number i, increase 1 by 1
# have a count, while less than goal, inc count
# begin loop by inc i, to avoid 1, 
#    & when exit loop i is correct number
# when hit goal return the number (i)
def goalPrime(goal):
	i = 1
	count = 0
	while count < goal:
		i += 1
		if prime(i):
			count += 1
	return i
	


#testers:
print(multiples(10))
print(multiples(13))

print(prime(10))
print(prime(13))

print(goalPrime(1))
print(goalPrime(2))
print(goalPrime(3))
print(goalPrime(4))
print(goalPrime(5))
print(goalPrime(6))
#print(goalPrime(10001))


