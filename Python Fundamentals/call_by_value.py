def change_int(x):
    x += 10              # ints are immutable: this rebinds local x to a new object
    print("inside int:", x)

def mutate_list(lst):
    lst.append(99)       # mutates the shared object: caller sees this

def rebind_list(lst):
    lst = [1, 2, 3]      # rebinds the local name only: caller is unaffected
    print("inside rebind:", lst)

n = 5
change_int(n)
print("after change_int:", n)        # 5 (looks like call by value)

nums = [1, 2]
mutate_list(nums)
print("after mutate_list:", nums)    # [1, 2, 99] (looks like call by reference)

rebind_list(nums)
print("after rebind_list:", nums)    # [1, 2, 99] (the rebind did not leak out)