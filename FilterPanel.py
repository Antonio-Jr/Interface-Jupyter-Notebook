# encoding: utf-8

import ast
from IPython.display import display, HTML
from ipywidgets import widgets
from Appearance import LayoutSytle
from SearchFiles import FindFiles, RefineJson, ApplyFilters

_lt = LayoutSytle()

class BuildFilterPanel:

    def __init__(self, path):

        self._css = """
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
        self._static = widgets.HBox()
        self._multiple_box = widgets.VBox()
        self._uniquePlusCollapse = widgets.HBox()
        self._selectMultiple = widgets.SelectMultiple()
        self._select = widgets.VBox()

        ###### Buttons Creation ######
        self._collapse = widgets.Button(description="", tooltip="Collapse", icon="fa-angle-double-up")
        self._filter_btn = widgets.Button(description="Aplicar Filtros", icon="fa-paper-plane", button_style="primary")
        self._applyChooses = widgets.Button(description="Aplicar", button_style="primary", icon="fa-check-circle")

        ###### Variables Creation ######
        self._path = path
        self._unicos = list()
        self._multiplas = list()
        self.finded = list()
        self._filtro = dict()
        self._arquivo = dict()
        self._arquivos = dict()
        self._refined = dict()
        self._fullFiles = dict()
        self._file_Path = dict()

        ###### Variable that receive external methods return - Creation ######
        self._emExibicao = widgets.Label(value="", align_self="center")
        self._buildJson = FindFiles(self._path)
        self._mj = self._buildJson.montaJson()
        self._refineJson = RefineJson(self._mj)
        self._json = self._refineJson.build()

        self._leftBox()

    def _buildSingularFilters(self):
        uniKey = self._json['unique'].keys()
        for i in uniKey:
            key = str(i.encode("ascii", "replace"))
            value = str(self._json['unique'][i])
            value = value.encode("ascii", "replace")
            description = str(self._json['unique'][i])

            self._unicos.append(self._labelSingularFilter(key, value ,description))

        if len(self._unicos) == 0:
            self._unicos.append(self._notUnicos())

        return self._unicos

    @staticmethod
    def _notUnicos():
        return widgets.Label(value="Nao Ha Caracteristicas Unicas", description="Nao ha", display="flex-shrink", layout = _lt.notUnicos_layout()).add_class('vazio')

    @staticmethod
    def _labelSingularFilter(key, value, description):
        return widgets.Label(value=key + ": " + value, description=description, display="flex-wrap", width="95%", style={'description_width':'initial'}).add_class('space').add_class('blue')

    def _buildMultipleFilters(self):
        multiplos = dict()
        multKey = self._json['multiple'].keys()
        for j in multKey:
            listaDeCheckBox = list()
            for k in self._json['multiple'][j]:
                option = self._checkBoxMultipleFilters(unicode(str(k)), str(j))
                option.observe(self._change, names='value')
                listaDeCheckBox.append(option)

            multiplos[j] = listaDeCheckBox


        for k, v in multiplos.iteritems():
            sBox = widgets.VBox()
            sBox.children=[self._labelMultipleFilter(str(k), str(k)), self._boxMultipleFilters(v)]
            sBox.log.info = str(k)
            # print(sBox.log.info)
            self._multiplas.append(sBox)
            # self._multiplas.append(self._labelMultipleFilter(str(k),str(k)))
            # self._multiplas.append(self._boxMultipleFilters(v))


    def _change(self, x):
        key = x.owner.style.description_width
        value = x.owner.description
        if x.new:
            if not key in self._filtro.keys():
                self._filtro[key] = list()
            if not value in self._filtro[key]:
                self._filtro[key].append(value)
        else:
            if len(self._filtro[key]) == 1:
                del (self._filtro[key])
            else:
                self._filtro[key].remove(value)

    @staticmethod
    def _checkBoxMultipleFilters(description, auxiliar):
        return widgets.Checkbox(description=description, encoding="ascii", width="100%", display='flex', indent=False, style={"description_width": auxiliar}).add_class('space-checkBox')

    @staticmethod
    def _labelMultipleFilter(value, description):
        return widgets.Label(value=value.capitalize(), description=description.capitalize(), display="flex-shrink", layout=_lt.labelFilterMultiple_layout()).add_class("space")

    def _boxMultipleFilters(self, childrens):
        boxMultipleFilter = widgets.HBox([v for v in childrens], layout=_lt.boxMultipleFilter_layout())
        return boxMultipleFilter

    def _staticBox(self):
        unicos = self._buildSingularFilters()
        self._static.children = [i for i in unicos]
        self._static.layout = _lt.staticBox_layout()
        return self._static

    def _multipleBox(self):
        self._buildMultipleFilters()
        self._multiple_box.layout = _lt.multipleBox_layout()
        self._multiple_box.style = {'description_width': 'initial'}
        self._multiple_box.children = [i for i in self._multiplas]
        return self._multiple_box

    def _filterButton(self):
        self._filter_btn.layout = _lt.filterBtn_layout()
        self._filter_btn.style.button_color = '#009850'  # '#2CD660'
        self._filter_btn.on_click(self._aplicaFiltros)
        return self._filter_btn

    def _multiSelection(self):
        self._selectMultiple.layout = _lt.selectMultiple_layout()
        return self._selectMultiple

    def _applyChooseButton(self):
        self._applyChooses.layout = _lt.applyChooseButton_layout()
        self._applyChooses.style.button_color = "#009850"
        self._applyChooses.on_click(self._renderJson)
        return self._applyChooses

    def _getIndices(self):
        indices = dict()
        for i in self._selectMultiple.index:
            for j in self._mj:
                if self._file_Path[self._selectMultiple.options[i]] in self._mj[j]['file']:
                    indices[j] = self._selectMultiple.options[i]

        self._arquivos = indices
        return indices

    def _getProperties(self, dictionary):
        intersection = dict()
        indexes = dictionary.keys()
        keys = self._mj[indexes[0]]['content'].keys()
        for i in indexes:
            for j in keys:
                if not dictionary[i] in intersection:
                    intersection[dictionary[i]] = dict()
                intersection[dictionary[i]][j] = self._mj[i]['content'][j]  # - intersection[j]

        self._refined = intersection
        return intersection

    def _renderJson(self, n):
        indices = self._getIndices()
        intersection = self._getProperties(indices)

        from PreRenderJson import BuildTree
        mt = BuildTree()

        for i in intersection.keys():
            for j in intersection[i]['message']:
                if isinstance(j, unicode) and ":" in j:
                    k = j.split(":")
                    j = str("{'"+k[0]+"'"+":'"+k[1]+"'}")
                if not isinstance(j, unicode):
                    mt.fillNumProperties(ast.literal_eval(j))
            self._arquivo[i] = mt.dict

        from RenderJson import RenderJSON
        for k, v in self._arquivo.iteritems():
            pass
            # print k
            # display(RenderJSON(v))

    def exibeFiltrados(self, jsons):
        self._selectMultiple = self._multiSelection()
        items = list()

        for i in jsons:
            for j in self._mj:
                if i == self._mj[j]['file']:
                    fullPath = str(i).split("/")
                    arq = fullPath[-1]
                    self._file_Path[arq] = i
                    items.append(arq)
        options = [i for i in items]
        self._selectMultiple.options = options
        self._selectMultiple.layout.visibility = "visible"
        self._select.children = [self._selectMultiple, self._applyChooseButton()]
        self._fullFiles = self._file_Path
        display(self._select)

    def _aplicaFiltros(self, n):
        af = ApplyFilters(self._filtro, self._mj)
        filtrado = af.make()
        capturados = set()
        for k in filtrado.keys():
            for v in filtrado[k]:
                capturados.add(v)

        if len(filtrado.keys()) != 0:
            self._emExibicao.value = "Sua busca retornou " + str(len(capturados)) + " de " + str(len(self._mj.keys())) + " arquivos"

        self.finded = list(capturados)
        # display('Os arquivos estao salvos na varivel finded. Para visualizar solicite a impressao da mesma. Caso queira exibir na caixa de dialogo, invoque o metodo exibeFiltrados.')

    def _uniqueCollapse(self):
        self._uniquePlusCollapse.children = [widgets.Label(value="Caracteristicas Unicas", description="Caracteristicas Unicas", display="flex-shrink", layout = _lt.uniqueCollapse_layout()), self._collapsable()]
        return self._uniquePlusCollapse

    def _collapseUnicas(self, n):
        if (self._static.layout.visibility == "hidden"):
            self._collapse.icon = "fa-angle-double-up"
            self._collapse.tooltip = "Collapse"
            self._static.layout.height = "100%"
            self._static.layout.visibility = "visible"
        else:
            self._static.layout.visibility = "hidden"
            self._static.layout.height = "0"
            self._collapse.tooltip = "Expand"
            self._collapse.icon = "fa-angle-double-down"

    def _collapsable(self):
        self._collapse.layout = _lt.collapseButton()
        self._collapse.style.button_color = "white"
        self._collapse.on_click(self._collapseUnicas)
        return self._collapse

    def _exibicao(self):
        self._emExibicao = widgets.Label(value="Foram encontrados "+str(len(self._mj))+ " arquivos.").add_class("center")
        return self._emExibicao

    def _leftBox(self):
        left_box = widgets.VBox()
        left_box.children = [self._exibicao(),
                            widgets.Label(value="Filtros", description="Filtros", display="flex-shrink", layout=_lt.leftBox_layout()),
                             self._uniqueCollapse(),
                             self._staticBox(),
                             widgets.Label(value="Caracteristicas Multiplas", description="Caracteristicas Multiplas", display="flex-shrink",
                                           layout=_lt.labelCaracteristicasMultiplas_layout()).add_class('top-line'),
                             self._multipleBox(),
                             self._filterButton()]

        left_box.layout = _lt.leftBox_layout()
        display(HTML(self._css))
        display(left_box)