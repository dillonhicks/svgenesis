from svgenesis.primitives.path import *
from svgenesis.maps.usa.counties.county import County
from xml.dom import minidom
import sys 

COUNTY_TPL_STR="""from svgenesis.core import *
from svgenesis.namespace import *
from svgenesis.primitives import Path, Group
from svgenesis.primitives.path import *
from svgenesis.maps.usa.counties.county import County

class %(NAME)s(County):
    DEFAULT_POINTS = %(POINTS)s

    def __init__(self, fill=rgb(200,200,200), stroke=rgb(0,0,0), stroke_width=1.0, 
                 opacity=1.0, stroke_opacity=1.0):
        County.__init__(self, points=self.DEFAULT_POINTS, fill=fill,
                      stroke_width=stroke_width, stroke_opacity=stroke_opacity, 
                      opacity=opacity, stroke=stroke, fips_code='%(FIPS)s', state='%(STATE)s')
    def to_node(self):
        node = Path.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'County')
        node.setAttribute(SVGENESIS_STATE, '%(STATE)s')
        node.setAttribute(SVGENESIS_COUNTY, '%(NAME)s')
        return node
"""

INKSCAPE_LABEL='inkscape:label'
filename = sys.argv[1]
doc = minidom.parse(filename)
paths = doc.getElementsByTagName('path')
all_path_points = {}
fips_code_to_county = {}
def make_names(elem):
    if elem.hasAttribute(INKSCAPE_LABEL):
        label = elem.getAttribute(INKSCAPE_LABEL)
        try:
            county, state = label.split(',')
        except ValueError:
            return label, None
        county = county.strip()
        county = county.replace(' ', '-')
        county = county.replace('-', '_')
        county = county.replace('.', '')
        county = county.replace("'", '')
        county = county.lower()
        state = state.strip()
        state = state.lower()
        return county, state
    else:
        return elem.getAttribute('id'), None


for path in paths:
    points = []
    tmp = path.getAttribute('d')
    name, state = make_names(path)    
    if not state:
        # state is none, so it is another type of svg element, not a county.
        continue
    fips = path.getAttribute('id')
    print name, state, fips
    if not fips_code_to_county.has_key(state):
        fips_code_to_county[state] = {}
    fips_code_to_county[state].update({name : fips})
    points_string = tmp.replace(' ', ',')
    raw_points = points_string.split(',')
    relpoints = []
    while len(raw_points): 
        elem = raw_points.pop(0)
        if elem.isalpha():
            if elem == 'M':
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                if y.endswith('M'):
                    y, m = y.split('M')
                    raw_points.insert(0,m)
                points.append(MovePoint(x,y))
                
            if elem == 'L':
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                if y.endswith('M'):
                    y, m = y.split('M')
                    raw_points.insert(0,m)
                points.append(LinePoint(x,y))

            if elem == 'C':
                x1 = raw_points.pop(0)
                y1 = raw_points.pop(0)
                x2 = raw_points.pop(0)
                y2 = raw_points.pop(0)
                x = raw_points.pop(0)
                y = raw_points.pop(0)
                if y.endswith('M'):
                    y, m = y.split('M')
                    raw_points.insert(0,m)
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

    if not all_path_points.has_key(state):
        all_path_points[state] = {}
    all_path_points[state].update({name : tuple(points)})




import os
os.system('rm -rf counties')
os.mkdir('counties')
os.chdir('counties')
for state in all_path_points.keys():
    os.mkdir(state)
    with open('%s/__init__.py'%state, 'w') as outfile:
        outfile.write(' ')
os.chdir('..')

os.system('rm -rf countiessvg')
os.mkdir('countiessvg')
os.chdir('countiessvg')
for state in all_path_points.keys():
    os.mkdir(state)
os.chdir('..')

with open('counties/__init__.py', 'w') as outfile:
    outfile.write(' ')

for state in all_path_points.keys():
    for (i, spoints) in enumerate(all_path_points[state].items()):
        if not any(map(lambda c : c.isdigit(), spoints[0])):
            name = spoints[0].replace('_',' ')
            name = name.title()
            name = name.replace(' ', '')
        else:
            name = 'County%s'%i
        filename = 'counties/%s/%s.py'%(state.lower(), name.lower())

        county_dict = { 
            "NAME" : name,
            "POINTS": spoints[1],
            "FIPS"  : fips_code_to_county[state][spoints[0]],
            'STATE' : state}
        filetext = COUNTY_TPL_STR % county_dict
        with open(filename, 'w') as outfile:
            outfile.write(filetext)

import counties
fips_dict = {}
fips_header = ""
for state in all_path_points.keys():
    for (i, spoints) in enumerate(all_path_points[state].items()):
        if not any(map(lambda c : c.isdigit(), spoints[0])):
            name = spoints[0].replace('_',' ')
            name = name.title()
            name = name.replace(' ', '')
        else:
            name = 'County%s'%i
            
        # print state.lower(), name.lower()
        mod = __import__('counties.%s.%s'%(state.lower(), name.lower()), fromlist=[name,])
    
        doc = SVGDocument(2000, 2000)    
    
        county = getattr(mod, name)()
        fips_dict[county.fips_code] = '%s.%s.%s'%(state.lower(), name.lower(), name)
        doc.add_svg_object(county)
        fips_header += 'import %s.%s\n'%(state.lower(), name.lower())
        with open('countiessvg/%s/%s.svg'%(state, name), 'w') as outfile:
            outfile.write(doc.toprettyxml())

from pprint import pprint
with open('fips.py', 'w') as outfile:
    outfile.write(fips_header)
    outfile.write('\n\n')
    pprint(fips_dict, stream=outfile)

