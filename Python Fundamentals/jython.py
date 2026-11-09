text = "Python"
modified = "J" + text[1:]
print(modified)


a = [10, 20, 30]
b = a

del a
# print(a) - will raise an error if del a is there as its deleted
print(b)