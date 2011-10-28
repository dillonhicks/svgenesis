#!/usr/bin/env python
import sys
import os
import random
import math
import unittest
import textstyle as style


from svgenesis.primitives import *
from svgenesis.composites import *
from svgenesis.templates.abstractgridgraph import *
from svgenesis.templates.activitytimeline import *

TEST_OUTPUT_DIR = os.getcwd()+'/test_out/'

#####################################################
#
# Random Primitive Generators and Helper Functions
#
######################################################

def gen_shape_style(count=1):
    color = rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    stroke = rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    stroke_opacity = random.uniform(0.5,1.0)
    opacity = random.uniform(0.5,1.0)
    stroke_width = random.randint(1, 10)
    return color, stroke, stroke_opacity, opacity, stroke_width


def gen_colored_rectangles(count=20):
    for num_rectangles in range(count):
        x, y, width, height = (random.uniform(100,1000), random.uniform(100,1000), 
                               random.uniform(0,200),random.uniform(0,200))
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        rect = Rectangle(x, y, width, height, fill=color, 
                         stroke=stroke, stroke_opacity=stroke_opacity,
                         opacity=opacity, stroke_width=stroke_width)

        yield rect


def gen_squares(count=20):
    for num_squares in range(count):
        x, y, side_len = (random.uniform(100,1000), random.uniform(100,1000), 
                          random.uniform(100, 1000))
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        square = Square(x, y, side_length=side_len, fill=color, 
                      stroke=stroke, stroke_opacity=stroke_opacity,
                      opacity=opacity, stroke_width=stroke_width)

        yield square



def gen_circles(count=20):
    for num_circles in range(count):
        circ = Circle(random.uniform(100,1000),
                      random.uniform(100,1000),random.uniform(0,100))

        #print repr(circ)
        yield circ

def gen_colored_circles(count=20):
    for num_circles in range(count):
        cx, cy, radius = (random.uniform(100,1000),
                          random.uniform(100,1000),
                          random.uniform(0,100))
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        circ = Circle(cx, cy, radius, fill=color,
                      stroke=stroke, stroke_opacity=stroke_opacity,
                      opacity=opacity, stroke_width=stroke_width)

        #print repr(circ)
        yield circ

def gen_colored_ellipses(count=20):
    for num_ellipses in range(count):
        cx, cy, rx, ry = (random.uniform(100,1000),random.uniform(100,1000),random.uniform(0,100),random.uniform(0,100))
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        ellipse = Ellipse(cx, cy, rx, ry, fill=color,
                          stroke=stroke, stroke_opacity=stroke_opacity,
                         opacity=opacity, stroke_width=stroke_width)

        #print repr(ellipse)
        yield ellipse
    
def gen_random_points(count=20):
    for p in range(count):
        rx = random.randint(100,2000)
        ry = random.randint(100,2000)
        yield (rx, ry)

