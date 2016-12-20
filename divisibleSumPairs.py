#marinaescalante-unfinished

n = input()  # number of a nums in list
k = input()  # number we are dividing with

aList = []   # list containing the a numbers

# take in aList info
for num in range(n):
	aList.append(input())

count = 0  # how many pairs are LEGIT

for i in range(n):
	for j in range((i + 1), n):
		if (not(i == j)) and ((i + j) % k == 0):
			count += 1

print(count)
			

