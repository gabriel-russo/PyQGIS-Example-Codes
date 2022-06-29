from PyQt5.QtWidgets import QWidget
from qgis.core import QgsExpression, QgsFeatureRequest
from qgis.gui import QgsFeatureListComboBox
from qgis.utils import iface

def layer_change(): # Set to selected layer
    layer = iface.activeLayer()
    cbox_features.setSourceLayer(layer)

def print_selected():
    layer = cbox_features.sourceLayer()
    print(f'Im Using this field to list features in combo box: {cbox_features.displayExpression()}')
    print(f'Selected feature name is {cbox_features.currentText()}')
    print('Now search me using QgsFeatureRequest') 
    find_me(layer, cbox_features.displayExpression(), cbox_features.currentText())

def find_me(layer, field_name, feature_value):
    selection = layer.getFeatures(QgsFeatureRequest(QgsExpression(f"{field_name} = '{feature_value}'")))
    for feat in selection:
        print(feat.attributes())

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
cbox_features.currentFeatureChanged.connect(print_selected) # If change selected feature

new_dialog.show()
