#Exercice 1 

age = int(input("Quelle âge avez-vous ?\n"))
if age >= 18 :
    print("Vous êtes majeur ")
else :
    print("Vous êtes mineur")


nb = float(input("Veuillez saisir un nombre : \n"))
if nb < 0 :
    print("Le nombre est négatif")
elif nb == 0:
    print("Le nombre est nul")
else :
    print("le nombre est positif ")


nb1=int(input("Veuillez saisir un premier nombre : \n"))
nb2=int(input("Veuillez saisir un deuxième nombre : \n"))
if nb1>nb2 :
    print(f"Le plus grand nombre est {nb1} ")
else :
    print(f"Le plus grand nombre est {nb2} ")