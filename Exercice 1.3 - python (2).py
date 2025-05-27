try:
    nb=int(input("Veuillez saisir un nombre : \n"))
except ValueError:
    print("Erreur, le caractère saisi n'est pas un nombre entier.")


try:
   with open("fichier.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)
except FileNotFoundError:
    print("Erreur, le fichier n'existe pas.")
    
 
try:
    nb1=int(input("Veuillez saisir un premier nombre : \n"))
    nb2=int(input("Veuillez saisir un deuxième nombre : \n"))
    if nb1 != 0 or nb2 != 0:
       division = nb1//nb2
       print(division)
except ZeroDivisionError:
       print("La division par 0 est impossible")
