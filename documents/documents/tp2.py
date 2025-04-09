# Fonction personnalisée pour obtenir un entier aléatoire entre a et b inclus
# Pour générer un nombre de 1 à 6, par exemple, on utilise : math.floor(6*random())+1
def randint(a, b):
    return math.floor((b - a + 1) * random()) + a

# Génère 5 entiers aléatoires entre 1 et 20, un par symbole
def init_valeurs_symboles():
    valeurs = []
    for i in range(5):
        valeurs.append(randint(1, 20))
    return valeurs

# Variables globales pour stocker l'état du jeu
grid = None                  # Grille (5x5) des indices de symboles
valeurs_symboles = None      # Valeurs secrètes pour chaque symbole
target_row_sums = None       # Somme cible pour chaque rangée
target_col_sums = None       # Somme cible pour chaque colonne
revelations = None           # Tableau des booléens indiquant si un symbole est révélé

# Étape 1 : Initialisation et configuration du jeu
def etape1_initialisation():
    global grid, valeurs_symboles, target_row_sums, target_col_sums, revelations

    # 1. Générer les valeurs secrètes pour les 5 symboles
    valeurs_symboles = init_valeurs_symboles()
    print("Valeurs secrètes des symboles :", valeurs_symboles)

    # 2. Générer la grille 5x5 (chaque case contient un indice entre 0 et 4)
    grid = []
    for i in range(5):
        ligne = []
        for j in range(5):
            ligne.append(randint(0, 4))
        grid.append(ligne)
    print("Grille générée :")
    for ligne in grid:
        print(ligne)

    # 3. Calculer la somme cible pour chaque rangée
    target_row_sums = []
    for i in range(5):
        somme = 0
        for j in range(5):
            somme += valeurs_symboles[grid[i][j]]
        target_row_sums.append(somme)
    print("Sommes cibles par ligne :", target_row_sums)

    # 4. Calculer la somme cible pour chaque colonne
    target_col_sums = []
    for j in range(5):
        somme = 0
        for i in range(5):
            somme += valeurs_symboles[grid[i][j]]
        target_col_sums.append(somme)
    print("Sommes cibles par colonne :", target_col_sums)

    # 5. Initialiser le tableau de révélations (aucun symbole n'est révélé au départ)
    revelations = [False] * 5

# Appel de la fonction de la première étape pour tester l'initialisation
etape1_initialisation()

def etape2_interface():
    global grid, target_row_sums, target_col_sums

    # On définit la liste des images associées aux symboles (indices 0 à 4)
    symboles = ["circle.svg", "pyramide.svg", "penta.svg", "cube.svg", "star.svg"]

    html = ""
    html += "<div id='controls'>"
    html += "<button id='btnNewGame' onclick='init()'>Nouvelle partie</button>"
    html += "<p id='message'>Bienvenue dans La somme des symboles!</p>"
    html += "</div>"
    html += "<div id='jeu'><table border='1' cellspacing='0' cellpadding='5'>"
    
    # Création des 5 lignes de la grille
    for i in range(5):
        html += "<tr>"
        for j in range(5):
    # Affiche l'image correspondant à l'indice stocké dans grid[i][j]
            sym_index = grid[i][j]
            html += (
            "<td id='case_" + str(i) + "_" + str(j) + "'>" +
            "<img src='symboles/" + symboles[sym_index] + "' width='80' height='80'>" +
            "</td>"
            )
    
    # Dernière ligne pour les sommes des colonnes
    html += "<tr>"
    for j in range(5):
        html += "<td id='colSum_" + str(j) + "'>" + str(target_col_sums[j]) + "</td>"
    html += "<td id='empty'></td></tr>"
    html += "</table></div>"

    # Mettre le HTML généré dans la div principale
    document.querySelector("#main").innerHTML = html

# Appel de l'étape 2 (après avoir exécuté l'étape 1)
etape2_interface()
