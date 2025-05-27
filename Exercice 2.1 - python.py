#Exercice 2.1

etudiant = {
    "nom" : "Dupont",
    "age" : "20",
    "adresse" : "5 Rue du Guesclin"
    }

print(etudiant["nom"])
print(etudiant["age"], "ans")
print(etudiant["adresse"])
    
    
message = "Bonjour à vous tous"
lettre = "o"

message = message.lower()
mots = message.split()
occurence = {}

for mot in mots:
    occurence[mot] = mot.count(lettre)

print(occurence)



etudiant = {
    "nom" : "Dupont",
    "age" : "20",
    "adresse" : "5 Rue du Guesclin"
    }

etudiant = {
    "nom" :"Dupont",
    "age" :"21",
    "adresse" : "5 Rue du Guesclin"
    }


print(etudiant["nom"])
print(etudiant["age"], "ans")
print(etudiant["adresse"])





