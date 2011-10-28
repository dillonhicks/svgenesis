from svgenesis.core import *
from svgenesis.namespace import SVGENESIS_TYPE
from svgenesis.primitives import Path, Group
from svgenesis.primitives.path import *



class OuterEvilEye(Path):
    DEFAULT_POINTS = (
        MovePoint(495.63381, 632.00091),
        ContinuePoint(410.85888, 282.66508),
        ContinuePoint(365.39353, 674.5939),
        ContinuePoint(451.85833, 293.45941),
        ContinuePoint(289.29921, 711.38722),
        ContinuePoint(492.91849, 388.3485),
        ContinuePoint(169.1766, 658.8315),
        ContinuePoint(508.41198, 468.33371),
        ContinuePoint(96.018192, 530.93046),
        ContinuePoint(473.12094, 479.39381),
        ContinuePoint(60.601587, 428.4282),
        ContinuePoint(415.97189, 537.10728),
        ContinuePoint(34.639441, 325.69984),
        ContinuePoint(377.06027, 597.41481),
        ContinuePoint(133.95501, 224.92057),
        ContinuePoint(309.50596, 575.43662),
        ContinuePoint(248.61377, 131.41978),
        ContinuePoint(212.51013, 544.28989),
        ContinuePoint(346.5313, 121.11004),
        ContinuePoint(194.72763, 498.28005),
        ContinuePoint(477.85551, 156.15285),
        ContinuePoint(167.08427, 427.73314),
        ContinuePoint(540.38578, 218.30275),
        ContinuePoint(169.2978, 360.61593),
        ContinuePoint(635.04718, 352.92366),
        ContinuePoint(185.73111, 306.25622),
        ContinuePoint(641.45513, 462.72561),
        ContinuePoint(291.38205, 270.46294),
        ContinuePoint(615.68903, 570.82239),
        ContinuePoint(329.36083, 243.70228),
        ContinuePoint(495.63381, 632.00091),
        ClosePoint())
    def __init__(self, x, y, fill=rgb(0,0,0), stroke=rgb(0,0,0), stroke_width=1.0, 
                 opacity=1.0, stroke_opacity=1.0):
        Path.__init__(self, points=self.DEFAULT_POINTS, fill=fill,
                      stroke_width=stroke_width, stroke_opacity=stroke_opacity, 
                      opacity=opacity, stroke=stroke)
    def to_node(self):
        node = Path.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'OuterEvilEye')
        return node



