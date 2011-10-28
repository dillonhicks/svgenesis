#!/bin/env python
"""
itervals2timeline.py

"""
import random 
from svgenesis.primitives import generate_template
from svgenesis.templates.activitytimeline import *

##############################################
# Bogus value generation for default values,
# provides a little demo of how it can work.
# Just run ./intervals2timeline.py and look
# at bogus_timeline.svg.
##############################################
BOGUS_COUNT = 5
BOGUS_NAMES = ','.join(['Activity-%i' % i for i in range(1,BOGUS_COUNT+1)])
def _bogus_intervals():
    intervals='['
    for i in range(4):
        s_time = random.uniform(0,1)
        e_time = random.uniform(s_time,(s_time*2.0%1.0))
        intervals += '(%s,%s),'%(s_time,e_time)
    intervals += ']'
    return intervals

BOGUS_INTERVALS = ','.join([ _bogus_intervals() for x in range(BOGUS_COUNT)])


######################################################
# Functions to parse the command line options into Python data
# structures.
######################################################
def make_name_list(names):    
    """
    Split the comma separated activity names, as specified on the
    command line, into a list of strings.
    """
    return names.split(',')

def make_interval_list(interval_str):
    """
    Process the interval lists from the command line into separate
    lists of 2-tuples. Each list corresponds to an activity name, and
    each 2-tuple to an active interval.
    """
    tuples_lists = eval(interval_str)
    if len(tuples_lists) == 1:
        tuples_lists = (tuples_lists,)
    return tuples_lists
                                   
def create_activities(names, interval_lists):
    """
    Create :class:`activitytimeline.Activity` objects to add to the
    :class:`ActivityTimelineGraph` instance in
    :func:`create_timeline()`. The result of which is that each of the
    activities will show up on the resultant timeline graph.
    """
    # Sanity checking, they should be equal or an activity will not
    # have intervals, or there will be intervals for which there is no
    # corresponding activity.
    assert(len(names) == len(interval_lists))
    activities = []
    for (i, name) in enumerate(names):
        intervals = interval_lists[i]
        act = Activity(name)
        for it in intervals:
            act.add_interval(it[0], it[1])
        activities.append(act)
    return activities


##############################################
# TIMELINE CREATION HERE
##############################################
def create_timeline():
    """
    Creates the timeline.
    """
    # Getting rid of the Param.
    width = Params.width 
    height = Params.height
    title = Params.title
    x_axis_label = Params.xaxis_label
    y_axis_label = Params.yaxis_label
    names = make_name_list(Params.names)
    intervals = make_interval_list(Params.intervals)
    time_samples = Params.time_samples

    # Each name corresponds to an activity, so the number of names
    # should be the maximum number of activities.
    max_activities = len(names)
    if len(names) < 10:
        # This configuration is more aesthetically pleasing for lower
        # numbers since this also determines the number of horizontal
        # lines.
        max_activities = 10
    
    # The start and end times of the window of intervals from which to
    # make the time line.
    start_time = Params.start_time
    end_time = Params.end_time

    timeline = ActivityTimelineGraph(width=width,
                                     height=height,
                                     start_time=start_time,
                                     end_time=end_time,
                                     title=title,
                                     x_axis_label=x_axis_label,
                                     y_axis_label=y_axis_label,
                                     time_samples=time_samples,
                                     max_activities=10  )

    # Create and add all of the activites to the timeline so they can
    # be graphed.
    for act in create_activities(names, intervals): 
        timeline.add_activity(act)
    
    filename = Params.outfile
    with open(filename, 'w') as outfile:
        template_str = generate_template(width, height)
        filetext = template_str % dict(SVG_IMAGE_CODE=str(timeline))
        outfile.write(filetext)
    

                          

########################################################
#
# All of the test modules will need the same options front
# end, so this can be imported where one would normally
# place the optparse template. 
#
if __name__ == '__main__':
    # imports required if this module is called as a
    # command
    import optparse, sys, os
    from pprint import *
    
    # Define the set of permitted parameters, including the
    # command arguments.  The initialization method creates
    # the parser and defines the defaults. The parse()
    # method actually parses the arguments one the command
    # line. This was done so that the instance of the class
    # could be global and thus available to all
    # routines. and then parse the arguments to this call
    # according to the specification
    class Params_Set:
        USAGE = "usage: %prog [options]"
    
        def __init__(self):
            # Create the argument parser and then tell it
            # about the set of legal arguments for this
            # command. The parse() method of this class
            # calls parse_args of the optparse module
            self.p = optparse.OptionParser(usage=self.USAGE)
    
            # Boring and totally standard verbose and
            # debugging options that should be common to
            # virtually any command
            #
            self.p.add_option("-d", action="store_const", const=1,        
                              dest="debug_level", 
                              help="Turn on diagnostic output at level 1")
            self.p.add_option("-D", action="store", type ="int",    
                              dest="debug_level", 
                              help="Turn on diagnostic output at level DEBUG_LEVEL")
            self.p.add_option("-v", action="store_const", const=1,        
                              dest="verbose_level", 
                              help="Turn on narrative output at level 1")
            self.p.add_option("-V", action="store", type ="int",    
                              dest="verbose_level", 
                              help="Turn on narrative output at level VERBOSE_LEVEL")
            
            # Command specific options. We can specify a
            # configuration file to parse, which defaults to
            # stdin, and an output file name, which defaults
            # to stdout.
            self.p.add_option("-o", "--outfile", action="store", type ="string", 
                              dest="outfile", 
                              help="The name of the .svg file produced without suffix.")
    
    
        
            # Now tell the parser about the default values of all the options
            # we just told it about
            self.p.set_defaults(
                debug_level      = 0,          
                verbose_level    = 0,
                outfile          = 'timeline.svg',
                height           = 800,
                width            = 1200,
                time_samples     = 20,
                names            = BOGUS_NAMES,
                intervals        = BOGUS_INTERVALS,
                title            = 'Bogus Timeline',
                yaxis_label      = '',
                xaxis_label      = 'Time',
                start_time       = 0,
                end_time         = 1,
                )       
            
        def parse(self):
            self.options, self.args = self.p.parse_args()
            self.debug_level     = self.options.debug_level    
            self.verbose_level   = self.options.verbose_level  
            self.outfile          = self.options.outfile
            self.height         = self.options.height 
            self.width          = self.options.width  
            self.time_samples    = self.options.time_samples
            self.names          = self.options.names      
            self.intervals      = self.options.intervals  
            self.title          = self.options.title      
            self.yaxis_label    = self.options.yaxis_label
            self.xaxis_label    = self.options.xaxis_label
            self.start_time     = self.options.start_time
            self.end_time       = self.options.end_time
        # Defining this method defines the string representation of the
        # object when given as an argument to str() or the "print" command
        #
        def __str__(self):
            param_print_str = \
    """Parameters:
      debug_level    : %d
      verbose_level  : %d
      outfile         : %s
    """ 
    
            str_output = param_print_str % \
                (self.debug_level, 
                 self.verbose_level,
                 self.outfile)  
            
            return str_output
        
    def main():
        # Global level params class instance was
        # created before calling main(). We make it
        # global so that other code can access the set
        # of Parameters, simply by accessing the Params
        # instance. Here, however, we call the parse()
        # method to actually get the arguments, since
        # we have been called from the command line.
        Params.parse()
        debug_level = Params.debug_level
        if Params.debug_level >= 2:
            print Params
        
        create_timeline()
            
        
        
        
    
    global Params
    Params = Params_Set()
    
    main()
