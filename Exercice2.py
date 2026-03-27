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

#Code python

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


#Version pseudo code
# a) avec POUR
"""
Algorithme CroissanceCumulative_Pour
    Entrée : N (nombre de jours)
    Sortie : croissance (croissance cumulée)
Début
    Ecrire "Entrez le nombre de jours : "
    Lire N
    Tant que N < 0 faire
        Ecrire "Le nombre de jours doit être supérieur ou égal à 0."
        Ecrire "Entrez le nombre de jours : "
        Lire N
    croissance <- 1
    Pour i de 1 à N faire
        croissance <- croissance * i
    Fin Pour
    Ecrire "Croissance cumulée sur ", N, " jours : ", croissance
Fin
"""

# b) avec TANT QUE
"""
Algorithme CroissanceCumulative_TantQue
    Entrée : N (nombre de jours)
    Sortie : croissance (croissance cumulée)
Début
    Ecrire "Entrez le nombre de jours : "
    Lire N
    Tant que N < 0 faire
        Ecrire "Le nombre de jours doit être supérieur ou égal à 0."
        Ecrire "Entrez le nombre de jours : "
        Lire N
    croissance <- 1
    i <- 1
    Tant que i <= N faire
        croissance <- croissance * i
        i <- i + 1
    Fin Tant que
    Ecrire "Croissance cumulée sur ", N, " jours : ", croissance
Fin    
"""


