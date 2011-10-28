from svgenesis.core import *
from abstractgeometry import AbstractGeometry

class AbstractPoly(AbstractGeometry):
    """
    """
    @staticmethod
    def xml_parse_handler(xml_elem):
       attrs = {}
       for key, value in xml_elem.attributes.items():
          if key.startswith('svgenesis:'):
             continue
          key = str(key.replace('-', '_'))
          if key == 'points':
             # Translates the points from the x1,y1 x2,y2...
             # xml-attribute-string to the Python tuple string
             # representation ((x1, y1), (x2, y2)...) that is able
             # to be parsed directly to a tuple from the string
             # with eval()
             value = value.split(' ')
             value = filter(lambda v: v != '', value)
             value = map(lambda v: '(' + v +')', value)
             value = '(' + ', '.join(value) + ')'
          try:
             # Try to parse the value into a Pythonic type and
             # value (for example 1, 3.4, (2,3,4)). 
             attrs[key] = eval(value)
          except NameError:
             # Parsing failed, so make it a string and hope it was
             # the right thing to do.
             attrs[key] = eval("\"%s\""%value)
       return attrs
    
    def __init__(self, points=[], stroke_width=1, stroke_opacity=1.0, 
                 opacity=1.0, stroke=rgb(0,0,0), fill='white'):
       
       AbstractGeometry.__init__(self, stroke_width=stroke_width, 
                                stroke_opacity=stroke_opacity, 
                                opacity=opacity, stroke=stroke)
       self.fill = fill
       self._points = points
       self.attribute_filter = ['points', 'stroke_width',  'stroke', 'fill']
       
    def points_to_string(self):
       """
       :returns: The list of len-2 tuples as a string in the form
       "x,y x2,y2 x3,y3 ...".
       """
       X_COORD = 0
       Y_COORD = 1

       points_str = ''
       for point in self._points:
          x = point[X_COORD]
          y = point[Y_COORD]
          points_str += "%s,%s " % (x,y)
       return points_str
    
    points = property(points_to_string)

    def __repr__(self):
        cls_name = self.__class__.__name__
        attrs = []
        for (attr, value) in self.get_data_as_dict().items():
            if attr == 'POINTS':
                attrs.append('%s=%s' % (attr.lower(), repr(self._points)))
            else:
                attrs.append('%s=%s'%(attr.lower(), value))
        attrs = ', '.join(attrs)
        return '%s(%s)'%(cls_name, attrs)


