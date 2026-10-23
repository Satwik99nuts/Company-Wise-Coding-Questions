def square_number(n):
    k = int(n**0.5) + 1

    while True:
        square = k * k

        if str(square) == str(square)[::-1]:
            return square - n

        k += 1

n = int(input())
print(square_number(n))
