#EXERCICE 1
l1=[1,10,9,3,8,6,5] #voici la 1ère liste 
l2=[6,16,12,4,19,8] #voici la 2èeme liste
l3=[] # on a declaré une 3ème liste pour stocker les éléments qu'on va les exporter depuis les deux listes 
for i in range(1,len(l1),2): #on a utilisé la boucle 'for' qui va commencer depuis l'indice 1 jusqu'à la fin de la première liste avec deux pas pour qu'il va prendre seulement les éléments avec l'indice impair
    l3.append(l1[i]) #on a utilisé la boucle 'append' pour lorsqu'il trouve un élément avec indice impair il va le stocker dans la 3ème liste
for i in range(0,len(l2),2): #on a utilisé une autre boucle 'for' comme la précédente , mais maintenant pour les éléments avec indices pairs(la boucle va commencer depuis l'indice 0 cette fois)
    l3.append(l2[i]) #même chose dans la précédente

print(l3) #ici on va afficher la liste qui contient les éléments avec indices IMPAIRS de la 1ère liste , et les éléments avec indices PAIRS de la 2ème 