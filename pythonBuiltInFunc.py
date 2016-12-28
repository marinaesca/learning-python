#marinaescalante-unfinished

# more python, learning builtin functions

data = list()

data.append(3)
data.append(6)
data.append(9)

print(data)

last = data.pop()

print("%r, last: %s" % (data, last))

more_data = ["polly", "kiep", "daffy", "angel"]

print("Does this work with strings? ")
print(more_data.index("polly"))
print(more_data.index("angel"))

more_data.insert(2, "mickey")

print(more_data)