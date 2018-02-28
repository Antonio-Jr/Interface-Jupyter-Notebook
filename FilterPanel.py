from Elements import Elements

elmt = Elements()
unicos = list()
multiplas = list()

class BuildFilterPanel:

    def __init__(self, jsonRefinado):
        self.json = jsonRefinado

    def BuildSingularFilters(self):
        global unicos
        uniKey = self.json['unique'].keys()
        for i in uniKey:
            key = str(i.encode("ascii", "replace"))
            value = str(self.json['unique'][i])
            value = value.encode("ascii", "replace")
            description = str(self.json['unique'][i])

            unicos.append(elmt.labelSingularFilter(key, value ,description))

        if len(unicos) == 0:
            unicos.append(elmt.notUnicos())

        return unicos

    def BuildMultipleFilters(self):
        from Events import Events
        evnt = Events()
        global multiplas
        multiplos = dict()
        multKey = self.json['multiple'].keys()
        for j in multKey:
            listaDeCheckBox = list()
            for k in self.json['multiple'][j]:
                option = elmt.checkBoxMultipleFilters(unicode(str(k)), str(j))
                option.observe(evnt.change, names='value')
                listaDeCheckBox.append(option)

            multiplos[j] = listaDeCheckBox


        for k, v in multiplos.iteritems():
            multiplas.append(elmt.labelMultipleFilter(str(k),str(k)))
            multiplas.append(elmt.boxMultipleFilters(v))