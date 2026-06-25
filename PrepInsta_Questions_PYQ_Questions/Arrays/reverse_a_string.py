a = input("Write the character: ").strip()
res = ""
for i in range(len(a)-1,-1,-1):
    res+=a[i]
print(res)