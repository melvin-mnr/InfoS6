#import matplotlib.pyplot as plt

class Hashtable :
    def __init__(self,h,n):
        #fontion de hachage défini avec fonction lambda
        self.__h=h
        #taille de la table de hachage
        self.__n=n
        #initialisation de la table
        self.table=[[] for i in range(n)]


    def put(self, key, value):
        indice=self.__h(key)%self.__n
        case=self.table[indice]
        #on implémente rezise
        if sum[len(i) for i in self.table]>1.2*self.__n:



        #cas le plus simple : la case est vide donc on ajoute simplement le tuple
        if len(case)==0:
            case.append((key,value))
            return
        #sinon la case n'est pas vide donc on peut parcourir les tuples qui y sont rangés
        for k in range(len(case)) :
            if key == case[k][0] :
                case[k]=(key,value)
                return
        #la clé ne se trouve pas déjà dans la case même si elle n'est pas vide
        case.append((key,value))

    def get(self,key):
        indice=self.__h(key)%self.__n
        case=self.table[indice]
        #la clé ne se trouve pas dans la table
        if len(case)==0:
            return None
        #la clé se trouve dans la table, donc on renvoie la valeur correspondant à la bonne clé parmi celles rangées dans la même case
        for k in range(len(case)) :
            if key == case[k][0] :
                return case[k][1]

    def repartition(self):
        #je n'ai pas matplotlib sur ma machine

        #width = 1/1.5
        #plt.bar(range(self.__n),[len(i) for i in self.table], width, color="blue")
        #plt.show()
        return [len(i) for i in self.table]

    def resize(self):
        t2=Hashtable(self.__h,2*self.__n)
        for i in range(self.__n):
            for j in self.__n[i]:
                t2.put(j)
        return t2


def recupMots(fichier):
# Ouvrir le fichier en mode lecture
    with open(fichier, 'r') as f:
    # Lire les lignes du fichier
        lines = f.readlines()
# Supprimer les caractères de nouvelle ligne
    lines = [line.strip('\n') for line in lines]
    return(lines)

def efficaciteHachage(f,n):
    t1=Hashtable(f,n)
    mots=recupMots('frenchssaccent.dic')
    for i in mots :
        t1.put(i, len(i))
    return(t1.repartition())

def jenkins(key):
    #fonction de jenkins donnée dans le cours
    hash = 0
    for c in key:
        hash += ord(c)
        hash += (hash << 10)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    return hash