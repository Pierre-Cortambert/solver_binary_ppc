# X : les variables x1, ... , xn (sont entières)  4
# D : les domaines des variables (liste de liste de dimension n * dim(xi)) [[1,4,5,8],[2,3,5,7,9],[4,8,7,9],[1,4,5,7,8,9]]
# C : les contraintes s'exprimant sur les var xi (on va les binariser pour qu'elles ne portent que sur 2 var) 

from consistance import AC3,forward_checking
import numpy as np
import random

#teste la validité instantiation I (partielle ou non)
def valide(I,X,D,C):
    for i in range(len(I)-1):
        for j in range(i+1,len(I)): #range(i+1,X) enlève des combinaisons
            #print("I :",I)
            #print("(i,j) :",i,j)
            # s'il y a une contrainte entre xi et xj et que les valeurs attribuées n'appartient pas à l'espace des contraintes
            #print("np.array([I[i,1],I[j,1]]) :",np.array([I[i,1],I[j,1]]))
            if 0 not in C[I[i,0],I[j,0]] and [I[i,1],I[j,1]] not in C[I[i,0],I[j,0]]: #les contraintes doivent être symétrique si I pas ordonné
                return False
    return True

def Backtrack_1(I,X,D,C,cons,branch,summ): #I affectation partielle [[1,2],[3,7]] si variable x2=2 et x4=7 (c'est un np.array([[1,2],[3,7]] ))
    global solution
    solution = "pas possible" 
    if not valide(I,X,D,C) or [] in D:
        solution = "pas possible"  
        return False
    if len(I) == X : #ie I est complète dès le début
        return True,I
    else : #choisir une variable non insanciée
        if branch == 0: #on branche sur les variables x instanciée par ordre croissant (par défaut)
            x = 0
            while x in I[:,0] : #and x < X-1 : # x indice variable non instanciée
                x+=1
        if branch == 1:#on branche sur les variables x choisies aléatoirement
            x=random.randint(0,X-1)
            while x in I[:,0]:
                x=random.randint(0,X-1)
        if branch == 2: # on branche sur la variable avec le plus petit domaine de définition
            l = [len(k) for k in D]
            x = np.argmin(l)
            while x in I[:,0] :
                l[x]= np.max(l)+1
                x = np.argmin(l)
        if branch == 3: # on branche sur la variable avec le plus grand domaine de définition
            l = [len(k) for k in D]
            x = np.argmax(l)
            while x in I[:,0] :
                l[x]= np.min(l)-1
                x = np.argmax(l)
        d=D.copy()
        for v in D[x]: # Rq : on prend les valeurs dans l'ordre de D[x], on aurait pu prendre un ordre aléatoire avec random.shufle(D[x])
            if sum(I[:,1])+v <= summ : #si pas de contrainte, summ est fixé à plus grand float
                J = np.append( I, [np.array([x,v])],axis=0)
                if cons == 2 or cons == 3 :
                        D = forward_checking(J,X,D,C)
                if Backtrack_1(J,X,D,C,cons,branch,summ) :
                    if len(J) == X : 
                        solution=J
                    return True    
                else : 
                    if cons==2 or cons==3:
                        D = d.copy()               
        return False


def Backtrack_0(I,X,D,C,cons,branch,summ): 
    print("Obtient-on une solution réalisable ? ",Backtrack_1(I,X,D,C,cons,branch,summ))
    return solution
