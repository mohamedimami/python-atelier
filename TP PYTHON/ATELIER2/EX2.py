#EXERCICE2
my_list=[11, 45, 8, 23, 14, 12, 78, 45, 89]
l1=[]
l2=[]
l3=[] 
#on a crée ces trois listes pour stocker les éléments de la liste
P=int(len(my_list)/3) #on prend un variable 'P' qui égale un tiers de la longueur de my_list pour qu'on peut diviser la liste en trois listes (on a declaré P de type 'int' pour que P soit un nombre naturel)

for i in range(P): #on utilise la boucle 'for' pour commencer à prendre les éléments de my_list commençant avec le 1er élément(indice 0) jusqu'à l'élément qui a l'indice un tiers (1/3) de la longueur (P)(dans ce cas depuis l'indice 0 jusqu'à l'indice : P = 9/3 =3)
    l1.append(my_list[i]) #la fonction 'append' va commencer à ajouter les éléments du 1er tiers de la my_list dans l1
for i in range(P,P*2): #même chose dans la boucle for précédente mais dans ce cas il va commencer depuis P jusqu'à P*2(le 2ème tiers de my_list)
    l2.append(my_list[i]) #la fonction 'append' va commencer à ajouter les éléments du 2ème tiers de my_list dans l2
for i in range(P*2,P*3+len(my_list)%3): #ici la boucle 'for' va prendre le reste des éléments de my_list (les éléments du 3ème tiers + le reste si le longueur n'est pas divisible sur 3 (len(my_list)%3))
    l3.append(my_list[i]) #la fonction 'append' va commencer à ajouter le reste de my_list dans l3

#après la division de my_list en trois listes : l1,l2 et l3 , on va les inverser avec l'opération '[::-1]'
print(l1[::-1])

print(l2[::-1])

print(l3[::-1])