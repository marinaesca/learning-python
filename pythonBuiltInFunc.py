#marinaescalante-unfinished

# more python, learning builtin functions

print("~~~~~~~~~~~~~~~~~~ lists ~~~~~~~~~~~~~~~~~~")

data = list()

data.append(3)
data.append(6)
data.append(9)

print(data)

last = data.pop()

print("%r, last: %s" % (data, last))

more_data = ["polly", "kiep", "daffy", "angel"]

print("Does this work with strings? yes")
print("Tia's dog is at index %d" % (more_data.index("polly")))
print("Michelle's dog is at index %d" % (more_data.index("angel")))

more_data.insert(2, "mickey")

print(more_data)

print("~~~~~~~~~~~~~~~~~~ sets ~~~~~~~~~~~~~~~~~~")
# when my sets print on commandline they look weird, maybe bc python 2.7?

unique = set()

unique.add(15)
unique.add(17)
unique.add(18)
unique.add(19)
unique.add(21)

print(unique)

print(3 in unique)
print(17 in unique)

unique.remove(21)
print(unique)

evens = {2, 4, 6, 8}
print(evens)

rando_list = [1, 1, 2, 3, 4]
fib = set(rando_list)
print(fib)

print("~~~~~~~~~~~~~~~~~~ maps ~~~~~~~~~~~~~~~~~~")
# again appears I have different syntac when printin maps

squadAges = dict()

print("can maps have string key with an int value? yes")

squadAges["CJ"] = 15
squadAges["Dat"] = 17
squadAges["Tia"] = 18
squadAges["Marina"] = 19
squadAges["Thao"] = 21

print(squadAges)
print(squadAges["Marina"])

for key, value in squadAges.items():
	print(key, value)
print("rando order!")

counter = dict()
numbers = [1, 3, 3, 3, 8]

for value in numbers:
	if value not in counter:
		counter[value] = 0
	counter[value] += 1

print(counter)

print("~~~~~~~~~~~~~~~~~~ split ~~~~~~~~~~~~~~~~~~")

friends = "madi~jackie~tia"
print(friends.split("~"))

secretmessage = "pj41koj41klj41klj41kyj41kpj41kej41kpj41kpj41kej41kr"
decode = secretmessage.split("j41k")
print(decode)


print("~~~~~~~~~~~~~~~~~~ join ~~~~~~~~~~~~~~~~~~")
# crucial: Iterables include things like strings, lists, etc.

letters = ["a", "b", "c"]
print(",".join(letters))
print("".join(decode)) # from previous split section
print("THIS IS SO COOL")

print("~~~~~~~~~~~~~~~~~~ super secret spy ~~~~~~~~~~~~~~~~~~")

secretmessage = "pj41koj41klj41klj41kyj41kpj41kej41kpj41kpj41kej41kr"
decode = secretmessage.split("j41k")
print("".join(decode))

print("~~~~~~~~~~~~~~~~~~ reversed ~~~~~~~~~~~~~~~~~~")

nums = [2, 4, 6, 8]
print(list(reversed(nums)))

sent = "daffy doodle"
print("".join(reversed(sent)))

print("~~~~~~~~~~~~~~~~~~ zip ~~~~~~~~~~~~~~~~~~")

evens = [0, 2, 4]
odds = [1, 3, 5]

for x, y in zip(evens, odds):
	print(x, y)

print("~~~~~~~~~~~~~~~~~~ enumerate ~~~~~~~~~~~~~~~~~~")

dogs = ["polly", "kiep", "daffy", "angel", "mickey", "cocoa"]

for i, value in enumerate(dogs):
	print("At index %d, found the dog %s " % (i, value))



