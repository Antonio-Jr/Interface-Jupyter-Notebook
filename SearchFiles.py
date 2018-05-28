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
        print(self.caminho)
        caminhoAbsoluto = os.path.abspath(self.caminho)
        for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
            arquivos_log.extend([os.path.join(pastaAtual, arquivo) for arquivo in arquivos if arquivo.endswith('.log')])

        for i in arquivos_log:
            files[j] = dict()
            files[j]['file'] = i
            files[j]['config'] = dict()
            files[j]['content'] = dict()
            with codecs.open(i, "rb") as log:
                for line in log:
                    try:
                        data = json.loads(line.encode("ascii"))
                        if "T(" in data['message']:
                            stringJson = data['message'][2:-1]
                            splitString = stringJson.split("=")
                            lista = list()

                            for row in splitString:
                                row = row.encode("ascii", "replace").replace("u'", "").replace("'", "")
                                if row[0] == '[':
                                    endKey = string.find(row, "]")
                                    lista.append(row[:endKey + 1])
                                    lista.append(row[endKey + 2:].replace(" ", ""))
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
                            for val in data.viewitems():
                                if not val[0] in files[j]['content']:
                                    files[j]['content'][val[0]] = set()
                                    if type(val[1]) is dict:
                                        conjunto = set(Hashabledict(val[1]))
                                        files[j]['content'][val[0]].update(conjunto)
                                    else:
                                        files[j]['content'][val[0]].add(val[1])
                                else:
                                    if type(val[1]) is dict:
                                        conjunto = str(val[1])
                                        files[j]['content'][val[0]].add(conjunto)
                                    else:
                                        files[j]['content'][val[0]].add(val[1])
                    except BaseException as error:
                        pass
            j += 1
        return files

class Hashabledict(dict):
    def __hash__(self):
        return hash(self)

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
            for k in self.filter.keys():
                k = k.encode("ascii", "replace")
                if k in self.files[i]['config']:
                    try:
                        for v in self.filter[k]:
                            v = v.encode("ascii", "replace")

                            try:
                                value = ast.literal_eval(v)
                            except Exception:
                                value = v

                            if value == self.files[i]['config'][k]:
                                if not k in response:
                                    response[k] = list()
                                response[k].append(self.files[i]['file'])
                    except Exception as error:
                        pass
        return response