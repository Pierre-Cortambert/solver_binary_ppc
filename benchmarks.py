import numpy as np

def reines(n):
    X = n
    D=n*[[k for k in range(1,n+1)]]
    #D = np.array([[k for k in range(1,n+1)] for i in range(n)]) #les lignes et colonnes sont numérotées à partir de 0
    C = np.zeros((n,n),list)
    for i in range(n):
        for j in range(n):
            if i==j:
                C[i,j]=[0]
            if i!=j : #si i=j, on reste sur une liste avec zero
                C[i,j]=[]
                for k in range(1,n+1):
                    for l in range(1,n+1):
                        if k!=l and i-j!=k-l and j-i!=k-l :
                            C[i,j].append([k,l])
    return X,D,C


def lecture_colorabilite(fichier): #fichier est de type .col
    filin = open(fichier,"r")
    lines = filin.readlines()
    L=[]
    for line in lines :
        l = line.split()
        if l[0]=='p':
            n = int(l[2])
            L=[[] for k in range(n)]
        if l[0]=='e':
            L[int(l[1])-1].append(int(l[2])) #-1 car decallage dans indexation indices en python
    filin.close()
    return n,L

def colorabilite(n,m,L): # n nombre de noeuds, L[i] liste des noeuds voisins de i
    X=n
    D=n*[[k for k in range(1,m+1)]] #chaque sommet i a une couleur D[i], au maximum n couleurs pour un graphe complet
    C = np.zeros((n,n),list)
    for i in range(n):
        for j in range(n):
            if j+1 not in L[i] or i==j: #pas de contrainte entre i et j (decallage de 1 pour l'indexation via python)
                C[i,j]=[0]
            else:                
                C[i,j]=[]
                for k in range(1,n+1):
                    for l in range(1,n+1):
                        if k!=l:
                            C[i,j].append([k,l])
    return X,D,C


