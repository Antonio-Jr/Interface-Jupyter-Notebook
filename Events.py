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

    def collapseUnicas(self, n):
        import Elements as elm
        if (elm.static.layout.visibility == "hidden"):
            elm.collapse.icon = "fa-angle-double-up"
            elm.collapse.tooltip = "Collapse"
            elm.static.layout.height = "100%"
            elm.static.layout.visibility = "visible"
        else:
            elm.static.layout.visibility = "hidden"
            elm.static.layout.height = "0"
            elm.collapse.tooltip = "Expand"
            elm.collapse.icon = "fa-angle-double-down"

    def renderJson(self, n):
        import Elements as elm
        conjuntos = set
        indices = list()
        for i in elm.selectMultiple:
            for j in retorno:
                if file_Path[elm.selectMultiple.options[i]] in retorno[j]['file']:
                    indices.append(j)

        for i in conjuntos:
            conjuntos.append(retorno[j]['content'])
            conj = set(conjuntos[i]) & conj

        print conj

    #     for i in indices:
    #         for j in conj:
    #             print retorno[i]['content'][j]

    def montar_accordions(self, jsons):
        import Elements as elmt
        from Appearance import Layouts
        lt = Layouts()
        applyChooses = self.elm.applyChooseButton()
        selectMultiple = self.elm.selectMultiple()
        main_box = elmt.mainBox
        items = list()

        for i in jsons:
            for j in retorno:
                if i == retorno[j]['file']:
                    fullPath = str(i).split("/")
                    arq = fullPath[-1]
                    file_Path[arq] = i
                    #                 accord = widgets.HBox()
                    #                 label = widgets.Label(value=str(i))
                    #                 multKey = set(retorno[j]['config']) & set(t['multiple'])
                    #                 children=[label]
                    # #                 children=[RenderJSON(v) for v in retorno[j]['content']]
                    #                 accord.children = children
                    # #                 accord.set_title(0, str(i))
                    #                 accordions.append(accord)

                    items.append(arq)
        selectMultiple.options = [i for i in items]
        self.recolheMenu(0)
        main_box.children = [widgets.VBox([widgets.Label(value='Arquivos Retornados:'), selectMultiple, applyChooses],layout=lt.accordionChildren_layout())]
        display(main_box)

    def change(self, x):
        global filtro
        key = x.owner.style.description_width
        value = x.owner.description
        if x.new:
            if not key in filtro.keys():
                filtro[key] = list()
            if not value in filtro[key]:
                filtro[key].append(value)
        else:
            if len(filtro[key]) == 1:
                del (filtro[key])
            else:
                filtro[key].remove(value)

    def aplicaFiltros(self, n):
        global filtro
        af = ApplyFilters(filtro, retorno)
        filtrado = af.make()
        capturados = set()
        for k in filtrado.keys():
            for v in filtrado[k]:
                capturados.add(v)

        if len(filtrado.keys()) != 0:
            self.emExibicao.value = "Exibindo " + str(len(capturados)) + " de " + str(len(retorno.keys())) + " arquivos"

        self.montar_accordions(jsons=capturados)

