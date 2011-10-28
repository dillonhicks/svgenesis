"""
:mod:`activitytimeline` -- Binary State Activity Interval Visualizations
=========================================================================
 
.. moduleauthor:: Dillon Hicks <hhicks@ittc.ku.edu>

This module allows for the representation of the set of state based
interval data for a set of activitys as an activity timeline. This
translates to a parallel waveform representation of each activity (y
axis) where the activity state in question is represented as a color
filled rectangle across that spans the time of the interval (x axis).

"""

import random
from svgenesis.core import *
from svgenesis.primitives import Rectangle
from svgenesis.templates.abstractgridgraph import *

#################################
###      Helper Classes       ###
#################################

class Interval: 
    """
    A container a time interval supporting a start time, end time and
    calculation of a total time duration.
    """
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def calculate_total_time(self):
        """
        Calcultaes the total interval time as the difference of the
        start_time and the end_time.
        """
        return self.end_time - self.start_time
    total_time = property(calculate_total_time)
    
    def __str__(self):
        return '(%s, %s)' % (self.start_time, self.end_time)
    


class Activity:
    """
    An activity has multiple active Intervals (as a list). In turn an
    activity may be plotted on a wave-form in ActivityTimelineGraph,
    where each high time on the ActivityTimelineGraph corresponds to
    an active interval for the activity.
    """
    def __init__(self, name='activity'):
        """
        :param name: The name (id) of the Activity, will be used as a
            label when applicable.
        :type name: str
        """
        self.active_intervals = []
        self.name = name

    def add_interval(self, start_time, end_time):
        """
        Add an interval to the active intervals list for this
        Activity.
        """ 
        a_interval = Interval(start_time, end_time)
        self.active_intervals.append(a_interval)
        return a_interval

    def remove_interval(self, interval):
        """
        Remove the interval from the active_intervals.  
        :returns: True if the interval was found and removed and False
          if the interval was not found.
        """
        if interval in self.active_intervals:
            self.active_intervals.remove(interval)
            return True
        return False

########## END HELPER CLASSES ################

class ActivityTimelineGraph(AbstractGridGraph, Interval):
    
    CELL_HEIGHT_RATIO = 0.65
    def __init__(self,  width=0, height=0, start_time=0, end_time=0, time_samples=10, 
                 max_activities=10, title="Simple Grid Graph", x_axis_label="x-axis", 
                 y_axis_label="y-axis", x_offset=50, y_offset=0, vert_padding=200, 
                 horz_padding=200, fill='white',  
                 opacity=0.0, stroke=rgb(255,255,255), stroke_width=1, 
                 stroke_opacity=1.0, show_vert_lines=True, show_horz_lines=True):
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
        Interval.__init__(self, start_time, end_time)
        AbstractGridGraph.__init__(
            self, width, height, title, x_axis_label, 
            y_axis_label, x_offset, y_offset, vert_padding, 
            horz_padding, time_samples, max_activities, fill, 
            opacity, stroke, stroke_width, stroke_opacity,
            show_vert_lines=show_vert_lines, show_horz_lines=show_horz_lines)



        self.maximum_activities = max_activities
        self.time_samples = time_samples                
        self.activities = []
        self.time_ratio = float(self.grid_width)/self.total_time

        self.skip_lines = True

        self.time_labels = []
        # Make the time interval for each of the intervals for the X
        # axis.
        for i in xrange(self.time_samples+1):
            stime = i * float(self.total_time)/self.time_samples + self.start_time
            x_coord = self.grid_x + i * float(self.grid_width)/self.time_samples
            y_coord = self.grid_y + self.grid_height
            self.time_labels.append(Text('--'+str(stime), x_coord, y_coord, 
                                              font_size=20, rotation=(45, x_coord-10, y_coord)))

            
    def add_activity(self, act):
        """
        Appends `act` to the activities list.
        
        :param act: The activity to add to the Timeline.
        :type act: Acivity
        """
        self.activities.append(act)

       
    def get_interval_code(self):
        """
        Get the resulting xml code for each of the intervals for each
        of the activities.
        """
        # Holds the xml fragment for each activity interval 
        activity_code = []
        
        # The maximum height that the active interval rectangle with
        # have within its respective grid-graph cell.
        height = self.cell_height * self.CELL_HEIGHT_RATIO 
        
        for (index, activity) in enumerate(self.activities):
            if self.skip_lines:
                index *= -2 
                index -= 1
            else:
                index += 1
                index *= -1 # To fill graph from bottom up
            red = random.randint(0,50)
            green = random.randint(0,50)
            blue = random.randint(100,256)

            color =  rgb(red, green, blue)
            opacity = (75 + random.randint(0,26))*10**-2
            line = self.grid_lines.horz_line_list[index]
            activity_code.append(Text(activity.name, 0, line.y, font_size=25)) 
            
            for interval in activity.active_intervals:
                if interval.start_time < self.start_time:
                    if interval.end_time > self.start_time:
                        interval = Interval(self.start_time, interval.end_time)
                    else:
                        continue
                elif interval.start_time > self.end_time:
                    continue
                
                if interval.end_time > self.end_time:
                    if interval.start_time <  self.end_time:
                        interval = Interval(interval.start_time, self.end_time)
                    else:
                        continue

                x_coord = self.grid_x + (interval.start_time-self.start_time) * self.time_ratio
                width = interval.total_time * self.time_ratio
                line = self.grid_lines.horz_line_list[index]
                y_coord = line.y - height

                activity_code.append(Rectangle(x_coord, y_coord, width, height, 
                                               fill=color, opacity=opacity))
        return activity_code


    def to_node(self):
        node = AbstractGridGraph.to_node(self)
        intervals_group = Group( elements=self.get_interval_code())
        node.appendChild(intervals_group.to_node())
        return node
    
    def __str__(self):
        return self.to_node.toxml()


