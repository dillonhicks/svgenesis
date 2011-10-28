from svgenesis.core import *
from svgenesis.composites import GridLines
from svgenesis.primitives import Group, Text

class AbstractGridGraph(Group):
    """
    Provides a grid graph on which to plot appropriate 2D grid based
    graphs. Contains the logic for the grid for the graph, title, x
    axis label and y axis label.
    """
    def __init__(self,  width=0, height=0, title="Simple Grid Graph", x_axis_label="x-axis", 
                 y_axis_label="y-axis", x_offset=0, y_offset=0, vert_padding=25, 
                 horz_padding=25, vert_lines=10, horz_lines=10, fill='white', 
                 opacity=1.0, stroke=rgb(255,255,255), stroke_width=1, stroke_opacity=1.0, 
                 show_vert_lines=True, show_horz_lines=True):
        """
        :param width: The maximum width (x-dimension) of the gridgraph
            including labels and gridlines.
        :param height: The maximum height (y-dimension) of the
            gridgraph including labels and gridlines.
        :param title: The text label for the entire graph. Normally centered on the width.
        :param x_axis_label: The label for the x axis of the graph.
        :param y_axis_label: The label for the y axis of the graph
        :param x_offset: The offset for graph image within the document on the x axis.
        :param y_offset: The offset for graph image within the document on the y axis.
        :param vert_padding: The amount of space between the graph
          image and the horizontal sides of the document. This could
          also be deemed a top/bottom margin since it gives space
          (equally divided) to each the top and bottom of the document
          for labels.
        :param horz_padding:The amount of space between the graph
          image and the vertical sides of the document. This could
          also be deemed a left/right margin since it gives space
          (divided equally) to each the left and right of the document
          for labels.
        :param vert_lines: The number of vertical lines for the grid.
        :param horz_lines: The number of horizontal lines for the grid.
        :param fill: The background fill color for the grid.
        :param opacity: The opacity of the grids background fill color.
        :param stroke: The boarder color of the grid.
        :param stroke_width: The width of the grid's border.
        :param stroke_opacity: The opacity of the grid's border.
  
        :type width: int or float
        :type height: int or float
        :type title: str
        :type x_axis_label: str
        :type y_axis_label: str
        :type x_offset: int or float
        :type y_offset: int or float
        :type vert_padding: int or float
        :type horz_padding: int or float
        :type vert_lines: int
        :type horz_lines: int
        :type fill: :class:`rgb`
        :type opacity: int or float
        :type stroke: :class:`rgb`
        :type stroke_width: int or float
        :type stroke_opacity: int or float
        """
        self.width = width
        self.height = height

        # Calculate the width and height of the grid as the difference
        # of the width/height of the document and the respective
        # horizontal/vertical padding (margin) of the grid.
        self.grid_width = width - horz_padding
        self.grid_height = height - vert_padding 

        # Calculates the starting x and y for the grid as half of the
        # padding in each direction since the padding is evenly
        # divided on each side. For example, if the {horz,
        # vert}_padding = 100, then there would be a 50 pixel padding
        # between the grid and the boarder of the document. It follows
        # that the starting x,y coord for the top left corder of the
        # grid would then be (50,50).
        self.grid_x = horz_padding/2.0
        self.grid_y = vert_padding/2.0

        # A simple translation by adding the offset to the expected
        # grid x and y to get the final x and y of the grid.
        self.grid_x += x_offset 
        self.grid_y += y_offset
      
        self.cell_height = float(self.grid_height)/horz_lines
        self.cell_width = float(self.grid_width)/vert_lines
 
        self.grid_lines = GridLines(
            x=self.grid_x, y=self.grid_y, width=self.grid_width, height=self.grid_height, 
            vert_lines=vert_lines,  horz_lines=horz_lines, 
            fill=fill, opacity=opacity, stroke=stroke, 
            stroke_width=stroke_width, stroke_opacity=stroke_opacity,
            show_vert_lines=show_vert_lines, show_horz_lines=show_horz_lines)
        

        # TODO: Make these calulations a little more robust. These are
        # completely hacked at the moment.
        self.title = Text(title, width/3, 75)
        self.x_axis_label = Text(x_axis_label, width/2.5, self.height-25)
        self.y_axis_label = Text(y_axis_label, 75, height/2, rotation=(90,25,height/2))
        
        all_elements = [self.grid_lines, self.title, self.x_axis_label, self.y_axis_label]

        Group.__init__(self, elements = all_elements)

      
