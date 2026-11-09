a = [1,2,3]
a.append([4,5]) #Adds the entire object as one element.
print(a)

b = [1,2,3]
b.extend([4,5]) #Adds elements from an iterable individually.
print(b)

# Memory trick
# - append() = Add one object.
# - extend() = Add multiple elements from an iterable.