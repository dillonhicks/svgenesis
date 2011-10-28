from svgenesis.core import *
from svgenesis.primitives import Polygon
from svgenesis.namespace import SVGENESIS_TYPE

class Triangle(Polygon):
    """
    Represents a triangle by its three vertexes.
    """
    @staticmethod
    def xml_parse_handler(xml_elem):
        return Polygon.xml_parse_handler(xml_elem)

    def __init__(self, points=((0,0), (0,0), (0,0)), stroke_width=3, 
                 stroke_opacity=1.0, opacity=1.0, stroke=rgb(0,0,0), 
                 fill=rgb(255, 255, 255)):
        Polygon.__init__(self, points=points, stroke_width=stroke_width,
                         stroke_opacity=stroke_opacity, stroke=stroke,
                         fill=fill)


    def to_node(self):
        node = Polygon.to_node(self)
        node.setAttribute(SVGENESIS_TYPE, 'Triangle')
        return node

