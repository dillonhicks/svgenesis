"""
:mod:`core` -- Core Functionality for svgenesis
=================================================

.. moduleauthor: Dillon Hicks <hhicks@ittc.ku.edu>
.. $Rev$

Overview
----------

When adding more images to svgenesis, you will need to import this module::

from svgenesis.core import *

Or at minimum::

from svgenesis.core import node_name_to_type, node_name_to_parse_handler

This will allow you to properly update the parsing information
dictionaries **node_name_to_type** and **node_name_to_parse_handler**
that will allow a new image class to be parsed from
object->XML->new-object without problems.



"""

from xml.dom import minidom
from svgenesis.namespace import SVGENESIS_TYPE

SVG_PARSE_HELPER_TPL = """<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
xmlns:svgenesis="http://www.ittc.ku.edu/kusp/svgenesis">%s</svg>"""

SVG_XML_LOAD_STR = """<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="1000" height="1000" version="1.1"
xmlns="http://www.w3.org/2000/svg"
xmlns:svgenesis="http://www.ittc.ku.edu/kusp/svgenesis">
</svg>"""



FILL_COLORS = [
'purple',
'blue',
'red',
'gray',
'green',
'orange',
'magenta',
'cyan'
'yellow',
'slategray']

SVGENESIS_TYPE = 'svgenesis:type'

global node_name_to_type
global node_name_to_parse_handler
try:
    node_name_to_type
except NameError:
    node_name_to_type = {}
try:
    node_name_to_parse_handler
except NameError:
    node_name_to_parse_handler = {}

def generate_template(width, height):
    """
    Return a SVG document template string with the specified width and
    height for the resulting image.
    """
    return SVG_FILE_TEMPLATE_STR % \
        dict(SVG_IMAGE_WIDTH=width, SVG_IMAGE_HEIGHT=height)

def parse(svgfile):
    """
    Parse .svg file into a :class:`SVGDocument`
    """
    pass


def object_from_xml(xml_elem):
    """
    Given a XML node or the XML node's string representation, return
    the SVG Primitive that corresponds to the particular node/element.
    """
    if type(xml_elem) is str:
        xml_elem = minidom.parseString(SVG_PARSE_HELPER_TPL%xml_elem.strip())
        # Go to the XML tag
        xml_elem = xml_elem.firstChild
        # Go to svg tag
        xml_elem = xml_elem.nextSibling
        # Get svg object xml code
        xml_elem = xml_elem.firstChild
        
    if not isinstance(xml_elem, minidom.Element):
        raise TypeError("Cannot create an SVG object instance from %s" % 
                        xml_elem.__class__.__name__)

    if not xml_elem.hasAttribute(SVGENESIS_TYPE):
        node_name = xml_elem.nodeName
    else:
        node_name = xml_elem.getAttribute(SVGENESIS_TYPE)
 
    handler = node_name_to_parse_handler[node_name]
    object_type = node_name_to_type[node_name]
    if handler:
        retval = handler(xml_elem)
        if isinstance(retval, SVGElement):
            return retval
        attrs = retval
    else:
        attrs = {}
    
        for key, value in xml_elem.attributes.items():
            key = str(key.replace('-', '_'))
            attrs[key] = eval(value)
    
    return object_type(**attrs)
    

class rgb:
    """
    Color class for SVG elements specifying Red, Green and Blue.
    Makes it easy to convert between the "rgb(xxx, xxx, xxx)" and this
    class.
    """
    def __init__(self, red, green, blue):
        colors = (red, green, blue)
        if not all(map(lambda clr: type(clr) is int, colors)):
            try:
                red = int(red)
                blue = int(blue)
                green = int(green)
            except ValueError, eargs:
                raise ValueError("The value for each color red, green and "
                             "blue must be int or a value coercable to int")

                
        if not all(map(lambda clr: 0 <= clr and clr <= 255, colors)):
            raise ValueError("The values for each color red, green and "
                             "blue must be 0 <= color <= 255.")
        self.red = red
        self.green = green 
        self.blue = blue

    def __str__(self):
        return "rgb(%s, %s, %s)" % \
            (self.red, self.green, self.blue)


    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if type(other) is str:
            return other == str(self)
        elif not isinstance(other, rgb):
            raise TypeError('Cannot compare types rgb and ' % type(other))
        return all((self.red == other.red, 
                    self.blue == other.blue, 
                    self.green == other.green))


class SVGElement(object):
    def __init__(self):
        pass

class SVGDocument(object):
    """
    The :class:`SVGDocument` is a light wrapper to the Python
    xml.dom.minidom.Document.
    """
    
    def __init__(self, width, height):
        self.width = str(width)
        self.height = str(height)
        self.svg_elements = []


    def __gen_doc(self):
        doc = minidom.parseString(SVG_XML_LOAD_STR)
        parent_node = doc.getElementsByTagName('svg')[0]
        parent_node.setAttribute('width', self.width)
        parent_node.setAttribute('height', self.height)
        for obj in self.svg_elements:
            parent_node.appendChild(obj.to_node())
        return doc

    def add_svg_object(self, obj):
        self.svg_elements.append(obj)

    def toxml(self):
        doc = self.__gen_doc()
        return doc.toxml()

    def toprettyxml(self):
        doc = self.__gen_doc()
        return doc.toprettyxml()

