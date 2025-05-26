#Exercice 2

for i in range(0, 100+1):
    if i % 2 == 0:
        print(i)

liste = [15,15,27,62,92,42,52,73]
somme = 0
for i in liste:
    somme = somme + i
print(f"La somme des nombres de la liste est égal à : {somme}")


nb = int(input("Veuillez saisir un nombre : \n"))
for i in range(11):
    print(f"{nb} * {i} = {nb*i}")