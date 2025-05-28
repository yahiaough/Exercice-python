#Exercice 1.4

with open('FichierTest.txt', 'r') as f:
    contenu = f.read()
print(contenu)


with open('TestFichier', 'w',  encoding='utf-8') as f:
    ligne = ["Bonjour à vous"]
    for liste in ligne:
        f.write(liste)
f.close()
print("Le fichier à bien été créer ")


with open('FichierTest.txt', 'a') as f:
    ligne1 = input("Ajouter du texte : \n")
    ligne1 = ligne1.split()
    for liste1 in ligne1:
        f.write(liste1 + "\n")
f.close()
print("Vous avez ajouté du texte à votre fichier")



with open('FichierProjet.txt', 'r') as f:
    contenu = f.read()
    print("Le contenu du fichier est : \n ",contenu)
    mots = contenu.split()  
    nb_mots = len(mots)
    print(f"Il y a {nb_mots} mots dans le fichier ")
    
    lignes = contenu.splitlines()
    cpt_ligne = len(lignes)
    print(f"Il y a {cpt_ligne} lignes dans le fichier")
    
    