class InnerEvilEye(Path):
    DEFAULT_POINTS = (
        MovePoint(351.04951, 355.28773), 
        BiezerCubicPointR(-1.2828,4.65836, -2.5611,9.31771, -3.59635,14.03992),
        ContinuePoint(-0.92356,4.83462, -2.84215,9.38439, -4.22551,14.08849),
        ContinuePoint(-0.85783,4.28323, -1.8647,8.52549, -2.91121,12.76504),
        ContinuePoint(-1.36044,3.75817, -1.5703,7.46642, -1.29518,11.40628),
        ContinuePoint(0.32451,3.28636, 0.59617,6.57483, 0.69131,9.8762),
        ContinuePoint(0.0363,3.20918, -0.0216,6.41877, -0.0461,9.62795),
        ContinuePoint(-0.0213,2.92765, -0.02,5.8554, -0.0176,8.78311),
        ContinuePoint(0.36274,2.37555, -1.4488,4.4267, -1.33019,6.72871),
        ContinuePoint(0.79031,2.33997, 1.19639,4.73524, 1.38693,7.1909),
        ContinuePoint(-0.23287,0.45588, 0.37881,4.59214, 0.26676,4.77996),
        ContinuePoint(-0.0749,0.1255, -0.23284,-0.40608, -0.32581,-0.29333),
        ContinuePoint(-4.42012,5.36097, -8.61301,10.90531, -12.91952,16.35797),
        ContinuePoint(4.39716,-10.04331, 10.88005,-18.01859, 17.24359,-27.33592),
        ContinuePoint(-20.13972,28.17393, -11.03039,18.06556, -8.35577,11.34836),
        ContinuePoint(0.83656,-2.10099, 1.34376,-4.2354, 1.78003,-6.44597),
        ContinuePoint(0.70705,-5.18285, 0.44472,-10.43356, 0.30543,-15.6449),
        ContinuePoint(-0.22948,-5.06707, -0.0806,-10.14342, -0.35629,-15.20698),
        ContinuePoint(-0.54953,-5.20186, -1.06875,-10.40416, -1.3304,-15.62942),
        ContinuePoint(-0.14047,-3.00102, -0.0679,-6.00514, -4.1e-4,-9.00682),
        ContinuePoint(0.0619,-3.17907, 0.0631,-6.35886, 0.0603,-9.5384), 
        ContinuePoint(-0.006,-2.85664, -0.0118,-5.71327, -0.0142,-8.56992),
        ContinuePoint(0,0, 13.59432,-16.43472, 13.59432,-16.43472), 
        LinePointR(0,0), 
        BiezerCubicPointR(10e-4,2.85837, 0.004,5.71673, 0.009,8.57509),
        ContinuePoint(0.003,3.18732, 0.003,6.37472, -0.0304,9.56191),
        ContinuePoint(-0.0339,2.98787, -0.17041,5.97461, -0.11854,8.96315),
        ContinuePoint(0.14792,5.22321, 0.57869,10.42963, 1.24221,15.61319),
        ContinuePoint(0.49437,5.075, 0.1998,10.183, 0.43498,15.27556),
        ContinuePoint(0.14455,5.28962, 0.4293,10.5951, 0.0176,15.87943),
        ContinuePoint(-1.60114,12.51443, -8.28074,19.39805, -16.31015,30.48241),
        ContinuePoint(3.43647,-5.14868, 6.88603,-10.28864, 10.3094,-15.44603),
        ContinuePoint(0.43492,-0.65523, -0.91898,1.27737, -1.34383,1.93917),
        ContinuePoint(-1.81431,2.82617, -0.51741,0.81405, -1.70506,3.639),
        ContinuePoint(-1.21323,2.88581, -0.24175,-0.19587, -0.9502,2.23502),
        ContinuePoint(-7.88995,10.12467, -15.03918,25.65409, -15.0092,11.40929),
        ContinuePoint(-0.0695,-2.34356, -0.17385,-4.72091, -1.09989,-6.91234),
        ContinuePoint(-1.26164,-3.28031, 0.13454,-3.9837, 0.95534,-7.07908),
        ContinuePoint(-0.003,-2.93535, -0.007,-5.87074, 0.0132,-8.80604),
        ContinuePoint(0.0237,-3.19449, 0.063,-6.38885, 0.0783,-9.5834),
        ContinuePoint(-0.0194,-3.28266, -0.19011,-6.55916, -0.5595,-9.82262),
        ContinuePoint(-0.3741,-4.03281, -0.84912,-7.98496, 0.80245,-11.82404),
        ContinuePoint(0.88405,-4.29579, 2.32473,-8.46747, 2.85252,-12.84155),
        ContinuePoint(1.20366,-4.75702, 3.19179,-9.24613, 4.34825,-14.01685),
        ContinuePoint(0.88752,-4.70666, 2.04607,-9.39215, 3.52499,-13.94539),
        ContinuePoint(0,0, 13.93429,-16.18239, 13.93429,-16.18239),
        ClosePoint())

    def __init__(self, x, y, fill=rgb(255,204,0), stroke=rgb(255,204,0), stroke_width=1.0, 
                 opacity=1.0, stroke_opacity=1.0):
        Path.__init__(self, points=self.DEFAULT_POINTS, fill=fill,
                      stroke_width=stroke_width, stroke_opacity=stroke_opacity, 
                      opacity=opacity, stroke=stroke)
    

    def to_node(self):
        node = Path.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'InnerEvilEye')
        return node


class EvilEye(Group):

    def __init__(self, x, y):
        elems = []
        elems.append(OuterEvilEye(x, y))
        elems.append(InnerEvilEye(x, y))
        Group.__init__(self, elements=elems)

    def to_node(self):
        node = Group.to_node(self)
        # Add the extra information to the XML tag to help parsing to
        # the object from XML.
        node.setAttribute(SVGENESIS_TYPE, 'EvilEye')
        return node
