# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for i in range(1, len(B)): 
    k = B[i]
    j = i-1
    while j >= 0 and k < B[j]:
        B[j + 1] = B[j]
        j -= 1
        B[j + 1] = k

print(B)