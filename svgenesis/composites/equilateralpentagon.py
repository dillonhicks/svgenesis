import math
from svgenesis.core import *
from svgenesis.namespace import SVGENESIS_TYPE
from svgenesis.primitives import Polygon
from equilateralpolygon import EquilateralPolygon


class EquilateralPentagon(EquilateralPolygon):
    """
    Pentagon with five equal sides centered at cx,cy.
    """

    @staticmethod
    def xml_parse_handler(xml_elem):
        return EquilateralPolygon.xml_parse_handler(xml_elem)

    def __init__(self, cx=0.0, cy=0.0, side_length=10, rotation=(-math.pi/6.0), 
                 stroke_width=3, stroke_opacity=1.0, opacity=1.0, stroke=rgb(0,0,0), 
                 fill=rgb(255, 255, 255)):

        EquilateralPolygon.__init__(self, cx=cx, cy=cy, sides=5, side_length=side_length, 
                                    rotation=rotation, stroke_width=stroke_width,
                                    stroke_opacity=stroke_opacity, stroke=stroke,
                                    fill=fill)


    def to_node(self):
        node = Polygon.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'EquilateralPentagon')
        return node
