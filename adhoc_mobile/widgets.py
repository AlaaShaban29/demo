
from import_export import fields, resources, widgets

from import_export.widgets import ForeignKeyWidget

class CustomBooleanWidget(widgets.Widget):
    
    def __init__(self, active=None):
        self.active = active

        



