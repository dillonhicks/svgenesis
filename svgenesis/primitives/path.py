from svgenesis.core import * 
from abstractgeometry import AbstractGeometry
 
class PathPoint:
    """
    Validator class for points used in the Path class.
    """
    
    # All of the typical types of points come in two flavors, the
    # capital leter designation for absolute coordinates, and a lower
    # case for relative (to the previous point) coordinates. The
    # exception is CLOSE_PATH which takes no arguments and does not
    # differentiate between the upper and lower case point code.
    MOVE_ABS                      = 'M'
    MOVE_REL                      = 'm'
    LINETO_ABS                    = 'L'
    LINETO_REL                    = 'l'
    BIEZER_CUBIC_CURVETO_ABS      = 'C'
    BIEZER_CUBIC_CURVETO_REL      = 'c'
    BIEZER_QUADRATIC_CURVETO_ABS  = 'Q'
    BIEZER_QUADRATIC_CURVETO_REL  = 'q'
    ARCTO_ABS                     = 'A'
    ARCTO_REL                     = 'a'
    HORIZONTAL_LINETO_ABS         = 'H'
    HORIZONTAL_LINETO_REL         = 'h'
    VERTICAL_LINETO_ABS           = 'V'
    VERTICAL_LINETO_REL           = 'v'
    SMOOTH_CUBIC_CURVETO_ABS      = 'S'
    SMOOTH_CUBIC_CURVETO_REL      = 's'
    SMOOTH_QUADRATIC_CURVETO_ABS  = 'T'
    SMOOTH_QUADRATIC_CURVETO_REL  = 't'
    CLOSE_PATH                    = 'z'
    CLOSE_PATH_ALT                = 'Z'
    CONTINUATION                  = ''

    # Maps the point type to the expected args for that point type.
    # Used for argument validation in the constructor and to provide
    # clearer error messages.
    POINT_TYPE_TO_ARGS = {
        MOVE_ABS                     : ('x', 'y'),
        MOVE_REL                     : ('x', 'y'),
        LINETO_ABS                   : ('x', 'y'),
        LINETO_REL                   : ('x', 'y'),
        BIEZER_CUBIC_CURVETO_ABS     : ('x1', 'y1', 'x2', 'y2', 'x', 'y'),
        BIEZER_CUBIC_CURVETO_REL     : ('x1', 'y1', 'x2', 'y2', 'x', 'y'),
        BIEZER_QUADRATIC_CURVETO_ABS : ('x', 'y'),
        BIEZER_QUADRATIC_CURVETO_REL : ('x', 'y'),
        ARCTO_ABS                    : ('rx', 'ry', 'x-axis-rotation', 
                                        'large-arc-flag', 'sweep-flag', 
                                        'x', 'y'),
        ARCTO_REL                    : ('rx', 'ry', 'x-axis-rotation', 
                                        'large-arc-flag', 'sweep-flag', 
                                        'x', 'y'),
        HORIZONTAL_LINETO_ABS        : ('y',),
        HORIZONTAL_LINETO_REL        : ('y',),
        VERTICAL_LINETO_ABS          : ('x',),
        VERTICAL_LINETO_REL          : ('x',),
        SMOOTH_CUBIC_CURVETO_ABS     : ('x2', 'y2', 'x' 'y'),
        SMOOTH_CUBIC_CURVETO_REL     : ('x2', 'y2', 'x' 'y'),
        SMOOTH_QUADRATIC_CURVETO_ABS : ('x1', 'y1', 'x', 'y'),
        SMOOTH_QUADRATIC_CURVETO_REL : ('x1', 'y1', 'x', 'y'),
        CLOSE_PATH                   : (),
        CLOSE_PATH_ALT               : (),
        CONTINUATION                 : None
        }

    # Tuple of all point types to clairfy the point type validation.
    ALL_POINT_TYPES = ( MOVE_ABS,
                        MOVE_REL,
                        LINETO_ABS,
                        LINETO_REL,
                        BIEZER_CUBIC_CURVETO_ABS,
                        BIEZER_CUBIC_CURVETO_REL,
                        BIEZER_QUADRATIC_CURVETO_ABS,
                        BIEZER_QUADRATIC_CURVETO_REL,
                        ARCTO_ABS,
                        ARCTO_REL,
                        HORIZONTAL_LINETO_ABS,
                        HORIZONTAL_LINETO_REL,
                        VERTICAL_LINETO_ABS,
                        VERTICAL_LINETO_REL,
                        SMOOTH_CUBIC_CURVETO_ABS,
                        SMOOTH_CUBIC_CURVETO_REL,
                        SMOOTH_QUADRATIC_CURVETO_ABS,
                        SMOOTH_QUADRATIC_CURVETO_REL,
                        CLOSE_PATH,
                        CLOSE_PATH_ALT,
                        CONTINUATION)

    def __init__(self, ptype, *args):

        # Check to see if the point type is valid b
        if not ptype in self.ALL_POINT_TYPES:
            raise ValueError('The point type %s is not '
                             'valid for an SVG Path Point.' % repr(ptype))
        
        pargs = self.POINT_TYPE_TO_ARGS[ptype]
        if not pargs is None:
            if len(args) != len(pargs):
                raise TypeError("__init__ expected exactly %s argument, got %s"
                                "\nExpected arguments for PathPoint of type `%s' are:"
                                "\n    %s" % (len(pargs), len(args), ptype, pargs))
        # Type and Value checking for the basic attributes.
        # x Coord value should be a float or an int, as is sensical.
        # If not a float or an int, a type coersion to float is
        # attempted if, for example, x is a string.  If type coersion
        # fails a TypeError is raised.
        for (i, arg) in enumerate(args):
            if not type(arg) in (float, int):
                try: 
                    arg = float(arg)
                except ValueError:
                    raise TypeError(pargs[i]+" must be a int, or float")

        self.point_type = ptype
        self.args = args


    def __str__(self):
        """
        :returns: A string with the format "<point_type> [list-of-points]"
        """
        if self.point_type in (self.CLOSE_PATH, self.CLOSE_PATH_ALT) :
            return ' %s' % self.point_type
        else:
            return ' %s %s ' % \
                (self.point_type, ' '.join(map(lambda v: str(v),self.args)))

    
    def __repr__(self):
        cls_name = self.__class__.__name__
        if cls_name == 'PathPoint':
            return '%s(%s,%s)' % (cls_name, repr(self.point_type),
                                   ', '.join(map(lambda v: str(v),self.args))) 
        else:
            return '%s(%s)' % (cls_name, ', '.join(map(lambda v: str(v),self.args))) 



