tab = []

nbrEntrer = int(input("Combien de nombres voulez-vous trier ? "))

for i in range(nbrEntrer):

    tab.append(int(input(f"Entrée n° {i + 1} : ")))

for i in range(len(tab) - 1):

    for j in range(len(tab) - i - 1):

        if tab[j] > tab[j + 1] :

            tab[j], tab[j + 1] = tab[j + 1], tab[j]

print(tab)