# sophie.libby.main.py cleyton jhonnison 
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
MANSAO="https://i.pinimg.com/736x/3d/74/b1/3d74b17105ce1d2046935a29331cc55e.jpg "
CLARK="https://imagensemoldes.com.br/wp-content/uploads/2020/04/Imagem-Olaf-Cenouras-Frozen-Frozen-PNG-1280x720.png"
class OLAF ():
    def __init__(self): 
        self.mansao=Cena(img=MANSAO)
        self.clark=Elemento(img=CLARK)
        self.clark.entra(self.mansao)
        self.mansao.vai()
OLAF()
        
        