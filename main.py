import pandas as pd
import numpy as np
import requests as rq
from bs4 import BeautifulSoup as bs
import time

soup =bs("", "html.parser")

def parsers(e):
    """"Cette fonction vérifie si un élément sélectionner dans soup exite puis
    affiche contenu comme text; On utilise cette appelle cette fonction
    dans la fonction simple_find crée en dessus.
    
    Args:
        e (une balise): _description_

    Returns:
        _type_: _description_
    """
    if e:
        return e.text
    return None