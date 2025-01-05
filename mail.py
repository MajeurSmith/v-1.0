import win32com.client as win32
import os


localPath = os.path.dirname(os.path.abspath(__file__))

def envoieMail(destinataire : str, objet : str, txt : str, annexe : bool = False):
    """
    destinataire : addresse mail du destinataire au format str
    objet : objet du mail au format str
    txt : texte du mail au format str; possibilité de l'écrire dans le language HTML
    annexe : si annexe == True alors le fichier TableauVol.pdf se trouvant dans icones est envoyé au déstinataire, sinon il n'est pas envoyé
    envoie un mail au déstinataire
    """
    outlook = win32.Dispatch('outlook.application')   # création avec Outlook
    email = outlook.CreateItem(0)                     # Création d'un e-mail
    email.to = destinataire
    email.Subject = objet
    email.HTMLBody = txt
    if annexe:
        email.Attachments.Add(localPath + "Logo.png")
    email.Send()

