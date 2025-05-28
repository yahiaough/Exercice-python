contact = {}

def gestionnaire():
    print("Gestionnaire de contact :")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Supprimer un contact")
    print("4. Afficher les contacts")

def ajouter():
    try:
        nom = input("Entrez le nom : ")
        numero = input("Entrez le numéro de téléphone : ")
        mail = input("Entrez l'adresse mail : ")
        contact["nom"] = nom
        contact["numéro de téléphone"] = numero
        contact["mail"] = mail
        print("Contact ajouté.")
    except Exception as e:
        print("Une erreur est survenue lors de l'ajout :", e)

def modifier():
    try:
        if not contact:
            print("Aucun contact à modifier.")
            return
        print("Quel élément voulez-vous modifier ?")
        print("1. Nom")
        print("2. Numéro de téléphone")
        print("3. Mail")
        nb_modif = input("Votre choix : ")
        if nb_modif == "1":
            contact["nom"] = input("Nouveau nom : ")
        elif nb_modif == "2":
            contact["numéro de téléphone"] = input("Nouveau numéro : ")
        elif nb_modif == "3":
            contact["mail"] = input("Nouvelle adresse mail : ")
        else:
            print("Choix invalide.")
        print("Contact modifié.")
    except Exception as e:
        print("Erreur de modification :", e)

def supprimer():
    try:
        contact.clear()
        print("Vous avez supprimé le contact.")
    except Exception as e:
        print("Erreur de suppression :", e)

def afficher():
    try:
        if contact:
            print("Nom :", contact["nom"])
            print("Téléphone :", contact["numéro de téléphone"])
            print("Mail :", contact["mail"])
        else:
            print("Aucun contact.")
    except Exception as e:
        print("Erreur d'affichage :", e)

# Main
gestionnaire()
try:
    nb = int(input("Veuillez saisir un nombre : \n "))
    while nb < 1 or nb > 4:
        nb = int(input("Veuillez resaisir un nombre valide : "))
    
    if nb == 1:
        ajouter()
    elif nb == 2:
        modifier()
    elif nb == 3:
        supprimer()
    elif nb == 4:
        afficher()
except ValueError:
    print("Erreur : veuillez saisir un nombre entier.")


