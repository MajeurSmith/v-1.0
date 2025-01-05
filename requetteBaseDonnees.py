import firebase_admin
from firebase_admin import credentials, db
import os
import hashlib

localPath = os.path.dirname(os.path.abspath(__file__))
firebase_admin.initialize_app(credentials.Certificate(localPath+'/exemple-a4226-firebase-adminsdk-8einv-3440cd1c81.json'), {'databaseURL': 'https://exemple-a4226-default-rtdb.europe-west1.firebasedatabase.app/'})

def hash(password: str) -> str:
    """
    Procédure qui renvoie la chaîne de caractère 'password' encodée
    en sha256 sous la forme d'une chaîne de caractère.

    Args:
        password (str): la chaîne de caractère à encoder

    Returns:
        str: la chaîne de caractère encodée
    """
    assert(type(password) == str), "Erreur de type pour 'password' (requis: str)"
    h = hashlib.new("SHA256") # Choix du type d'encodage
    h.update(password.encode()) # Encodage
    hashedPassword = h.hexdigest() # Conversion en chaîne de caractère
    return(hashedPassword) # Renvoie du mot de passe encodé

def ajouterUtilisateur(infosUtilisateurs : tuple):
    """
    le tuple infosUtilisateurs doit avoir le format (nom : str, prenom : str, mail : str, mdp : str)
    Ajoute un utilisateur dans la base de données qui a pour clef "comptes"
    """
    try :
        if "@" in infosUtilisateurs[2] : 
            # Ajouter un utilisateur
            db.reference('comptes').child(infosUtilisateurs[2].replace(".","")).set({
                'nom': infosUtilisateurs[0],
                'prenom': infosUtilisateurs[1],
                'mail' : infosUtilisateurs[2],
                'mdp' : infosUtilisateurs[3],
            })
        else:
            print("mail incorrect")
    except:
        print("connexion internet instable")

def modifierMdpUtilisateur(infosUtilisateurs):
    """
    infosUtilisateurs doir être au format (clefUtilisateur : str, nouveauMdp : str)
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur 
    """
    try:
        db.reference('comptes').child(infosUtilisateurs[0]).update({
            'mdp': infosUtilisateurs[1]
        })
    except:
        print("connexion internet instable")

def modifierMailUtilisateur(infosUtilisateurs : tuple):
    """
    infosUtilisateurs doit être au format (clefUtilisateur : str, nouveauMail : str)
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouveauMail est le nouveau mail
    permet de remplacer la valeur de mail par nouveauMail
    """
    try:
        db.reference('comptes').child(infosUtilisateurs[0]).update({
            'mail': infosUtilisateurs[1]
        })
    except:
        print("connexion internet instable")

def modifierNom(infosUtilisateurs : tuple):
    """
    infosUtilisateurs doit être au format (clefUtilisateur : str, nouveauMail : str)
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouvelleValeur est la nouvelle valeur
    permet de remplacer la valeur de nom par nouveauNom
    """
    try:
        db.reference('comptes').child(infosUtilisateurs[0]).update({
            'nom': infosUtilisateurs[1]
        })
    except:
        print("connexion internet instable")

def modifierPrenom(infosUtilisateurs : tuple):
    """
    infosUtilisateurs doit être au format (clefUtilisateur : str, nouveauMail : str)
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    nouvelleValeur est la nouvelle valeur
    permet de remplacer la valeur de prenom par nouveauPrenom
    """
    try:
        db.reference('comptes').child(infosUtilisateurs[0]).update({
            'prenom': infosUtilisateurs[1]
        })
    except:
        print("connexion internet instable")

def supprimerUtilisateur(clefUtilisateur : str):
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur
    permet de supprimer un utilisateur de la base de données
    """
    try:
        db.reference('comptes').child(clefUtilisateur).delete()
    except:
        print("connexion internet instable")

def lireUtilisateur(clefUtilisateur : str)->dict:
    """
    clefUtilisateur est la clef qui renvoie aux données de l'utilisateur 
    """
    try:
        return(db.reference('comptes').child(clefUtilisateur).get())
    except:
        print("connexion internet instable")

def getTousUtilisateurs()->dict:
    """
    permet de renvoyer l'ensemble des données stockées 
    ne prend pas d'argument
    """
    return(db.reference('comptes').get())

def getNomUtilisateur(utilisateur : dict)->str:
    return utilisateur["nom"]

def getPrenomUtilisateur(utilisateur : dict)->str:
    return utilisateur["prenom"]

def getMailUtilisateur(utilisateur : dict)->str:
    return utilisateur["mail"]

def getMdpUtilisateur(utilisateur : dict)->str:
    return utilisateur["mdp"]