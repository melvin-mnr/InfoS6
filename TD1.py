scoreLettre={'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}

def recupMots(fichier):
# Ouvrir le fichier en mode lecture
    with open(fichier, 'r') as f:
    # Lire les lignes du fichier
        lines = f.readlines()
# Supprimer les caractères de nouvelle ligne
    lines = [line.strip('\n') for line in lines]
    return(lines)

def possibleTirage(mot, tirage):
    #Parcourir les caractères du mot
    copieTirage=tirage.copy()
    for i in mot :
        #Vérifier que le caractère est dans le tirage, si oui on supprime cette lettre du tirage
        if i not in copieTirage :
            return False
        copieTirage.remove(i)
    return True

def plusLongPossible(tirage, fichier):
    #Extraire tous les mots possibles avec le tirage
    dico=recupMots(fichier)
    dicoPossible=[]
    for mot in dico :
        if possibleTirage(mot, tirage) :
            dicoPossible.append(mot)
    #Parcourir les mots possibles en gardant en mémoire l'indice le plus long rencontré
    l=0
    imax=0
    for i in range(len(dicoPossible)):
        if len(dicoPossible[i]) > l:
            imax = i
            l = len(dicoPossible[i])
    return dicoPossible[imax]

def score(mot):
    #à l'aide de scoreLettre on donne le score d'un mot
    s=0
    for i in mot :
        s+= scoreLettre[i]
    return s

def maxScore(listeMot):
    #donne le tuple (mot,score) du mot qui a le score maximal de la liste
    smax=0
    imax=0
    for i in range(len(listeMot)):
        if score(listeMot[i]) > smax :
            smax = score(listeMot[i])
            imax = i
    return (listeMot[imax],score(listeMot[imax]))

