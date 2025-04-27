def readFile(path):
    try:
        return open(path, 'rb').read().decode('utf-8')
    except FileNotFoundError:
        print("❌ Fichier introuvable :", path)
    except UnicodeDecodeError:
        print("❌ Erreur de décodage UTF-8 :", path)

readFile('documents/aideRoman.txt')
