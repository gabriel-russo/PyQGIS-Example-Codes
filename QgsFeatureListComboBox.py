import sys
from PyQt5.QtWidgets import QWidget, QApplication
from qgis.core import QgsVectorLayerCache, QgsExpression
from qgis.gui import (QgsFeatureListComboBox)
from qgis.utils import iface

def layer_change(): # Set to selected layer
    layer = iface.activeLayer()
    cbox_features.setSourceLayer(layer)

def print_selected():
    layer = iface.activeLayer()
    print(cbox_features.displayExpression())
    print(cbox_features.currentText())
    # Work in Progress: Get Feature using QgsFeatureRequest
    # column_name = cbox_features.displayExpression()
    # row_value = cbox_features.currentText()
    # expr = QgsExpression(f"{column_name}={row_value}")
    # it = layer.getFeatures(QgsFeatureRequest(expr))
    # print([i.id() for i in it])

selected_layer = iface.activeLayer()

new_dialog = QWidget()
new_dialog.resize(300,500)

# Creating and initial configurations
cbox_features = QgsFeatureListComboBox(new_dialog) # Create Widget
cbox_features.setSourceLayer(selected_layer) # Set to selected layer
cbox_features.setMinimumWidth(250)
cbox_features.setAllowNull(False)

# On change Events
iface.layerTreeView().currentLayerChanged.connect(layer_change) # If change selected layer
cbox_features.identifierValueChanged.connect(print_selected)


new_dialog.show()
