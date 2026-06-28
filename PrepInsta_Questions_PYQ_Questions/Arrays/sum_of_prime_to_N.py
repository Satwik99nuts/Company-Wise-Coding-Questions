def prime(num):
    prime = [True]*(num+1)
    
    prime[0] = False
    prime[1] = False

    i = 2
    while i*i<=num:
        if prime[i]:
            j = i*i
            while j<=num:
                prime[j] = False
                j+=1
        i+=1
        
    for i in range(2,num+1):
        if prime[i]:
            print(i,end=" ")
num = int(input("Write the number = "))