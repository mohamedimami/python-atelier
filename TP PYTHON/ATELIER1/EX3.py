def somme(S): #on a définit la récursivité 'somme()' qui va prendre le nombre S et tant qu'il n'égale pas à 0 , il va retourner S+somme(S-1), et ainsi de suite .
    if S==0:
        return 0
    else:
        return S+somme(S-1)

a=int(input("Entrez le nombre de termes : "))
print("la somme égale :")
print(somme(a))