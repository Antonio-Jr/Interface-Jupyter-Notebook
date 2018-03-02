from IPython.display import Javascript, display
from ipywidgets import widgets

from Elements import Elements
from modulo_busca_arquivos import retorno, ApplyFilters

filtro = dict()
cells_visable = True
file_Path = dict()

class Events:
    def __init__(self):
        self.elm = Elements()
        self.emExibicao = self.elm.exibicao(exib=str(len(retorno.keys())), total=str(len(retorno.keys())))

    def toggle_code_cells(self, btn):
        global cells_visable
        if cells_visable:
            display(Javascript("$('div.input').hide();"))
            btn.description = "Mostrar Celulas"
        else:
            display(Javascript("$('div.input').show();"))
            btn.description = "Esconder Celulas"
        cells_visable = not cells_visable

    def recolheMenu(self, n):
        import Elements as elm
        if elm.left_box.layout.visibility == "hidden":
            elm.vBox.layout.width = "50%"
            elm.left_box.layout.visibility = "visible"
            elm.left_box.layout.width = "50%"
        else:
            elm.left_box.layout.visibility = "hidden"
            elm.left_box.layout.width = "0%"
            elm.vBox.layout.width = "100%"











