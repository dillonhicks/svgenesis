"""
:mod:`composites` -- Classes for Simple, Non-Primitive, SVG Shapes
===================================================================

.. moduleauthor:: Dillon Hicks <hhicks@ittc.ku.edu>

For clairity, "primitive" means a type of shape or class that has a
tag within SVG specification. Such objects are Groups, Rectagles,
Circles, Lines, etc. 

The composites (non-primitive) shapes/objects are convience classes
that provide a little higher level of abstraction when working with
SVG. Most of the classes in composites subclass either Polygon,
Rectangle or Group in some way, but add methods and naming
convientions that ease the use of commonly used shapes that are not
part of the SVG specification. 

These classes also embed extra infomration within the XML tag for the
base shape to assist the svgenesis.core parsing algorithms when
parsing the svg-xml from the Composite.to_xml(), method back to the
original Python object.

Composite Shapes and Objects
=============================

* Triangle
* Equilateral Polygon
* Equilateral Triangle
* Equilateral Pentagon
* Equilateral Hexagon
* Equilateral Octogon
* (N-Pointed) Star
* GridLines
"""

from triangle import Triangle
from equilateraltriangle  import EquilateralTriangle
from equilateralpolygon   import EquilateralPolygon
from equilateralpentagon  import EquilateralPentagon
from equilateralhexagon   import EquilateralHexagon
from equilateraloctogon   import EquilateralOctogon
from square    import Square
from star      import Star
from gridlines import GridLines
from evileye   import OuterEvilEye, InnerEvilEye, EvilEye

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
    'Triangle'     : Triangle,
    'EquilateralPolygon': EquilateralPolygon,
    'EquilateralTriangle': EquilateralTriangle,
    'EquilateralPentagon': EquilateralPentagon,
    'EquilateralHexagon': EquilateralHexagon,
    'EquilateralOctogon': EquilateralOctogon,
    'Square' : Square,
    'Star' : Star,
    'GridLines' : GridLines,
    'OuterEvilEye' : OuterEvilEye,
    'InnerEvilEye' : InnerEvilEye,
    'EvilEye' : EvilEye,


})
    
node_name_to_parse_handler.update({
    'Triangle'     : Triangle.xml_parse_handler,
    'EquilateralPolygon': EquilateralPolygon.xml_parse_handler,
    'EquilateralTriangle': EquilateralTriangle.xml_parse_handler,
    'EquilateralPentagon': EquilateralPentagon.xml_parse_handler,
    'EquilateralHexagon': EquilateralHexagon.xml_parse_handler,
    'EquilateralOctogon': EquilateralOctogon.xml_parse_handler,
    'Square' : None,
    'Star' : Star.xml_parse_handler,
    'GridLines' : GridLines.xml_parse_handler,
    'OuterEvilEye' : None,
    'InnerEvilEye' : None,
    'EvilEye' : None

})
