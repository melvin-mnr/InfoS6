D'un point de vue global, ton fichier est bien présenté, avec des tests et des commentaires, donc c'est positif.
Le code de ta classe `Tree` est propre et m'a l'air correct pour les fonctions que tu as écrites.
J'ai l'impression que le souci vient plus de tes tests, et notamment des test d'égalité: on veut comparer des arbres, donc tu veux vérifier que `Tree('a') == Tree('a')`, et non `Tree('a') == 'a'`.
Néanmoins, tu as quand même plutôt réussi le TP, car la plupart de tes méthodes marchent, même si les tests sont moins bien écrits, mais ca vient plus d'un problème de compréhension de ce que tu veux tester que d'un souci de programmation.

Voici le corrigé si tu veux regarder: https://github.com/thomas-vinet/Mines-TD-PSD
