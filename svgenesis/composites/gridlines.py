from svgenesis.core import *
from svgenesis.primitives import *
from svgenesis.namespace import SVGENESIS_TYPE


class GridLines(Group):
    """
    Gridlines is a rectangle for which there is specified number of
    evenly spaced vertical and horizontal lines such that it makes a
    grid. Gridlines can be used as an SVG representation of a
    cortesian plane or something for which the analogy.
    """
    
    def __init__(self, x=0, y=0, width=0, height=0, vert_lines=10, 
                 horz_lines=10, fill=rgb(255, 255, 255), opacity=1.0, stroke=rgb(255,255,255), 
                 stroke_width=1, stroke_opacity=1.0, show_vert_lines=True, 
                 show_horz_lines=True):

        self.background = Rectangle(x=x, y=y, width=width, height=height, 
                                    stroke_width=stroke_width, stroke_opacity=stroke_opacity, 
                                    stroke=stroke, fill=fill, opacity=opacity)


        self.show_vert_lines = show_vert_lines
        self.show_horz_lines = show_horz_lines

        # The number of vertical | and horizonatal - lines in the
        # grid.
        self.vert_lines = vert_lines
        self.horz_lines = horz_lines
                
        # Contains all lines, both horizontal and vertical
        self.line_list = []
        # Contians horizontal lines only as a convenience.
        self.horz_line_list = []
        # Contians vertical lines only as a convenience.
        self.vert_line_list = []
        
        vert_interval = float(self.background.width)/self.vert_lines
        horz_interval = float(self.background.height)/self.horz_lines
        
        # Plus 1 to get both borders inclusive.
        for v in xrange(self.vert_lines+1):
            x_coord = v * vert_interval + self.background.x
            y = self.background.y
            y2 = y + self.background.height

            if self.show_vert_lines or \
                    (v == 0 or v == self.vert_lines):
                v_line = Line(x_coord, y, x_coord, y2)
            else:
                v_line = Line(x_coord, y, x_coord, y2, stroke_opacity=0)

            self.line_list.append(v_line)
            self.vert_line_list.append(v_line)

        for h in xrange(self.horz_lines+1):
            y_coord = h * horz_interval + self.background.y
            x = self.background.x
            x2 = x + self.background.width
            if self.show_horz_lines or \
                    (h == 0 or h == self.horz_lines):

                h_line = Line(x, y_coord, x2, y_coord)
            else:
                h_line = Line(x, y_coord, x2, y_coord, stroke_opacity=0)
            self.line_list.append(h_line)
            self.horz_line_list.append(h_line)

        all_elements = [self.background] + self.line_list
        Group.__init__(self, elements=all_elements)

