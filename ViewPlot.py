# encoding: utf-8
import ast
from itertools import izip

from ipywidgets import widgets, Label, Layout
from IPython.display import display, HTML
from filterPanel import _arquivos, _refined, _fullFiles
from preRenderJson import MontaTree
from plotter import Plot


class PlotView():
    def __init__(self, userFiles=None):
        self._css = '''
        <style>         
            /*.container{
                width: 95%
            }*/
            .widget-radio-box{
                display: inline-block;
            }
            
            .widget-radio-box > label{
                margin-left: 5%;
                width:25%;
            }
            
            .widget-text > label{
                font-weight: normal;
                font-size: 12px;
            }
            
            .widget-dropdown > label{
                font-weight: normal;
                font-size: 12px;
            }
            
            .space{
                text-align: left;
                font-size: 13px;
            }            
            .center{
                text-align: center;
                font-size: 17px;
            }
            </style>
        '''

        ### Internal Variables ###
        self._userFiles = userFiles
        # if self._userFiles != None:
        # display(HTML('''<style>.container{width: 98%;}</style>'''))
        self._files = _arquivos
        self._fullPath = _fullFiles
        self._refined = _refined

        ### Boxes Graph Creation ####
        self._plotMainBox = widgets.VBox()
        self._filesBox = widgets.VBox()
        self._axeType = widgets.HBox()
        self._lineStyle = widgets.HBox()
        self._drop = widgets.Dropdown(options=['-', '--', 'v', '^', '<', '>', '*', 'o', '+'], value='-', description='Line Type 1:', style={"description_width": "initial"}, disabled=False,
                                layout=Layout(align_self="flex-start")).add_class('space')
        self._drop2 = widgets.Dropdown(options=['-', '--', 'v', '^', '<', '>', '*', 'o', '+'], value='-', description='Line Type 2:', style={"description_width": "initial"},
                                 disabled=False, layout=Layout(align_self="flex-end")).add_class('space')

        ### Input Text Creation ####
        self._xLabel = widgets.Text(description="X Label").add_class('space').remove_class('widget-label')
        self._yLabel = widgets.Text(description="Y Label").add_class('space').remove_class('widget-label')
        self._x2Label = widgets.Text(description="Second X Axe Label", layout=Layout(width="90%", align_self="flex-end"), style={"description_width": "initial"}).add_class('space').remove_class(
            'widget-label')
        self._y2Label = widgets.Text(description="Second Y Axe Label", layout=Layout(width="90%", align_self="flex-end"), style={"description_width": "initial"}).add_class('space')
        self._loc = widgets.Text(description="LOC Number: ", placeholder="Default: loc=2", style={"description_width": "initial"}, layout=Layout(align_self="flex-start")).add_class('space')
        self._col = widgets.Text(description="COL Number: ", placeholder="Default: ncol=3", style={"description_width": "initial"}, layout=Layout(align_self="flex-end")).add_class('space')
        self._graphLabel = widgets.Text(description="Graph Labels: ", placeholder="Input the labels like this: label1, label2, label3, ...",  style={"description_width": "initial"},
                                        layout=Layout(align_self="flex-start", width="98.5%", margin_left="5%")).add_class('space')

        self._axes = None
        self._propsList = list()
        self._filtersList = list()
        self._filesToPlot = list()

        self._plotter()

    #############################################################################################################################################
    ##### Métodos para a plotagem dos gráficos #####
    #############################################################################################################################################

    def _labelCharacteristic(self):
        return widgets.Label(value="Choose Graph Characteristics", layout=widgets.Layout(width="95%")).add_class('center')

    def _labelProperties(self):
        return widgets.Label(value="Choose Graph Properties", layout=widgets.Layout(width="95%")).add_class('space')

    def changed(self, n):
        if n.owner.index == 0:
            self._y2Label.layout.visibility = 'hidden'
            self._x2Label.layout.visibility = 'hidden'
            self._drop2.layout.visibility = 'hidden'
        elif n.owner.index == 1:
            self._y2Label.layout.visibility = 'hidden'
            self._x2Label.layout.visibility = 'visible'
            self._drop2.layout.visibility = 'visible'
            self._axes = 'twinx'
        else:
            self._y2Label.layout.visibility = 'visible'
            self._x2Label.layout.visibility = 'hidden'
            self._drop2.layout.visibility = 'visible'
            self._axes = 'twiny'

    def _radioGraphStyle(self):
        label = widgets.Label(value="Axe Type", layout=Layout(width="95%")).add_class('space')
        rad = widgets.RadioButtons(options=['Single Axe X/Y', 'Double X Axe (twinx)', 'Double Y Axe (twiny)'], value='Single Axe X/Y',
                                   disabled=False, layout=Layout(width="98%", justify_content="space-between", align_self="center"))
        rad.observe(self.changed, names="value")
        self._y2Label.layout.visibility = 'hidden'
        self._x2Label.layout.visibility = 'hidden'
        return widgets.VBox([label, rad], layout=Layout(width="99%", justify_content="space-between", align_items="flex-start"))

    def _chooseLineType(self):
        lineTypeLabel = widgets.Label(value="Choose Line Types", layout=Layout(width="99%")).add_class('space')
        self._drop2.layout.visibility = 'hidden'
        hbox = widgets.HBox(children=[self._drop, self._drop2], layout=Layout(align_self="flex-start", width="100%", justify_content="space-between"))
        return widgets.VBox(children=[lineTypeLabel, hbox], layout=Layout(align_self="flex-start", width="100%", justify_content="space-between"))

    def _numberLocCol(self):
        locLabel = widgets.Label(value="Loc-Col Numbers", layout=Layout(width="99%")).add_class('space')
        hBox = widgets.HBox(children=[self._loc, self._col], layout=Layout(align_self="flex-start", width="100%", justify_content="space-between"))
        return widgets.VBox(children=[locLabel, hBox], layout=Layout(align_self="flex-start", width="100%", justify_content="space-between"))

    def _inputLabels(self):
        labelInputs = widgets.Label(value="Axe Label Names", layout=Layout(width="99%")).add_class('space')
        singleAxe = widgets.VBox([self._xLabel, self._yLabel], layout=Layout(width="40%"))
        multiAxeBox = widgets.VBox([self._x2Label, self._y2Label], layout=Layout(width="60%"))
        container = widgets.HBox(children=[singleAxe, multiAxeBox], layout=Layout(width="100%", justify_content="space-between"))
        return widgets.VBox(children=[labelInputs, container, self._chooseLineType(), self._numberLocCol()], layout=Layout(width="99%", justify_content="space-between", align_items="center"))

    def _filterGraphButton(self, fileName):
        b = widgets.Button(description="Filter", button_style="primary", style={"button_color": "#6c757d"}, tooltip="Choose Graph Filters",
                           icon="fa-filter", display="flex-shrink")
        b._model_name = str(fileName)
        b.on_click(self._chooseFilter)
        return b

    def _plotButton(self):
        p = widgets.Button(description="Plot!", button_style="success", tooltip="Plot the graph", icon="fa-cogs", style={"button_color": "#009850"}, display="flex-shrink", layout=Layout(align_self="flex-end"))
        p.on_click(self._runPlotter)
        return p

    def _runPlotter(self, b):
        xLabel = self._xLabel.value
        yLabel = self._yLabel.value
        loc = self._loc.value
        ncol = self._col.value
        lineTypeOne = self._drop.value
        lineTypeTwo = None
        x2Label = None
        y2Label = None

        if self._axes == 'twinx':
            x2Label = self._x2Label.value
            lineTypeTwo = self._drop2.value
        elif self._axes == 'twiny':
            y2Label = self._y2Label.value
            lineTypeTwo = self._drop2.value

        graphLabel = self._graphLabel.value.split(",")
        prop = list()
        for i in xrange(1, len(self._propsList)):
            k = izip(self._propsList[::2], self._propsList[i::2])
            prop.append(k.next())

        Plot(files=self._filesToPlot, filters=self._filtersList, properties=prop, labelX=xLabel, labelY=yLabel, graphLabel=graphLabel, lineStyleOne=lineTypeOne, loc=loc,
             ncol=ncol,
             lineStyleTwo=lineTypeTwo, label2X=x2Label, label2Y=y2Label, axeType=self._axes)

    def _changeProperty(self, x):
        item = x.owner.style.description_width
        print item
        name = x.owner.style._model_name
        file = self._fullPath[name]
        if x.new:
            if not item in self._propsList:
                self._propsList.append(item)
            if not file in self._filesToPlot:
                self._filesToPlot.append(file)
        elif not x.new:
            self._propsList.remove(item)
            self._filesToPlot.remove(file)


    def _changeFilter(self, x):
        item = ast.literal_eval(x.owner.style.description_width)
        if x.new:
            if not item in self._filtersList:
                self._filtersList.append(item)
        else:
            self._filtersList.remove(item)

    def _cbProperties(self, file):
        options = list()
        options.append(widgets.Label(value='message'))
        p = MontaTree()
        fileName = file
        breadcrumb = list()
        breadcrumb.append('message')

        def _sortList(d, list):
            listLength = len(list) - 1
            i = 0
            while (True):
                firstKey = list[i]
                lastKey = list[listLength]
                if i == listLength or i > listLength:
                    break
                if isinstance(d[firstKey], dict):
                    if not isinstance(d[lastKey], dict):
                        aux = list[i]
                        list[i] = list[listLength]
                        list[listLength] = aux
                        i += 1
                        listLength -= 1
                    else:
                        listLength -= 1
                else:
                    i += 1
            return list

        def _createPropertyCheckBox(d, path=[]):
            isDictionary = {}
            keys = _sortList(d, d.keys())
            for k in keys:
                if isinstance(d[k], dict):
                    isDictionary = isDictionary.setdefault(k, d[k])
                    x = '.' + str(k)
                    if x == '.perLabel' and breadcrumb[-1] != '.values':
                        breadcrumb.pop(-1)
                    if (x == '.macro' or x == '.micro') and breadcrumb[-1] != '.values':
                        del(breadcrumb[2:])
                    breadcrumb.append(x)
                    if isinstance(options[-1], widgets.Label):
                        options.pop(-1)
                    options.append(widgets.Label(value=str(''.join(breadcrumb))))
                    if breadcrumb[-2] == '.perLabel':
                        breadcrumb.pop(-1)
                    _createPropertyCheckBox(isDictionary, path + [k])
                else:
                    option = widgets.Checkbox(description=k, encoding="ascii", width="100%", display='flex', indent=False)
                    option.style.description_width = ''.join(breadcrumb)+'.'+str(k)
                    option.style._model_name = fileName
                    option.observe(self._changeProperty, names="value")
                    options.append(option)

        for j in self._refined[file]['message']:
            if isinstance(j, unicode) and ":" in j:
                k = j.split(":")
                j = str("{'" + k[0] + "'" + ":'" + k[1] + "'}")
            if not isinstance(j, unicode):
                p.fillNumProperties(ast.literal_eval(j))
        props = p.dict
        _createPropertyCheckBox(props['message'])
        box = widgets.VBox(children=[i for i in options])
        return box

    def _cbFilters(self, file):
        options = list()
        f = MontaTree()
        for j in self._refined[file]['message']:
            if isinstance(j, unicode) and ":" in j:
                k = j.split(":")
                j = str("{'" + k[0] + "'" + ":'" + k[1] + "'}")
            if not isinstance(j, unicode):
                f.fillFiltProperties(ast.literal_eval(j))
        filters = f.filtDict
        for k,v in filters['message'].iteritems():
            options.append(widgets.Label(value='message.'+k))
            for val in v:
                cb = widgets.Checkbox(description=str(val), encoding="ascii", width="100%", display='flex', indent=False,
                                      style={"description_width": '("message.'+str(k)+'", "'+str(val)+'")'})
                cb.observe(self._changeFilter, names='value')
                options.append(cb)
        box = widgets.VBox(children=[i for i in options])
        return box

    def nestTable(self, file):
        table = widgets.Tab()
        table.set_title(0, 'Filters')
        table.set_title(1, 'Properties')
        table.children = [self._cbFilters(file), self._cbProperties(file)]
        return table

    def _createAccordion(self):
        if self._userFiles:
            arq = self._userFiles
        else:
            arq = self._files
        box = list()
        for v in arq.values():
            accordion = widgets.Accordion(children=[self.nestTable(v)])
            accordion.set_title(0, v)
            box.append(accordion)
        self._filesBox.children = [i for i in box]
        return (self._filesBox)

    def _graphLabels(self):
        return self._graphLabel;

    def _plotter(self):
        self._plotMainBox.children = [widgets.Label(value="Plotting Module", layout=widgets.Layout(width="98%")).add_class("center"),
                                      self._labelProperties(), self._createAccordion(), self._labelCharacteristic(),
                                      self._radioGraphStyle(), self._inputLabels(), self._graphLabels(), self._plotButton()]
        # self._labelProperties(), self._filePlotBox(), self._labelCharacteristic(),
        # self._radioGraphStyle()]
        display(HTML(self._css))
        display(self._plotMainBox)