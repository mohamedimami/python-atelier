set1={23, 42, 65, 57, 78, 83, 29}
set2={57, 83, 29, 67, 73, 43, 48}
#on a declaré deux sets
set3=set1.intersection(set2) #cette set3 est le résultat de l'intersection de la set1 avec set2, on a utilisé l'operation : set1.intersection(set2) 
print('intersection',set3) #on a afficher set3
print('set1 apres supression',set1.difference(set2)) #on a utilisé l'opération suivante : set1.difference(set2) pour supprimer les éléments communs entre la set1 et set2 de la set1  
