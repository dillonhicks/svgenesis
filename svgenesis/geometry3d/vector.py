"""
:mod:`vector.py` -- Python vector representation with numpy
==============================================================

.. moduleauthor:: Dillon Hicks <hhicks@ittc.ku.edu>

"""

from numpy import ndarray, cross, vdot, power, sqrt, add, arccos, divide, cos
from operator import mul, eq, and_
import types



class Vector:
    """
    """
    def __init__(self, *dims):
        self._array = ndarray((len(dims),))
        for (i, dim) in enumerate(dims):
            self._array[i] = dim
        self._num_dims = len(self._array)

    @property
    def array(self):
        return self._array

    @property
    def unit_vector(self):
        return (1.0/self.length)*self

    @property
    def length(self):
        return sqrt(self * self)

    @property
    def ortho_vector(self):
        lhs = -reduce(add, self[:-1])
        rhs = self[-1]
        lhs /= rhs
        dims = [1] * (len(self)-1)
        dims += [lhs]
        return Vector(*dims)



    def __str__(self):
        return str(self._array)

    def __len__(self):
        return self._num_dims

    def __setitem__(self, index, value):
        self._array[index] = value

    def __setslice__(self, start, end, value):
        self._array[start:end] = value

    def __getslice__(self, start, end):
        if end > len(self):
            end = len(self)
        return self._array[start:end]

    def __repr__(self):
        class_name = self.__class__.__name__
        values = ['%.3f'] * len(self)
        values = map(lambda (i, v): v % self[i], enumerate(values))
        values = ', '.join(values)
        return class_name + '(' + values + ')'

    def __getitem__(self, index):
        return float(self._array[index])

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        if isinstance(other, Vector):
            return vdot(self.array, other.array)

             # Pure-Python way  
#            return reduce(add, 
#                          map(lambda pair : pair[0]*pair[1], 
#                              zip(self, other)))
        elif type(other) in [int, float, long]:
            # Scalar Multiplication
            return Vector(*map(lambda i: other*i, self))
        else:
            
            error_str = 'Cannot multiply Vector and %s.'
            if type(other) is types.InstanceType:
                error_str = error_str % other.__class__
            else:
                error_str = error_str % type(other)
            print error_str
            raise TypeError(error_str)



    def __radd__(self, other):
        if not isinstance(other, Vector):
             error_str = 'Cannot add Vector and %s.'
             if type(other) is types.InstanceType:
                 error_str = error_str % other.__class__
             else:
                 error_str = error_str % type(other)
             raise TypeError(error_str)

        if len(self) < len(other):
            vect = self
            ret_vect = Vector(*other)
        else:
            vect = other
            ret_vect = Vector(*self)

        for (i, value) in enumerate(vect):
            ret_vect[i] += value
            
        return ret_vect

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        if len(self) != len(other):
            return False
        return reduce(and_,
                      map(lambda pair: pair[0] == pair[1], 
                          zip(self, other))) 
        
    def __hash__(self):
        return hash(repr(self))

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return -1*self

    def __pow__(self, other):
        return self.cross(other)

    def cross(self, other):
        if not isinstance(other, Vector):
             error_str = 'Cannot cross Vector and %s.'
             if type(other) is types.InstanceType:
                 error_str = error_str % other.__class__
             else:
                 error_str = error_str % type(other)
             raise TypeError(error_str)
        
        return Vector(*cross(self.array, other.array))



    def angle_between(self, other):
        if not isinstance(other, Vector):
             error_str = 'Cannot find angle between Vector and %s.'
             if type(other) is types.InstanceType:
                 error_str = error_str % other.__class__
             else:
                 error_str = error_str % type(other)
             raise TypeError(error_str)

        return arccos(self.unit_vector*other.unit_vector)


    def project_onto(self, other):
        if not isinstance(other, Vector):
             error_str = 'Cannot project Vector onto %s.'
             if type(other) is types.InstanceType:
                 error_str = error_str % other.__class__
             else:
                 error_str = error_str % type(other)
             raise TypeError(error_str)

        return divide((self * other),(other * other))*other


    def scalar_project_onto(self, other):
        return self.length * cos(self.angle_between(other))