def gen_colored_polygons(count=20):
    for polygon in range(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        yield Polygon([point for point in gen_random_points()], 
                      stroke_width=stroke_width, opacity=opacity, 
                      stroke_opacity=stroke_opacity, stroke=stroke, fill=color)


def gen_prism_lines(count=20):
    for x2, y2 in gen_random_points(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        width = random.randint(1,10)
        ln = Line(0, 0, x2, y2, stroke=stroke, stroke_width=stroke_width)
        #print repr(ln)
        yield ln


def gen_time_intervals(min_size, max_size, max_time=100000):
    r = random.randint(min_size, max_size)
    q = max_time/float(r)
    for i in xrange(r):
        stime = i * q
        etime = random.randint(int(stime), int(stime+q))
        yield (stime, etime)

def gen_activities(max_size=25, step=25, count=5):
    lower = 1
    upper = lower+max_size
    for num_act in range(count):
        act = Activity("Thread-%i" % num_act)
        for stime, etime in gen_time_intervals(lower, upper):
            act.add_interval(stime, etime)
        lower += step
        upper = lower+max_size
        yield act
        
def gen_triangles(count=10):
    for num_triangle in xrange(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        p1, p2, p3 = [point for point in gen_random_points(3)] 
    
        tri = Triangle((p1, p2, p3), stroke_width=stroke_width, opacity=opacity, 
                 stroke_opacity=stroke_opacity, stroke=stroke, fill=color)
        #print repr(tri)
        yield tri
    
import math
def gen_equilateral_triangles(count=10):
    for num_triangle in xrange(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        side_length = random.randint(100,300)
        cx, cy = [point for point in gen_random_points(1)][0]
        rotation = random.randint(1, 121)
            
        tri = EquilateralTriangle(cx=cx, cy=cy, rotation=rotation, side_length=side_length, stroke_width=stroke_width, opacity=opacity, 
                 stroke_opacity=stroke_opacity, stroke=stroke, fill=color)
        #print repr(tri)
        yield tri


def gen_equilateral_pentagons(count=10):
    for num_pentagon in xrange(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        side_length = random.randint(100,300)
        cx, cy = [point for point in gen_random_points(1)][0]
        rotation = random.randint(1, 121)
            
        tri = EquilateralPentagon(cx=cx, cy=cy, rotation=rotation, 
                                  side_length=side_length, stroke_width=stroke_width, opacity=opacity, 
                                  stroke_opacity=stroke_opacity, stroke=stroke, fill=color)
        #print repr(tri)
        yield tri
    

def gen_equilateral_hexagons(count=10):
    for num_hexagon in xrange(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        side_length = random.randint(100,300)
        cx, cy = [point for point in gen_random_points(1)][0]
        rotation = random.randint(1, 121)
            
        tri = EquilateralHexagon(cx=cx, cy=cy, rotation=rotation, 
                                  side_length=side_length, 
                                 stroke_width=stroke_width, opacity=opacity, 
                                  stroke_opacity=stroke_opacity, 
                                 stroke=stroke, fill=color)
        #print repr(tri)
        yield tri

def gen_stars(count=10):
    for num_star in xrange(count):
        color, stroke, stroke_opacity, opacity, stroke_width = gen_shape_style()
        ri = random.randint(50,300)
        ro = random.randint(ri+100,ri+500)
        num_points = random.randint(3,10)
        cx, cy = [point for point in gen_random_points(1)][0]
        rotation = random.randint(1, 121)
            
        tri = Star(cx=cx, cy=cy, ro=ro, ri=ri,
                   rotation=rotation, 
                   num_points=num_points, 
                   stroke_width=stroke_width, opacity=opacity, 
                   stroke_opacity=stroke_opacity, 
                   stroke=stroke, fill=color)
        #print repr(tri)
        yield tri
    

#####################################################
#
# Auto-Gen Images From XML Node
#
######################################################
class XMLAutogenTest(unittest.TestCase):
    IMAGE_WIDTH = 2200
    IMAGE_HEIGHT = 2200
    OUT_PREFIX = TEST_OUTPUT_DIR + 'autogen_xml_'
    

    def test_svg_document(self):
        """Autogen (XML): 20 Rectangles, 20 Circles and 20 Ellipses""" 
        # Doc test with primatives
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for rect in gen_colored_rectangles():
            doc.add_svg_object(rect)
    
        for ellipse in gen_colored_ellipses():
            doc.add_svg_object(ellipse)

        for circle in gen_colored_circles():
            doc.add_svg_object(circle)

        with open( self.OUT_PREFIX + 'SVGDocument_test.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())

    def test_gridlines(self):
        """Autogen (XML): Gridlines"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)
        
        doc.add_svg_object(GridLines(0, 0, 1000, 1000))

        with open( self.OUT_PREFIX + 'gridlines_xml.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())


    def test_prism_lines(self):
        """Autogen (XML): Prism Lines"""
        # Lines from corners
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)
    
        for line in gen_prism_lines(100):
            doc.add_svg_object(line)

        with open( self.OUT_PREFIX + 'prism_lines.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())

    def test_timeline(self):
        """Autogen (XML): ActivityTimelineGraph with random data"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)
        timeline =  ActivityTimelineGraph(
            2000, 1000, 0, 60000, 20, 10, "Activity Timeline Graph",  'Time', 
            y_axis_label='', vert_padding=250, horz_padding=200, 
            y_offset=-30, show_vert_lines=False)
    
        for act in gen_activities():
            timeline.add_activity(act)

        doc.add_svg_object(timeline)

        with open( self.OUT_PREFIX + 'timelinegraph_xml.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())



    def test_triangles(self):
        """Autogen (XML): 10 Triangles"""
        # Doc test with primatives
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for triangle in gen_triangles():
            doc.add_svg_object(triangle)

        with open( self.OUT_PREFIX + 'triangles.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())
    

    def test_equilateraltriangles(self):
        """Autogen (XML): 10 EquilateralTriangles"""
        # Doc test with primatives
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for triangle in gen_equilateral_triangles():
            doc.add_svg_object(triangle)

        with open( self.OUT_PREFIX + 'equilateraltriangles.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())

    def test_equilateralpentagons(self):
        """Autogen (XML): 10 EquilateralPentagons"""
        # Doc test with primatives
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for pentagon in gen_equilateral_pentagons():
            doc.add_svg_object(pentagon)

        with open( self.OUT_PREFIX + 'equilateralpentagons.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())
    

    def test_equilateralhexagons(self):
        """Autogen (XML): 10 EquilateralHexagons"""
        # Doc test with primatives
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for hexagon in gen_equilateral_hexagons():
            doc.add_svg_object(hexagon)

        with open( self.OUT_PREFIX + 'equilateralhexagons.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())

    def test_square(self):
        """Autogen (XML): 10 Squares with varying numbers of points"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for square in gen_squares():
            doc.add_svg_object(square)

        with open( self.OUT_PREFIX + 'squares.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())
    

    def test_star(self):
        """Autogen (XML): 10 Stars with varying numbers of points"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        for star in gen_stars():
            doc.add_svg_object(star)

        with open( self.OUT_PREFIX + 'stars.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())


    def test_path(self):
        """Autogen (XML): Paths"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        points = (
        PathPoint('M', 500, 100),
        PathPoint('L', 800, 400),
        PathPoint('L', 500, 700),        
        PathPoint('C', 200, 400, 10, 10, 10, 10),
        #PathPoint('L', 400, 200),
        PathPoint('L', 240, 190),
        PathPoint('L', 240, 150),
        PathPoint('L', 500, 100),
        PathPoint('Z'))

        doc.add_svg_object(Path(points, fill=rgb(140,140,140), opacity=0.7))

        with open( self.OUT_PREFIX + 'paths.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())


    def test_evileye(self):
        """Autogen (XML): EvilEye"""
        doc = SVGDocument(self.IMAGE_WIDTH, self.IMAGE_HEIGHT)

        doc.add_svg_object(EvilEye(0,0))

        with open( self.OUT_PREFIX + 'evileye.svg', 'w') as outfile:
            outfile.write(doc.toprettyxml())


      

 

if __name__ == "__main__":
  
    print 
    print style.bold_blue_text('svgtests.py')
    print

    if not os.path.exists(TEST_OUTPUT_DIR):
        os.mkdir(TEST_OUTPUT_DIR)

    
    try:
        unittest.main()
    except SystemExit:
        pass

    print
    print style.bold_text("[Information]:"), "This test created a series of"\
        "output images that can be used as a sanity check. "\
        "These images are located at:\n\n%s\n" % TEST_OUTPUT_DIR
