## Ce projet correspond au cours de Programmation Par Contrainte du Master Parisien de Recherche Opérationnelle
Il a été entierement réalisé par Pierre Cortambert sur la base du cours de David Savourey.

L’objectif du projet est d’implémenter un solveur générique de CSP où les contraintes sont binaires et les variables entières. 
Les domaines des variables seront finis. 

# Nous considérons des CSP sous forme de triplet (X,D,C) , avec :
**X** : les variables x1, ... , xn (sont entières)  
**D** : les domaines des variables 
**C** : les contraintes sont définies sur deux variables (i,j) par un ensemble de tuples C[i,j] (2 valeurs ordonnées) qui satisfont la contrainte

# Vous pourrez trouver dans les fichiers suivants :

**main.py** : fichier principal appelant les autres fonctions 

**benchmarks.py** : mets en format CSP les problèmes de n-reines et de colorabilité

**backtrack.py** : fonction validité d'une instance par rapport aux contraintes et fonction de backtrack (prend en argument d'autres paramètres définis plus tard)

**consistance.py** : fonctions d'arc consistance AC3 et de forward checking

Pour utiliser le solveur :

- vous pouvez faire appel à main.py (via python3 main.py), dans cet appel, vous pouvez choisir le problème et y appliquer certains paramètres

- vous pouvez faire appel directement au solveur via main.py en ajoutant des termes :
	
	le 1er est le **problème considéré**    : 0 pour problème vu en cours, 1 pour les n-reines, 2 pour la colorabilité
    	
	le 2e est la **méthode de résolution**  : 0 backtracking, 1 backtracking + AC3, 2 backtracking + forward checking, 3 backtracking + forward checking + AC3
    	
	Si vous avez choisi comme problème le numéro 1 : il faut ajouter la **dimension n du plateau**
    	
					   le numéro 2 : il faut ajouter le **nom du fichier** et le **nombre de couleur à tester**
    
    Ensuite, si vous voulez ajouter des paramètres supplémentaires, il faut ajouter des termes: (vous pouvez en ajouter soit les 2 premiers soit les 4)

	pour l'**initialisation** : 0 pour prendre la valeur par défaut, 1 pour variable randomisée, 2 variable initiale à choisir

	pour les **branchements** : 0 pour prendre la valeur par défaut, 1 pour brancher aléatoirement, 2 branchement par indice de la variable avec le plus petit domaine de définition, et 3 avec le plus grand
    	
	ajout de wrapper :
		**alldiff** : mettre à 1 pour mettre la contrainte que toutes les variables ont une valeur différente
    		**summ** : mettre à un entier n pour mettre la contrainte que la somme des variables soit inférieure à cet entier (si vous ne voulez pas appliquer cette contrainte mettre à 0)
    		
# Exemples :

	pour vérifier les 12-reines avec un backtrack + AC3 :

**python3 main.py 1 1 12**

	pour vérifier la 12 colorabilité de jean.col (se trouvant dans le foldeur instance_couleur/) avec un backtrack + forward checking + AC3 en commançant avec une variable randomisée

**python3 main.py 2 3 jean.col 12 1 0**

	pour vérifier le problème du cours (j'ai changé une contrainte), avec backtrack, une initialisation et branchement par défaut et la contrainte alldiff:
	
**python3 main.py 0 0 0 0 1 0**
