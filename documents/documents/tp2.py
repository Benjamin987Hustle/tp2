import math, random

# Générateur d'entiers aléatoires entre a et b inclus
def randint(a, b):
    return math.floor((b - a + 1) * random.random()) + a

# Variables globales
grid = []                   # grille 5×5 indices 0–4
valeurs_symboles = []       # valeurs secrètes pour chaque symbole
target_row_sums = []        # sommes par ligne
target_col_sums = []        # sommes par colonne

# Étape 1 : initialise les données du jeu
def etape1_initialisation():
    global grid, valeurs_symboles, target_row_sums, target_col_sums
    # 1) Générer les valeurs secrètes
    valeurs_symboles = []
    for _ in range(5):
        valeurs_symboles.append(randint(1, 20))
    print("Valeurs secrètes des symboles :", valeurs_symboles)
    # 2) Générer la grille 5×5 d'indices
    grid = []
    for _ in range(5):
        ligne = []
        for _ in range(5):
            ligne.append(randint(0, 4))
        grid.append(ligne)
    print("Grille générée :")
    for ligne in grid:
        print(ligne)
    # 3) Calculer les sommes par ligne
    target_row_sums = []
    for ligne in grid:
        s = 0
        for idx in ligne:
            s += valeurs_symboles[idx]
        target_row_sums.append(s)
    print("Sommes cibles par ligne :", target_row_sums)
    # 4) Calculer les sommes par colonne
    target_col_sums = []
    for j in range(5):
        s = 0
        for i in range(5):
            s += valeurs_symboles[grid[i][j]]
        target_col_sums.append(s)
    print("Sommes cibles par colonne :", target_col_sums)

# Étape 2 : construire l'interface et lier le clic
# Injecte l'HTML dans #main et ajoute un <script> pour gérer les clics

def etape2_interface():
    symboles = ["circle.svg", "pyramide.svg", "penta.svg", "cube.svg", "star.svg"]
    html = ""
    # Contrôles
    html += "<div id='controls'>"
    html += "<button onclick='init()'>Nouvelle partie</button>"
    html += "<p>Bienvenue dans La somme des symboles!</p>"
    html += "</div>"
    # Début du tableau
    html += "<table border='1' cellspacing='0' cellpadding='5'>"
    # Lignes de symboles + somme par ligne
    for i in range(5):
        html += "<tr>"
        for j in range(5):
            idx = grid[i][j]
            val = valeurs_symboles[idx]
            # Appel d'une fonction JavaScript avec la valeur
            html += "<td onclick='checkValue(" + str(val) + ")'>"
            html += "<img src='symboles/" + symboles[idx] + "' width='80' height='80'>"
            html += "</td>"
        # somme de la ligne
        html += "<td class='somme'>" + str(target_row_sums[i]) + "</td>"
        html += "</tr>"
    # Sommes par colonne
    html += "<tr>"
    for j in range(5):
        html += "<td class='somme'>" + str(target_col_sums[j]) + "</td>"
    html += "<td></td></tr>"
    html += "</table>"
    # Ajout de la fonction JavaScript pour gérer les clics
    html += """
    <script>
    function checkValue(expected) {
        var ans = prompt('Entrez la valeur pour ce symbole :');
        if (ans !== null) {
            if (parseInt(ans) === expected) {
                alert('Bravo !');
            } else {
                alert('Faux');
            }
        }
    }
    </script>
    """


# Fonction init: démarre et réinitialise le jeu
def init():
    etape1_initialisation()
    etape2_interface()

# Lancement initial de la partie
init()
