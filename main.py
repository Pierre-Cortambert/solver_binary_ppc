import sys
import time
import numpy as np
import random
from benchmarks import reines,colorabilite,lecture_colorabilite
from backtrack import valide,Backtrack_0,Backtrack_1
from consistance import AC3,forward_checking

def main() :
    print("Bonjour, vous êtes sur le mini solveur de CSP binaires de Pierre Cortambert.")
    if len(sys.argv)>1 :
        probleme=int(sys.argv[1]) # = 0, 1 ou 2
        cons = int(sys.argv[2]) # = 0, 1, 2 ou 3
        print("methode de resolution cons = ",cons)
        if probleme == 0 :
            print("Le CSP est l'exemple donné dans le cours (cours 1 - slide 12) avec une contrainte supplémentaire dans C2 : (1,7). ")
            X = 4
            D = np.array([[1,4,5,8],[2,3,5,7,9],[4,8,7,9],[1,4,5,7,8,9]])
            C = np.array([[[0],[0],[[1,7],[1,9],[5,9]],[[1,1],[1,5],[1,7],[5,5],[5,9],[8,9]]],[[0],[0],[0],[[2,7],[2,9],[5,8],[7,9],[9,9]]],[[[7,1],[9,1],[9,5]],[0],[0],[[4,1],[8,1],[9,7]]],[[[1,1],[5,1],[7,1],[5,5],[9,5],[9,8]],[[7,2],[9,2],[8,5],[9,7],[9,9]],[[1,4],[1,8],[7,9]],[0]]])
            k=3
        elif probleme == 1 : #n-reines
            n=int(sys.argv[3])
            print("Vous avez sélectionné le problème des n-Reines avec n = ",n)
            X,D,C = reines(n)
            k=4
        elif probleme == 2 : #colorabilite
            fichier = "instance_couleur/" + sys.argv[3]
            m = int(sys.argv[4])
            n,L=lecture_colorabilite(fichier)
            print("Vous avez sélectionné le problème de colorabilité pour le fichier ",fichier,", instance possédant ",n,"sommets. Vous essayez de la colorier avec",m," couleurs.")
            X,D,C=colorabilite(n,m,L)
            k=5
        else :
            print("Vous n'avez pas bien rentré le numéro de problème à traiter")

        init= 0
        branch=0
        alldiff=0
        summ=float('inf')
        if len(sys.argv)>=k+1: #ie plus de paramétrisation
            init = int(sys.argv[k])
            print("init = ",init)
            if init not in [0,1,2] :
                print("Votre initialisation est éronnée.")
            branch = int(sys.argv[k+1])
            print("branch = ",branch)
            if branch not in [0,1,2,3] :
                print("Votre branchement est éronné.")
            if len(sys.argv)>k+2 :
                alldiff = int(sys.argv[k+2])
                print("alldiff = ",alldiff)
                summ = int(sys.argv[k+3])
                print("summ = ",summ)           
                if type(summ)==int or summ==0:
                    summ=float('inf')
        else :
            print("Vous n'avez pas choisi de paramétrisation supplémentaire.")



    else :    
        #PROBLEME - benchmarks
        print("Quel problème voulez vous tester ?") #benchmarks
        print("0 : CSP binaire tiré du cours")
        print("1 : n-Reines")
        print("2 : colorabilité")
        probleme = int(input())

        #METHODE RESOLUTION - backtrack et consistance
        print("Quel méthode de résolution voulez vous tester ?") #backtrack
        print("0 : Backtracking")
        print("1 : Backtracking + AC3")
        print("2 : Backtracking + forward checking")
        print("3 : Backtracking + forward checking + AC3")
        cons= int(input())
        if cons not in [0,1,2,3]:
            print("Vous n'avez pas rentré de méthode de résolution possible.")

        #INITIALISATION de X,D,C 
        if probleme == 0 :
            print("Le CSP est l'exemple donné dans le cours (cours 1 - slide 12) avec une contrainte supplémentaire dans C2 : (1,7). ")
            X = 4
            D = np.array([[1,4,5,8],[2,3,5,7,9],[4,8,7,9],[1,4,5,7,8,9]])
            C = np.array([[[0],[0],[[1,7],[1,9],[5,9]],[[1,1],[1,5],[1,7],[5,5],[5,9],[8,9]]],[[0],[0],[0],[[2,7],[2,9],[5,8],[7,9],[9,9]]],[[[7,1],[9,1],[9,5]],[0],[0],[[4,1],[8,1],[9,7]]],[[[1,1],[5,1],[7,1],[5,5],[9,5],[9,8]],[[7,2],[9,2],[8,5],[9,7],[9,9]],[[1,4],[1,8],[7,9]],[0]]])
        elif probleme == 1 :
            print("Vous avez sélectionné le problème des n-Reines.")
            print("Quelle dimension n souhaitez-vous (correspondant à la taille du plateau) ?")
            n= int(input())
            X,D,C = reines(n)
        elif probleme == 2 :
            print("Vous avez sélectionné le problème de colorabilité.")
            print("Il faut choisir un nom de fichier dans instance_couleur/ (par exemple anna.col, huck.col, jean.col ou homer.col")
            name=input() #input donne un type string
            fichier = "instance_couleur/"+name
            n,L=lecture_colorabilite(fichier)
            #n,L = 4, np.array([[2,3,4],[1,3],[1,2],[1]]) #ex triangle avec un sommet rattaché
            print("Ce fichier a ",n," sommets. Vous voulez tester quel nombre de colorabilité ?")
            m=int(input())
            X,D,C=colorabilite(n,m,L)
            print("Nombre de sommets du graphe :", n)

        else :
            print("Vous n'avez pas bien rentré le numéro de problème à traiter")
        
        print("Voulez vous plus de paramétrisation ? (répondre 1 pour oui et 0 pour non)")
        param = int(input())
        init= 0
        branch=0
        alldiff=0
        summ=float('inf')
        if param == 1:
            print("Quelle initialisation ?")
            print("0 : variable initiale x=0 à D[0][0] (par défaut)")
            print("1 : variable initiale x randomisée selon la taille X")
            print("2 : variable initiale à choisir")
            init = int(input())
            if init not in [0,1,2] :
                print("Votre initialisation est éronnée.")
            print("Quel est votre choix de branchement ?")
            print("0 : par ordre croissant selon l'indice des variables (par défaut)")
            print("1 : par indice de variable non instanciée randomisée")
            print("2 : par indice de la variable avec le plus petit domaine de définition")
            print("3 : par indice de la variable avec le plus grand domaine de définition ")
            branch = int(input())
            if branch not in [0,1,2,3] :
                print("Votre branchement est éronné.")
            print("Voulez vous ajouter une contrainte ? (répondre 1 pour oui)")
            contr=int(input())
            if contr == 1:
                print("Variales toutes différentes : (répondre 1 pour oui)")
                alldiff=int(input())
                print("Variable de somme maximale : (oui : entrer entier naturel, non: entrer 0)")
                summ = int(input())
                if type(summ)==int or summ==0:
                    summ=float('inf')
        elif param == 0:
            print("Vous n'avez pas choisi de paramétrisation supplémentaire.")
        elif param not in [0,1]:
            print("Demande de paramétrisation incorrecte.")

    #initialisation :
    if init == 0:
        variable_init=0
    elif init ==1:
        variable_init=random.randint(0,X-1)
    elif init==2:
        print("Choisissez un entier entre 0 et ",X-1)
        variable_init = int(input())
        if variable_init not in [k for k in range(X)]:
            print("Mauvaise entrée... On commence l'algorithme sur la valeur par défaut")
            variable_init=0
    if branch in [0,2,3]:
        I = np.array([[variable_init,D[0][0]]]) 
    elif branch == 1:
        I = np.array([[variable_init,random.choice(D[0])]])

    #DEBUT TEMPS
    start = time.time()

    if cons == 1 or cons == 3 :
        D = AC3(X,D,C) 

    if alldiff == 1: #on va changer C
        for i in range(X):
            for j in range(X):
                if 0 not in C[i,j]:
                    for k in range(len(C[i,j])):
                        c=[]
                        if C[i,j][k][0] != C[i,j][k][1]:
                            c.append(C[i,j][k])
                    C[i,j]=c
                        
    d=D.copy()
    solution = Backtrack_0(I,X,D,d,C,cons,branch,summ)
    print("Solution : ")
    print(solution)
    end = time.time()

    print("L'algorithme a tourné pendant ",end-start," secondes !")
    if probleme == 2 and type(solution)!= np.ndarray:
        g = max(solution[:,1])
        print("Nombre de couleur dans le graphe : ",g)
    
main()

