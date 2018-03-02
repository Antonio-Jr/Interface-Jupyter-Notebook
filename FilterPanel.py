# encoding: utf-8
from Appearance import Layouts
from ipywidgets import widgets
from IPython.display import display, HTML
from modulo_busca_arquivos import FindFiles, RefineJson, ApplyFilters

lt = Layouts()

class BuildFilterPanel:

    def __init__(self, path):

        self.css = """
            <style> 
            /*.container{
                    width: 98%;
                }*/
        
            .output{
                height:100%;
                }
        
            .output_scroll{
                height: 100%;
                }
        
            .widget-label{
                    height: 100px;
                    white-space: wrap;
                    font-weight: bold;
                    font-size: 16px;
                    text-align: left;
                    }
        
            .widget-checkbox {
                    width: 90%;
                }
        
            .space{
                text-align: left;
                font-size: 13px;
                }
                
            .space-checkBox{
                text-align: left;
                font-size: 13px;
                margin-left: 3%;
                }
        
            .vazio{
                color: red;
                font-size: 12px;
                text-align: left;
                }
            
            .center{
                text-align: center;
                font-size: 17px;
                }
                
            .blue{
                color: blue;
                font-size: 11.5px;
                }
        
            .vertical-line{
                border-right: 1px groove black;
                }
        
            .horizontal-line{
                border-bottom: 1px groove black;
                }
        
            .top-line{
                border-top: 1px groove black;
                }
            .border{
                border: 1px groove black;
                border-radius: 5px;
                }
            </style>"""

        ###### Boxes Creation ######
        self.static = widgets.HBox()
        self.multiple_box = widgets.VBox()
        self.uniquePlusCollapse = widgets.HBox()
        self.selectMultiple = widgets.SelectMultiple()

        ###### Buttons Creation ######
        self.collapse = widgets.Button(description="", tooltip="Collapse", icon="fa-angle-double-up")
        self.filter_btn = widgets.Button(description="Aplicar Filtros", icon="fa-paper-plane", button_style="primary")
        self.applyChooses = widgets.Button(description="Aplicar", button_style="primary", icon="fa-check-circle")

        ###### Variables Creation ######
        self.unicos = list()
        self.multiplas = list()
        self.finded = list()
        self.filtro = dict()

        ###### Variable that receive external methods return - Creation ######
        self.emExibicao = widgets.Label(value="", align_self="center");
        self.buildJson = FindFiles(path)
        self.mj = self.buildJson.montaJson()
        self.refineJson = RefineJson(self.mj)
        self.json = self.refineJson.build()

        self._leftBox()

    def _buildSingularFilters(self):
        uniKey = self.json['unique'].keys()
        for i in uniKey:
            key = str(i.encode("ascii", "replace"))
            value = str(self.json['unique'][i])
            value = value.encode("ascii", "replace")
            description = str(self.json['unique'][i])

            self.unicos.append(self._labelSingularFilter(key, value ,description))

        if len(self.unicos) == 0:
            self.unicos.append(self._notUnicos())

        return self.unicos

    def _notUnicos(self):
        return widgets.Label(value="Nao Ha Caracteristicas Unicas", description="Nao ha", display="flex-shrink", layout = lt.notUnicos_layout()).add_class('vazio')

    def _labelSingularFilter(self, key, value, description):
        return widgets.Label(value=key + ": " + value, description=description, display="flex-wrap", width="95%", style={'description_width':'initial'}).add_class('space').add_class('blue')

    def _buildMultipleFilters(self):
        multiplos = dict()
        multKey = self.json['multiple'].keys()
        for j in multKey:
            listaDeCheckBox = list()
            for k in self.json['multiple'][j]:
                option = self._checkBoxMultipleFilters(unicode(str(k)), str(j))
                option.observe(self._change, names='value')
                listaDeCheckBox.append(option)

            multiplos[j] = listaDeCheckBox


        for k, v in multiplos.iteritems():
            self.multiplas.append(self._labelMultipleFilter(str(k),str(k)))
            self.multiplas.append(self._boxMultipleFilters(v))


    def _change(self, x):
        key = x.owner.style.description_width
        value = x.owner.description
        if x.new:
            if not key in self.filtro.keys():
                self.filtro[key] = list()
            if not value in self.filtro[key]:
                self.filtro[key].append(value)
        else:
            if len(self.filtro[key]) == 1:
                del (self.filtro[key])
            else:
                self.filtro[key].remove(value)

    def _checkBoxMultipleFilters(self, description, auxiliar):
        return widgets.Checkbox(description=description, encoding="ascii", width="100%", display='flex', indent=False, style={"description_width": auxiliar}).add_class('space-checkBox')

    def _labelMultipleFilter(self, value, description):
        return widgets.Label(value=value.capitalize(), description=description.capitalize(), display="flex-shrink", layout=lt.labelFilterMultiple_layout()).add_class("space")

    def _boxMultipleFilters(self, childrens):
        boxMultipleFilter = widgets.HBox([v for v in childrens], layout=lt.boxMultipleFilter_layout())
        return boxMultipleFilter

    def _staticBox(self):
        unicos = self._buildSingularFilters()
        self.static.children = [i for i in unicos]
        self.static.layout = lt.staticBox_layout()
        return self.static

    def _multipleBox(self):
        self._buildMultipleFilters()
        self.multiple_box.layout = lt.multipleBox_layout()
        self.multiple_box.style = {'description_width': 'initial'}
        self.multiple_box.children = [i for i in self.multiplas]
        return self.multiple_box

    def _filterButton(self):
        self.filter_btn.layout = lt.filterBtn_layout()
        self.filter_btn.style.button_color = '#009850'  # '#2CD660'
        self.filter_btn.on_click(self._aplicaFiltros)
        return self.filter_btn

    def _selectMultiple(self):
        self.selectMultiple.layout = lt.selectMultiple_layout()
        return self.selectMultiple

    def _applyChooseButton(self):
        self.applyChooses.layout = lt.applyChooseButton_layout()
        self.applyChooses.style.button_color = "#009850"
        self.applyChooses.on_click(self._renderJson)

    def _renderJson(self, n):
        import Elements as elm
        conjuntos = set
        indices = list()
        for i in elm.selectMultiple:
            for j in self.mj:
                if self.exibeFiltrados.file_Path[elm.selectMultiple.options[i]] in self.mj[j]['file']:
                    indices.append(j)

        for i in conjuntos:
            conjuntos.append(self.mj[j]['content'])
            conj = set(conjuntos[i]) & conj

        print conj

    #     for i in indices:
    #         for j in conj:
    #             print retorno[i]['content'][j]

    def exibeFiltrados(self, jsons):
        applyChooses = self._applyChooseButton()
        self.selectMultiple = self._selectMultiple()
        items = list()
        file_Path = dict()

        for i in jsons:
            for j in self.mj:
                if i == self.mj[j]['file']:
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
        options = [i for i in items]
        self.selectMultiple.options = options
        self.selectMultiple.layout.visibility = "visible"
        display(self.selectMultiple)
        # display(self.finded)
        # main_box.children = [widgets.VBox([widgets.Label(value='Arquivos Retornados:'), selectMultiple, applyChooses],layout=lt.accordionChildren_layout())]
        # display(main_box)

    def _aplicaFiltros(self, n):
        af = ApplyFilters(self.filtro, self.mj)
        filtrado = af.make()
        capturados = set()
        for k in filtrado.keys():
            for v in filtrado[k]:
                capturados.add(v)

        if len(filtrado.keys()) != 0:
            self.emExibicao.value = "Sua busca retornou " + str(len(capturados)) + " de " + str(len(self.mj.keys())) + " arquivos"

        self.finded = list(capturados)
        display('Os arquivos estao salvos na varivel finded. Para visualizar solicite a impressao da mesma. Caso queira exibir na caixa de dialogo, invoque o metodo exibeFiltrados.')
        # self.exibeFiltrados(jsons=capturados)

    def _uniqueCollapse(self):
        self.uniquePlusCollapse.children = [widgets.Label(value="Caracteristicas Unicas", description="Caracteristicas Unicas", display="flex-shrink", layout = lt.uniqueCollapse_layout()), self._collapsable()]
        return self.uniquePlusCollapse

    def _collapseUnicas(self, n):
        if (self.static.layout.visibility == "hidden"):
            self.collapse.icon = "fa-angle-double-up"
            self.collapse.tooltip = "Collapse"
            self.static.layout.height = "100%"
            self.static.layout.visibility = "visible"
        else:
            self.static.layout.visibility = "hidden"
            self.static.layout.height = "0"
            self.collapse.tooltip = "Expand"
            self.collapse.icon = "fa-angle-double-down"

    def _collapsable(self):
        self.collapse.layout = lt.collapseButton()
        self.collapse.style.button_color = "white"
        self.collapse.on_click(self._collapseUnicas)
        return self.collapse

    def _exibicao(self):
        self.emExibicao = widgets.Label(value="Foram encontrados "+str(len(self.mj))+ " arquivos.").add_class("center")
        return self.emExibicao

    def _leftBox(self):
        left_box = widgets.VBox()
        left_box.children = [self._exibicao(),
                            widgets.Label(value="Filtros", description="Filtros", display="flex-shrink", layout=lt.leftBox_layout()),
                             self._uniqueCollapse(),
                             self._staticBox(),
                             widgets.Label(value="Caracteristicas Multiplas", description="Caracteristicas Multiplas", display="flex-shrink",
                                           layout=lt.labelCaracteristicasMultiplas_layout()).add_class('top-line'),
                             self._multipleBox(),
                             self._filterButton()]

        left_box.layout = lt.leftBox_layout()
        display(HTML(self.css))
        display(left_box)

