InputProjet2=open('Input2-ProjetsTypesConstruits.txt','r')
VariableProjet=InputProjet2.read()

a = VariableProjet.split('\n')

#pourquoi faire?
j1='ABC'
j2='XYZ'

#scores
won = 6
nul = 3
lost = 0

cailloux = 1
feuille = 2
ciseaux = 3


                  
#partie 1
#admettons que les elfs jouent 1500 manches:
score = 0

for meh in range(len(a)):
        #manches avec le cailloux
        if a[meh] == 'A Z':
                score = score+ won+cailloux
        elif a[meh] == 'A Y':
                score = score + nul + cailloux
        elif a[meh] == 'A X':
                score = score + lost + cailloux

        #avec la feuille
        elif a[meh] == 'B Z':
                score = score + won + feuille
        elif a[meh] == 'B Y':
                score = score + nul + feuille
        elif a[meh] == 'B X':
                score = score + lost + feuille

        #avec les ciseaux
        elif a[meh] == 'C Z':
                score =score + ciseaux + won
        elif a[meh] == 'C Y':
                score =score + ciseaux + nul
        elif a[meh] == 'C X':
                score =score + ciseaux + lost


#on imprime le score a la fin
print(score)
                  
                  
#partie 2
for meh2 in range(len(a)):
    #manches avec le cailloux (adversaire)
        if a[meh] == 'A Z': #gagner contre la pierre, donc utiliser feuille
                score = score + won + feuille
        elif a[meh] == 'A Y': #nul contre pierre, donc pierre
                score = score + nul + cailloux
        elif a[meh] == 'A X': #perdre contre pierre, donc ciseaux
                score = score + lost + ciseaux

        # ... etc ...
        
        #avec la feuille (adversaire)
        elif a[meh] == 'B Z':
                score = score + won + ciseaux
        elif a[meh] == 'B Y':
                score = score + nul + feuille
        elif a[meh] == 'B X':
                score = score + lost + cailloux

        #avec les ciseaux (adversaire)
        elif a[meh] == 'C Z':
                score =score + cailloux + won
        elif a[meh] == 'C Y':
                score =score + ciseaux + nul
        elif a[meh] == 'C X':
                score =score + feuille + lost
                
#on imprime le score à la fin
print(score)
