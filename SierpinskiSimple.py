texte = lambda * N : str().join([chr(i + 65) for i in N]) # génère une chaîne de caractères correspondant au numéro de la colonne

def generate() -> dict[str: list[str]]:

    graphe = {}   # graphe
    liste  = None # liste temporaire générée pour chaque sommet

    # on parcourt toutes les possibilités
    # chaque lettre correspondont à la colonne d'un anneau
    for i in range(3):         # premier anneau
        for j in range(3):     # deuxième anneau
            for k in range(3): # troisième anneau

                liste = []

                # plus petit anneau
                # il peut être déplacé sur toutes les colonnes sauf la sienne
                for a in range(3):
                    if a != k:
                        liste.append(texte(i, j, a))

                # moyen anneau
                # il ne peut être déplacé que si le plus petit anneau est sur une autre colonne
                # dans ce cas, on peut le déplacer sur la seule colonne restante (deux possibilités mais le plus petit anneau est sur l'une des deux)
                if j != k:
                    for a in range(3):
                        if a != j and a != k:
                            liste.append(texte(i, a, k))

                # plus grand anneau
                # les conditions s'élargissent
                # il ne doit pas être sur la même colonne qu'un des deux autres anneaux
                # par ailleurs, si les deux autres anneaux sont sur deux colonnes différentes, il n'y a aucune possibilité pour le plus grand
                if i != j and j == k: # équivaut à 'i != j and i != k and j != k', en simplifié
                    for a in range(3):
                        if a != i and a != j:
                            liste.append(texte(a, j, k))

                # mise à jour du graphe
                graphe[texte(i, j, k)] = liste

    return graphe
