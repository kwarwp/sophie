# sophie.grace.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"]= 1350, "600px"
RIO = "https://i.imgur.com/wz5XKcr.jpg"
VADER = "https://i.imgur.com/dmRivpB.png"
praia = Cena(RIO).vai()
Elemento(VADER, cena=praia)