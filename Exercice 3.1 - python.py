#Exercice 3.1

def tuple():
     return 3, 4, 18, 21, 10
    
a = tuple()
n = len(a)
total = sum(a)

print("La somme est : ", sum(a))
print("La moyenne est : ",total/n )


ensemble_a = set(['1','2','5','8','9','12'])
ensemble_b = set(['12','62','5','7','9','11'])
nouvel_ensemble = ensemble_a.intersection(ensemble_b)
print("Les éléments communs au deux ensembles sont : ", nouvel_ensemble)



def sous_ensemble(ensemble_a, ensemble_b):
    for i in ensemble_a:
        if i not in ensemble_b:
            print("L'ensemble A n'est pas un sous ensemble de l'ensemble B")
            return 
    print("L'ensemble A est un sous ensemble de l'ensemble B")
    
n=sous_ensemble([1,2], [1,2,4,5,6])
print(n)






