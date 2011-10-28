from svgenesis.core import *
from abstractgeometry import AbstractGeometry

class Text(AbstractGeometry):
    """
    
    """

    SVG_TAG_NAME = 'text'

    def __init__(self, text="Text", x=0, y=0, font_size=40, fill='black', rotation=(0,0,0)):
        AbstractGeometry.__init__(self, x=x, y=y) 
        self.text = text
        self.fill = fill
        self.font_size = font_size
        self.rotation = rotation
        self.attribute_filter = [ 'x', 'y', 'text', 'fill', 
                                  'font_size', 'rotation'] 


    def to_node(self):
        node = AbstractGeometry.to_node(self)
        text_node = minidom.Document().createTextNode(self.text)
        node.appendChild(text_node)
        return node


