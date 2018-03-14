import numpy as np
import matplotlib.pyplot as plt
from analysis.plot import readSequence

class Plot:
    def __init__(self, files, filters, properties, labelX, labelY, legend=None):
        self.files = files
        self.filters = filters
        self.properties = properties
        self.labelX = labelX
        self.labelY = labelY
        self.legend = legend
        self.plotting()
    def plotting(self):
        for file in self.files:
            data = np.asarray(readSequence(filename=file,
                                          filter=(self.filters),
                                          properties=(self.properties)
                                           )
                              )
            fig, ax1 = plt.subplots()
            ax2 = ax1.twinx()
            ax2.plot(data[:, 0], data[:, 1], label=self.labelX)
        ax1.set_xlabel(self.labelX)
        ax1.set_ylabel(self.labelY)
        ax2.set_ylabel('Accuracy')

        plt.legend(bbox_to_anchor=(0.,1.02,1.,.102), loc=3, ncol=4, mode="expand", borderaxespad=0.)
        plt.show()


pt = Plot(files=["/home/antonio/Documentos/lia-pln-notebooks/shortdoc_class/distant_supervision/log/train"
                 "/henrico_cic_dilma.log"],
         filters=("message.name", "EvalFMetric"),
         properties=("message.epoch", "message.iteration", "message.values.macro.f", "message.values.micro.f"),
         labelX="Epoch",
         labelY="Loss")
# pt.plotting()

