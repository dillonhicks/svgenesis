from svgenesis.vector import Vector
from numpy import sqrt
from operator import add

VX, VY, VZ = range(3)

class View3D:
    def __init__(self,
        world_position=Vector(0.0, 0.0, -1.0),
        look_vector=Vector(0.0, 0.0, 0.0),
        view_width=600.,
        view_height=600.):
                 
        self._position = world_position
        # X direction
        self._width = view_width
        # y direction
        self._height = view_height
        self._world_position = world_position
        self._viewing_vector = look_vector - world_position
        self._viewplane_vector_w = self._viewing_vector + Vector(self._height, 0.0, 0.0)
        self._viewplane_vector_h = self._viewing_vector + Vector(0.0, self._height, 0.0)
        
        self._a2cx = sqrt(0.75*self._width**2)
        self._a2cy = sqrt(0.75*self._height**2)
        


        self._render_objects = []




    def adjust_point_for_distance(self, point):
        distance = (point[VZ] - self._world_position[VZ])
        new_point = Vector(0.0, 0.0, point[VZ])
        print point, new_point
        new_point[VX] =  point[VX] * self._a2cx/(distance + self._a2cx) 
        new_point[VY] =  point[VY] * self._a2cy/(distance + self._a2cy) 
        print new_point
        return new_point
        
        

    def adjust_object_for_distance(self, obj):
        return obj.__class__(
            *map(lambda pt: self.adjust_point_for_distance(pt), 
                 obj.get_points()))


    def add_rendered_object(self, robj):
        self._render_objects.append(robj)


    def render_objects(self):
        return map(lambda obj : self.adjust_object_for_distance(obj),
                   self._render_objects)
            
        
    def to_xml(self):
        polygons = reduce(list.extend, map(lambda obj: obj.as_polygons(), self.render_objects()))
        return reduce(add, map(str, polygons))
