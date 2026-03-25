"""
Exercice 1 Analyse de données climatiques 
Écrire (et implémenter en python) un algorithme qui lit N températures journalières (°C) et calcule : 
1. la somme 
2. le produit (optionnel, interprétation scientifique) 
3. la température moyenne 
Le nombre N est saisi au clavier. 
Résoudre : 
a) avec POUR 
b) avec RÉPÉTER…JUSQU’À 
c) avec TANT QUE 

"""

# a) avec POUR
N = int(input("Entrez le nombre de températures journalières : "))
while N <= 0:
    print("Le nombre de températures doit être supérieur à 0.")
    N = int(input("Entrez le nombre de températures journalières : "))

somme = 0
produit = 1
temperature_moyenne = 0

for i in range(N):
    temperature = float(input(f"Entrez la température du jour {i+1} : "))
    somme += temperature
    produit *= temperature

temperature_moyenne = somme / N
print(f"Somme des températures : {somme}")
print(f"Produit des températures : {produit}")
print(f"Température moyenne : {temperature_moyenne}")


# b) avec RÉPÉTER…JUSQU’À
N = int(input("Entrez le nombre de températures journalières : "))
while N <= 0:
    print("Le nombre de températures doit être supérieur à 0.")
    N = int(input("Entrez le nombre de températures journalières : "))
somme = 0
produit = 1
temperature_moyenne = 0

i = 0
while True:
    temperature = float(input(f"Entrez la température journalière {i+1} : "))
    somme += temperature
    produit *= temperature
    i += 1
    if i >= N:
        break
temperature_moyenne = somme / N
print(f"Somme des températures : {somme}")
print(f"Produit des températures : {produit}")
print(f"Température moyenne : {temperature_moyenne}")


# c) avec TANT QUE
N = int(input("Entrez le nombre de températures journalières : "))

while N <= 0:
    print("Le nombre de températures doit être supérieur à 0.")
    N = int(input("Entrez le nombre de températures journalières : "))

somme = 0
produit = 1
temperature_moyenne = 0
i = 0
while i < N:
    temperature = float(input(f"Entrez la température journalière {i+1} : "))
    somme += temperature
    produit *= temperature
    i += 1

temperature_moyenne = somme / N
print(f"Somme des températures : {somme}")
print(f"Produit des températures : {produit}")
print(f"Température moyenne : {temperature_moyenne}")


"""
VERSION SPEUDO_CODE
"""
#a) Version avec POUR

"""
ALGORITHME AnalyseClimatique_POUR

VARIABLES
    N : ENTIER
    T : REEL
    somme : REEL
    produit : REEL
    moyenne : REEL

DEBUT

    ECRIRE "Entrer le nombre de températures : "
    LIRE N

    TANT QUE N < 0 FAIRE
        ECRIRE "N doit être positif. Réessayez : "
        LIRE N
    FIN TANT QUE

    somme ← 0
    produit ← 1

    POUR i ← 1 A N FAIRE
        ECRIRE "Entrer la température ", i, " : "
        LIRE T

        somme ← somme + T
        produit ← produit * T
    FIN POUR

    SI N > 0 ALORS
        moyenne ← somme / N
    SINON
        moyenne ← 0
    FIN SI

    ECRIRE "Somme = ", somme
    ECRIRE "Produit = ", produit
    ECRIRE "Moyenne = ", moyenne

FIN
"""

#b) Version avec RÉPÉTER...JUSQU'À

"""
ALGORITHME AnalyseClimatique_REPETER
VARIABLES
    N : ENTIER
    T : REEL
    somme : REEL
    produit : REEL
    moyenne : REEL
    i : ENTIER
DEBUT

    REPETER
        ECRIRE "Entrer N : "
        LIRE N
    JUSQU'A N >= 0

    somme ← 0
    produit ← 1
    i ← 1

    REPETER
        SI i > N ALORS
            SORTIR
        FIN SI

        ECRIRE "Entrer température ", i, " : "
        LIRE T

        somme ← somme + T
        produit ← produit * T

        i ← i + 1
    JUSQU'A i > N

    SI N > 0 ALORS
        moyenne ← somme / N
    SINON
        moyenne ← 0
    FIN SI

    ECRIRE "Somme = ", somme
    ECRIRE "Produit = ", produit
    ECRIRE "Moyenne = ", moyenne

FIN
"""
#c) Version avec TANT QUE

"""
ALGORITHME AnalyseClimatique_TANT_QUE
VARIABLES
    N : ENTIER
    T : REEL
    somme : REEL
    produit : REEL
    moyenne : REEL
    i : ENTIER
DEBUT

    ECRIRE "Entrer N : "
    LIRE N

    TANT QUE N < 0 FAIRE
        ECRIRE "N invalide. Réessayer : "
        LIRE N
    FIN TANT QUE

    somme ← 0
    produit ← 1
    i ← 1

    TANT QUE i ≤ N FAIRE
        ECRIRE "Entrer température ", i, " : "
        LIRE T

        somme ← somme + T
        produit ← produit * T

        i ← i + 1
    FIN TANT QUE

    SI N > 0 ALORS
        moyenne ← somme / N
    SINON
        moyenne ← 0
    FIN SI

    ECRIRE "Somme = ", somme
    ECRIRE "Produit = ", produit
    ECRIRE "Moyenne = ", moyenne

FIN
 """

