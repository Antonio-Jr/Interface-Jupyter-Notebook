# -*- coding: utf-8 -*-

class MontaTree:

    def __init__(self):
        self.numProperties = {}
        self.filtProperties = {}
        self.dict = {'message': self.numProperties}
        self.filtDict = {'message': self.filtProperties}

    def _addPath(self, path, val):
        d = self.numProperties
        for p in path[:-1]:
            d = d.setdefault(p, {})
        numProp = path[-1]
        d.setdefault(numProp, val)

    def _addFiltPath(self, path, val):
        d = self.filtProperties
        for p in path[:-1]:
            d = d.setdefault(p, {})
        namProp = path[-1]
        if not str(namProp[0]).isupper():
            d.setdefault(namProp, set())
            d[namProp].add(val)

    def fillNumProperties(self, d, path=[]):
        if isinstance(d, dict):
            for key, val in d.items():
                self.fillNumProperties(val, path + [key])
        elif isinstance(d, (float, int)):
            self._addPath(path, d)

    def fillFiltProperties(self, d, path=[]):
        if isinstance(d, dict):
            for key, val in d.items():
                self.fillFiltProperties(val, path + [key])
        else:
            try:
                j = ast.literal_eval(d)
            except Exception:
                j = d
            if isinstance(j, (unicode, str)):
                self._addFiltPath(path, j)