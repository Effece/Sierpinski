texte = lambda * N : str().join([chr(i + 65) for i in N]) # génère une chaîne de caractères correspondant au numéro de la colonne

def sommet(num: int, colonnes: int, * N: list[int]) -> list[int]:
    """
    Trouve tous les voisins d'un sommet.
    """

    # vérifier qu'aucun anneau plus petit n'est au-dessus
    v = N[num]
    for i in N[num + 1 :]:
        if v == i:
            return []

    # il peut être déplacé sur toutes les colonnes non couvertes par lui-même ou les anneaux plus petits
    Np = N[num :]
    poss = [i for i in range(colonnes) if not i in Np]

    # résultat
    return [texte(* N[: num], p, * N[num + 1 :]) for p in poss]

def generer(n: int = 3, colonnes: int = 3) -> dict[str: list[str]]:
    """
    Génère le graphe avec n anneaux.
    """

    return recur({}, [0 for _ in range(n)], 0, colonnes)

def recur(grapheT: dict, presetT: list[int], ind: int, colonnes: int = 3) -> dict[str: list[str]]:
    """
    Fonction récursive de génération du graphe.
    """

    graphe = grapheT.copy()
    preset = presetT.copy()

    long = len(preset)
    liste = None
    
    for n in range(colonnes):
        
        preset[ind] = n
        
        if ind == long - 1:
            liste = []
            for i in range(long):
                liste += sommet(i, colonnes, * preset)
            graphe[texte(* preset)] = liste
            continue

        graphe = recur(graphe, preset, ind + 1, colonnes)

    return graphe

print(generer())
print(generer(4))
print(generer(3, 4))
