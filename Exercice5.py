"""
Exercice 5 Synchronisation climatique (PGCD) 
Deux phénomènes climatiques se répètent selon des cycles (ex : pluie tous les A jours, vent tous les 
B jours). 
Écrire un algorithme qui calcule le P.G.C.D. de A et B (algorithme d’Euclide). 

Permet de savoir quand les deux phénomènes coïncident
"""


A = int(input("Entrez la période du premier phénomène : "))
B = int(input("Entrez la période du deuxième phénomène : "))

# Algorithme d'Euclide pour calculer le P.G.C.D.
while A != B:
    if A > B:
        A -= B
    else:
        B -= A

print(f"Les deux phénomènes coïncident tous les {A} jours.")

#VERSION PSEUDO CODE
"""

ALGORITHME SynchronisationClimatique

VARIABLES
    A : ENTIER
    B : ENTIER
DEBUT
    ECRIRE "Entrez la période du premier phénomène : "
    LIRE A
    ECRIRE "Entrez la période du deuxième phénomène : "
    LIRE B
    TANT QUE A != B FAIRE
        SI A > B ALORS
            A ← A - B
        SINON
            B ← B - A
        FINSI
    FINTANTQUE
    ECRIRE "Les deux phénomènes coïncident tous les ", A, " jours."

"""

