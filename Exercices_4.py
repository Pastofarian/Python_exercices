#Exercice 4.2
#Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.

a = 0
b = 7
while a < 20:
	a = a +1
	print(a, a*b)


#Exercice 4.3
#Écrivez un programme qui affiche une table de conversion de sommes d’argent exprimées en
#euros, en dollars canadiens. La progression des sommes de la table sera « géométrique »,
#comme dans l’exemple ci-dessous :

a, b = 1, 1.65
while a < 16385:
	print(a, "euro(s)", b, "dollar(s)")
	a, b = a*2, b*2

	
#Exercices 4.4
#Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au
#triple du terme précédent.

b, c = 15, 1
while c < 12:
	print(b)
	b, c = b*3, c+1
	
#Exercice 4.5
#Écrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont fournis
#au départ la largeur, la hauteur et la profondeur.

largeur = 20
hauteur = 25
longueur = 50
print ("largeur X hauteur X longueur = ", largeur * hauteur * longueur)

# Exercice 4.6
#Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en un
#nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur modulo : %
#).

#random seconds number:
sec = 9258236253         

y = sec % 31536000
year = sec // 31536000

nm = y % 2592000
month = y // 2592000

d = nm % 86400
day = nm //86400

h = d % 3600
hour = d // 3600

m = h % 60
minute = h // 60

s = m % 60
second = m % 60

print (sec, "seconds are equal to :", year, "year(s)", month, "month(s)", day, "day(s)", hour, "hour(s)", minute, "minute(s)", second, "seconds")

# Exercice 4.7
#Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en
#signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
#Exemple : 7 14 21 * 28 35 42 * 49 ...

a = 0
b = 7
while (a < 20):
    a = a + 1
    c = a*b
    if (c % 3 ==0):
        print (c, "*", end =" ")
    else:
        print (c, end =" ")
    
# Exercice 4.8
#Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
#mais n’affiche que ceux qui sont des multiples de 7.    

a = 0
b = 13
while (a < 50):
    a = a + 1
    c = a*b
    if (c % 7 == 0):
        print (c, end =" ")

#Écrivez un programme qui affiche la suite de symboles suivante :

a = 0
b = 1
while (a < 7):
    a = a + 1
    c = a * b
    print (c*"*")
