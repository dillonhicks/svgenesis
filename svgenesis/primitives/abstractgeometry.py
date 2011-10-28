from xml.dom import minidom
from svgenesis.core import *

class AbstractGeometry(SVGElement):
    """
    Abstract class that specifies the geometric shared properties for
    most SVG elements. Few have less than what is specified here, but
    we just ignore those with the attribute_filter list.
    """

    SVG_TAG_NAME = 'abstract'
    
    def __init__(self, x=0, y=0, stroke_width=1, stroke_opacity=1.0, 
                 opacity=1.0, stroke=rgb(0,0,0), id=None):
        """
        :param x: The starting X-coord.
        :param y: The starting Y-coord.
        :param stroke_width: The width of the stroke of the perimeter of a shape.
        :param stroke_opacity: The opacity of the stroke-line.
        :param opacity: The opacity of the element in general.
        :param stroke: The color of the stroke-line.
    
        :type x: int or float
        :type y: int or float
        :type stroke_width: int of float
        :type stroke_opacity: float (0 <= num <= 1.0)
        :type opacity: float (0 <= num <= 1.0)
        :type stroke: rgb-tuple or hex-string
        """

        # Type and Value checking for the basic attributes.
        # x Coord value should be a float or an int, as is sensical.
        # If not a float or an int, a type coersion to float is
        # attempted if, for example, x is a string.  If type coersion
        # fails a TypeError is raised.
        if not type(x) in (float, int):
            try: 
                x = float(x)
            except ValueError:
                raise TypeError("x must be a int, or float")

        # y coord value should be a float or an int, as is
        # sensical. If not a float or an int, a type coersion to float
        # is attempted. A type coersion would happen if, for eyample,
        # y is a string.  If type coersion fails a TypeError is
        # raised.
        if not type(y) in (float, int):
            try: 
                y = float(y)
            except ValueError:
                raise TypeError("y must be a int, or float")

        # stroke_width value should be an int greater or equal to 0.
        # If stroke_width is not an int, a type coersion to int is
        # attempted. A type coersion would happen if, for eyample, y
        # is a string.  If type coersion fails a ValueError is raised
        # and if stroke width < 0 a valueerror is raised..
        if not type(stroke_width) in(float, int):
            try: 
                stroke_width = float(stroke_width)
            except ValueError:
                raise TypeError("stroke_width must be a int/float or "
                                 "a type and value coercable to int/float.")
        if not stroke_width >= 0:
            raise ValueError("stroke_width must be >= 0.")

        # stroke_opacity value should be an float greater or equal to 0.
        # If stroke_opacity is not an float, a type coersion to float is
        # attempted. A type coersion would happen if, for eyample, y
        # is a string.  If type coersion fails a ValueError is raised
        # and if 0.0 < stroke opacity < 1.0 a valueerror is raised.
        if not type(stroke_opacity) is float:
            try: 
                stroke_opacity = float(stroke_opacity)
            except ValueError:
                raise ValueError("stroke_opacity must be a float, or "
                                 "a type and value coercable to float.")
        if not 0.0 <= stroke_opacity and \
                not stroke_opacity <= 1.0:
            raise ValueError("stroke_opacity must be in the range "
                             "0.0 <= stroke_opacity <= 1.0.")

        # opacity value should be an float greater or equal to 0.
        # If opacity is not an float, a type coersion to float is
        # attempted. A type coersion would happen if, for eyample, y
        # is a string.  If type coersion fails a ValueError is raised
        # and if 0.0 < opacity < 1.0 a valueerror is raised.
        if not type(opacity) is float:
            try: 
                opacity = float(opacity)
            except ValueError:
                raise ValueError("opacity must be a float, or "
                                 "a type and value coercable to float.")
        if not 0.0 <= opacity and \
                not opacity <= 1.0:
            raise ValueError("opacity must be in the range "
                             "0.0 <= opacity <= 1.0.")


        self.x = x
        self.y = y
        self.stroke_width = stroke_width
        self.stroke_opacity = stroke_opacity
        self.opacity = opacity
        self.stroke = stroke
        self.id = id
        self.attribute_filter = ['x', 'y', 'stroke_width', 
                                 'stroke_opacity', 
                                 'stroke', 'opacity']


    def get_data_as_dict(self):
        """
        :return: The attributes of the elements as a dictionary keyed
          by the proper uppercased variable name.
        """
        data_dict = {}
        for attr in self.attribute_filter:
            data_dict[attr.upper()] = getattr(self, attr)
        return data_dict

    def __str__(self):
        return str(self.to_node().toxml())

    def __repr__(self):
        """
        :returns: The string that will recreate this class when called
            with eval(repr_str), where repr_str = repr(obj).
        """
        cls_name = self.__class__.__name__
        attrs = []
        for (attr, value) in self.get_data_as_dict().items():
            attrs.append('%s=%s'%(attr.lower(), value))
        attrs = ', '.join(attrs)
        return '%s(%s)'%(cls_name, attrs)
    
    def to_node(self):
        """
        :returns: The XML Element node representation of the class.
        """
        node = minidom.Element(self.SVG_TAG_NAME)        
        for (attr, value) in self.get_data_as_dict().items():
            attr = attr.replace('_', '-')
            node.setAttribute(attr.lower(),str(value))
        return node
        

    def to_xml(self):
        """
        :returns: The string representation of the XML node created
            with to_node().
        """
        return self.to_node().toxml()        

    def __eq__(self, other):
        """
        Checks if the type and values of *other* are equal to the same
        as this classes type and value to determine if they are
        equivalent.
        """
        if self.__class__ != other.__class__:
            return False

        return (self.get_data_as_dict() == 
                    other.get_data_as_dict())
