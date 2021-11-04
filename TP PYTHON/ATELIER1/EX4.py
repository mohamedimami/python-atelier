def fibonacci(N):
    if(N <= 1):
        return N
    else:
        return (fibonacci(N-1) + fibonacci(N-2))

p = int(input("Donnez le nombre de termes: "))


for i in range(p):
    print(fibonacci(i))