class MovePoint(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'M', x, y)

class MovePointR(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'm', x, y)

class LinePoint(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'L', x, y)

class LinePointR(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'l', x, y)

class BiezerCubicPoint(PathPoint):
    def __init__(self,  x1, y1, x2, y2, x, y):
        PathPoint.__init__(self, 'C', x1, y1, x2, y2, x, y)

class BiezerCubicPointR(PathPoint):
    def __init__(self,  x1, y1, x2, y2, x, y):
        PathPoint.__init__(self, 'c', x1, y1, x2, y2, x, y)


class BiezerQuadraticPoint(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'Q', x, y)

class BiezerQuadraticPointR(PathPoint):
    def __init__(self, x, y):
        PathPoint.__init__(self, 'q', x, y)


# class MovePoint(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'M', x, y)

# class MovePointR(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'm', x, y)


# class MovePoint(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'M', x, y)

# class MovePointR(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'm', x, y)


# class MovePoint(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'M', x, y)

# class MovePointR(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'm', x, y)


# class MovePoint(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'M', x, y)

# class MovePointR(PathPoint):
#     def __init__(self, x, y):
#         PathPoint.__init__(self, 'm', x, y)


class ClosePoint(PathPoint):
    def __init__(self):
        PathPoint.__init__(self, 'Z')

class ClosePointR(PathPoint):
    def __init__(self):
        PathPoint.__init__(self, 'z')


class ContinuePoint(PathPoint):
    def __init__(self, *args):
        PathPoint.__init__(self, '', *args)




class Path(AbstractGeometry):
    SVG_TAG_NAME = 'path'

    def __init__(self, points=[], fill=rgb(0,0,0), stroke_width=1, 
                 stroke_opacity=1.0, opacity=1.0, stroke=rgb(0,0,0)):

        AbstractGeometry.__init__(self, stroke_width=stroke_width, 
                                  stroke_opacity=stroke_opacity, 
                                  opacity=opacity, stroke=stroke)
        self._points = points
        self.fill = fill
        self.attribute_filter = ['d', 'fill', 'stroke_width', 
                                 'stroke_opacity', 
                                 'stroke', 'opacity']

    def points_to_string(self):
        """
        :returns: 
        """

        points_str = ''
        for point in self._points:
            points_str += str(point)
        return points_str

    d = property(points_to_string)

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


