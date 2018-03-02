from ipywidgets import widgets
from Appearance import Layouts

lt = Layouts()

#####  Buttons #####

toggle_filter = widgets.Button(description="Esconder Filtros", icon="fa-eye-slash", button_style="info")
toggle_cell = widgets.Button(description="Esconder Celulas", icon="fa-eye-slash", button_style="danger")



#####  Boxes  #####
mainBox = widgets.VBox()

right_box = widgets.VBox().add_class('horizontal-line')
vBox = widgets.VBox()

box = widgets.Box()


class Elements:








    def toggleFilter(self):
        toggle_filter.layout = lt.toggleFilter_layout()
        toggle_filter.style.button_color = "#4D4D4D"
        from Events import Events
        evnt = Events()
        toggle_filter.on_click(evnt.recolheMenu)
        return toggle_filter

    def toggleCell(self):
        toggle_cell.layout = lt.toggleCell_layout()
        toggle_cell.style.button_color = "#FF3030"
        from Events import Events
        evnt = Events()
        toggle_cell.on_click(evnt.toggle_code_cells)
        return toggle_cell



    def mainBox(self):
        mainBox.layout = lt.main_layout()
        return mainBox

    def rightBox(self):
        from modulo_busca_arquivos import retorno
        right_box.children=[self.toggleFilter(), self.exibicao(str(len(retorno)), str(len(retorno))), self.toggleCell()]
        right_box.layout = lt.right_layout()
        return right_box

    def vBox(self):
        vBox.children=[self.rightBox(), self.mainBox()]
        vBox.layout = lt.vBox_layout()
        return vBox



    def exibicao(self, exib, total):
        return widgets.Label(value="Exibindo " + exib + " de " + total + " arquivos", description="Quantidade de Arquivos")






    def parentBox(self):
        box.children=[self.leftBox(), self.vBox()]
        box.layout = lt.box_layout()
        return box