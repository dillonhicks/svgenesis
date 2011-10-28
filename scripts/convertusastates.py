from svgenesis.primitives.path import *
from xml.dom import minidom
import sys 

STATE_TPL_STR="""from svgenesis.core import *
from svgenesis.namespace import SVGENESIS_TYPE
from svgenesis.primitives import Path, Group
from svgenesis.primitives.path import *
from mapviz.usa.states.statecounties import StateCounties

class %(NAME)s(Path):
    DEFAULT_POINTS = %(POINTS)s

    def __init__(self, fill=rgb(200,200,200), stroke=rgb(0,0,0), stroke_width=1.0, 
                 opacity=1.0, stroke_opacity=1.0):
        Path.__init__(self, points=self.DEFAULT_POINTS, fill=fill,
                      stroke_width=stroke_width, stroke_opacity=stroke_opacity, 
                      opacity=opacity, stroke=stroke)
    def to_node(self):
        node = Path.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, '%(NAME)s')
        return node


class %(NAME)sCounties(StateCounties):
    def __init__(self, fill=rgb(200,200,200), stroke=rgb(0,0,0), stroke_width=0.5, 
                 opacity=1.0, stroke_opacity=1.0):
        StateCounties.__init__(self, state='%(NAME)s', fill=fill, stroke=stroke, 
                               stroke_width=stroke_width, opacity=opacity, 
                               stroke_opacity=stroke_opacity)


"""


filename = sys.argv[1]
doc = minidom.parse(filename)
paths = doc.getElementsByTagName('path')

all_path_points = {}
for path in paths:
    points = []
    tmp = path.getAttribute('d')
    name = path.getAttribute('id')
    name = name.replace('_','')
    points_string = tmp.replace(' ', ',')
    raw_points = points_string.split(',')
    relpoints = []
    while len(raw_points): 
        elem = raw_points.pop(0)
        if elem.isalpha():
            if elem == 'M':
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                points.append(MovePoint(x,y))
                
            if elem == 'L':
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                points.append(LinePoint(x,y))

            if elem == 'C':
                x1 = raw_points.pop(0)
                y1 = raw_points.pop(0)
                x2 = raw_points.pop(0)
                y2 = raw_points.pop(0)
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                points.append(BiezerCubicPoint(x1, y1, x2, y2, x, y))
                 
            if elem in ('z', 'Z'):
                points.append(ClosePoint())


    # for i in range(len(points)):
    #     curpoint = points[i]
    #     if i == 0:
    #         relpoints.append(curpoint)
    #     else:
    #         if curpoint.point_type in ('Z', 'z'):
    #             continue
            
    #         xp = prevpoint.x
    #         yp = prevpoint.y
    #         xc = curpoint.x
    #         yc = curpoint.y
    #         newx = float(xc) - float(xp)
    #         newy = float(yc) - float(yp)
    #         ptype = curpoint.point_type
            
    #         if ptype == 'L':
    #             newpoint =  LinePointR(*curpoint.args)    
    #         if ptype == 'C':
    #             newpoint =  BiezerCubicPointR(*curpoint.args)    

    #         newpoint.x = newx
    #         newpoint.y = newy
    #         relpoints.append(newpoint)
    #     prevpoint = curpoint

    all_path_points.update({name : tuple(points)})




import os
os.system('rm -rf states')
os.mkdir('states')
os.system('rm -rf statessvg')
os.mkdir('statessvg')

with open('states/__init__.py', 'w') as outfile:
    outfile.write(' ')

for (i, spoints) in enumerate(all_path_points.items()):
    if not any(map(lambda c : c.isdigit(), spoints[0])):
        name = spoints[0]

    else:
        continue
    
    filename = 'states/%s.py'%name.lower()

    state_dict = { 
        "NAME" : name,
        "POINTS": spoints[1]}
    filetext = STATE_TPL_STR % state_dict
    with open(filename, 'w') as outfile:
        outfile.write(filetext)

import states

for i in range(len(all_path_points.items())):
    spoints = all_path_points.items()[i]
    if not any(map(lambda c : c.isdigit(), spoints[0])):
        name = spoints[0]
    else:
        continue

    filename = 'states/%s.py'%name.lower()
    mod = __import__('states.%s'%name.lower(), fromlist=[name,])
    doc = SVGDocument(2000, 2000)    
    
    state = getattr(mod, name)()
    doc.add_svg_object(state)

    with open('statessvg/%s.svg'%name, 'w') as outfile:
        outfile.write(doc.toprettyxml())
