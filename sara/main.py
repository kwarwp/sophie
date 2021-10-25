# sophie.sara.main.py/ana clara kaicke
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import INVENTARIO  as inv
CASA= "https://www.plantapronta.com.br/projetos/140/01.jpg"
BART= "https://minilua.com/wp-content/uploads/2011/05/cartoons011_thumb.jpg"
PREDIO= "https://i.pinimg.com/originals/ff/30/4e/ff304e7727b7782d04e0eecb5b238eb8.jpg"
WANDINHA="https://images.uncyc.org/pt/thumb/9/9a/Familia-addams-2-05.jpg/300px-Familia-addams-2-05.jpg"
class bartsimpson ( ):
    def __init__(self):
	self.casa=Cena(img=CASA)
	self.bart= Elemento(img=BART)
	self.predio=Cena(img=PREDIO)
	self.wandinha=Elemento(img=WANDINHA) 
	self.casa.direita=self.casa
	self.predio.esquerda=self.predio
	self.bart.entra(self.casa)
	self.wandinha.entra(self.predio)
	self.casa.vai()
bartsimpson()
