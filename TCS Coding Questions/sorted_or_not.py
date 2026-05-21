# giv_arr = list(map(int, input("Write the array: ").split()))
# n = len(giv_arr)
# for i in range(n-1):
#     if giv_arr[i] > giv_arr[i+1]:
#         print("It is not a sorted array")
#         break
# else:
#     print("It is a sorted array")

raw = input("Write the array: ")

# If user gives spaces → split normally, else split each digit
if " " in raw:
    giv_arr = list(map(int, raw.split()))
else:
    giv_arr = list(map(int, raw))  # splits each character

n = len(giv_arr)
for i in range(n - 1):
    if giv_arr[i] > giv_arr[i + 1]:
        print("It is not a sorted array")
        break
else:
    print("It is a sorted array")
