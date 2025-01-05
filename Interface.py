from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from requetteBaseDonnees import ajouterUtilisateur , hash ,supprimerUtilisateur , getTousUtilisateurs
from mail import envoieMail
from requetteAviationStack import *


win0 = ""
win1 = ""
win2 = ""
win3 = ""
win4 = ""
win6 = ""
win7 = ""
app =  ""


def connexion():   #Ouvre la page de connexion
    global win1
    win1.close()
    win1.setWindowTitle("Page de connexion")
    win1.setWindowIcon(QIcon("icones/Logo3.png"))
    win1.Mail1.setPlaceholderText("E-Mail")
    win1.MDP1.setPlaceholderText("Mot de passe")
    win1.Confirmer1.clicked.connect(connecter) #Relier fonction de ton code
    win1.Retour1.clicked.connect(fin_win1)
    win1.show()

def connecter():
    global win1
    mail = win1.Mail1.text()
    clef = ""
    for letter in mail:
        if letter == ".":
            continue
        clef += letter
    mdp = win1.MDP1.text()
    code = hash(mdp)
    dico = getTousUtilisateurs()
    if clef in dico.keys() :
        if code == dico[clef]['mdp'] :
            prenom = dico[clef]['prenom']
            win0.Bienvenue.setText(f"Bienvenue {prenom}")
            win1.close()

def creation():    #Ouvre la page de création de compte
    global win2
    win2.close()
    win2.setWindowTitle("Page de création de compte")
    win2.setWindowIcon(QIcon("icones/Logo3.png"))
    win2.MDP2.setPlaceholderText("Mot de passe")
    win2.Nom2.setPlaceholderText("Nom")
    win2.Prenom2.setPlaceholderText("Prenom")
    win2.Mail2.setPlaceholderText("E-Mail")
    win2.Confirmer2.clicked.connect(creer)  
    win2.Annuler2.clicked.connect(fin_win2)
    win2.show()

def creer():
    global win2
    
    mdp = win2.MDP2.text()
    code = hash(mdp)
    nom = win2.Nom2.text()
    prenom = win2.Prenom2.text()
    mail = win2.Mail2.text()
    clef = mail.replace(" ","")
    clef.replace(".","")
    tuple = (nom, prenom, mail, code)
    texte = "Bonjour, nous sommes ravis de vous compter parmi nos utilisateurs ! Votre compte a bien été créé sur MAFR, et vous êtes maintenant prêt(e) à explorer toutes les fonctionnalités que nous avons à offrir."
    clef = ""
    for letter in mail:
        if letter == "." and letter == " ":
            continue
        clef += letter
    dico = getTousUtilisateurs()
    if clef in dico.keys() :
        win2.label.setText("Vous avez déjà un compte lier à cet E-Mail")
    else :
        ajouterUtilisateur(tuple)
        envoieMail(mail,"Objet : Bienvenue sur MAFR !",texte)
        win0.Bienvenue.setText(f"Bienvenue {prenom}")
        win2.close()
    
def suppression():    #Ouvre la page de suppression de compte
    global win3
    win3.close()
    win3.setWindowTitle("Page de suppression de compte")
    win3.setWindowIcon(QIcon("icones/Logo3.png"))
    win3.Mail3.setPlaceholderText("E-Mail")
    win3.MDP3.setPlaceholderText("Mot de passe")
    win3.Confirmer3.clicked.connect(supprimer) #Relier fonction de ton code
    win3.Annuler3.clicked.connect(fin_win3)
    win3.show()

def supprimer():
    global win3
    mail = win3.Mail3.text()
    clef = ""
    for letter in mail :
        if letter == "." :
            continue
        clef += letter
    mdp = win3.MDP3.text()
    code = hash(mdp)
    dico = getTousUtilisateurs()
    if clef in dico.keys():
        if code == dico[clef]['mdp'] :
            supprimerUtilisateur(clef)
            win3.close()

def aeroport(aeroportClique : str):    #Ouvre la page d'interface des aéroports
    global win4 , app
    win4.close()
    win4.Liste4_1.clear()
    win4.Liste4_2.clear()
    win4.setWindowTitle("Interface aéroport")
    win4.setWindowIcon(QIcon("icones/Logo3.png"))
    ville = app.sender()                                                       #Place la bonne ville dans le titre
    win4.Titre4.setText(f"Liste des vols opérant depuis {ville.objectName()}")
    numéro_vol1 = []
    volDeppart = chercherDeppart(aeroportClique)
    for e in volDeppart:
        numéro_vol1.append(numeroVol(e))
    for num in range(len(numéro_vol1)) :
        win4.Liste4_1.addItem(str(numéro_vol1[num]))
    numéro_vol2 = []
    volArrive = chercherArriver(aeroportClique)
    for f in volArrive:
        numéro_vol2.append(numeroVol(f))
    for num in range(len(numéro_vol2)):
        win4.Liste4_2.addItem(str(numéro_vol2[num]))
    win4.Liste4_1.itemClicked.connect(lambda item: vol_départ(volDeppart,item))
    win4.Liste4_2.itemClicked.connect(lambda item: vol_arrivé(volArrive,item))
    win4.Retour4.clicked.connect(fin_win4)
    win4.show()

