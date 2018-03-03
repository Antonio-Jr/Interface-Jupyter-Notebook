# -*- coding: utf-8 -*-

class MontaTree:

    def __init__(self):
        self.numProperties = {}
        self.dict = {'message': self.numProperties}

    def _addPath(self, path):
        d = self.numProperties
        for p in path[:-1]:
            d = d.setdefault(p, {})
        numProp = path[-1]
        d.setdefault(numProp, None)

    def fillNumProperties(self, d, path=[]):
        if isinstance(d, dict):
            for key, val in d.items():
                self.fillNumProperties(val, path + [key])
        elif isinstance(d, (float, int)):
            self._addPath(path)
