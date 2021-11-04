l=[2,6,8,6,9,4,2,6,4,9] 
dictionnaire={}
#on déclare une liste et un dictionnaire vide

for i in range(len(l)): 
    a=0 #on a declaré un variable 'a' qui va compter un élément combien de fois a été répétées
    for j in range(len(l)): #on a fait deux boucles 'for' , une pour exporter les éléments et autre pour trouver est ce qu'il y a un élément égale à un autre
        if l[j]==l[i]: 
            a=a+1
        #lorsqu'il trouve 2 éléments égaux, le compteur 'a' va être ajouté par 1, et ainsi de suite     
    dictionnaire[l[i]]=a #ici il va être stocker l'élément avec nombre de fois trouvés répétées dans la liste, dans le dictionnaire , la boucle va être répétée jusqu'à la fin de la liste
print(dictionnaire) #il va afficher le dictionnaire