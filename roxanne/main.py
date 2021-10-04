# sophie.roxanne.main.py/isaque kaicke cleyton/
from _spy.vitollino.main import Cena,Elemento,Texto
#from _spy.vitollino.main import INVETARIO as inv
CASA= "https://e7.pngegg.com/pngimages/789/105/png-clipart-house-house.png"
SAITAMINHA= "https://www.disneyria.com.br/wp-content/uploads/2019/12/olaf-alivio-comico.jpg"
YORK= "https://www.bigdream.com.br/_uploads/05bc1762-649c-44aa-8634-b992f998852d_Zoom.jpg"
furia= "https://e7.pngegg.com/pngimages/816/446/png-clipart-hiccup-horrendous-haddock-iii-how-to-train-your-dragon-astrid-toothless-others-dragon-fictional-character.png"

class kaka():
    def __init__ (self):
	self.casa=Cena(img=CASA)
	self.saitaminha=Elemento(img=SAITAMINHA)
	self.saitaminha.entra(self.casa)
	self.casa.vai()
kaka()

