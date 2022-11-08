nbInitial = int(input("entrez un nombre en base 10 de 0 à 2401 : ")) #on entre le nombre a conv en base de 10

#on verif qu'on ne dépasse pas 2401:
if nbInitial > 2401:
    nbInitial = int(input("veuillez entrer un nombre inférieur ou égal à 2401 : ")) #on redemande un nombre

nb2 = nbInitial #on garde l'initial dans la poche pour la fin donc on le copie

nbBaseS = [] #on crée une liste vide pour pouvoir mettre notre nombre à l'envers:

#etapes de l'algo
''' 
nb3 = nb2 // 7
nb4 = nb3 * 7
nb5 = nb2 - nb4
print(nb5) #dernier chiffre de la conversion
'''

i = 4 #étant donné que le programme a une limite à 2401, on peut limiter le nombre de tours à 5
#on va devoir répéter l'algo autant de fois qu'il faut pour atteindre x-0, x sera notre premier chiffre
while i >= 0: #c'est nb4 qui doit atteindre 0
    nb3 = nb2 // 7
    #print(nb3)
    nb4 = nb3 * 7
    #print(nb4)
    nb5 = nb2 - nb4
    #print(nb5) #le resultat à retourner
    nbBaseS.append(nb5)
    nb2 = nb3
    i = i - 1 #pour que i atteigne 0 un jour, sinon ça crash :)

print(' ') #Pas forcément utile, sert a espacer les deux lignes à la sortie
nbBaseS.reverse() #on reverse la liste pour avoir notre nombre dans le bon sens
#print(''.join(map(str, nbBaseS))) #on retrouve cette ligne en dessous, elle sert à transformer la liste en chaine de characteres.
print('Le nombre', nbInitial, 'correspond en base de 7 à', ''.join(map(str, nbBaseS)))
