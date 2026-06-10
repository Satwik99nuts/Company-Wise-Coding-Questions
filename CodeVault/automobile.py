v = int(input("Enter number of vehicles: "))
w = int(input("Enter total number of wheels: "))

if w < 2 * v or w > 4 * v or w % 2 != 0:
    print("Invalid Input")
else:
    four_wheelers = (w - 2 * v) // 2
    two_wheelers = v - four_wheelers
    print(f"TW = {two_wheelers} and FW = {four_wheelers}")
