from svgenesis.core import *
from abstractgeometry import AbstractGeometry

class Line(AbstractGeometry):
    """
    Defines an SVG line with a start/end coords, color and a width.
    """

    SVG_TAG_NAME = 'line'
           
    def __init__(self, x1=0.0, y1=0.0, x2=0.0, y2=0.0, 
                 stroke=rgb(0,0,0), stroke_width=1, stroke_opacity=1.0):
        """
        :param x: The starting X-coord.
        :param y: The starting Y-coord.
        :param width: The width of the line.
        :param color: The color of the stroke-line.

        :type x: int or float
        :type y: int or float
        :type width: int of float
        :type color: rgb-tuple or hex-string
        """

        AbstractGeometry.__init__(self, x=x1, y=y1, 
                                  stroke_width=stroke_width, 
                                  stroke=stroke, stroke_opacity=stroke_opacity) 

        # Type and Value checking for the basic attributes.
        # x2 Coord value should be a float or an int, as is sensical.
        # If not a float or an int, a type coersion to float is
        # attempted if, for example, x2 is a string.  If type coersion
        # fails a TypeError is raised.
        if not type(x2) in (float, int):
            try: 
                x2 = float(x2)
            except ValueError:
                raise TypeError("x2 must be a int, or float")

        # y2 coord value should be a float or an int, as is
        # sensical. If not a float or an int, a type coersion to float
        # is attempted. A type coersion would happen if, for eyample,
        # y2 is a string.  If type coersion fails a TypeError is
        # raised.
        if not type(y2) in (float, int):
            try: 
                y2 = float(y2)
            except ValueError:
                raise TypeError("y2 must be a int, or float")

        self.x1 = self.x
        self.y1 = self.y
        self.x2 = x2
        self.y2 = y2
        self.stroke = stroke
        self.attribute_filter = [ 'x1', 'y1', 'x2', 'y2', 
                                  'stroke', 'stroke_width',
                                  'stroke_opacity'] 


