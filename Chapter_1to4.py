Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = y = 7           #Sous Python, on peut assigner une valeur à plusieurs variables simultanément
>>> x
7
>>> y
7
>>> a, b = 4, 8.33      #affectations parallèles à l’aide d’un seul opérateur
>>> a
4
>>> b
8.33
>>> largeur = 20
>>> hauteur = 5 * 9.3
>>> largeur * hauteur
930.0
>>>                         #5.9*5*20 = 930.0#
>>>                         # Display the text “Hello, World!” on the screen.
print(“Hello, World!”)
SyntaxError: invalid character in identifier
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> a = 3
>>> b = 5
>>> c = 7
>>> a-b//c
3
>>> a+b//c
3
>>> a+b
8
>>> a-b
-2
>>> a-b/c
2.2857142857142856
>>> a=4
>>> b=3
>>> a//b
1
>>> a=9.5
>>> b=5
>>> a/b
1.9
>>> a//b
1.0
>>>                   # // est floordivision. it means that it round to the low unit
>>> a, b = 7.3, 12    #assigne automatiquement le type « réel » à la variable a,
                      #et le type « entier » à la variable b.
>>> y = 3*a + b/5
>>> y
24.299999999999997
>>> 10 % 3
1
>>> 10 % 5
0
>>> 45 % 6
3
>>> 20 % 4
0
>>> 21 % 6
3
>>> # 6 * 3 = 18   21 - 18 = 3
>>> # Modulo %
>>> r, pi = 12, 3.14159
>>> s = pi * r**2
>>> print(s)
452.38896
>>> print (type(r), type(pi), type(s))
<class 'int'> <class 'float'> <class 'float'>
>>> # fonction "type()" = entier, réel ...
>>> h, m, s = 15, 27, 34
>>> print("nombre de secondes écoulées depuis minuit = ", h*3600 + m*60 + s)
nombre de secondes écoulées depuis minuit =  55654
>>> # Coool algorithme !

>>> >>> a, b = 3,7
>>> a = b
>>> b = a
>>> print(a, b)
7 7
>>> a, b = 3, 7
>>> b=a
>>> a=b
>>> print(a,b)
3 3
>>> # Vous obtiendrez un résultat contraire si vous intervertissez les 2e et 3e lignes.
>>> a = 150
>>> if (a > 100):
	print ("a dépassé la centaine")
  
  a dépassé la centaine
>>> a = 20
>>> if (a > 100):
	print ("a dépassé la centaine")
else:
	print ("a ne dépasse pas la centaine")

	
a ne dépasse pas la centaine
>>> a = 0
>>> if a > 0:
	print ("a est positif")
elif a < 0 :
	print("a est négatif")
else:
	print ("a est nul")

	
a est nul
