# X : les variables x1, ... , xn (sont entières)  4
# D : les domaines des variables (liste de liste de dimension n * dim(xi)) [[1,4,5,8],[2,3,5,7,9],[4,8,7,9],[1,4,5,7,8,9]]
# C : les contraintes s'exprimant sur les var xi (on va les binariser pour qu'elles ne portent que sur 2 var) 
import numpy as np

#Bactrack_ 10 : backtrack + AC3
#Bactrack_ 20 : backtrack + forward checking
#Bactrack_ 30 : backtrack + forward checking + AC3

def AC3(X,D,C):
    atester = []
    for i in range(X):
        for j in range(X): # prend pas la symétrie 
            if 0 not in C[i,j]:
                atester.append([i,j])
    while atester != [] :
        #print(atester)
        [x,y] = atester.pop()
        # v (une valeur de la variable x) n'est pas supportée (par les valeurs de la variable y)
        d = []
        for i in range(len(D[x])):
            #print(x,y,i)
            if D[x][i] in np.array(C[x,y])[:,0] :
                d.append(D[x][i])
            else :
                for z in range(X):
                    if z != y :
                        if 0 not in C[z,x]:
                            atester.append([z,x])
        D[x] = d
    return D



def forward_checking(I,X,D,C) : # I instantiation partielle où on vient de fixer <x,a>
    #I affectation partielle [[1,2],[3,7]] si variable x2=2 et x4=7 (c'est un np.array([[1,2],[3,7]] )), ici on vient de fixer x4=7
    x = I[len(I)-1,0]
    a = I[len(I)-1,1]
    for y in range(X):
        if y not in I[:,0] and 0 not in C[x,y]: # y not in I
            d = []
            #print("D[y]=" , D[y])
            for b in D[y]:
                if [a,b] in C[x,y]: # si (x,y) = (a,b) possible, alors on garde b dans D[y]
                    d.append(b)
            D[y] = d
    return D


