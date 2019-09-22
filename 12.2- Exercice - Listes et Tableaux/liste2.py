# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

max = 0
index1 = 0
index2 = 0

for n, i in enumerate(tab):
    for m, j in enumerate(i):
        if max < j:
            max = j
            index1 = n
            index2 = m
print("La valeur maximum est : {0} et elle se trouve à l'indice [ {1} ][ {2} ]".format(max, index1, index2))


