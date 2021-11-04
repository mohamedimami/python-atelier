liste1=[47, 64, 69, 37, 76, 83, 95, 97] #Déclaration de la liste
liste2=[] #Déclaration d'une nouvelle liste pour stocker les éléments qui existent dans le dictionaire 
dict1={"Yassine":47 , "Imane":69 , "Mohamed":76 , "Abir":97} #Déclaration du dictionaire

for i in liste1: #Boucle 'for' pour lire chaque élément dans la liste
        if i in dict1.values():
            liste2.append(i) #Remplir les éléments qui existent dans le dictionnaire dans la liste1
    

print(liste2) #Affichage de la liste résultante