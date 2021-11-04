def Compter(N):
    if N ==0:
        return 0   
    else :   
        return 1+Compter(N//10) 
        #le programme va diviser sur 10 jusqu'il arrive à 1 après il va retourrner la dernière valeur


A=int(input("Entrez un nombre : "))

print("Le nombre de chiffre est : ")

print(Compter(A))