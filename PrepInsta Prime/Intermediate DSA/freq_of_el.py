def countfreq(arr):
    mp = {}
    ans = []

    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    for num, freq in mp.items():
        ans.append([num, freq])

    return ans

if __name__ == "__main__":
    arr = list(map(int, input("Write the array : ").split()))
    print(countfreq(arr))
