from ipywidgets import Layout

class Layouts:

    def box_layout(self):
        return Layout(width="100%", display="flex", flex_direction="column", border="2px groove grey", align_items='stretch')

    def vBox_layout(self):
        return Layout(width="50%", align_content="flex-start", display="flex")

    def left_layout(self):
        return Layout(width="50%", flex_flow="column", display="flex", align_items="flex-start",align_self="center")

    def right_layout(self):
        return Layout(width="99%", flex_flow="row", justify_content="space-between", display="flex", align_items="flex-end", align_self="center")

    def main_layout(self):
        return Layout(width="90%", top="1%", align_self="center", display="justify-content")

    def selectMultiple_layout(self):
        return Layout(width='99%', flex_flow='column', display="flex", align_items='inherit')

    def staticBox_layout(self):
        return Layout(width="95%", flex_flow="column", display="inline-flex", align_self="center")

    def multipleBox_layout(self):
        return Layout(width="90%", flex_direction="column", display="flex")

    def collapseButton(self):
        return Layout(width="30px", align_self="flex-end", display="flex-wrap")

    def accordionChildren_layout(self):
        return Layout(width="40%")

    def toggleFilter_layout(self):
        return Layout(align_self="center", display="flex-wrap")

    def toggleCell_layout(self):
        return Layout(width="149px", align_self="center", display="flex-shrink")

    def filterBtn_layout(self):
        return Layout(align_self="flex-end", display="flex-wrap")

    def uniqueCollapse_layout(self):
        return Layout(width="100%", align_self="flex-start")

    def leftBox_layout(self):
        return Layout(width="100%", align_self="center")

    def labelCaracteristicasMultiplas_layout(self):
        return Layout(width="91%", align_self="flex-start", left="2%")

    def labelFilterMultiple_layout(self):
        return Layout(width="95%", align_self="center")

    def applyChooseButton_layout(self):
        return Layout(align_self="flex-end", display="flex-end")

    def notUnicos_layout(self):
        return Layout(width="95%", align_self="center")

    def boxMultipleFilter_layout(self):
        return Layout(width="100%", flex_flow="column", display="inline-flex")