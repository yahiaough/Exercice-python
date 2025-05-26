#Exercice 1.2
from random import randint
nb_max=0
nb_min=100

liste = []
for i in range(10):
    liste.append(randint(1, 100))
    if liste[i] > nb_max :
        nb_max = liste[i]
    if liste[i] < nb_min:
        nb_min = liste[i]
print(liste)
print(f"Le nombre le plus grand est {nb_max} et le nombre le plus petit est {nb_min} ")


liste = [1, 3, 2, 2, 3, 1, 4]
for i in range(len(liste)):
    j = i + 1
    while j < len(liste):
        if liste[i] == liste[j]:
            del liste[j]
        else:
            j += 1


print(liste)

liste = [1,2,3,4,5,6,7,8,9]
liste.reverse()
print(liste)





