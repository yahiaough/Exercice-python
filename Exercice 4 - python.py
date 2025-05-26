def addition(nb1, nb2):
    return nb1 + nb2

def soustraction(nb1, nb2):
    return nb1 - nb2

def division(nb1, nb2):
    if nb2 == 0:
        return "Erreur : division par zéro"
    return nb1 / nb2

def multiplication(nb1, nb2):
    return nb1 * nb2

def menu():
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
    nb = int(input("Veuillez choisir un nombre entre 1 et 5 : "))

    if nb >= 5 or nb < 0:
        print("Vous avez quitté.")
        return 
    
    nb1 = int(input("Veuillez choisir un premier nombre : "))
    nb2 = int(input("Veuillez choisir un deuxième nombre : "))

    if nb == 1:
        print("Résultat :", addition(nb1, nb2))
    elif nb == 2:
        print("Résultat :", soustraction(nb1, nb2))
    elif nb == 3:
        print("Résultat :", multiplication(nb1, nb2))
    elif nb == 4:
        print("Résultat :", division(nb1, nb2))
    else:
        print("Veuillez relancer.")

menu()
