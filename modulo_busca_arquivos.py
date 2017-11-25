# *--coding utf-8--*
import os, json, ast, sys
import string


class FindFiles:
    def __init__(self, caminho):
        self.caminho = caminho

    def montaJson(self):
        arquivos_log = []
        files = dict()
        j = 0
        caminhoAbsoluto = os.path.abspath(self.caminho)
        for pastaAtual, subPastas, arquivos in os.walk(caminhoAbsoluto):
            arquivos_log.extend([os.path.join(pastaAtual, arquivo) for arquivo in arquivos if arquivo.endswith(
                '.log')])

        for i in arquivos_log:
            files[j] = {}
            files[j]['file'] = i
            files[j]['config'] = {}
            files[j]['content'] = []
            with open(i) as log:
                for line in log:
                    try:

                        data = json.loads(line, encoding="utf-8")
                        if "T(" in data['message']:
                            x = dict()
                            t = data['message'][2:-1].replace("=", ':').encoding('utf-8')
                            if 'lr' in t:
                                idxKey = t.index('lr')
                                endKey = string.find(t, ':', idxKey)
                                idxVal = string.find(t, ", ", endKey)
                                x[t[idxKey:endKey]]= t[endKey+1:idxVal]
                            if 'train' in t:
                                idxKey = t.index('train')
                                endKey = string.find(t, ':', idxKey)
                                idxVal = string.find(t, ", ", endKey)
                                x[t[idxKey:endKey]]= t[endKey+1:idxVal]
                            if 'dev' in t:
                                idxKey = t.index('dev')
                                endKey = string.find(t, ':', idxKey)
                                idxVal = string.find(t, ", ", endKey)
                                x[t[idxKey:endKey]]= t[endKey+1:idxVal]
                            if 'hidden_size' in t:
                                idxKey = t.index('hidden_size')
                                endKey = string.find(t, ':', idxKey)
                                idxVal = string.find(t, ", ", endKey)
                                x[t[idxKey:endKey]]= t[endKey+1:idxVal]
                            if 'decay' in t:
                                idxKey = t.index('decay')
                                endKey = string.find(t, ':', idxKey)
                                idxVal = string.find(t, ", ", endKey)
                                x[t[idxKey:endKey]]= t[endKey+1:idxVal]

                            del(data['message'])
                            data['message'] = x
                        if not files[j]['config']:
                            if 'train' in data['message']:
                                files[j]['config']['train'] = data['message']['train']

                            if 'dev' in data['message']:
                                files[j]['config']['dev'] = data['message']['dev']

                            if 'lr' in data['message']:
                                files[j]['config']['lr'] = data['message']['lr']

                            if 'hidden_size' in data['message']:
                                files[j]['config']['hidden_size'] = data['message']['hidden_size']

                            if 'decay' in data['message']:
                                files[j]['config']['decay'] = data['message']['decay']
                        else:
                            files[j]['content'].append(data)

                    except BaseException as error:
                        pass
                        # print ('Ocorreu um erro ao manipular o arquivo %s.\n {}').format(error) %i
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


            if 'lr' in self.dicionario[i]['config']:
                if not 'lr' in self.refinado['unique'] and not 'lr' in self.refinado['multiple']:
                    self.refinado['unique']['lr'] = self.dicionario[i]['config']['lr']

                elif ('lr' in self.refinado['unique'] and not 'lr' in self.refinado['multiple']) and self.refinado['unique']['lr'] != self.dicionario[i]['config']['lr']:
                    self.refinado['multiple']['lr'] = list()
                    self.refinado['multiple']['lr'].append(self.refinado['unique']['lr'])
                    del self.refinado['unique']['lr']

                elif 'lr' in self.refinado['multiple']:
                    self.refinado['multiple']['lr'].append(self.dicionario[i]['config']['lr'])

            if 'hidden_size' in self.dicionario[i]['config']:
                if not 'hidden_size' in self.refinado['unique'] and not 'hidden_size' in self.refinado['multiple']:
                    self.refinado['unique']['hidden_size'] = self.dicionario[i]['config']['hidden_size']

                elif 'hidden_size' in self.refinado['unique'] and self.refinado['unique']['hidden_size'] != self.dicionario[i]['config']['hidden_size']:
                    self.refinado['multiple']['hidden_size'] = list()
                    self.refinado['multiple']['hidden_size'].append(self.refinado['unique']['hidden_size'])
                    del self.refinado['unique']['hidden_size']

                elif 'hidden_size' in self.refinado['multiple']:
                    self.refinado['multiple']['hidden_size'].append(self.dicionario[i]['config']['hidden_size'])

            if 'train' in self.dicionario[i]['config']:
                if not 'train' in self.refinado['unique'] and not 'train' in self.refinado['multiple']:
                    self.refinado['unique']['train'] = self.dicionario[i]['config']['train']

                elif 'train' in self.refinado['unique'] and self.dicionario[i]['config']['train'] != self.refinado['unique']['train']:
                    self.refinado['multiple']['train'] = list()
                    self.refinado['multiple']['train'].append(self.refinado['unique']['train'])
                    del self.refinado['unique']['train']

                elif 'train' in self.refinado['multiple']:
                    self.refinado['multiple']['train'].append(self.dicionario[i]['config']['train'])

            if 'dev' in self.dicionario[i]['config']:
                if not 'dev' in self.refinado['unique'] and not 'dev' in self.refinado['multiple']:
                    self.refinado['unique']['dev'] = self.dicionario[i]['config']['dev']

                elif 'dev' in self.refinado['unique'] and self.refinado['unique']['dev'] != self.dicionario[i]['config']['dev']:
                    self.refinado['multiple']['dev'] = list()
                    self.refinado['multiple']['dev'].append(self.refinado['unique']['dev'])
                    del self.refinado['unique']['dev']

                elif 'dev' in self.refinado['multiple']:
                    self.refinado['multiple']['dev'].append(self.dicionario[i]['config']['dev'])

            if 'decay' in self.dicionario[i]['config']:
                if not 'decay' in self.refinado['unique'] and not 'decay' in self.refinado['multiple']:
                    self.refinado['unique']['decay'] = self.dicionario[i]['config']['decay']

                elif 'decay' in self.refinado['unique'] and self.refinado['unique']['decay'] != self.dicionario[i]['config']['decay']:
                    self.refinado['multiple']['decay'] = list()
                    self.refinado['multiple']['decay'].append(self.refinado['unique']['decay'])
                    del self.refinado['unique']['decay']

                elif 'decay' in self.refinado['multiple']:
                    self.refinado['multiple']['decay'].append(self.dicionario[i]['config']['decay'])

        key = self.refinado['multiple'].keys()
        for i in key:
            conj = set(self.refinado['multiple'][i])
            lista = list(conj)
            del self.refinado['multiple'][i]
            self.refinado['multiple'][i] = sorted(lista)
        return self.refinado


    def montaToggleButtons(self):
        listLr = []
        if 'lr' in self.refinado['multiple']:
            for v in self.refinado['multiple']['lr']:
                listLr.append(v)
        return listLr

class applyFilters:
    def __init__(self, filters, files):
        self.filter = filters
        self.files = files
        response = dict()
        try:
            for i in self.files:
                for j in self.filter:
                    for k in self.filter[j]:
                        if cmp(k,str(self.files[i]['config'][j])) == 0:
                            if not i in response:
                                response[j] = list()
                            print(i);
                            response[j].append(self.files[i]['file'])
        except:
            pass
        print (response)



info = raw_input("Insira o nome da pasta que deseja abrir os logs: \n")
ff = FindFiles(info)
retorno = ff.montaJson()
# print (retorno)
rf = RefineJson(retorno)
t = rf.build()
b = rf.montaToggleButtons()
# print b