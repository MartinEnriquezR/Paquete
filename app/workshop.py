import requests

#test del modulo python -m doctest module.py

def unreleased():
    """
    Retorna los proximos cursos en codigo facilito
    >>> type(unreleased()) == type(dict())
    True
    """
    
    response = requests.get(
        url = "https://codigofacilito.com/api/v2/workshops/unreleased"
    )
    if response.status_code == 200:
        payload = response.json()
        return payload['data']