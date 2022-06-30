from PyQt5.QtWidgets import QWidget
from qgis.core import QgsExpression, QgsFeatureRequest, QgsWkbTypes
from qgis.gui import QgsFeaturePickerWidget
from qgis.utils import iface

def layer_changed():
    picker_features.setLayer(iface.activeLayer())

def feature_details():
    feat = picker_features.feature()
    print(f'My id is: {feat.id()}')
    print(f'My attributes is {feat.attributes()}')
    print(f'My geometry type is {QgsWkbTypes.displayString(feat.geometry().wkbType())}')

# Creating main window
new_dialog = QWidget()
new_dialog.resize(300,400)

# Creating and initial configurations
picker_features = QgsFeaturePickerWidget(new_dialog) # Create Widget
picker_features.setMinimumWidth(250)
picker_features.setLayer(iface.activeLayer()) # Initial layer

# Creating change layer event
iface.layerTreeView().currentLayerChanged.connect(layer_changed)

# Creating change feature event
picker_features.featureChanged.connect(feature_details)

new_dialog.show()
