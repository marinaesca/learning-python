#marinaescalante-finished

#tempdata1 = "6 3"
#tempdata2 = "1 3 2 6 1 2"
#datalist1 = (tempdata1).split() # n & k
#datalist2 = (tempdata2).split() # a list

datalist1 = str(raw_input()).split() # n & k
datalist2 = str(raw_input()).split() # a list

n = int(datalist1[0])  # number of a nums in list
k = int(datalist1[1])  # number we are dividing with
aData = [int(x) for x in datalist2]

aList = []   # list containing the a numbers

# take in aList info
for num in range(n):
	aList.append(aData[num])

count = 0  # how many pairs are LEGIT

for i in range(n):
	for j in range((i + 1), n):
		if (not(i == j)) and ((i + j) % k == 0):
			count += 1

print(count)
			

