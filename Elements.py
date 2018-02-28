from ipywidgets import widgets
from Appearance import Layouts

lt = Layouts()

#####  Buttons #####
collapse = widgets.Button(description="", tooltip="Collapse", icon="fa-angle-double-up")
toggle_filter = widgets.Button(description="Esconder Filtros", icon="fa-eye-slash", button_style="info")
toggle_cell = widgets.Button(description="Esconder Celulas", icon="fa-eye-slash", button_style="danger")
filter_btn = widgets.Button(description="Aplicar Filtros", icon="fa-paper-plane", button_style="primary")
applyChooses = widgets.Button(description="Aplicar", button_style="primary", icon="fa-check-circle")

#####  Boxes  #####
mainBox = widgets.VBox()
static = widgets.HBox()
selectMultiple = widgets.SelectMultiple()
multiple_box = widgets.VBox()
uniquePlusCollapse = widgets.HBox()
right_box = widgets.VBox().add_class('horizontal-line')
vBox = widgets.VBox()
left_box = widgets.VBox().add_class('vertical-line')
box = widgets.Box()


class Elements:


    def selectMultiple(self):
        selectMultiple.layout = lt.selectMultiple_layout()
        return selectMultiple

    def staticBox(self):
        from FilterPanel import unicos
        static.children = [i for i in unicos]
        static.layout= lt.staticBox_layout()
        return static

    def multipleBox(self):
        from FilterPanel import multiplas
        multiple_box.layout = lt.multipleBox_layout()
        multiple_box.style={'description_width': 'initial'}
        multiple_box.children = [i for i in multiplas]
        return multiple_box

    def collapse(self):
        collapse.layout = lt.collapseButton()
        collapse.style.button_color = "white"
        from Events import Events
        evnt = Events()
        collapse.on_click(evnt.collapseUnicas)
        return collapse

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

    def filterButton(self):
        filter_btn.layout = lt.filterBtn_layout()
        filter_btn.style.button_color = '#009850'  # '#2CD660'
        from Events import Events
        evnt = Events()
        filter_btn.on_click(evnt.aplicaFiltros)
        return filter_btn

    def uniqueCollapse(self):
        uniquePlusCollapse.children = [widgets.Label(value="Caracteristicas Unicas", description="Caracteristicas Unicas", display="flex-shrink", layout = lt.uniqueCollapse_layout()), self.collapse()]
        return uniquePlusCollapse

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

    def leftBox(self):
        left_box.children = [widgets.Label(value="Filtros", description="Filtros", display="flex-shrink", layout = lt.leftBox_layout()),
                             self.uniqueCollapse(),
                             self.staticBox(),
                             widgets.Label(value="Caracteristicas Multiplas", description="Caracteristicas Multiplas", display="flex-shrink", layout = lt.labelCaracteristicasMultiplas_layout()).add_class('top-line'),
                             self.multipleBox(),
                             self.filterButton()]

        left_box.layout = lt.leftBox_layout()
        return left_box

    def exibicao(self, exib, total):
        return widgets.Label(value="Exibindo " + exib + " de " + total + " arquivos", description="Quantidade de Arquivos")

    def applyChooseButton(self):
        applyChooses.layout = lt.applyChooseButton_layout()
        applyChooses.style.button_color = "#009850"
        from Events import Events
        evnt = Events()
        applyChooses.on_click(evnt.renderJson)

    def labelSingularFilter(self, key, value, description):
        return widgets.Label(value=key + ": " + value, description=description, display="flex-wrap", width="95%", style={'description_width':'initial'}).add_class('space').add_class('blue')

    def labelMultipleFilter(self, value, description):
        return widgets.Label(value=value.capitalize(), description=description.capitalize(), display="flex-shrink", layout = lt.labelFilterMultiple_layout()).add_class("space")

    def checkBoxMultipleFilters(self, description, auxiliar):
        return widgets.Checkbox(description=description, encoding="ascii", width="100%", display='flex', indent=False, style={"description_width": auxiliar}).add_class('space')

    def boxMultipleFilters(self, childrens):
        boxMultipleFilter = widgets.HBox([v for v in childrens], layout = lt.boxMultipleFilter_layout())
        return boxMultipleFilter

    def notUnicos(self):
        return widgets.Label(value="Nao Ha Caracteristicas Unicas", description="Nao ha", display="flex-shrink", layout = lt.notUnicos_layout()).add_class('vazio')

    def parentBox(self):
        box.children=[self.leftBox(), self.vBox()]
        box.layout = lt.box_layout()
        return box