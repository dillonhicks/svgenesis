from numpy import array
from svgenesis.vector import Vector
from svgenesis.primitives import Polygon

class AbstractGeometry3D:
    def __init__(self, *points):
        self._points = array(points)
        self._triangles = []
    
    def get_point(self, index):
        return self._points[index]

    def set_point(self, index, value):
        self._points[index] = value 

    
    def as_polygons(self):
        poly_list = []
        for triangle in self._triangles:
            poly_list.append(Polygon(map(lambda vect: (vect[0],vect[1]), 
                                        triangle.get_points())))
        return poly_list



    def get_points(self):
        return self._points

    
#    def __init__(self, *points):
#        self._array = ndarray((len(dims),))
#        for (i, dim) in enumerate(dims):
#            self._array[i] = dim
#
#
#
#   @property
#    def line_vectors(self):
#        return (,)





class Triangle3D(AbstractGeometry3D):
    # each point should be a vector
    def __init__(self, p0, p1, p2):
        AbstractGeometry3D.__init__(self, p0, p1, p2)
        self._triangles = [self]
    @property
    def line_vectors(self):
        return set( [self._points[0] - self._points[1],
                    self._points[1] - self._points[2],
                    self._points[2] - self._points[0]])
        

    
class Quad3D(AbstractGeometry3D):
    def __init__(self, p0, p1, p2, p3):
        AbstractGeometry3D.__init__(self, p0, p1, p2, p3)
        self._triangles = array([Triangle3D(p0, p1, p2), 
                                 Triangle3D(p2, p3, p0)])
        


    @property
    def line_vectors(self):
        return reduce(set.union, 
                      map(lambda t: t.line_vectors,
                          self._triangles))    
