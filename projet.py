import random
import string

def generer_cle_substitution():
    """
    Génère aléatoirement une clé de chiffrement monoalphabétique.
    """
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    cle = dict(zip(string.ascii_uppercase, alphabet))
    return cle

def chiffre_substitution(message, cle):
    """
    Chiffre le message en utilisant le chiffrement de substitution monoalphabétique avec la clé donnée.
    """
    message_chiffre = ""
    for lettre in message:
        if lettre.upper() in cle:
            # Conserver la casse d'origine
            if lettre.isupper():
                message_chiffre += cle[lettre.upper()].upper()
            else:
                message_chiffre += cle[lettre.upper()].lower()
        else:
            # Si la lettre n'est pas dans la clé, la laisser telle quelle
            message_chiffre += lettre
    return message_chiffre

def chiffre_cesar(message, decalage):
    """
    Chiffre un message selon le decalage donne en utilisant le chiffrement Cesar.
    """
    resultat = []
    for lettre in message:
        if lettre.isalpha():
            # Si la lettre est en minuscule, elle utilise le code ASCII de la lettre 'a' comme base,
            #sinon elle utilise le code ASCII de la lettre 'A' comme base. Cela permet de garder la casse d'origine.
            base = ord('a') if lettre.islower() else ord('A')
            #elle calcule la nouvelle lettre en ajoutant le décalage au code ASCII de la nouvelle lettre
            #elle re transforme également le code ascii en lettre
            nouvelle_lettre = chr(base + (ord(lettre) - base + decalage) % 26)
            resultat.append(nouvelle_lettre)
        else:
            # Si ce n'est pas une lettre, garder le caractere tel quel
            resultat.append(lettre)
    # Joindre la liste de caracteres pour former le message chiffre
    return ''.join(resultat)

def chiffre_vigenere(message, cle):
    """
    Chiffre un message en utilisant le chiffrement de Vigenere avec la cle donnee.
    """
    resultat = []  # Crée une liste vide pour stocker le message chiffré
    longueur_cle = len(cle)  # Calcule la longueur de la clé
    indice_cle = 0  # Initialise l'indice de la clé à 0

    for lettre in message:  # Parcourt chaque lettre du message
        if lettre.isalpha():  # Vérifie si la lettre est alphabétique
            # Trouve le code ASCII de la lettre de base (a-z ou A-Z)
            base = ord('a') if lettre.islower() else ord('A')
            # Obtiens le décalage à partir de la clé, en tenant compte du cas
            decalage = ord(cle[indice_cle % longueur_cle].lower()) - ord('a')
            # Applique le décalage à la lettre actuelle pour la chiffrer selon Vigenère
            nouvelle_lettre = chr(base + (ord(lettre) - base + decalage) % 26)
            resultat.append(nouvelle_lettre)  # Ajoute la lettre chiffrée à la liste résultat
            indice_cle += 1  # Passe à la lettre suivante de la clé
        else:
            resultat.append(lettre)  # Si ce n'est pas une lettre, conserve le caractère tel quel

    # Joindre la liste de caractères pour former le message chiffré final
    return ''.join(resultat)

def chiffre_transposition(message, cle):
    """
    Chiffre un message en utilisant le chiffrement par grille de colonnes avec la cle donnee.
    """
    # Retirer les espaces du message et le convertir en majuscules
    message = message.replace(" ", "").upper()
    
    # Determiner le nombre de colonnes a partir de la cle
    n = len(cle)
    
    # Creer une liste de colonnes pour stocker le message
    colonnes = [[] for _ in range(n)]
    
    # Remplir les colonnes avec le message
    for i, lettre in enumerate(message):
        colonnes[i % n].append(lettre)
    
    # Trier les colonnes selon l'ordre de la cle
    ordre = sorted(range(n), key=lambda x: cle[x])
    
    # Creer le message chiffre en lisant les colonnes dans l'ordre de la cle
    message_chiffre = ""
    for i in ordre:
        message_chiffre += "".join(colonnes[i])
    
    return message_chiffre

def menu():
    """
    Affiche le menu et demande a l'utilisateur de choisir une option.
    """
    print("Menu :")
    print("1. Code Cesar")
    print("2. Code Vigenere")
    print("3. Chiffrement par transposition")
    print("4. Chiffrement de substitution monoalphabétique")
    print("5. Quitter")
    
    choix = input("Selectionnez une option (1-5) : ")
    
    if choix == "1":
        # Code Cesar
        decalage = int(input("Entrez le decalage (un nombre entier) : "))
        message = input("Entrez le message a chiffrer : ")
        message_chiffre = chiffre_cesar(message, decalage)
        print(f"Message chiffre (Cesar) : {message_chiffre}")
    elif choix == "2":
        # Code Vigenere
        cle = input("Entrez la cle (une chaine de caracteres) : ")
        message = input("Entrez le message a chiffrer : ")
        message_chiffre = chiffre_vigenere(message, cle)
        print(f"Message chiffre (Vigenere) : {message_chiffre}")
    elif choix == "3":
        # Chiffrement par transposition
        cle = input("Entrez la cle (une chaine de caracteres sans espaces) : ")
        message = input("Entrez le message a chiffrer : ")
        message_chiffre = chiffre_transposition(message, cle)
        print(f"Message chiffre (transposition) : {message_chiffre}")
    elif choix == "4":
        # Chiffrement de substitution monoalphabétique
        cle = generer_cle_substitution()
        print("Clé de chiffrement générée :")
        for lettre, remplacement in cle.items():
            print(f"{lettre} -> {remplacement}")
        message = input("Entrez le message à chiffrer : ")
        message_chiffre = chiffre_substitution(message, cle)
        print(f"Message chiffré (substitution monoalphabétique) : {message_chiffre}")
    elif choix == "5":
        print ("ByeBye")
        exit()
    else:
        print("Option invalide. Veuillez selectionner une option valide (1-5).")
    
    # Appel recursif pour afficher a nouveau le menu
    menu()

# Appel de la fonction menu pour demarrer le programme
menu()
