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
        # if self.caminho == "":
        #     print(caminhoAbsoluto)
        for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
            arquivos_log.extend([os.path.join(pastaAtual, arquivo) for arquivo in arquivos if arquivo.endswith('.log')])

        for i in arquivos_log:
            # files = dict()
            files[j] = dict()
            files[j]['file'] = i
            files[j]['config'] = dict()
            files[j]['content'] = dict()
            files[j]['keys'] = dict()
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
                                        conjunto = set(hashabledict(val[1]))
                                        files[j]['content'][val[0]].update(conjunto)
                                    else:
                                        files[j]['content'][val[0]].add(val[1])
                                else:
                                    if type(val[1]) is dict:
                                        conjunto = str(val[1])
                                        files[j]['content'][val[0]].add(conjunto)
                                    else:
                                        files[j]['content'][val[0]].add(val[1])

                            # keys = set()
                            # values = set()
                            # for k, v in data.iteritems():
                            #     keys.add(k)
                            #     if type(v) == dict:
                            #         for p, q in v:
                            #             keys.add(p)
                            #             values.add(q)
                            #     values.add(v)

                            # files[j]['keys'].append(k.encode("ascii", "replace"))
                            # print files[j]['keys']
                            # if not files[j]['keys'][v]:
                            #     files[j]['keys'][k] = set()
                            # files[j]['keys'][k].add(v)
                            # print(files[j]['keys']);
                            # print(files[j]['keys'][k][v])

                    except BaseException as error:
                        pass
            j += 1

        # for i in filt:
        #     try:
        #         j = ast.literal_eval(i)
        #         print j
        #         print type(j)
        #     except:
        #         print(i)
        return files

class hashabledict(dict):
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


# teste = {'test': ['/data/ner/test_set_1.txt'], 'normFactor': ['0.1'], 'seed': ['31'], 'label_file': [
# '/home/eraldo/lia/src/lia-pln-datasets-models/ner/data/labels.txt', '/data/ner/labels.txt'], 'hidden_size': ['200']}

# teste = {'eval_per_iteration': ['100'], 'lr': ['0.005', '0.01']}

# teste = {u'test': [u'/data/ner/test_set_1.txt'], u'normFactor': [u'0.1'], u'seed': [u'31'], u'label_file': [
# u'/home/eraldo/lia/src/lia-pln-datasets-models/ner/data/labels.txt', u'/dpgs-data/ner/data/labels.txt'], u'hidden_size': [u'200']}

info = raw_input("Insira o nome da pasta que deseja abrir os logs: \n")
ff = FindFiles(info)
retorno = ff.montaJson()
rj = RefineJson(retorno)
refinado = rj.build()

# print retorno[0]['file']
# print set(retorno[0]['config'])
# print len(set(retorno[0]['config'])),"\n\n"
#
# print set(t['multiple'])
# print len(set(t['multiple'])),"\n\n"
#
# j = set(t['multiple']) & set(retorno[0]['config'])
# print j
# print json.dumps(t, indent=4)
# j = ApplyFilters(teste, retorno)
# print(j.make())


