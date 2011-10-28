from xml.dom import minidom
import math
from svgenesis.core import *
from svgenesis.primitives import Polygon
from svgenesis.namespace import SVGENESIS_TYPE


class EquilateralPolygon(Polygon):
    """
    Defines a convex Polygon of N equal-length sides.
    """
    @staticmethod
    def xml_parse_handler(xml_elem):
        return Polygon.xml_parse_handler(xml_elem)

    def __init__(self, cx=0.0, cy=0.0, sides=10, side_length=10, 
                 rotation=0.0, stroke_width=3, 
                 stroke_opacity=1.0, opacity=1.0, stroke=rgb(0,0,0), 
                 fill=rgb(255, 255, 255)):
        points = []
        for pt in xrange(sides):
            # Find the angle as the fraction of the circle that
            # defines the outer points of the polygon.
            angle = rotation + (2.0*math.pi/sides)*pt
            # Standard trig-operations to find x and y of the point at
            # that angle.
            x = cx + side_length * math.cos(angle)
            y = cy + side_length * math.sin(angle)
            points.append((x,y))
        Polygon.__init__(self, points=points, stroke_width=stroke_width,
                         stroke_opacity=stroke_opacity, stroke=stroke,
                         fill=fill)


    def to_node(self):
        node = Polygon.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'EquilateralPolygon')
        return node


