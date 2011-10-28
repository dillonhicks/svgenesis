"""
:mod:`primitives` -- Standard SVG Primitives
==============================================

.. moduleauthor: Dillon Hicks <hhicks@ittc.ku.edu>
.. $Rev$

Overview
----------

The :mod:`primitives` module provides Python class for all of the
built-in shape primitives in the SVG standard (Circles, Ellipses,
Lines, Text, Rectangles, Paths, Polylines, Polygons), a SVGDocument
wrapper class to the xml.dom.minidim.Document class to provide a
method by which SVG .xml files can be converted to and from their
Python object equivalents.

"""

from abstractgeometry import AbstractGeometry
from abstractpoly     import AbstractPoly
from circle    import Circle
from ellipse   import Ellipse
from group     import Group
from line      import Line
from path      import Path, PathPoint
from text import Text
from polygon   import Polygon
from polyline  import Polyline
from rectangle import Rectangle
 

############################################################
#
# Classes Soon to be Implemented, stubs only for now as a reminder.
#
###########################################################


from exceptions import NotImplementedError
class Defs:

    def __init__(self, svgdef):
        raise NotImplemented

class Use:
    def __init__(self):
        raise NotImplemented
    


from svgenesis.core import *
######################################################################
# Obtain the global parsing and type variables from svgenesis.core and
# update them with all of the name->object and name->parsing_function.
#  
# See svgenesis.core for original definition and their use by the
# parser.
#######################################################################

global node_name_to_type
global node_name_to_parse_handler    


node_name_to_type.update({
    'line' : Line,
    'text' : Text,
    'rect' : Rectangle,
    'polyline' : Polyline,
    'polygon' : Polygon,
    'path'    : Path,
    'circle'  : Circle,
    'ellipse' : Ellipse,
    'g'       : Group,
    'defs'    : Defs,
    'use'     : Use

})

# Most of the svg native primitives do not need special parsing since
# the parsing is simple enough that the svgenesis.core parser can
# handle them without an explicit algorithm.
node_name_to_parse_handler.update({
    'line' : None,
    'text' : None,
    'rect' : None,
    'polyline' : Polyline.xml_parse_handler,
    'polygon' : Polygon.xml_parse_handler,
    'path'    : None,
    'circle'  : None,
    'ellipse' : None,
    'g'       : Group.xml_parse_handler,
    'defs'    : None,
    'use'     : None

})

