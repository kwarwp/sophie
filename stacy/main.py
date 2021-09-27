# sophie.stacy.main.py/adrielly.jose myguel
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import INVENTARIO as inv
CASA = "https://img.freepik.com/vetores-gratis/bela-casa_24877-50819.jpg?size=626&ext=jpg"
STHICH="https://e7.pngegg.com/pngimages/620/826/png-clipart-lilo-stitch-lilo-pelekai-sticker-paper-others-sticker-fictional-character.png"
class  HOTDOG():   
    def __init__(self):
	self.casa=Cena(img=CASA)
	self.sthich =Elemento(img=STHICH)
	self.sthich.entra(self.casa)
	self.casa.vai()
HOTDOG()
