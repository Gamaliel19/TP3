"""
Exercice 2 Croissance cumulative (analogie factorielle) 
En agriculture, certaines grandeurs évoluent de manière cumulative. 
Écrire un algorithme qui calcule une croissance cumulée sur N jours : 
Croissance = 1 × 2 × 3 × ... × N 
avec : 
1. 0! = 1 
Résoudre : 
a) avec POUR 
b) avec TANT QUE 

"""

# a) avec POUR
N = int(input("Entrez le nombre de jours : "))
while N < 0:
    print("Le nombre de jours doit être supérieur ou égal à 0.")
    N = int(input("Entrez le nombre de jours : "))
croissance = 1
for i in range(1, N + 1):
    croissance *= i

print(f"Croissance cumulée sur {N} jours : {croissance}")


# b) avec TANT QUE
N = int(input("Entrez le nombre de jours : "))
while N < 0:
    print("Le nombre de jours doit être supérieur ou égal à 0.")
    N = int(input("Entrez le nombre de jours : "))  
croissance = 1
i = 1
while i <= N:
    croissance *= i
    i += 1

print(f"Croissance cumulée sur {N} jours : {croissance}")


