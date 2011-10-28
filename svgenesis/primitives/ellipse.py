from svgenesis.core import *
from abstractgeometry import AbstractGeometry

class Ellipse(AbstractGeometry):
    SVG_TAG_NAME = 'ellipse'
    
    def __init__(self, cx=0.0, cy=0.0, rx=0.0, ry=0.0, fill='black', 
                 stroke_width=1, stroke_opacity=1.0, opacity=1.0, stroke=rgb(255,255,255)):
        """
        :param cx: The ellipse center X-coord.
        :param cy: The ellipse center Y-coord.
        :param rx: The x axis radius of the ellipse.
        :param ry: The y axis radius of the ellipse.
        :param stroke_width: The width of the stroke of the perimeter of a shape.
        :param stroke_opacity: The opacity of the stroke-line.
        :param opacity: The opacity of the element in general.
        :param stroke: The color of the stroke-line.

        :type cx: int or float
        :type cy: int or float
        :param rx: int or float
        :param ry: int or float
        :type stroke_width: int of float
        :type stroke_opacity: float (0 <= num <= 1.0)
        :type opacity: float (0 <= num <= 1.0)
        :type stroke: rgb-tuple or hex-string
        """

        AbstractGeometry.__init__(self, x=cx, y=cy, stroke=stroke, opacity=opacity, 
                                  stroke_opacity=stroke_opacity, stroke_width=stroke_width)
        self.fill = fill
        self.rx = rx
        self.ry = ry
        self.cx = self.x
        self.cy = self.y

        self.attribute_filter = ['rx', 'ry', 'cx', 'cy', 'stroke', 'opacity',
                                 'fill', 'stroke_width', 'stroke_opacity']
