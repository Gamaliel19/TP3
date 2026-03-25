"""
Exercice 3 Simulation d’évolution climatique 
Écrire un algorithme qui calcule : 
T^N 
où : 
1. T = température initiale 
2. N = nombre de jours 
(par multiplications successives)
"""

# Demander à l'utilisateur d'entrer la température initiale et le nombre de jours
T = float(input("Entrez la température initiale (en degrés) : "))
N = int(input("Entrez le nombre de jours : "))

# Initialiser la variable pour stocker la température finale
final_temperature = T

# Calculer T^N par multiplications successives
for _ in range(N):
    final_temperature *= T

# Afficher le résultat
print(f"La température après {N} jours est : {final_temperature:.2f} degrés")



#VERSION SPEUDO CODE
"""
ALGORITHME EvolutionClimatique

VARIABLES
    T : REEL
    N : ENTIER
    final_temperature : REEL
DEBUT
    ECRIRE "Entrez la température initiale (en degrés) : "
    LIRE T

    ECRIRE "Entrez le nombre de jours : "
    LIRE N

    final_temperature <- T
    POUR i DE 1 A N FAIRE
        final_temperature <- final_temperature * T
    FIN POUR
    ECRIRE "La température après ", N, " jours est : ", final_temperature
FIN ALGORITHME    

"""

