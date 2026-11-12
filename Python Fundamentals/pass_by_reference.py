"""
Python: call by object reference (pass by assignment).
Python has neither pure call by value nor pure call by reference.
"""

# Looks like CALL BY VALUE: ints are immutable, so += rebinds the local name.
def change_int(x):
    x += 10
    print("inside change_int:", x)


# Looks like CALL BY REFERENCE: the list is mutable, and append changes
# the one shared object in place.
def mutate_list(lst):
    lst.append(99)


# Neither: reassigning the parameter only rebinds the local name.
# True call by reference would have changed the caller's list.
def rebind_list(lst):
    lst = [1, 2, 3]
    print("inside rebind_list:", lst)


# Swap test: this cannot swap the caller's variables in Python.
def swap_fails(a, b):
    a, b = b, a


n = 5
change_int(n)
print("after change_int:", n)          # 5

nums = [1, 2]
mutate_list(nums)
print("after mutate_list:", nums)      # [1, 2, 99]

rebind_list(nums)
print("after rebind_list:", nums)      # [1, 2, 99]

a, b = 1, 2
swap_fails(a, b)
print("after swap_fails:", a, b)       # 1 2

# Python swaps at the call site instead:
a, b = b, a
print("after a, b = b, a:", a, b)      # 2 1