
{'date': 'Mon Jun 01 2020 13:25:04.986 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 5
    Cena(RIO).vai()
  module _spy.vitollino.main line 1003
    self._cria_divs(width)
  module _spy.vitollino.main line 1008
    divesq.style.width = width // 3  # 100
TypeError: unsupported operand type(s) for //: 'str' and 'int'
'''},