def vol_arrivé(listeVols,item):
    global win6
    for e in listeVols:
        if numeroVol(e) == item.text():
            vol = e 
    win6.close()
    win6.setWindowTitle("Fenêtre arrivées")
    win6.setWindowIcon(QIcon("icones/Logo3.png"))
    compagnie = nomCompagnieVol(vol)
    avion = typeAvion(vol)
    piste = pisteArrive(vol)
    terminal = terminalArrive(vol)
    porte = porteArrive(vol)
    heure = heureArriveVolEstime(vol)
    retard = delayArrive(vol)
    win6.tableWidget.setItem(0 , 0 , QtWidgets.QTableWidgetItem(compagnie))
    win6.tableWidget.setItem(1 , 0 , QtWidgets.QTableWidgetItem(avion))
    win6.tableWidget.setItem(2 , 0 , QtWidgets.QTableWidgetItem(piste))
    win6.tableWidget.setItem(3 , 0 , QtWidgets.QTableWidgetItem(terminal))
    win6.tableWidget.setItem(4 , 0 , QtWidgets.QTableWidgetItem(porte))
    win6.tableWidget.setItem(5 , 0 , QtWidgets.QTableWidgetItem(heure))
    win6.tableWidget.setItem(6 , 0 , QtWidgets.QTableWidgetItem(retard))
    win6.show()

def vol_départ(listeVols,item):
    global win7
    win7.close()
    win7.setWindowTitle("Fenêtre départs")
    win7.setWindowIcon(QIcon("icones/Logo3.png"))
    for e in listeVols:
        if numeroVol(e) == item.text():
            vol = e 
    compagnie = nomCompagnieVol(vol)
    avion = typeAvion(vol)
    piste = pisteDepart(vol)
    terminal = terminalDeparture(vol)
    porte = porteDepart(vol)
    heure = heureDepartVolEstime(vol)
    retard = delayDepart(vol)
    win7.tableWidget.setItem(0 , 0 , QtWidgets.QTableWidgetItem(compagnie))
    win7.tableWidget.setItem(1 , 0 , QtWidgets.QTableWidgetItem(avion))
    win7.tableWidget.setItem(2 , 0 , QtWidgets.QTableWidgetItem(piste))
    win7.tableWidget.setItem(3 , 0 , QtWidgets.QTableWidgetItem(terminal))
    win7.tableWidget.setItem(4 , 0 , QtWidgets.QTableWidgetItem(porte))
    win7.tableWidget.setItem(5 , 0 , QtWidgets.QTableWidgetItem(heure))
    win7.tableWidget.setItem(6 , 0 , QtWidgets.QTableWidgetItem(retard))
    win7.show()

def fin_win1():
    win1.close()

def fin_win2():
    win2.close()

def fin_win3():
    win3.close()

def fin_win4():
    win4.Liste4_1.clear()
    win4.Liste4_2.clear()
    win4.close()

def fin_programme():
    win0.close()
    win1.close()
    win2.close()
    win3.close()
    win4.close()
    win6.close()
    win7.close()
    sys.exit()

def debut_programme():
    global win0 , win1 , win2 , win3 , win4 , win6 , win7 , app
    app = QtWidgets.QApplication([])
    win0 = uic.loadUi("ui/Carte-V3.ui") # fenêtre principal
    win0.setWindowTitle("Fenêtre principale")
    win0.setWindowIcon(QIcon("icones/Logo3.png"))
    #pixmap1 = QPixmap("icones/outre-mer à placer v2.png")
    win0.CarteOutremer.setPixmap(QPixmap("icones/outre-mer à placer v2.png"))
    #win0.CarteOutremer.setPixmap(pixmap1)
    pixmap2 = QPixmap("icones/01-Fond-carte-3d.jpg")
    win0.CarteMetropole.setPixmap(pixmap2)
    pixmap3 = QPixmap("icones/Logo.png")
    win0.Logo.setPixmap(pixmap3)
#Connexion des bouttons
    win0.Connexion.clicked.connect(connexion)
    win0.Quitter.clicked.connect(fin_programme)
    win0.Creation.clicked.connect(creation)
    win0.Suppression.clicked.connect(suppression)
#Connexion des villes :
    win0.Dunkerque.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Lille.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Amiens.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Cherbourg.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Rouen.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Caen.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Le_Havre.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Paris.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Reims.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Nancy.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Strasbourg.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Rennes.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Orleans.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Nantes.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Poitiers.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Dijon.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Limoges.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Lyon.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Clermont_Ferrand.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Bordeaux.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Toulouse.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Montpellier.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.Marseille.clicked.connect(lambda : aeroport(str("Marseille Provence Airport")))
    win0.Ajaccio.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.La_Guadeloupe.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.La_Guyane.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.La_Martinique.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win0.La_Reunion.clicked.connect(lambda a = "Dunkerque" : aeroport(a))
    win1 = uic.loadUi("ui/Page de connexion.ui")  # page de connexion
    win2 = uic.loadUi("ui/Création de compte.ui")  # page de création de compte
    win3 = uic.loadUi("ui/Suppression de compte.ui")  # page de suppression de compte
    win4 = uic.loadUi("ui/Interface aéroport.ui") # fenêtre aéroport
    win6 = uic.loadUi("ui/Infos vols V2.ui")
    win7 = uic.loadUi("ui/Infos vols départ.ui")
    win0.show()
    app.exec()

debut_programme()



