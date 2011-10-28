import math
from svgenesis.core import *
from svgenesis.primitives import Polygon
from svgenesis.namespace import SVGENESIS_TYPE

class Star(Polygon):
    """
    Defines a equilateral concave polygon.
    """
    @staticmethod
    def xml_parse_handler(xml_elem):
        return EquilateralPolygon.xml_parse_handler(xml_elem)


    def __init__(self, cx=0.0, cy=0.0, ri=10, ro=20, num_points=4, 
                 rotation=(-math.pi/6.0), stroke_width=3, 
                 stroke_opacity=1.0, opacity=1.0, stroke=rgb(0,0,0), 
                 fill=rgb(255, 255, 255)):
        points = []
        
        # For each point of a Star there are 2 sides
        sides = 2 * num_points
        for pt in xrange(sides):
            # Calculate the angle and its respective cosine and sine
            # value for clairity.
            angle = rotation + (2.0*math.pi/sides)*pt
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            
            if pt % 2 == 0:
                # Calculate the inner point for even numbered points.
                x = cx + ri * cos_a
                y = cy + ri * sin_a
            else:
                # Calculate the outer point for odd numbered points.
                x = cx + ro * cos_a
                y = cy + ro * sin_a
            points.append((x,y))
        Polygon.__init__(self, points=points, stroke_width=stroke_width,
                         stroke_opacity=stroke_opacity, stroke=stroke,
                         fill=fill)

            
