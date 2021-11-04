def fact(N):
    if N == 1: 
        return N #déterminer la fonction fact avec récursivité
    return N * fact(N - 1)

def deter(M):
    r = 0
    for i in range(1, M + 1):
        r = (fact(i)/i) + r
    return r

A=int(input("Entrez le nombres des facteurs \n"))
print(deter(A))