def findTime(train_A, N, t):
    train_B = [0.0] * N

    for i in range(1, N):
        train_B[i] = train_A[i] - train_A[i - 1]

    it = int(t)

    if 0.0 <= t <= 24.0 and (t - it) <= 60.0:
        for i in range(6):
            x = t + train_B[i]
            ix = int(x)

            if x - ix >= 0.60:
                x = x + 0.40
            if x > 24.00:
                x = x - 24.0

            print(f"{x:.2f}", end=" ")
            t = x
    else:
        print("Invalid Input")


train_A = [10.00, 10.04, 10.09, 10.15, 10.19, 10.22]
N = len(train_A)

t = float(input())
findTime(train_A, N, t)

