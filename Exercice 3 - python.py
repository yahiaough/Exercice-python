#Exercice 3

def somme(nb1,nb2):
    somme = nb1 + nb2
    print("La somme des deux nombres est :", somme)

somme(12,15)


def longueur(chaine):
    longueur_chaine = len(chaine)
    print("La longueur de la chaine de caractère est : ", longueur_chaine)
longueur("Comment allez-vous ?")


def nb_max(tab):
    n=0
    for i in range(len(tab)):
        if tab[i] > n :
            n = tab[i]
    print("Le nombre le plus grand est ", n )
nb_max([12,15,72,211,121,124,31,73,93,101])

    