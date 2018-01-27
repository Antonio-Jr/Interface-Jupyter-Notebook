# -*- coding: utf-8 -*-
import codecs
import os, json, ast
import string, itertools

class FindFiles:
    def __init__(self, caminho):
        self.caminho = caminho

    def montaJson(self):
        arquivos_log = []
        files = dict()
        j = 0
        caminhoAbsoluto = os.path.abspath(self.caminho)
        for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
            arquivos_log.extend([os.path.join(pastaAtual, arquivo) for arquivo in arquivos if arquivo.endswith('.log')])

        for i in arquivos_log:
            files[j] = {}
            files[j]['file'] = i
            files[j]['config'] = {}
            files[j]['content'] = []
            with codecs.open(i, "rb") as log:
                for line in log:
                    try:
                        data = json.loads(line.encode("ascii", "replace"))
                        if "T(" in data['message']:
                            stringJson = data['message'][2:-1]
                            splitString = stringJson.split("=")
                            lista = list()

                            for row in splitString:
                                row = row.encode("ascii", "replace").replace("u'", "").replace("'", "")
                                if row[0] == '[':
                                    endKey = string.find(row, "]")
                                    lista.append(row[:endKey+1])
                                    lista.append(row[endKey+2:].replace(" ", ""))
                                else:
                                    row = row.replace(" ", "")
                                    lista.extend(row.split(","))

                            newDict = dict(itertools.izip_longest(*[iter(lista)] * 2))
                            data['message'] = newDict

                        if not files[j]['config']:

                            for k, v in data['message'].iteritems():
                                if type(v) != bool:
                                    try:
                                        value = ast.literal_eval(v)
                                        files[j]['config'][k] = value
                                    except Exception:
                                        files[j]['config'][k] = v
                                else:
                                    files[j]['config'][k] = v

                        else:
                            files[j]['content'].append(data)

                    except BaseException:
                        pass
            j += 1
        return files

class RefineJson:
    def __init__(self, file):
        self.dicionario = file

    def build(self):
        self.refinado = dict()
        self.refinado['unique'] = dict()
        self.refinado['multiple'] = dict()

        for i in self.dicionario:
            for k, v in self.dicionario[i]['config'].iteritems():
                if not k in self.refinado['unique'] and not k in self.refinado['multiple']:
                    self.refinado['unique'][k] = v

                elif (k in self.refinado['unique'] and not k in self.refinado['multiple']) and self.refinado['unique'][k] != v:
                    self.refinado['multiple'][k] = list()
                    self.refinado['multiple'][k].append(self.refinado['unique'][k])
                    self.refinado['multiple'][k].append(v)
                    self.refinado['multiple'][k].sort()
                    del self.refinado['unique'][k]

                elif k in self.refinado['multiple'] and not v in self.refinado['multiple'][k]:
                    self.refinado['multiple'][k].append(v)
                    self.refinado['multiple'][k].sort()

        return self.refinado

class ApplyFilters:
    def __init__(self, filters, files):
        self.filter = filters
        self.files = files

    def make(self):
        response = dict()

        for i in self.files:
            for j in self.filter:
                if j in self.files[i]['config']:
                    try:
                        for v in self.filter[j]:
                            if cmp(v, ast.literal_eval(self.files[i]['config'][j])) == 0:
                                if not j in response:
                                    response[j] = list()
                                response[j].append(self.files[i]['file'])
                    except:
                        pass
        return response

info = raw_input("Insira o nome da pasta que deseja abrir os logs: \n")
ff = FindFiles(info)
retorno = ff.montaJson()
# print (retorno)
rj = RefineJson(retorno)
t = rj.build()
print json.dumps(t, indent=4)
# j = ApplyFilters(teste, retorno)
# j.make()