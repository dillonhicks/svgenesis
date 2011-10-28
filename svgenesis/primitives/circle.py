from svgenesis.core import *
from abstractgeometry import AbstractGeometry

class Circle(AbstractGeometry):

    SVG_TAG_NAME = 'circle'

    def __init__(self, cx=0.0, cy=0.0, r=0.0, fill='black', 
                 stroke_width=1, stroke_opacity=1.0, opacity=1.0, 
                 stroke=rgb(255,255,255)):
        """
        :param cx: The circle center X-coord.
        :param cy: The circle center Y-coord.
        :param radius: The radius of the circle.
        :param stroke_width: The width of the stroke of the perimeter of a shape.
        :param stroke_opacity: The opacity of the stroke-line.
        :param opacity: The opacity of the element in general.
        :param stroke: The color of the stroke-line.

        :type cx: int or float
        :type cy: int or float
        :type radius: int or float
        :type stroke_width: int of float
        :type stroke_opacity: float (0 <= num <= 1.0)
        :type opacity: float (0 <= num <= 1.0)
        :type stroke: rgb-tuple or hex-string
        """

        AbstractGeometry.__init__(self, x=cx, y=cy, stroke=stroke, opacity=opacity, 
                                  stroke_opacity=stroke_opacity, stroke_width=stroke_width)
        self.fill = fill
        self.r = r
        self.cx = self.x
        self.cy = self.y

        self.attribute_filter = ['r', 'cx', 'cy', 'stroke_width', 'stroke_opacity', 
                                 'stroke', 'opacity', 'fill' ]

