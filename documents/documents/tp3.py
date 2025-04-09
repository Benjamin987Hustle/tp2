
import math


# Fonction personnalisée pour obtenir un entier aléatoire entre a et b inclus
def randint(a, b):
    return math.floor((b - a + 1) * random()) + a

# Fonction pour initialiser les valeurs associées aux symboles (pour 5 symboles)
def init_valeurs_symboles():
    valeurs = []
    for i in range(5):
        valeurs.append(randint(1, 20))
    return valeurs

# Variables globales pour stocker l'état du jeu
grid = None                  # Grille (5x5) contenant les indices de symboles
valeurs_symboles = None      # Liste de 5 entiers (la valeur réelle de chaque symbole)
target_row_sums = None       # Somme totale (cible) de chaque ligne
target_col_sums = None       # Somme totale (cible) de chaque colonne
revelations = None           # Liste de booléens (pour chaque symbole, s'il est révélé ou non)

# Fonction appelée lors du clic sur une cellule de la grille
def on_click(i, j):
    global grid, valeurs_symboles, target_row_sums, target_col_sums, revelations
    symbole = grid[i][j]
    print("caca")
    # Si ce symbole a déjà été révélé, ne rien faire
    if revelations[symbole]:
        return

    # Demander à l'utilisateur de saisir la valeur du symbole
    guess_str = input("Entrez la valeur pour ce symbole : ")
    if not guess_str.strip().isdigit():
        input("Veuillez entrer un entier valide.")
        return
    else:
        guess = int(guess_str)

    # Vérification de la réponse
    if guess != valeurs_symboles[symbole]:
        input("Mauvaise réponse! Vous avez perdu.")
        return
    else:
        # Marquer le symbole comme révélé
        revelations[symbole] = True

        # Remplacer l'image par le nombre dans toutes les cellules contenant ce symbole
        for i2 in range(5):
            for j2 in range(5):
                if grid[i2][j2] == symbole:
                    cell = document.querySelector("#case_" + str(i2) + "_" + str(j2))
                    cell.innerHTML = str(guess)

        # Mettre à jour les sommes affichées pour chaque ligne
        for i2 in range(5):
            revealed_sum = 0
            for j2 in range(5):
                sym = grid[i2][j2]
                if revelations[sym]:
                    revealed_sum += valeurs_symboles[sym]
            remaining = target_row_sums[i2] - revealed_sum
            document.querySelector("#rowSum_" + str(i2)).innerHTML = str(remaining)

        # Mettre à jour les sommes affichées pour chaque colonne
        for j2 in range(5):
            revealed_sum = 0
            for i2 in range(5):
                sym = grid[i2][j2]
                if revelations[sym]:
                    revealed_sum += valeurs_symboles[sym]
            remaining = target_col_sums[j2] - revealed_sum
            document.querySelector("#colSum_" + str(j2)).innerHTML = str(remaining)

        # Vérifier si tous les symboles ont été révélés
        all_revealed = True
        for s in range(5):
            if not revelations[s]:
                all_revealed = False
        if all_revealed:
            alert("Bravo, vous avez gagné!")

# Fonction qui retourne un gestionnaire d'événement pour une cellule donnée
def make_handler(i, j):
    def handler(event):
        print("Cell clicked: " + str(i) + ", " + str(j))
        on_click(i, j)
    return handler

# Fonction alternative pour créer des gestionnaires avec fermeture correcte
def create_click_handler(i, j):
    return lambda event: (print("caca"), on_click(i, j))[1]

# Fonction init() qui génère les contrôles (bouton & message) et la grille, et initialise l'état du jeu
def init():
    global grid, valeurs_symboles, target_row_sums, target_col_sums, revelations
    main = document.querySelector("#main")
    print("pipi")

    # Création de la zone de contrôle (bouton et message)
    controls_html = """
      <div id="controls">
        <button id="btnNewGame" onclick="init()">Nouvelle partie</button>
        <p id="message">Bienvenue dans La somme des symboles!</p>
      </div>
    """

    # Réinitialiser l'état du jeu
    revelations = [False] * 5
    valeurs_symboles = init_valeurs_symboles()
    # Liste des symboles disponibles (les images doivent se trouver dans le dossier "symboles")
    symboles = ["circle.svg", "pyramide.svg", "penta.svg", "cube.svg", "star.svg"]

    # Construction du HTML pour la grille
    grid = []           # grille 5x5
    target_row_sums = []
    target_col_sums = [0] * 5  # pour 5 colonnes

    grid_html = """
      <style>
        #jeu table td {
            border: 1px solid black; 
            padding: 1px 2px;
            width: 80px;
            height: 80px;
            font-family: Helvetica; 
            font-size: 20px; 
            text-align: center;
            cursor: pointer;
        }
        #jeu table td img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            object-fit: contain;
            width: 80px;
            height: 80px;
        }
      </style>
      <div id="jeu">
        <table>
    """
    # Génération des 5 lignes contenant les symboles
    for i in range(5):
        grid_html += "<tr>"
        row = []
        row_sum = 0
        for j in range(5):
            # Sélection aléatoire d'un symbole (indice entre 0 et 4)
            sym_index = randint(0, 4)
            row.append(sym_index)
            grid_html += '<td id="case_' + str(i) + '_' + str(j) + '"><img src="symboles/' + symboles[sym_index] + '"></td>'
            row_sum += valeurs_symboles[sym_index]
            target_col_sums[j] += valeurs_symboles[sym_index]
        grid_html += '<td id="rowSum_' + str(i) + '"></td></tr>'
        grid.append(row)
        target_row_sums.append(row_sum)

    # Dernière ligne pour les sommes des colonnes
    grid_html += "<tr>"
    for j in range(5):
        grid_html += '<td id="colSum_' + str(j) + '"></td>'
    grid_html += '<td id="empty"></td></tr>'
    grid_html += "</table></div>"

    # On assemble la totalité du contenu sans onclick inline
    container_html = controls_html + grid_html

    # Injection dans la div "main"
    main.innerHTML = '<div id="globalContainer">' + container_html + '</div>'

    # ATTENTION : Au lieu de récupérer le conteneur et lui ajouter l'event, 
    # on attache directement l'événement à la div "main"
    main.onclick = global_click_handler

    # Affichage initial des sommes cibles
    for i in range(5):
        document.querySelector("#rowSum_" + str(i)).innerHTML = str(target_row_sums[i])
    for j in range(5):
        document.querySelector("#colSum_" + str(j)).innerHTML = str(target_col_sums[j])

    # Attacher un gestionnaire d'événement à chaque cellule de symbole
    for i in range(5):
        for j in range(5):
            cell = document.querySelector("#case_" + str(i) + "_" + str(j))
            cell.onclick = create_click_handler(i, j)

# Fonction globale appelée lors d'un clic sur main (tout le contenu de #main)
def global_click_handler():
    print("codeboot zizi")
