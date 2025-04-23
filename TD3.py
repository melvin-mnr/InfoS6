class Tree :
    def __init__ (self, label, *children):
        self.__label=label
        self.__children=children
    def label(self):
        return str(self.__label)
    def children(self):
        return self.__children
    def nb_children(self):
        return len(self.__children)
    def child(self,i):
        if i>=len(self.__children):
            return('pas de '+str(i)+'-ème fils')
        else :
            return self.__children[i]
    def is_leaf(self):
        if len(self.__children)==0:
            return True
        else :
            return False

    def depth(self):
        if self.is_leaf():
            return 0
        else :
            k=0
            for i in self.__children:
                if i.depth()>k:
                    k=i.depth()
            return k+1

    def __str__(self):
        #cas pour une feuille donc le nom est juste le label
        if self.is_leaf():
            return self.label()
        #si l'arbre n'est pas une simple feuille on construit l'appelation par récursivité
        else :
            #onconstruit d'abord l'appelation des enfants en commençant par le 1er
            childStr=self.child(0).__str__()
            #puis s'il y a plusieurs enfants on concatène avec des virgules entre
            for i in range(1,self.nb_children()):
                childStr= childStr + ',' + self.__children[i].__str__()
            #enfin on ajoute le label de l'arbre
            return(self.label() + '(' + childStr + ')')


    def __eq__(self, __value):
        #fonction récursive, on commence par éliminer si les deux arbres n'ont pas le même label ni le même nombre d'enfants
        if self.label()!=__value.label():
            return False
        if self.nb_children()!=__value.nb_children():
            return False
        #condition d'arrêt de la récursivité, sachant qu'on a déjà vérifié le label
        if self.is_leaf() and __value.is_leaf():
            return True
        #on parcours les enfants de self et on vérifie qu'il existe un enfant de __value qui soit équivalent à chacun (par récursivité de la méthode), en gardant en mémoire ceux déjà appareillés dans EnfantValueEq au cas où 2 enfants de l'un seraient équivalents à 1 enfant de l'autre. Pour ce même cas de figure on choisit de sortir de la boucle lorsqu'on trouve 1 enfant équivalent pour ne pas éliminer 2 enfants de __value qui seraient équivalents à 1 enfant de self
        EnfantValueEq=[]
        for i in self.children() :
            EnfantEq=False
            j=0
            while not(EnfantEq) :
                if j >= __value.nb_children():
                    return False
                if j not in EnfantValueEq :
                    if i.__eq__(__value.child(j)):
                        EnfantEq=True
                        EnfantValueEq.append(j)
                j+=1


#il y a une erreur dans mon code que je n'arrive pas à déceler, il ne renvoie pas le bon résultat dans les tests que j'ai pu effectuer






#import unittest
#class TestTree(unittest.TestCase):
#    def test_label(self):
 #       t1=Tree('f',Tree('a'),Tree('b'))
  #      self.assertEqual(t1.label(), 'f')
   # def test_children(self):
    #    self.assertEqual(TestCase.children,['a','b'])
#    def test_nb_children(self):
 #       t1=Tree('f',Tree('a'),Tree('b'))
  #      self.assertEqual(t1.nb_children(),2)
   #     t2=Tree('a')
    #    self.assertEqual(t2.nb_children(),0)
#    def test_child(self):
 #       t1=Tree('f',Tree('a'),Tree('b'))
  #      self.assertEqual(t1.child(0),'a')
   #     self.assertEqual(t1.child(1),'b')
    #    self.assertEqual(t1.child(2),('pas de 2-ème fils'))
#    def test_is_leaf(self):
 #       t1=Tree('f',Tree('a'),Tree('b'))
  #      self.assertFalse(t1.is_leaf())
   #     t2=Tree('a')
    #    self.assertTrue(t2.is_leaf())

#if __name__ == '__main__':
 #   unittest.main()



