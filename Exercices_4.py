#Exercice 4.2
a = 0
b = 7
while a < 20:
	a = a +1
	print(a, a*b)


#Exercice 4.3
a, b = 1, 1.65
while a < 16385:
	print(a, "euro(s)", b, "dollar(s)")
	a, b = a*2, b*2

	
#Exercices 4.4
b, c = 15, 1
while c < 12:
	print(b)
	b, c = b*3, c+1
#Exercice 4.5
largeur = 20
hauteur = 25
longueur = 50
print ("largeur X hauteur X longueur = ", largeur * hauteur * longueur)

# Exercice 4.6
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

