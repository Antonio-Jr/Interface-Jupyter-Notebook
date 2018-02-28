
from FilterPanel import BuildFilterPanel
from IPython.display import display, HTML
from modulo_busca_arquivos import refinado

css = """
<style> 
.container{
        width: 98%;
    }

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
        text-align: center;
        }

.widget-checkbox {
        width: 95%;
    }

.space{
    text-align: left;
    font-size: 13px;
    }

.vazio{
    color: red;
    font-size: 12px;
    text-align: left;
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
</style>"""


# info = raw_input("Insira o nome da pasta que deseja abrir os logs: \n")
# ff = FindFiles(info)
# retorno = ff.montaJson()
# rj = RefineJson(retorno)
# json = rj.build()

bfp = BuildFilterPanel(jsonRefinado=refinado)
unique = bfp.BuildSingularFilters()
multiple = bfp.BuildMultipleFilters()

from Elements import Elements
elm = Elements()
display(elm.parentBox())
display(HTML(css))







