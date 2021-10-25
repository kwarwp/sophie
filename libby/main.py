# sophie.libby.main.py cleyton jhonnison 
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
MANSAO="https://i.pinimg.com/736x/3d/74/b1/3d74b17105ce1d2046935a29331cc55e.jpg "
CLARK="https://imagensemoldes.com.br/wp-content/uploads/2020/04/Imagem-Olaf-Cenouras-Frozen-Frozen-PNG-1280x720.png"
CASA="https://static3.depositphotos.com/1008559/246/v/600/depositphotos_2467738-stock-illustration-vector-illustration-of-house.jpg"
NARUTO="https://i.pinimg.com/originals/ed/fb/bf/edfbbf577811081d08dbf0a91c83bfb1.png"
class OLAF ():
    def __init__(self): 
        self.mansao=Cena(img=MANSAO)
        self.clark=Elemento(img=CLARK)
        self.casa=Cena(img=CASA)
        self.naruto=Elemento(img=NARUTO)
        self.mansao.direita=self.casa
        self.casa.esquerda=self.mansao
        self.naruto.entra(self.casa)
        self.clark.entra(self.mansao)
        self.mansao.vai()
OLAF()
      
        