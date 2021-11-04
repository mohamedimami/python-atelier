def pos(T,x):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if p==A[i][j]:
                x=i
                y=j
                return x,y
        

A = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
p=int(input("cherche un élément : "))
a=pos(A,p)
print("la position (i,j) de  ",p,"dans la matric est ",a)