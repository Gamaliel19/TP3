"""
Exercice 4 Indice hydrique cumulé 
Écrire un algorithme qui calcule : 
1 + 1/2 + 1/3 + ... + 1/N 
Interprétation : 

indice de variation progressive de l’humidité du sol 
"""

N = int(input("Entrez le nombre de jours : "))
while N <= 0:
    print("Le nombre de jours doit être supérieur à 0.")
    N = int(input("Entrez le nombre de jours : "))

indice_hydrique_cumule = 0
i = 1
while i <= N:
    indice_hydrique_cumule += 1 / i
    i += 1

print(f"L'indice hydrique cumulé après {N} jours est : {indice_hydrique_cumule:.2f}")

#VERSION PSEUDO CODE
"""
ALGORITHME IndiceHydriqueCumule

VARIABLES
    N : ENTIER
    indice_hydrique_cumule : REEL
    i : ENTIER
DEBUT
    ECRIRE "Entrez le nombre de jours : "
    LIRE N
    TANT QUE N <= 0 FAIRE
        ECRIRE "Le nombre de jours doit être supérieur à 0."
        ECRIRE "Entrez le nombre de jours : "
        LIRE N
    FINTANTQUE
    indice_hydrique_cumule ← 0
    i ← 1
    TANT QUE i <= N FAIRE
        indice_hydrique_cumule ← indice_hydrique_cumule + 1 / i
        i ← i + 1
    FINTANTQUE
    ECRIRE "L'indice hydrique cumulé après ", N, " jours est : ", indice_hydrique_cumule
"""

