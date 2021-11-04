def bin(B): #on a posé cette fonction pour qu'il fait les calculs de convertion du nombre décimal en nombre binaire
    x=0
    y=1
    while(B!=0): #on a utilisé la boucle 'while' qui va prendre B et il va le diviser sur 2 et le reste va se stocker dans x et y
        z=B%2
        x +=z*y
        y=y*10
        B//=2
    return x

n=int(input("Donnez un nombre :  "))

print("Le résultat de la covertion est : ")

print(bin(n))    