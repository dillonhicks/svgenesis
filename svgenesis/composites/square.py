from svgenesis.core import *
from svgenesis.primitives import Rectangle

class Square(Rectangle):
    
    def __init__(self, x=0, y=0, side_length=10, rx=0, ry=0, 
                 fill=rgb(0,0,0), opacity=1.0, stroke=rgb(0,0,0), stroke_width=1, 
                 stroke_opacity=1.0):
        """
        :param x: The center X-coord.
        :param y: The center Y-coord.
        :param rx: Corner rounding on the x axis.
        :param ry: Corner rounding on the y axis.
        :param stroke_width: The width of the stroke of the 
            perimeter of a shape.
        :param stroke_opacity: The opacity of the stroke-line.
        :param opacity: The opacity of the element in general.
        :param stroke: The color of the stroke-line.
        :type x: int or float
        :type y: int or float
        :type rx: float (0 <= num <= 1.0)
        :type ry: float (0 <= num <= 1.0)
        :type stroke_width: int of float
        :type stroke_opacity: float (0 <= num <= 1.0)
        :type opacity: float (0 <= num <= 1.0)
        :type stroke: rgb or hex-string
        """

        Rectangle.__init__(self, x=x, y=y, width=side_length, height=side_length, 
                           rx=rx, ry=ry, fill=fill, opacity=opacity, stroke=stroke, 
                           stroke_width=stroke_width, stroke_opacity=stroke_opacity)

    def to_node(self):
        node = Rectangle.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'Square')
        return node



