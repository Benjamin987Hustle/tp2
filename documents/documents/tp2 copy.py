import math, random

# Fonction personnalisée pour obtenir un entier aléatoire entre a et b inclus
def randint(a, b):
    return math.floor((b - a + 1) * random.random()) + a

# Génère 5 valeurs secrètes (1–20)
def init_valeurs_symboles():
    valeurs = []
    for i in range(5):
        valeurs.append(randint(1, 20))
    return valeurs

# Variables globales
# grid : grille 5×5 d'indices (0–4)
# valeurs_symboles : valeurs associées à chaque indice
# target_row_sums : somme des lignes
# target_col_sums : somme des colonnes
grid = []
valeurs_symboles = []
target_row_sums = []
target_col_sums = []

# Étape 1 : initialisation des données
def etape1_initialisation():
    global grid, valeurs_symboles, target_row_sums, target_col_sums

    # 1. Générer et afficher les valeurs secrètes des symboles
    valeurs_symboles = init_valeurs_symboles()
    print("Valeurs secrètes des symboles :", valeurs_symboles)

    # 2. Génération de la grille d'indices et affichage
    grid = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(randint(0, 4))
        grid.append(row)
    print("Grille générée :")
    for row in grid:
        print(row)

    # 3. Calcul et affichage des sommes par ligne
    target_row_sums = []
    for row in grid:
        s = 0
        for idx in row:
            s += valeurs_symboles[idx]
        target_row_sums.append(s)
    print("Sommes cibles par ligne :", target_row_sums)

    # 4. Calcul et affichage des sommes par colonne
    target_col_sums = []
    for j in range(5):
        s = 0
        for i in range(5):
            s += valeurs_symboles[grid[i][j]]
        target_col_sums.append(s)
    print("Sommes cibles par colonne :", target_col_sums)

# Étape 2 : construction de l'interface HTML avec onclick simplifié
# document est accessible globalement dans Codeboot
def etape2_interface():
    symboles = ["circle.svg", "pyramide.svg", "penta.svg", "cube.svg", "star.svg"]
    html = ""

    # Contrôles
    html += "<div id='controls'>"
    html += "<button id='btnNewGame' onclick='init()'>Nouvelle partie</button>"
    html += "<p id='message'>Bienvenue dans La somme des symboles!</p>"
    html += "</div>"

    # Tableau de jeu
    html += "<div id='jeu'><table border='1' cellspacing='0' cellpadding='5'>"
    case_id = 0
    for i in range(5):
        html += "<tr>"
        for j in range(5):
            case_id += 1
            idx = grid[i][j]
            val = valeurs_symboles[idx]
            html += "<td id='case" + str(case_id) + "' onclick=\"alert('Valeur associée : " + str(val) + "')\">"
            html += "<img src='symboles/" + symboles[idx] + "' width='80' height='80'>"
            html += "</td>"
        html += "<td><strong>" + str(target_row_sums[i]) + "</strong></td>"
        html += "</tr>"
    html += "<tr>"
    for j in range(5):
        html += "<td><strong>" + str(target_col_sums[j]) + "</strong></td>"
    html += "<td></td></tr>"
    html += "</table></div>"

    # Injection dans la page
    document.querySelector("#main").innerHTML = html

# Fonction de démarrage / réinitialisation
def init():
    etape1_initialisation()
    etape2_interface()

# Lancement initial
init()