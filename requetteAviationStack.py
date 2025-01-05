import requests

def chercherDeppart(aeroport : str, key = "403e689007c360fc591f24f924406e6b")->list:
    """
    aeroport : str, corresppond à l'aéroport de déppart
    key : str, clef de l'api utilisateur
    attention : utilise une recherche !!
    renvoie la liste des vol au déppart de aéroport
    """
    url = "https://api.aviationstack.com/v1/flights?access_key="+key
    response = requests.get(url)
    response=response.json()
    listeVol=[]
    for i in range(len(response["data"])):
        if response["data"][i]["departure"]["airport"] == aeroport:
            listeVol.append(response["data"][i])
    return listeVol

def chercherArriver(aeroport : str, key = "403e689007c360fc591f24f924406e6b")->list:
    """
    aeroport : str, corresppond à l'aéroport de départ
    key : str, clef de l'api utilisateur
    attention : utilise une recherche !!
    renvoie la liste des vols qui arrivent à aeroport
    """
    url = "https://api.aviationstack.com/v1/flights?access_key="+key
    response = requests.get(url)
    response=response.json()
    listeVol=[]
    for i in range(len(response["data"])):
        if response["data"][i]["arrival"]["airport"] == aeroport:
            listeVol.append(response["data"][i])
    return listeVol

def numeroVol(vol : list)-> str:
    """
    vol : list
    renvoie le nuémro de vol du vol sous forme de str
    """
    return str(vol['flight']["number"])

def typeAvion(vol : list)->str:
    """
    vol : list
    renvoie le type de l'avion du vol sous forme de str
    """
    return str(vol["aircraft"])

def pisteArrive(vol : list) -> str:
    """
    vol : list
    renvoie la piste d'arrivé du vol sous forme de str
    """
    return str(vol["arrival"]["actual_runway"])

def pisteDepart(vol : list)->str:
    """
    vol : list
    renvoie la piste de départ du vol sous forme de str
    """
    return str(vol["departure"]["actual_runway"])

def porteArrive(vol : list)->str:
    """
    vol : list
    renvoie la porte d'arrivé du vol sous forme de str
    """
    return str(vol["arrival"]["gate"])

def porteDepart(vol : list)->str:
    """
    vol : list
    renvoie la porte de départ du vol sous forme de str
    """
    return str(vol["departure"]["gate"])

def terminalArrive(vol : list)->str:
    """
    vol : list
    renvoie le terminal d'arrivé du vol sous forme de str
    """
    return str(vol["arrival"]["terminal"])

def terminalDeparture(vol : list)->str:
    """
    vol : list
    renvoie le terminal de départ sous forme de str
    """
    return str(vol["departure"]["terminal"])

def delayArrive(vol : list)->str:
    """
    vol : list
    renvoie le retard à l'arrivé du vol sous forme de str
    """
    return str(vol["arrival"]["delay"])

def delayDepart(vol : list)->str:
    """
    vol : list
    renvoie le retard au départ du vol sous forme de str
    """
    return str(vol["departure"]["delay"])

def nomCompagnieVol(vol : list)->str:
    """
    vol : list
    renvoie le nom de la compagnie du vol sous forme de str
    """
    return str(vol["airline"]["name"])

def heureDepartVolEstime(vol : list)->str:
    """
    vol : list
    renvoie l'heure de départ éstimée du vol sous forme de str 
    """
    return str(vol["departure"]["estimated"])

def heureArriveVolEstime(vol : list)->str:
    """
    vol : list
    renvoie l'heure d'arrivé éstimée du vol sous forme de str
    """
    return str(vol["arrival"]["estimated"])