#TRI_A_BULL
def tri_bull(tab):
    n = len(tab)

    for i in range(n):
        for j in range(0, n - i - 1):

            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


tab = [7, 2, 6, 5, 3, 8, 1, 4]

tri_bull(tab)

print("Le tableau trié à bull est:")
for i in range(len(tab)):
    print("%d" % tab[i])




#TRI_PAR_SEELCTION
def tri_selection(tab):
    for i in range(len(tab)):

        min = i

        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp

    return tab    

tab = [7, 2, 6, 5, 3, 8, 1, 4]
tri_selection(tab)    
print("Le tableau trié par selection est:")
for i in range(len(tab)):
    print ("% d" % tab[i])    

#TRI_PAR_INSERTION
def tri_insertion(tab):

    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k


tab = [7, 2, 6, 5, 3, 8, 1, 4]
tri_insertion(tab)
print ("Le tableau trié par insertion est:")
for i in range(len(tab)):
    print ("% d" % tab[i])    