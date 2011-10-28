from svgenesis.core import *
from abstractpoly import AbstractPoly
 
class Polyline(AbstractPoly):
    """
    Polylines are strange.
    """

    SVG_TAG_NAME = 'polyline'

    @staticmethod
    def xml_parse_handler(xml_elem):
        return AbstractPoly.xml_parse_handler(xml_elem)

    def __init__(self, points=[], stroke_width=1, stroke_opacity=1.0, 
                 opacity=1.0, stroke=rgb(0,0,0), fill='white'):
        """
        :param points: A list of len-2 tuples for each xy coord of the Polyline.
        :param stroke_width: The width of the stroke of the perimeter of a shape.
        :param stroke_opacity: The opacity of the stroke-line.
        :param opacity: The opacity of the element in general.
        :param stroke: The color of the stroke-line.

        :type points: list of len-2 tuples
        :type stroke_width: int of float
        :type stroke_opacity: float (0 <= num <= 1.0)
        :type opacity: float (0 <= num <= 1.0)
        :type stroke: rgb-tuple or hex-string
        """
        AbstractPoly.__init__(self, points=points, stroke_width=stroke_width, stroke_opacity=stroke_opacity,
                              opacity=opacity, stroke=stroke, fill=fill)




