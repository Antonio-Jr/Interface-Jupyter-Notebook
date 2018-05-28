import numpy as np
import matplotlib.pyplot as plt
from analysis.plot import readSequence

class Plot:
    def __init__(self, files, filters, properties, labelX, labelY, graphLabel, lineStyleOne, loc=2, ncol=3, lineStyleTwo=None, label2X=None, label2Y=None, axeType=None):
        self.files = files
        self.filters = filters
        self.properties = properties
        self.labelX = labelX
        self.labelY = labelY
        self.graphLabel = graphLabel
        self.lineStyleOne = lineStyleOne
        self.loc = loc
        self.ncol = ncol
        self.lineStyleTwo = lineStyleTwo
        self.label2X = label2X
        self.label2Y = label2Y
        self.axeType = axeType
        self.plotting()

    def plotting(self):
        global ax2
        ax2 = None
        fig, ax1 = plt.subplots(figsize=(16, 9))
        if self.axeType == 'twinx':
            ax2 = ax1.twinx()
            ax2.set_ylabel(self.label2X)
        elif self.axeType == 'twiny':
            ax2 = ax1.twiny()
            ax2.set_xlabel(self.label2Y)
        plots = []

        i = 0
        for filed in self.files:
            j = 0
            for (filt, prop) in zip(self.filters, self.properties):
                var = np.asarray(readSequence(filename=filed, filter=filt, properties=prop))

                if ax2 is not None:
                    if j % 2 == 1:
                        plots.append(ax1.plot(var[:, 0], var[:, 1], self.lineStyleOne, label=self.graphLabel[i]))
                    else:
                        plots.append(ax2.plot(var[:, 0], var[:, 1], self.lineStyleTwo, label=self.graphLabel[i]))
                else:
                    plots.append(ax1.plot(var[:, 0], var[:, 1], self.lineStyleOne, label=self.graphLabel[i]))
                j += 1
            i += 1

        ax1.set_xlabel(self.labelX)
        ax1.set_ylabel(self.labelY)

        # Show
        plt.legend(bbox_to_anchor=(-0., 1.02, 1., .102), loc='center', ncol=self.ncol, mode="expand", borderaxespad=0.)
        plt.show(i for i in plots)

# path = "/home/junior/PycharmProjects/lia-pln-notebooks/shortdoc_class/log/tokenized/"
# pt = Plot(
#         files=['/home/junior/PycharmProjects/lia-pln-notebooks/shortdoc_class/log/tokenized/lr0.1_100epochs.txt'],
#         #files=[path+"log.not2.wnn-lr0.1-numepochs50.txt", path+"log.not2.wnn-lr0.01-numepochs50.txt", path+"log.not2.wnn-lr0.001-numepochs50.txt"],
#          filters=[('message.name', 'TrainLoss'), ('message.name', 'EvalAccuracy')],
#          properties=[('message.epoch', 'message.values.loss'), ('message.epoch', 'message.values.accuracy')],
#          labelX="EvalLoss",
#          labelY="EvalFMetric",
#          label2X='Accuracy',
#          lineStyleOne="-",
#          lineStyleTwo='--',
#          axeType='twinx',
#          graphLabel=['EvalLoss', 'EvalFMetric'])
         # label=["lr 0.1", "lr 0.01", "lr 0.001"])
# pt.plotting()

