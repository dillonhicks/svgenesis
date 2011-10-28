#!/usr/bin/env python
""" 
primitivestest.py
====================

Unit testing for all of SVG primitives in svgenesis.primitives.

Each primitive class has its own Test class that contains 100 class
objects and 100 XML strings. There are two test function for each
class.  

The first test function test_<class-name>_to_xml() validates
that the object.to_xml() creates the the expected XML string. 

The second test function test_<class-name>_from_xml() validates that
the primitive_from_xml() module function produces the expected object
instance from the xml string.
"""
from svgenesis.core import object_from_xml
from svgenesis.primitives import *
import unittest

class LineTest(unittest.TestCase):
    """Test For svgenesis.primitives.Line"""
    ################################################
    # Line Objects and XML Strings
    ################################################
    line_objects = (
        Line(y2=418, stroke_width=8, x2=567, stroke=rgb(48, 199, 243), y1=0, x1=0),
        Line(y2=131, stroke_width=4, x2=812, stroke=rgb(159, 171, 203), y1=0, x1=0),
        Line(y2=1060, stroke_width=3, x2=983, stroke=rgb(133, 186, 14), y1=0, x1=0),
        Line(y2=177, stroke_width=2, x2=961, stroke=rgb(225, 43, 126), y1=0, x1=0),
        Line(y2=1512, stroke_width=2, x2=488, stroke=rgb(122, 20, 198), y1=0, x1=0),
        Line(y2=958, stroke_width=6, x2=239, stroke=rgb(174, 199, 102), y1=0, x1=0),
        Line(y2=1535, stroke_width=10, x2=892, stroke=rgb(107, 92, 201), y1=0, x1=0),
        Line(y2=260, stroke_width=5, x2=1607, stroke=rgb(212, 220, 94), y1=0, x1=0),
        Line(y2=1178, stroke_width=1, x2=1130, stroke=rgb(82, 128, 149), y1=0, x1=0),
        Line(y2=925, stroke_width=9, x2=273, stroke=rgb(195, 88, 70), y1=0, x1=0),
        Line(y2=664, stroke_width=5, x2=432, stroke=rgb(23, 226, 105), y1=0, x1=0),
        Line(y2=1891, stroke_width=10, x2=438, stroke=rgb(180, 74, 123), y1=0, x1=0),
        Line(y2=388, stroke_width=9, x2=488, stroke=rgb(33, 174, 192), y1=0, x1=0),
        Line(y2=610, stroke_width=8, x2=1664, stroke=rgb(178, 196, 97), y1=0, x1=0),
        Line(y2=1231, stroke_width=8, x2=454, stroke=rgb(89, 1, 164), y1=0, x1=0),
        Line(y2=1657, stroke_width=6, x2=632, stroke=rgb(66, 33, 28), y1=0, x1=0),
        Line(y2=427, stroke_width=4, x2=945, stroke=rgb(154, 58, 152), y1=0, x1=0),
        Line(y2=625, stroke_width=8, x2=1888, stroke=rgb(164, 189, 225), y1=0, x1=0),
        Line(y2=1689, stroke_width=5, x2=972, stroke=rgb(42, 88, 96), y1=0, x1=0),
        Line(y2=1243, stroke_width=5, x2=1317, stroke=rgb(71, 44, 68), y1=0, x1=0),
        Line(y2=114, stroke_width=6, x2=1499, stroke=rgb(52, 155, 188), y1=0, x1=0),
        Line(y2=901, stroke_width=5, x2=529, stroke=rgb(29, 85, 118), y1=0, x1=0),
        Line(y2=1624, stroke_width=8, x2=996, stroke=rgb(157, 235, 227), y1=0, x1=0),
        Line(y2=33, stroke_width=5, x2=1793, stroke=rgb(126, 208, 239), y1=0, x1=0),
        Line(y2=144, stroke_width=7, x2=1773, stroke=rgb(245, 143, 16), y1=0, x1=0),
        Line(y2=716, stroke_width=5, x2=634, stroke=rgb(64, 142, 30), y1=0, x1=0),
        Line(y2=213, stroke_width=7, x2=880, stroke=rgb(148, 17, 193), y1=0, x1=0),
        Line(y2=207, stroke_width=5, x2=1781, stroke=rgb(67, 247, 3), y1=0, x1=0),
        Line(y2=1088, stroke_width=5, x2=538, stroke=rgb(150, 63, 51), y1=0, x1=0),
        Line(y2=853, stroke_width=1, x2=765, stroke=rgb(104, 170, 1), y1=0, x1=0),
        Line(y2=1706, stroke_width=6, x2=582, stroke=rgb(160, 106, 252), y1=0, x1=0),
        Line(y2=1850, stroke_width=4, x2=879, stroke=rgb(173, 67, 178), y1=0, x1=0),
        Line(y2=605, stroke_width=7, x2=29, stroke=rgb(30, 195, 181), y1=0, x1=0),
        Line(y2=1669, stroke_width=5, x2=1990, stroke=rgb(190, 54, 233), y1=0, x1=0),
        Line(y2=292, stroke_width=10, x2=530, stroke=rgb(109, 156, 208), y1=0, x1=0),
        Line(y2=622, stroke_width=9, x2=1933, stroke=rgb(186, 93, 42), y1=0, x1=0),
        Line(y2=1914, stroke_width=2, x2=1986, stroke=rgb(140, 196, 33), y1=0, x1=0),
        Line(y2=1024, stroke_width=8, x2=161, stroke=rgb(190, 77, 156), y1=0, x1=0),
        Line(y2=911, stroke_width=9, x2=1797, stroke=rgb(110, 39, 137), y1=0, x1=0),
        Line(y2=1398, stroke_width=6, x2=1358, stroke=rgb(73, 89, 93), y1=0, x1=0),
        Line(y2=866, stroke_width=2, x2=1607, stroke=rgb(134, 249, 174), y1=0, x1=0),
        Line(y2=1955, stroke_width=9, x2=1781, stroke=rgb(197, 61, 52), y1=0, x1=0),
        Line(y2=1327, stroke_width=4, x2=991, stroke=rgb(168, 17, 220), y1=0, x1=0),
        Line(y2=273, stroke_width=8, x2=1132, stroke=rgb(161, 94, 35), y1=0, x1=0),
        Line(y2=259, stroke_width=6, x2=483, stroke=rgb(213, 116, 159), y1=0, x1=0),
        Line(y2=1116, stroke_width=2, x2=1000, stroke=rgb(74, 173, 166), y1=0, x1=0),
        Line(y2=1080, stroke_width=8, x2=836, stroke=rgb(176, 209, 214), y1=0, x1=0),
        Line(y2=1455, stroke_width=3, x2=685, stroke=rgb(44, 196, 113), y1=0, x1=0),
        Line(y2=1089, stroke_width=8, x2=439, stroke=rgb(186, 39, 46), y1=0, x1=0),
        Line(y2=1255, stroke_width=3, x2=1551, stroke=rgb(59, 127, 59), y1=0, x1=0),
        Line(y2=51, stroke_width=10, x2=518, stroke=rgb(33, 69, 62), y1=0, x1=0),
        Line(y2=812, stroke_width=9, x2=1055, stroke=rgb(19, 114, 91), y1=0, x1=0),
        Line(y2=851, stroke_width=7, x2=591, stroke=rgb(171, 108, 33), y1=0, x1=0),
        Line(y2=1126, stroke_width=10, x2=195, stroke=rgb(107, 102, 160), y1=0, x1=0),
        Line(y2=479, stroke_width=1, x2=823, stroke=rgb(83, 137, 252), y1=0, x1=0),
        Line(y2=1376, stroke_width=4, x2=316, stroke=rgb(99, 245, 87), y1=0, x1=0),
        Line(y2=1333, stroke_width=6, x2=133, stroke=rgb(33, 177, 94), y1=0, x1=0),
        Line(y2=1524, stroke_width=7, x2=1834, stroke=rgb(40, 245, 15), y1=0, x1=0),
        Line(y2=1952, stroke_width=5, x2=896, stroke=rgb(241, 50, 34), y1=0, x1=0),
        Line(y2=1527, stroke_width=7, x2=1799, stroke=rgb(193, 252, 26), y1=0, x1=0),
        Line(y2=451, stroke_width=9, x2=1799, stroke=rgb(11, 191, 51), y1=0, x1=0),
        Line(y2=1686, stroke_width=10, x2=20, stroke=rgb(161, 44, 173), y1=0, x1=0),
        Line(y2=148, stroke_width=5, x2=1129, stroke=rgb(86, 227, 25), y1=0, x1=0),
        Line(y2=497, stroke_width=7, x2=1793, stroke=rgb(236, 252, 215), y1=0, x1=0),
        Line(y2=1811, stroke_width=5, x2=525, stroke=rgb(7, 237, 95), y1=0, x1=0),
        Line(y2=1015, stroke_width=9, x2=1120, stroke=rgb(41, 237, 38), y1=0, x1=0),
        Line(y2=1340, stroke_width=9, x2=52, stroke=rgb(79, 179, 199), y1=0, x1=0),
        Line(y2=683, stroke_width=3, x2=20, stroke=rgb(172, 0, 236), y1=0, x1=0),
        Line(y2=914, stroke_width=3, x2=511, stroke=rgb(76, 48, 173), y1=0, x1=0),
        Line(y2=197, stroke_width=5, x2=1434, stroke=rgb(88, 162, 195), y1=0, x1=0),
        Line(y2=531, stroke_width=9, x2=1207, stroke=rgb(60, 169, 242), y1=0, x1=0),
        Line(y2=1181, stroke_width=4, x2=48, stroke=rgb(177, 152, 51), y1=0, x1=0),
        Line(y2=1222, stroke_width=7, x2=847, stroke=rgb(20, 114, 73), y1=0, x1=0),
        Line(y2=78, stroke_width=1, x2=227, stroke=rgb(34, 105, 215), y1=0, x1=0),
        Line(y2=1692, stroke_width=8, x2=670, stroke=rgb(233, 93, 54), y1=0, x1=0),
        Line(y2=368, stroke_width=1, x2=1920, stroke=rgb(195, 202, 224), y1=0, x1=0),
        Line(y2=721, stroke_width=7, x2=1311, stroke=rgb(193, 117, 45), y1=0, x1=0),
        Line(y2=865, stroke_width=2, x2=1376, stroke=rgb(58, 211, 7), y1=0, x1=0),
        Line(y2=1654, stroke_width=1, x2=1409, stroke=rgb(218, 155, 172), y1=0, x1=0),
        Line(y2=195, stroke_width=10, x2=583, stroke=rgb(200, 121, 182), y1=0, x1=0),
        Line(y2=1121, stroke_width=1, x2=1993, stroke=rgb(41, 249, 194), y1=0, x1=0),
        Line(y2=1738, stroke_width=6, x2=1856, stroke=rgb(76, 183, 105), y1=0, x1=0),
        Line(y2=1155, stroke_width=1, x2=1822, stroke=rgb(201, 136, 81), y1=0, x1=0),
        Line(y2=22, stroke_width=5, x2=715, stroke=rgb(181, 209, 33), y1=0, x1=0),
        Line(y2=690, stroke_width=5, x2=1521, stroke=rgb(223, 94, 248), y1=0, x1=0),
        Line(y2=68, stroke_width=2, x2=1319, stroke=rgb(197, 25, 106), y1=0, x1=0),
        Line(y2=1851, stroke_width=4, x2=594, stroke=rgb(147, 170, 222), y1=0, x1=0),
        Line(y2=1418, stroke_width=4, x2=938, stroke=rgb(97, 11, 171), y1=0, x1=0),
        Line(y2=1348, stroke_width=9, x2=1490, stroke=rgb(157, 28, 177), y1=0, x1=0),
        Line(y2=567, stroke_width=2, x2=1868, stroke=rgb(12, 153, 23), y1=0, x1=0),
        Line(y2=1909, stroke_width=9, x2=1619, stroke=rgb(215, 142, 166), y1=0, x1=0),
        Line(y2=308, stroke_width=9, x2=340, stroke=rgb(133, 224, 168), y1=0, x1=0),
        Line(y2=533, stroke_width=10, x2=939, stroke=rgb(8, 168, 101), y1=0, x1=0),
        Line(y2=839, stroke_width=6, x2=1327, stroke=rgb(7, 53, 8), y1=0, x1=0),
        Line(y2=803, stroke_width=9, x2=812, stroke=rgb(147, 159, 253), y1=0, x1=0),
        Line(y2=1863, stroke_width=5, x2=1796, stroke=rgb(191, 28, 181), y1=0, x1=0),
        Line(y2=421, stroke_width=2, x2=1833, stroke=rgb(205, 109, 187), y1=0, x1=0),
        Line(y2=142, stroke_width=6, x2=4, stroke=rgb(1, 183, 120), y1=0, x1=0),
        Line(y2=238, stroke_width=1, x2=1825, stroke=rgb(139, 89, 247), y1=0, x1=0),
        Line(y2=1162, stroke_width=10, x2=1035, stroke=rgb(157, 2, 79), y1=0, x1=0) )

    line_xml_strings = (
	"""<line stroke="rgb(48, 199, 243)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="567" y1="0" y2="418"/>""",
	"""<line stroke="rgb(159, 171, 203)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="812" y1="0" y2="131"/>""",
	"""<line stroke="rgb(133, 186, 14)" stroke-opacity="1.0" stroke-width="3" x1="0" x2="983" y1="0" y2="1060"/>""",
	"""<line stroke="rgb(225, 43, 126)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="961" y1="0" y2="177"/>""",
	"""<line stroke="rgb(122, 20, 198)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="488" y1="0" y2="1512"/>""",
	"""<line stroke="rgb(174, 199, 102)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="239" y1="0" y2="958"/>""",
	"""<line stroke="rgb(107, 92, 201)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="892" y1="0" y2="1535"/>""",
	"""<line stroke="rgb(212, 220, 94)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1607" y1="0" y2="260"/>""",
	"""<line stroke="rgb(82, 128, 149)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1130" y1="0" y2="1178"/>""",
	"""<line stroke="rgb(195, 88, 70)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="273" y1="0" y2="925"/>""",
	"""<line stroke="rgb(23, 226, 105)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="432" y1="0" y2="664"/>""",
	"""<line stroke="rgb(180, 74, 123)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="438" y1="0" y2="1891"/>""",
	"""<line stroke="rgb(33, 174, 192)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="488" y1="0" y2="388"/>""",
	"""<line stroke="rgb(178, 196, 97)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="1664" y1="0" y2="610"/>""",
	"""<line stroke="rgb(89, 1, 164)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="454" y1="0" y2="1231"/>""",
	"""<line stroke="rgb(66, 33, 28)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="632" y1="0" y2="1657"/>""",
	"""<line stroke="rgb(154, 58, 152)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="945" y1="0" y2="427"/>""",
	"""<line stroke="rgb(164, 189, 225)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="1888" y1="0" y2="625"/>""",
	"""<line stroke="rgb(42, 88, 96)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="972" y1="0" y2="1689"/>""",
	"""<line stroke="rgb(71, 44, 68)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1317" y1="0" y2="1243"/>""",
	"""<line stroke="rgb(52, 155, 188)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="1499" y1="0" y2="114"/>""",
	"""<line stroke="rgb(29, 85, 118)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="529" y1="0" y2="901"/>""",
	"""<line stroke="rgb(157, 235, 227)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="996" y1="0" y2="1624"/>""",
	"""<line stroke="rgb(126, 208, 239)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1793" y1="0" y2="33"/>""",
	"""<line stroke="rgb(245, 143, 16)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="1773" y1="0" y2="144"/>""",
	"""<line stroke="rgb(64, 142, 30)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="634" y1="0" y2="716"/>""",
	"""<line stroke="rgb(148, 17, 193)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="880" y1="0" y2="213"/>""",
	"""<line stroke="rgb(67, 247, 3)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1781" y1="0" y2="207"/>""",
	"""<line stroke="rgb(150, 63, 51)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="538" y1="0" y2="1088"/>""",
	"""<line stroke="rgb(104, 170, 1)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="765" y1="0" y2="853"/>""",
	"""<line stroke="rgb(160, 106, 252)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="582" y1="0" y2="1706"/>""",
	"""<line stroke="rgb(173, 67, 178)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="879" y1="0" y2="1850"/>""",
	"""<line stroke="rgb(30, 195, 181)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="29" y1="0" y2="605"/>""",
	"""<line stroke="rgb(190, 54, 233)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1990" y1="0" y2="1669"/>""",
	"""<line stroke="rgb(109, 156, 208)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="530" y1="0" y2="292"/>""",
	"""<line stroke="rgb(186, 93, 42)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1933" y1="0" y2="622"/>""",
	"""<line stroke="rgb(140, 196, 33)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1986" y1="0" y2="1914"/>""",
	"""<line stroke="rgb(190, 77, 156)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="161" y1="0" y2="1024"/>""",
	"""<line stroke="rgb(110, 39, 137)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1797" y1="0" y2="911"/>""",
	"""<line stroke="rgb(73, 89, 93)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="1358" y1="0" y2="1398"/>""",
	"""<line stroke="rgb(134, 249, 174)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1607" y1="0" y2="866"/>""",
	"""<line stroke="rgb(197, 61, 52)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1781" y1="0" y2="1955"/>""",
	"""<line stroke="rgb(168, 17, 220)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="991" y1="0" y2="1327"/>""",
	"""<line stroke="rgb(161, 94, 35)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="1132" y1="0" y2="273"/>""",
	"""<line stroke="rgb(213, 116, 159)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="483" y1="0" y2="259"/>""",
	"""<line stroke="rgb(74, 173, 166)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1000" y1="0" y2="1116"/>""",
	"""<line stroke="rgb(176, 209, 214)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="836" y1="0" y2="1080"/>""",
	"""<line stroke="rgb(44, 196, 113)" stroke-opacity="1.0" stroke-width="3" x1="0" x2="685" y1="0" y2="1455"/>""",
	"""<line stroke="rgb(186, 39, 46)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="439" y1="0" y2="1089"/>""",
	"""<line stroke="rgb(59, 127, 59)" stroke-opacity="1.0" stroke-width="3" x1="0" x2="1551" y1="0" y2="1255"/>""",
	"""<line stroke="rgb(33, 69, 62)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="518" y1="0" y2="51"/>""",
	"""<line stroke="rgb(19, 114, 91)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1055" y1="0" y2="812"/>""",
	"""<line stroke="rgb(171, 108, 33)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="591" y1="0" y2="851"/>""",
	"""<line stroke="rgb(107, 102, 160)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="195" y1="0" y2="1126"/>""",
	"""<line stroke="rgb(83, 137, 252)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="823" y1="0" y2="479"/>""",
	"""<line stroke="rgb(99, 245, 87)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="316" y1="0" y2="1376"/>""",
	"""<line stroke="rgb(33, 177, 94)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="133" y1="0" y2="1333"/>""",
	"""<line stroke="rgb(40, 245, 15)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="1834" y1="0" y2="1524"/>""",
	"""<line stroke="rgb(241, 50, 34)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="896" y1="0" y2="1952"/>""",
	"""<line stroke="rgb(193, 252, 26)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="1799" y1="0" y2="1527"/>""",
	"""<line stroke="rgb(11, 191, 51)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1799" y1="0" y2="451"/>""",
	"""<line stroke="rgb(161, 44, 173)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="20" y1="0" y2="1686"/>""",
	"""<line stroke="rgb(86, 227, 25)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1129" y1="0" y2="148"/>""",
	"""<line stroke="rgb(236, 252, 215)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="1793" y1="0" y2="497"/>""",
	"""<line stroke="rgb(7, 237, 95)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="525" y1="0" y2="1811"/>""",
	"""<line stroke="rgb(41, 237, 38)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1120" y1="0" y2="1015"/>""",
	"""<line stroke="rgb(79, 179, 199)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="52" y1="0" y2="1340"/>""",
	"""<line stroke="rgb(172, 0, 236)" stroke-opacity="1.0" stroke-width="3" x1="0" x2="20" y1="0" y2="683"/>""",
	"""<line stroke="rgb(76, 48, 173)" stroke-opacity="1.0" stroke-width="3" x1="0" x2="511" y1="0" y2="914"/>""",
	"""<line stroke="rgb(88, 162, 195)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1434" y1="0" y2="197"/>""",
	"""<line stroke="rgb(60, 169, 242)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1207" y1="0" y2="531"/>""",
	"""<line stroke="rgb(177, 152, 51)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="48" y1="0" y2="1181"/>""",
	"""<line stroke="rgb(20, 114, 73)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="847" y1="0" y2="1222"/>""",
	"""<line stroke="rgb(34, 105, 215)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="227" y1="0" y2="78"/>""",
	"""<line stroke="rgb(233, 93, 54)" stroke-opacity="1.0" stroke-width="8" x1="0" x2="670" y1="0" y2="1692"/>""",
	"""<line stroke="rgb(195, 202, 224)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1920" y1="0" y2="368"/>""",
	"""<line stroke="rgb(193, 117, 45)" stroke-opacity="1.0" stroke-width="7" x1="0" x2="1311" y1="0" y2="721"/>""",
	"""<line stroke="rgb(58, 211, 7)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1376" y1="0" y2="865"/>""",
	"""<line stroke="rgb(218, 155, 172)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1409" y1="0" y2="1654"/>""",
	"""<line stroke="rgb(200, 121, 182)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="583" y1="0" y2="195"/>""",
	"""<line stroke="rgb(41, 249, 194)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1993" y1="0" y2="1121"/>""",
	"""<line stroke="rgb(76, 183, 105)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="1856" y1="0" y2="1738"/>""",
	"""<line stroke="rgb(201, 136, 81)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1822" y1="0" y2="1155"/>""",
	"""<line stroke="rgb(181, 209, 33)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="715" y1="0" y2="22"/>""",
	"""<line stroke="rgb(223, 94, 248)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1521" y1="0" y2="690"/>""",
	"""<line stroke="rgb(197, 25, 106)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1319" y1="0" y2="68"/>""",
	"""<line stroke="rgb(147, 170, 222)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="594" y1="0" y2="1851"/>""",
	"""<line stroke="rgb(97, 11, 171)" stroke-opacity="1.0" stroke-width="4" x1="0" x2="938" y1="0" y2="1418"/>""",
	"""<line stroke="rgb(157, 28, 177)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1490" y1="0" y2="1348"/>""",
	"""<line stroke="rgb(12, 153, 23)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1868" y1="0" y2="567"/>""",
	"""<line stroke="rgb(215, 142, 166)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="1619" y1="0" y2="1909"/>""",
	"""<line stroke="rgb(133, 224, 168)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="340" y1="0" y2="308"/>""",
	"""<line stroke="rgb(8, 168, 101)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="939" y1="0" y2="533"/>""",
	"""<line stroke="rgb(7, 53, 8)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="1327" y1="0" y2="839"/>""",
	"""<line stroke="rgb(147, 159, 253)" stroke-opacity="1.0" stroke-width="9" x1="0" x2="812" y1="0" y2="803"/>""",
	"""<line stroke="rgb(191, 28, 181)" stroke-opacity="1.0" stroke-width="5" x1="0" x2="1796" y1="0" y2="1863"/>""",
	"""<line stroke="rgb(205, 109, 187)" stroke-opacity="1.0" stroke-width="2" x1="0" x2="1833" y1="0" y2="421"/>""",
	"""<line stroke="rgb(1, 183, 120)" stroke-opacity="1.0" stroke-width="6" x1="0" x2="4" y1="0" y2="142"/>""",
	"""<line stroke="rgb(139, 89, 247)" stroke-opacity="1.0" stroke-width="1" x1="0" x2="1825" y1="0" y2="238"/>""",
	"""<line stroke="rgb(157, 2, 79)" stroke-opacity="1.0" stroke-width="10" x1="0" x2="1035" y1="0" y2="1162"/>""")

    def test_line_to_xml(self):
        """Line: Object ---> XML"""
        assert len(self.line_objects) == len(self.line_xml_strings)
        for line, xml in zip(self.line_objects, self.line_xml_strings): 
            self.assertEqual(line.to_xml(), xml)

 
    def test_line_from_xml(self):
        """Line: XML ---> Object"""
        assert len(self.line_objects) == len(self.line_xml_strings)
        for line, xml in zip(self.line_objects, self.line_xml_strings): 
            self.assertEqual(line, object_from_xml(xml))
        





class TextTest(unittest.TestCase):
    """Test For svgenesis.primitives.Text"""
    ################################################
    # Text Objects and XML Strings
    ################################################
    plaintext_objects = ()

    plaintext_xml_strings = ()

    def test_plaintext_to_xml(self):
        """Text: Object ---> XML"""
        for plaintext, xml in zip(self.plaintext_objects, self.plaintext_xml_strings): 
            self.assertEqual(plaintext.to_xml(), xml)

 
    def test_plaintext_from_xml(self):
        """Text: XML ---> Object"""
        assert len(self.plaintext_objects) == len(self.plaintext_xml_strings)
        for plaintext, xml in zip(self.plaintext_objects, self.plaintext_xml_strings): 
            self.assertEqual(plaintext, object_from_xml(xml))



class RectangleTest(unittest.TestCase):
    """Test For svgenesis.primitives.Rectangle"""
    ################################################
    # Rectangle Objects and XML Strings
    ################################################
    rectangle_objects = (
        Rectangle(opacity=0.586122885514, stroke_opacity=0.515871710886, stroke_width=6, height=73.2821796413, width=51.7348003378, stroke=rgb(61, 110, 249), y=275.122396601, x=130.705762102, fill=rgb(168, 166, 61)),
        Rectangle(opacity=0.847710166448, stroke_opacity=0.535546237776, stroke_width=5, height=166.442861276, width=77.6286616236, stroke=rgb(184, 169, 143), y=343.755748831, x=101.208983987, fill=rgb(98, 6, 239)),
        Rectangle(opacity=0.646185276874, stroke_opacity=0.510543179454, stroke_width=2, height=180.242788255, width=76.2562997472, stroke=rgb(167, 114, 247), y=548.964856121, x=900.718965367, fill=rgb(224, 220, 164)),
        Rectangle(opacity=0.999845726329, stroke_opacity=0.810390686657, stroke_width=1, height=106.897942925, width=95.9140474173, stroke=rgb(171, 31, 133), y=704.572731903, x=147.720806503, fill=rgb(112, 88, 209)),
        Rectangle(opacity=0.89706688259, stroke_opacity=0.997304522241, stroke_width=7, height=126.704062386, width=53.6535113504, stroke=rgb(45, 255, 85), y=910.560217454, x=853.339512741, fill=rgb(149, 148, 251)),
        Rectangle(opacity=0.640550846406, stroke_opacity=0.784481680575, stroke_width=6, height=21.7747416352, width=79.9986557844, stroke=rgb(35, 66, 44), y=165.351786168, x=647.384030353, fill=rgb(105, 48, 184)),
        Rectangle(opacity=0.528578965412, stroke_opacity=0.554870346252, stroke_width=9, height=193.855345808, width=176.628271082, stroke=rgb(0, 19, 188), y=229.13413548, x=981.433710829, fill=rgb(214, 88, 251)),
        Rectangle(opacity=0.935646828321, stroke_opacity=0.511344664625, stroke_width=8, height=95.0865770621, width=173.801728803, stroke=rgb(11, 141, 238), y=790.660683516, x=172.234549951, fill=rgb(58, 219, 206)),
        Rectangle(opacity=0.934207681401, stroke_opacity=0.553632196775, stroke_width=3, height=31.7123881716, width=87.8300799974, stroke=rgb(7, 84, 156), y=232.240647755, x=379.979201429, fill=rgb(110, 179, 50)),
        Rectangle(opacity=0.899451298656, stroke_opacity=0.624539027284, stroke_width=8, height=106.473504266, width=44.1610031133, stroke=rgb(188, 104, 186), y=947.59447125, x=651.641861988, fill=rgb(195, 82, 99)),
        Rectangle(opacity=0.942893293661, stroke_opacity=0.682978642229, stroke_width=9, height=65.5973599918, width=137.743461504, stroke=rgb(157, 178, 61), y=560.31502753, x=163.877763322, fill=rgb(119, 64, 140)),
        Rectangle(opacity=0.746009613245, stroke_opacity=0.890315839423, stroke_width=7, height=62.9154389907, width=137.88962507, stroke=rgb(237, 89, 54), y=841.15695542, x=595.423031655, fill=rgb(73, 162, 113)),
        Rectangle(opacity=0.526627467565, stroke_opacity=0.947017299127, stroke_width=3, height=13.8977540142, width=136.802442565, stroke=rgb(139, 86, 109), y=527.18666801, x=532.361335012, fill=rgb(170, 177, 201)),
        Rectangle(opacity=0.902960250958, stroke_opacity=0.766010594535, stroke_width=3, height=13.8561072936, width=191.825151351, stroke=rgb(29, 142, 61), y=231.906865338, x=387.610969724, fill=rgb(130, 133, 44)),
        Rectangle(opacity=0.556582292133, stroke_opacity=0.839021129327, stroke_width=8, height=185.348023413, width=36.1723080074, stroke=rgb(226, 110, 137), y=975.728984683, x=468.239417946, fill=rgb(65, 145, 233)),
        Rectangle(opacity=0.973712898855, stroke_opacity=0.57645619748, stroke_width=1, height=114.300988643, width=64.3849177155, stroke=rgb(3, 174, 41), y=561.556728556, x=623.564998897, fill=rgb(195, 161, 163)),
        Rectangle(opacity=0.853565684547, stroke_opacity=0.81040652967, stroke_width=6, height=114.805046842, width=140.039125524, stroke=rgb(22, 8, 167), y=102.024045995, x=354.122818069, fill=rgb(157, 149, 101)),
        Rectangle(opacity=0.898122677592, stroke_opacity=0.557661766785, stroke_width=1, height=51.2684524067, width=99.9582311827, stroke=rgb(251, 237, 127), y=792.260085353, x=347.687301405, fill=rgb(210, 221, 231)),
        Rectangle(opacity=0.542798943781, stroke_opacity=0.704965421745, stroke_width=2, height=67.3637136714, width=174.986012779, stroke=rgb(231, 89, 219), y=314.284117709, x=892.574954495, fill=rgb(115, 49, 164)),
        Rectangle(opacity=0.886047103426, stroke_opacity=0.827015695052, stroke_width=2, height=189.308320967, width=115.968932804, stroke=rgb(199, 209, 176), y=792.59243612, x=567.502193163, fill=rgb(161, 176, 31)),
        Rectangle(opacity=0.917293329306, stroke_opacity=0.553987557194, stroke_width=9, height=30.8655473363, width=21.8070735482, stroke=rgb(156, 220, 170), y=748.507788882, x=781.882547906, fill=rgb(229, 167, 4)),
        Rectangle(opacity=0.883449225332, stroke_opacity=0.993459527505, stroke_width=4, height=6.50242046821, width=186.670628826, stroke=rgb(247, 60, 53), y=746.494052992, x=371.661114476, fill=rgb(91, 147, 1)),
        Rectangle(opacity=0.810650263352, stroke_opacity=0.60040935745, stroke_width=9, height=30.0715583658, width=197.425122923, stroke=rgb(131, 149, 42), y=246.880993368, x=418.360633235, fill=rgb(102, 137, 133)),
        Rectangle(opacity=0.967357576328, stroke_opacity=0.859090087535, stroke_width=9, height=42.6108312799, width=142.813121305, stroke=rgb(39, 75, 187), y=667.370819789, x=800.550136646, fill=rgb(88, 247, 163)),
        Rectangle(opacity=0.918896620829, stroke_opacity=0.885828071142, stroke_width=9, height=32.7462760631, width=52.8752506868, stroke=rgb(145, 45, 117), y=980.229593361, x=280.307625348, fill=rgb(54, 3, 160)),
        Rectangle(opacity=0.819108989697, stroke_opacity=0.57561822661, stroke_width=2, height=5.62742110308, width=87.052609303, stroke=rgb(157, 131, 238), y=597.708491973, x=237.626923154, fill=rgb(158, 93, 211)),
        Rectangle(opacity=0.604175749687, stroke_opacity=0.909113909265, stroke_width=3, height=122.848474169, width=71.9178105607, stroke=rgb(71, 52, 253), y=261.369809125, x=667.44939404, fill=rgb(149, 29, 156)),
        Rectangle(opacity=0.525326073195, stroke_opacity=0.957099030262, stroke_width=9, height=12.982784906, width=196.681153384, stroke=rgb(99, 122, 193), y=991.247275423, x=531.084213795, fill=rgb(48, 102, 7)),
        Rectangle(opacity=0.78236789162, stroke_opacity=0.815343748771, stroke_width=9, height=94.3179266375, width=173.684382202, stroke=rgb(155, 2, 206), y=151.347138735, x=789.854864277, fill=rgb(63, 101, 62)),
        Rectangle(opacity=0.936587004546, stroke_opacity=0.643532646549, stroke_width=1, height=8.80667788622, width=142.347408126, stroke=rgb(105, 57, 239), y=718.906053297, x=582.678365738, fill=rgb(176, 135, 249)),
        Rectangle(opacity=0.533254576912, stroke_opacity=0.562570924301, stroke_width=5, height=64.3663950318, width=163.919893029, stroke=rgb(155, 22, 151), y=348.039333303, x=243.609804846, fill=rgb(188, 211, 162)),
        Rectangle(opacity=0.788161722114, stroke_opacity=0.865793837306, stroke_width=6, height=11.6561115235, width=39.3516595415, stroke=rgb(120, 7, 35), y=359.875839698, x=861.383873545, fill=rgb(54, 234, 66)),
        Rectangle(opacity=0.699770262818, stroke_opacity=0.987623534736, stroke_width=3, height=174.984425906, width=5.15063769847, stroke=rgb(66, 92, 34), y=173.938581489, x=959.387623506, fill=rgb(150, 177, 126)),
        Rectangle(opacity=0.54302718379, stroke_opacity=0.913112939174, stroke_width=3, height=27.9574497335, width=151.886697352, stroke=rgb(165, 91, 94), y=873.158984397, x=370.982826242, fill=rgb(37, 57, 39)),
        Rectangle(opacity=0.610587426652, stroke_opacity=0.754107430918, stroke_width=8, height=84.9644467633, width=12.5654592755, stroke=rgb(107, 221, 1), y=939.821818272, x=945.964157452, fill=rgb(29, 108, 8)),
        Rectangle(opacity=0.728190060365, stroke_opacity=0.835603244704, stroke_width=8, height=157.506561937, width=182.061592779, stroke=rgb(211, 111, 155), y=714.725593003, x=724.435210527, fill=rgb(211, 77, 212)),
        Rectangle(opacity=0.572071200279, stroke_opacity=0.591447043479, stroke_width=8, height=156.33706961, width=196.376860987, stroke=rgb(226, 196, 211), y=708.685990009, x=727.676302626, fill=rgb(4, 138, 161)),
        Rectangle(opacity=0.925989330972, stroke_opacity=0.617665732781, stroke_width=9, height=145.615757539, width=64.6566204777, stroke=rgb(27, 50, 88), y=949.423743298, x=910.029544502, fill=rgb(215, 82, 167)),
        Rectangle(opacity=0.765788712871, stroke_opacity=0.518786968708, stroke_width=5, height=166.194479014, width=86.3329390049, stroke=rgb(230, 220, 66), y=302.961069487, x=136.1901471, fill=rgb(162, 155, 59)),
        Rectangle(opacity=0.990622146187, stroke_opacity=0.827574773293, stroke_width=7, height=168.506783658, width=187.143959004, stroke=rgb(60, 158, 72), y=564.509360966, x=542.803992674, fill=rgb(85, 162, 124)),
        Rectangle(opacity=0.904877023008, stroke_opacity=0.592763691665, stroke_width=10, height=175.581111165, width=136.536341493, stroke=rgb(101, 176, 212), y=867.270389829, x=126.098323227, fill=rgb(140, 73, 180)),
        Rectangle(opacity=0.896517364331, stroke_opacity=0.975490920294, stroke_width=10, height=54.3161652917, width=86.0080939804, stroke=rgb(133, 126, 190), y=981.273530573, x=186.629355141, fill=rgb(11, 154, 21)),
        Rectangle(opacity=0.541330395464, stroke_opacity=0.908987102349, stroke_width=9, height=145.979767139, width=100.206917581, stroke=rgb(238, 183, 37), y=548.449066253, x=730.488546378, fill=rgb(89, 246, 209)),
        Rectangle(opacity=0.959260103557, stroke_opacity=0.756323703131, stroke_width=10, height=62.279470392, width=61.9164442561, stroke=rgb(105, 108, 71), y=409.366336114, x=107.475276303, fill=rgb(125, 148, 53)),
        Rectangle(opacity=0.768809586744, stroke_opacity=0.593320216322, stroke_width=4, height=20.2580110916, width=52.2052910467, stroke=rgb(246, 122, 74), y=429.047703951, x=126.994359075, fill=rgb(16, 165, 84)),
        Rectangle(opacity=0.646381153146, stroke_opacity=0.772925494851, stroke_width=4, height=193.378413561, width=81.5313248731, stroke=rgb(138, 46, 238), y=953.263833529, x=386.066365699, fill=rgb(100, 15, 35)),
        Rectangle(opacity=0.528862562198, stroke_opacity=0.874145237368, stroke_width=4, height=31.5716070267, width=10.3378748934, stroke=rgb(234, 35, 255), y=467.739775045, x=543.665680934, fill=rgb(78, 171, 14)),
        Rectangle(opacity=0.731920282926, stroke_opacity=0.869951310795, stroke_width=3, height=89.836788895, width=140.745647355, stroke=rgb(69, 211, 115), y=149.759605997, x=910.587863634, fill=rgb(172, 122, 246)),
        Rectangle(opacity=0.819055301329, stroke_opacity=0.700645058769, stroke_width=9, height=32.6596408289, width=46.8619131084, stroke=rgb(129, 24, 77), y=176.941141365, x=856.774609545, fill=rgb(120, 11, 167)),
        Rectangle(opacity=0.546420611828, stroke_opacity=0.680338396142, stroke_width=2, height=18.3648232082, width=105.246864408, stroke=rgb(250, 249, 172), y=787.000768443, x=190.387867176, fill=rgb(86, 11, 5)),
        Rectangle(opacity=0.622996209222, stroke_opacity=0.891230029538, stroke_width=7, height=183.674798143, width=59.8482847677, stroke=rgb(21, 70, 206), y=348.701755447, x=345.022408967, fill=rgb(106, 72, 18)),
        Rectangle(opacity=0.960692448199, stroke_opacity=0.931765930172, stroke_width=7, height=87.8482663918, width=90.5667155345, stroke=rgb(99, 78, 180), y=776.96168857, x=645.539493195, fill=rgb(32, 116, 208)),
        Rectangle(opacity=0.970272984255, stroke_opacity=0.763424999633, stroke_width=6, height=178.956562614, width=91.0314171173, stroke=rgb(23, 125, 186), y=321.864969112, x=302.803409961, fill=rgb(245, 50, 80)),
        Rectangle(opacity=0.787177233981, stroke_opacity=0.597311938627, stroke_width=6, height=36.155137724, width=132.053106261, stroke=rgb(149, 104, 125), y=159.40184772, x=552.356560642, fill=rgb(77, 156, 39)),
        Rectangle(opacity=0.625876958784, stroke_opacity=0.803900514135, stroke_width=4, height=57.2774737116, width=56.4412047718, stroke=rgb(203, 170, 180), y=930.031451621, x=422.065610137, fill=rgb(221, 123, 228)),
        Rectangle(opacity=0.664595397302, stroke_opacity=0.583337769255, stroke_width=10, height=142.951809476, width=154.080846561, stroke=rgb(203, 208, 170), y=151.075357812, x=735.114429365, fill=rgb(202, 236, 180)),
        Rectangle(opacity=0.979982851783, stroke_opacity=0.603720030333, stroke_width=6, height=31.8504101497, width=192.596072971, stroke=rgb(117, 248, 97), y=876.773406729, x=631.182795318, fill=rgb(36, 200, 20)),
        Rectangle(opacity=0.638385215266, stroke_opacity=0.55445091655, stroke_width=2, height=46.8788460218, width=116.613025748, stroke=rgb(214, 151, 63), y=454.93805404, x=921.393158559, fill=rgb(255, 255, 103)),
        Rectangle(opacity=0.798933906688, stroke_opacity=0.939761082489, stroke_width=6, height=176.257044256, width=60.5757817933, stroke=rgb(101, 161, 136), y=851.992529664, x=398.282163219, fill=rgb(96, 30, 209)),
        Rectangle(opacity=0.793732430519, stroke_opacity=0.541985557936, stroke_width=8, height=14.2114293254, width=197.809100378, stroke=rgb(70, 230, 137), y=971.46720175, x=580.929517835, fill=rgb(34, 174, 109)),
        Rectangle(opacity=0.654594852183, stroke_opacity=0.859966206903, stroke_width=3, height=36.1512938891, width=105.101695287, stroke=rgb(53, 240, 219), y=810.564535923, x=783.316484433, fill=rgb(71, 247, 169)),
        Rectangle(opacity=0.989738104444, stroke_opacity=0.87128322404, stroke_width=10, height=34.9042004599, width=119.607127411, stroke=rgb(67, 145, 83), y=578.272029484, x=794.790987725, fill=rgb(166, 121, 124)),
        Rectangle(opacity=0.568381526788, stroke_opacity=0.988468485633, stroke_width=10, height=9.40264604234, width=130.229302544, stroke=rgb(218, 60, 203), y=454.318579496, x=493.190747889, fill=rgb(54, 107, 127)),
        Rectangle(opacity=0.540713273229, stroke_opacity=0.871619528718, stroke_width=2, height=163.518024282, width=84.490330701, stroke=rgb(51, 93, 195), y=723.423614818, x=938.035473514, fill=rgb(217, 72, 133)),
        Rectangle(opacity=0.789621623031, stroke_opacity=0.859460461678, stroke_width=6, height=5.936891418, width=29.9534741023, stroke=rgb(156, 253, 182), y=659.508598887, x=963.998222463, fill=rgb(44, 50, 169)),
        Rectangle(opacity=0.935374515793, stroke_opacity=0.714156206205, stroke_width=9, height=145.998646608, width=120.038725735, stroke=rgb(195, 251, 35), y=736.255961995, x=561.582212293, fill=rgb(7, 1, 163)),
        Rectangle(opacity=0.952530667559, stroke_opacity=0.720998402303, stroke_width=4, height=42.609823121, width=117.065301224, stroke=rgb(221, 47, 232), y=645.732624594, x=668.211368138, fill=rgb(134, 202, 215)),
        Rectangle(opacity=0.822555613407, stroke_opacity=0.628469672518, stroke_width=2, height=92.7390487304, width=66.9554834274, stroke=rgb(197, 149, 251), y=109.642662111, x=485.14339645, fill=rgb(214, 5, 15)),
        Rectangle(opacity=0.695460902312, stroke_opacity=0.549747867694, stroke_width=1, height=121.753514999, width=60.5932970572, stroke=rgb(8, 64, 8), y=200.774393771, x=510.727436869, fill=rgb(85, 179, 240)),
        Rectangle(opacity=0.609482127593, stroke_opacity=0.545518211955, stroke_width=8, height=25.795752672, width=51.534709257, stroke=rgb(125, 149, 203), y=199.160333675, x=187.866383807, fill=rgb(201, 182, 68)),
        Rectangle(opacity=0.638394660714, stroke_opacity=0.524145166786, stroke_width=3, height=191.410037547, width=146.282325943, stroke=rgb(153, 199, 36), y=526.675286831, x=590.806192557, fill=rgb(43, 124, 248)),
        Rectangle(opacity=0.910716900751, stroke_opacity=0.650420172252, stroke_width=9, height=184.397613128, width=83.8362761393, stroke=rgb(216, 56, 175), y=856.508856456, x=128.826514534, fill=rgb(243, 123, 86)),
        Rectangle(opacity=0.568597624297, stroke_opacity=0.818417497295, stroke_width=10, height=124.724501757, width=141.622646472, stroke=rgb(155, 164, 68), y=794.237348997, x=238.976733968, fill=rgb(143, 137, 68)),
        Rectangle(opacity=0.965976640999, stroke_opacity=0.874435162728, stroke_width=3, height=40.9094206461, width=0.935029119992, stroke=rgb(63, 230, 253), y=430.949480553, x=123.747376395, fill=rgb(38, 98, 204)),
        Rectangle(opacity=0.732057759598, stroke_opacity=0.762612954579, stroke_width=3, height=182.860915293, width=85.3528181032, stroke=rgb(192, 121, 234), y=399.180101185, x=597.218488351, fill=rgb(107, 79, 116)),
        Rectangle(opacity=0.887491487565, stroke_opacity=0.943250495104, stroke_width=1, height=88.1001354282, width=99.9693260729, stroke=rgb(221, 39, 92), y=621.858614506, x=404.61456736, fill=rgb(231, 111, 97)),
        Rectangle(opacity=0.991179309259, stroke_opacity=0.875359353996, stroke_width=2, height=122.364127494, width=41.6644641502, stroke=rgb(3, 118, 223), y=256.490948581, x=113.690393133, fill=rgb(154, 104, 160)),
        Rectangle(opacity=0.568804326866, stroke_opacity=0.603022511198, stroke_width=3, height=191.429048702, width=172.247453123, stroke=rgb(117, 238, 82), y=509.325666608, x=534.095243849, fill=rgb(44, 93, 236)),
        Rectangle(opacity=0.883276382905, stroke_opacity=0.838729242487, stroke_width=7, height=37.7369054932, width=89.1268400309, stroke=rgb(195, 242, 99), y=491.501819097, x=199.337326763, fill=rgb(94, 89, 164)),
        Rectangle(opacity=0.705389749908, stroke_opacity=0.725078908781, stroke_width=3, height=5.65687275798, width=168.226551176, stroke=rgb(6, 15, 249), y=846.187914681, x=156.187838771, fill=rgb(19, 188, 177)),
        Rectangle(opacity=0.598421126559, stroke_opacity=0.858703117345, stroke_width=2, height=140.374784118, width=135.203681303, stroke=rgb(243, 125, 152), y=376.22017128, x=981.053192173, fill=rgb(240, 37, 149)),
        Rectangle(opacity=0.925041391851, stroke_opacity=0.837415769951, stroke_width=1, height=125.30348986, width=31.9472093049, stroke=rgb(167, 149, 255), y=947.69815084, x=321.14084094, fill=rgb(85, 216, 94)),
        Rectangle(opacity=0.791417597925, stroke_opacity=0.645499899615, stroke_width=10, height=82.5258062501, width=149.286469015, stroke=rgb(244, 147, 28), y=925.056397381, x=862.733033585, fill=rgb(41, 233, 66)),
        Rectangle(opacity=0.709308468266, stroke_opacity=0.829892869366, stroke_width=1, height=56.933833366, width=109.889286559, stroke=rgb(114, 69, 10), y=554.077163415, x=908.806257426, fill=rgb(15, 22, 174)),
        Rectangle(opacity=0.679531775377, stroke_opacity=0.5067083659, stroke_width=8, height=2.16460973619, width=183.986790693, stroke=rgb(23, 171, 2), y=855.54730169, x=486.452604715, fill=rgb(117, 45, 75)),
        Rectangle(opacity=0.733323822065, stroke_opacity=0.713673506643, stroke_width=7, height=196.761352262, width=174.48470351, stroke=rgb(12, 100, 159), y=533.800606393, x=397.63929119, fill=rgb(204, 220, 140)),
        Rectangle(opacity=0.869044909442, stroke_opacity=0.995309755488, stroke_width=8, height=81.0460157757, width=121.492128176, stroke=rgb(158, 141, 174), y=779.011500191, x=675.222848721, fill=rgb(37, 142, 102)),
        Rectangle(opacity=0.891897539141, stroke_opacity=0.621826788857, stroke_width=8, height=129.628418069, width=17.873875198, stroke=rgb(57, 109, 247), y=743.068578517, x=187.607752134, fill=rgb(96, 113, 213)),
        Rectangle(opacity=0.778976865721, stroke_opacity=0.945249535313, stroke_width=7, height=194.523534776, width=21.5237930374, stroke=rgb(200, 143, 50), y=919.25803059, x=557.97940826, fill=rgb(171, 133, 88)),
        Rectangle(opacity=0.660202074715, stroke_opacity=0.932888285144, stroke_width=8, height=126.95235149, width=150.06084616, stroke=rgb(240, 243, 50), y=232.463673352, x=949.891272813, fill=rgb(85, 158, 53)),
        Rectangle(opacity=0.874524208824, stroke_opacity=0.646190727617, stroke_width=5, height=29.139560601, width=135.598367147, stroke=rgb(217, 251, 251), y=769.564173847, x=803.22282438, fill=rgb(42, 119, 0)),
        Rectangle(opacity=0.552280024676, stroke_opacity=0.877597376666, stroke_width=9, height=91.7500319564, width=172.718501954, stroke=rgb(71, 89, 177), y=692.490215395, x=502.657287726, fill=rgb(134, 171, 130)),
        Rectangle(opacity=0.527763261574, stroke_opacity=0.611001848585, stroke_width=1, height=168.869635593, width=176.437220067, stroke=rgb(230, 74, 216), y=889.100181333, x=523.085099117, fill=rgb(15, 28, 97)),
        Rectangle(opacity=0.670321604266, stroke_opacity=0.686439870144, stroke_width=1, height=140.060100374, width=2.20336478283, stroke=rgb(36, 99, 172), y=336.11298117, x=430.448986966, fill=rgb(251, 23, 127)),
        Rectangle(opacity=0.770865309429, stroke_opacity=0.8685644513, stroke_width=7, height=37.7945617144, width=5.42583228681, stroke=rgb(26, 71, 85), y=499.97854299, x=543.547328809, fill=rgb(215, 143, 68)),
        Rectangle(opacity=0.752969494511, stroke_opacity=0.762241451932, stroke_width=2, height=101.954678168, width=160.499944898, stroke=rgb(185, 7, 3), y=248.761734385, x=588.828926314, fill=rgb(232, 205, 31)),
        Rectangle(opacity=0.572251067568, stroke_opacity=0.705464712874, stroke_width=3, height=154.123563863, width=41.495723403, stroke=rgb(72, 107, 247), y=794.58160985, x=177.750961973, fill=rgb(204, 13, 171)),
        Rectangle(opacity=0.754473875408, stroke_opacity=0.678508802306, stroke_width=2, height=169.37123922, width=141.64735543, stroke=rgb(106, 30, 225), y=131.633687601, x=510.645045815, fill=rgb(100, 119, 228)),
        Rectangle(opacity=0.591259214487, stroke_opacity=0.804279767896, stroke_width=5, height=65.622764192, width=11.0060075602, stroke=rgb(197, 30, 149), y=503.123749501, x=735.317800282, fill=rgb(165, 158, 28)),
        Rectangle(opacity=0.938053769346, stroke_opacity=0.502493900886, stroke_width=8, height=62.1817311946, width=21.0800215482, stroke=rgb(200, 38, 26), y=661.570506434, x=754.90300962, fill=rgb(76, 43, 53)),
)

    rectangle_xml_strings = (
        """<rect fill="rgb(168, 166, 61)" height="73.2821796413" opacity="0.586122885514" rx="0" ry="0" stroke="rgb(61, 110, 249)" stroke-opacity="0.515871710886" stroke-width="6" width="51.7348003378" x="130.705762102" y="275.122396601"/>""",
        """<rect fill="rgb(98, 6, 239)" height="166.442861276" opacity="0.847710166448" rx="0" ry="0" stroke="rgb(184, 169, 143)" stroke-opacity="0.535546237776" stroke-width="5" width="77.6286616236" x="101.208983987" y="343.755748831"/>""",
        """<rect fill="rgb(224, 220, 164)" height="180.242788255" opacity="0.646185276874" rx="0" ry="0" stroke="rgb(167, 114, 247)" stroke-opacity="0.510543179454" stroke-width="2" width="76.2562997472" x="900.718965367" y="548.964856121"/>""",
        """<rect fill="rgb(112, 88, 209)" height="106.897942925" opacity="0.999845726329" rx="0" ry="0" stroke="rgb(171, 31, 133)" stroke-opacity="0.810390686657" stroke-width="1" width="95.9140474173" x="147.720806503" y="704.572731903"/>""",
        """<rect fill="rgb(149, 148, 251)" height="126.704062386" opacity="0.89706688259" rx="0" ry="0" stroke="rgb(45, 255, 85)" stroke-opacity="0.997304522241" stroke-width="7" width="53.6535113504" x="853.339512741" y="910.560217454"/>""",
        """<rect fill="rgb(105, 48, 184)" height="21.7747416352" opacity="0.640550846406" rx="0" ry="0" stroke="rgb(35, 66, 44)" stroke-opacity="0.784481680575" stroke-width="6" width="79.9986557844" x="647.384030353" y="165.351786168"/>""",
        """<rect fill="rgb(214, 88, 251)" height="193.855345808" opacity="0.528578965412" rx="0" ry="0" stroke="rgb(0, 19, 188)" stroke-opacity="0.554870346252" stroke-width="9" width="176.628271082" x="981.433710829" y="229.13413548"/>""",
        """<rect fill="rgb(58, 219, 206)" height="95.0865770621" opacity="0.935646828321" rx="0" ry="0" stroke="rgb(11, 141, 238)" stroke-opacity="0.511344664625" stroke-width="8" width="173.801728803" x="172.234549951" y="790.660683516"/>""",
        """<rect fill="rgb(110, 179, 50)" height="31.7123881716" opacity="0.934207681401" rx="0" ry="0" stroke="rgb(7, 84, 156)" stroke-opacity="0.553632196775" stroke-width="3" width="87.8300799974" x="379.979201429" y="232.240647755"/>""",
        """<rect fill="rgb(195, 82, 99)" height="106.473504266" opacity="0.899451298656" rx="0" ry="0" stroke="rgb(188, 104, 186)" stroke-opacity="0.624539027284" stroke-width="8" width="44.1610031133" x="651.641861988" y="947.59447125"/>""",
        """<rect fill="rgb(119, 64, 140)" height="65.5973599918" opacity="0.942893293661" rx="0" ry="0" stroke="rgb(157, 178, 61)" stroke-opacity="0.682978642229" stroke-width="9" width="137.743461504" x="163.877763322" y="560.31502753"/>""",
        """<rect fill="rgb(73, 162, 113)" height="62.9154389907" opacity="0.746009613245" rx="0" ry="0" stroke="rgb(237, 89, 54)" stroke-opacity="0.890315839423" stroke-width="7" width="137.88962507" x="595.423031655" y="841.15695542"/>""",
        """<rect fill="rgb(170, 177, 201)" height="13.8977540142" opacity="0.526627467565" rx="0" ry="0" stroke="rgb(139, 86, 109)" stroke-opacity="0.947017299127" stroke-width="3" width="136.802442565" x="532.361335012" y="527.18666801"/>""",
        """<rect fill="rgb(130, 133, 44)" height="13.8561072936" opacity="0.902960250958" rx="0" ry="0" stroke="rgb(29, 142, 61)" stroke-opacity="0.766010594535" stroke-width="3" width="191.825151351" x="387.610969724" y="231.906865338"/>""",
        """<rect fill="rgb(65, 145, 233)" height="185.348023413" opacity="0.556582292133" rx="0" ry="0" stroke="rgb(226, 110, 137)" stroke-opacity="0.839021129327" stroke-width="8" width="36.1723080074" x="468.239417946" y="975.728984683"/>""",
        """<rect fill="rgb(195, 161, 163)" height="114.300988643" opacity="0.973712898855" rx="0" ry="0" stroke="rgb(3, 174, 41)" stroke-opacity="0.57645619748" stroke-width="1" width="64.3849177155" x="623.564998897" y="561.556728556"/>""",
        """<rect fill="rgb(157, 149, 101)" height="114.805046842" opacity="0.853565684547" rx="0" ry="0" stroke="rgb(22, 8, 167)" stroke-opacity="0.81040652967" stroke-width="6" width="140.039125524" x="354.122818069" y="102.024045995"/>""",
        """<rect fill="rgb(210, 221, 231)" height="51.2684524067" opacity="0.898122677592" rx="0" ry="0" stroke="rgb(251, 237, 127)" stroke-opacity="0.557661766785" stroke-width="1" width="99.9582311827" x="347.687301405" y="792.260085353"/>""",
        """<rect fill="rgb(115, 49, 164)" height="67.3637136714" opacity="0.542798943781" rx="0" ry="0" stroke="rgb(231, 89, 219)" stroke-opacity="0.704965421745" stroke-width="2" width="174.986012779" x="892.574954495" y="314.284117709"/>""",
        """<rect fill="rgb(161, 176, 31)" height="189.308320967" opacity="0.886047103426" rx="0" ry="0" stroke="rgb(199, 209, 176)" stroke-opacity="0.827015695052" stroke-width="2" width="115.968932804" x="567.502193163" y="792.59243612"/>""",
        """<rect fill="rgb(229, 167, 4)" height="30.8655473363" opacity="0.917293329306" rx="0" ry="0" stroke="rgb(156, 220, 170)" stroke-opacity="0.553987557194" stroke-width="9" width="21.8070735482" x="781.882547906" y="748.507788882"/>""",
        """<rect fill="rgb(91, 147, 1)" height="6.50242046821" opacity="0.883449225332" rx="0" ry="0" stroke="rgb(247, 60, 53)" stroke-opacity="0.993459527505" stroke-width="4" width="186.670628826" x="371.661114476" y="746.494052992"/>""",
        """<rect fill="rgb(102, 137, 133)" height="30.0715583658" opacity="0.810650263352" rx="0" ry="0" stroke="rgb(131, 149, 42)" stroke-opacity="0.60040935745" stroke-width="9" width="197.425122923" x="418.360633235" y="246.880993368"/>""",
        """<rect fill="rgb(88, 247, 163)" height="42.6108312799" opacity="0.967357576328" rx="0" ry="0" stroke="rgb(39, 75, 187)" stroke-opacity="0.859090087535" stroke-width="9" width="142.813121305" x="800.550136646" y="667.370819789"/>""",
        """<rect fill="rgb(54, 3, 160)" height="32.7462760631" opacity="0.918896620829" rx="0" ry="0" stroke="rgb(145, 45, 117)" stroke-opacity="0.885828071142" stroke-width="9" width="52.8752506868" x="280.307625348" y="980.229593361"/>""",
        """<rect fill="rgb(158, 93, 211)" height="5.62742110308" opacity="0.819108989697" rx="0" ry="0" stroke="rgb(157, 131, 238)" stroke-opacity="0.57561822661" stroke-width="2" width="87.052609303" x="237.626923154" y="597.708491973"/>""",
        """<rect fill="rgb(149, 29, 156)" height="122.848474169" opacity="0.604175749687" rx="0" ry="0" stroke="rgb(71, 52, 253)" stroke-opacity="0.909113909265" stroke-width="3" width="71.9178105607" x="667.44939404" y="261.369809125"/>""",
        """<rect fill="rgb(48, 102, 7)" height="12.982784906" opacity="0.525326073195" rx="0" ry="0" stroke="rgb(99, 122, 193)" stroke-opacity="0.957099030262" stroke-width="9" width="196.681153384" x="531.084213795" y="991.247275423"/>""",
        """<rect fill="rgb(63, 101, 62)" height="94.3179266375" opacity="0.78236789162" rx="0" ry="0" stroke="rgb(155, 2, 206)" stroke-opacity="0.815343748771" stroke-width="9" width="173.684382202" x="789.854864277" y="151.347138735"/>""",
        """<rect fill="rgb(176, 135, 249)" height="8.80667788622" opacity="0.936587004546" rx="0" ry="0" stroke="rgb(105, 57, 239)" stroke-opacity="0.643532646549" stroke-width="1" width="142.347408126" x="582.678365738" y="718.906053297"/>""",
        """<rect fill="rgb(188, 211, 162)" height="64.3663950318" opacity="0.533254576912" rx="0" ry="0" stroke="rgb(155, 22, 151)" stroke-opacity="0.562570924301" stroke-width="5" width="163.919893029" x="243.609804846" y="348.039333303"/>""",
        """<rect fill="rgb(54, 234, 66)" height="11.6561115235" opacity="0.788161722114" rx="0" ry="0" stroke="rgb(120, 7, 35)" stroke-opacity="0.865793837306" stroke-width="6" width="39.3516595415" x="861.383873545" y="359.875839698"/>""",
        """<rect fill="rgb(150, 177, 126)" height="174.984425906" opacity="0.699770262818" rx="0" ry="0" stroke="rgb(66, 92, 34)" stroke-opacity="0.987623534736" stroke-width="3" width="5.15063769847" x="959.387623506" y="173.938581489"/>""",
        """<rect fill="rgb(37, 57, 39)" height="27.9574497335" opacity="0.54302718379" rx="0" ry="0" stroke="rgb(165, 91, 94)" stroke-opacity="0.913112939174" stroke-width="3" width="151.886697352" x="370.982826242" y="873.158984397"/>""",
        """<rect fill="rgb(29, 108, 8)" height="84.9644467633" opacity="0.610587426652" rx="0" ry="0" stroke="rgb(107, 221, 1)" stroke-opacity="0.754107430918" stroke-width="8" width="12.5654592755" x="945.964157452" y="939.821818272"/>""",
        """<rect fill="rgb(211, 77, 212)" height="157.506561937" opacity="0.728190060365" rx="0" ry="0" stroke="rgb(211, 111, 155)" stroke-opacity="0.835603244704" stroke-width="8" width="182.061592779" x="724.435210527" y="714.725593003"/>""",
        """<rect fill="rgb(4, 138, 161)" height="156.33706961" opacity="0.572071200279" rx="0" ry="0" stroke="rgb(226, 196, 211)" stroke-opacity="0.591447043479" stroke-width="8" width="196.376860987" x="727.676302626" y="708.685990009"/>""",
        """<rect fill="rgb(215, 82, 167)" height="145.615757539" opacity="0.925989330972" rx="0" ry="0" stroke="rgb(27, 50, 88)" stroke-opacity="0.617665732781" stroke-width="9" width="64.6566204777" x="910.029544502" y="949.423743298"/>""",
        """<rect fill="rgb(162, 155, 59)" height="166.194479014" opacity="0.765788712871" rx="0" ry="0" stroke="rgb(230, 220, 66)" stroke-opacity="0.518786968708" stroke-width="5" width="86.3329390049" x="136.1901471" y="302.961069487"/>""",
        """<rect fill="rgb(85, 162, 124)" height="168.506783658" opacity="0.990622146187" rx="0" ry="0" stroke="rgb(60, 158, 72)" stroke-opacity="0.827574773293" stroke-width="7" width="187.143959004" x="542.803992674" y="564.509360966"/>""",
        """<rect fill="rgb(140, 73, 180)" height="175.581111165" opacity="0.904877023008" rx="0" ry="0" stroke="rgb(101, 176, 212)" stroke-opacity="0.592763691665" stroke-width="10" width="136.536341493" x="126.098323227" y="867.270389829"/>""",
        """<rect fill="rgb(11, 154, 21)" height="54.3161652917" opacity="0.896517364331" rx="0" ry="0" stroke="rgb(133, 126, 190)" stroke-opacity="0.975490920294" stroke-width="10" width="86.0080939804" x="186.629355141" y="981.273530573"/>""",
        """<rect fill="rgb(89, 246, 209)" height="145.979767139" opacity="0.541330395464" rx="0" ry="0" stroke="rgb(238, 183, 37)" stroke-opacity="0.908987102349" stroke-width="9" width="100.206917581" x="730.488546378" y="548.449066253"/>""",
        """<rect fill="rgb(125, 148, 53)" height="62.279470392" opacity="0.959260103557" rx="0" ry="0" stroke="rgb(105, 108, 71)" stroke-opacity="0.756323703131" stroke-width="10" width="61.9164442561" x="107.475276303" y="409.366336114"/>""",
        """<rect fill="rgb(16, 165, 84)" height="20.2580110916" opacity="0.768809586744" rx="0" ry="0" stroke="rgb(246, 122, 74)" stroke-opacity="0.593320216322" stroke-width="4" width="52.2052910467" x="126.994359075" y="429.047703951"/>""",
        """<rect fill="rgb(100, 15, 35)" height="193.378413561" opacity="0.646381153146" rx="0" ry="0" stroke="rgb(138, 46, 238)" stroke-opacity="0.772925494851" stroke-width="4" width="81.5313248731" x="386.066365699" y="953.263833529"/>""",
        """<rect fill="rgb(78, 171, 14)" height="31.5716070267" opacity="0.528862562198" rx="0" ry="0" stroke="rgb(234, 35, 255)" stroke-opacity="0.874145237368" stroke-width="4" width="10.3378748934" x="543.665680934" y="467.739775045"/>""",
        """<rect fill="rgb(172, 122, 246)" height="89.836788895" opacity="0.731920282926" rx="0" ry="0" stroke="rgb(69, 211, 115)" stroke-opacity="0.869951310795" stroke-width="3" width="140.745647355" x="910.587863634" y="149.759605997"/>""",
        """<rect fill="rgb(120, 11, 167)" height="32.6596408289" opacity="0.819055301329" rx="0" ry="0" stroke="rgb(129, 24, 77)" stroke-opacity="0.700645058769" stroke-width="9" width="46.8619131084" x="856.774609545" y="176.941141365"/>""",
        """<rect fill="rgb(86, 11, 5)" height="18.3648232082" opacity="0.546420611828" rx="0" ry="0" stroke="rgb(250, 249, 172)" stroke-opacity="0.680338396142" stroke-width="2" width="105.246864408" x="190.387867176" y="787.000768443"/>""",
        """<rect fill="rgb(106, 72, 18)" height="183.674798143" opacity="0.622996209222" rx="0" ry="0" stroke="rgb(21, 70, 206)" stroke-opacity="0.891230029538" stroke-width="7" width="59.8482847677" x="345.022408967" y="348.701755447"/>""",
        """<rect fill="rgb(32, 116, 208)" height="87.8482663918" opacity="0.960692448199" rx="0" ry="0" stroke="rgb(99, 78, 180)" stroke-opacity="0.931765930172" stroke-width="7" width="90.5667155345" x="645.539493195" y="776.96168857"/>""",
        """<rect fill="rgb(245, 50, 80)" height="178.956562614" opacity="0.970272984255" rx="0" ry="0" stroke="rgb(23, 125, 186)" stroke-opacity="0.763424999633" stroke-width="6" width="91.0314171173" x="302.803409961" y="321.864969112"/>""",
        """<rect fill="rgb(77, 156, 39)" height="36.155137724" opacity="0.787177233981" rx="0" ry="0" stroke="rgb(149, 104, 125)" stroke-opacity="0.597311938627" stroke-width="6" width="132.053106261" x="552.356560642" y="159.40184772"/>""",
        """<rect fill="rgb(221, 123, 228)" height="57.2774737116" opacity="0.625876958784" rx="0" ry="0" stroke="rgb(203, 170, 180)" stroke-opacity="0.803900514135" stroke-width="4" width="56.4412047718" x="422.065610137" y="930.031451621"/>""",
        """<rect fill="rgb(202, 236, 180)" height="142.951809476" opacity="0.664595397302" rx="0" ry="0" stroke="rgb(203, 208, 170)" stroke-opacity="0.583337769255" stroke-width="10" width="154.080846561" x="735.114429365" y="151.075357812"/>""",
        """<rect fill="rgb(36, 200, 20)" height="31.8504101497" opacity="0.979982851783" rx="0" ry="0" stroke="rgb(117, 248, 97)" stroke-opacity="0.603720030333" stroke-width="6" width="192.596072971" x="631.182795318" y="876.773406729"/>""",
        """<rect fill="rgb(255, 255, 103)" height="46.8788460218" opacity="0.638385215266" rx="0" ry="0" stroke="rgb(214, 151, 63)" stroke-opacity="0.55445091655" stroke-width="2" width="116.613025748" x="921.393158559" y="454.93805404"/>""",
        """<rect fill="rgb(96, 30, 209)" height="176.257044256" opacity="0.798933906688" rx="0" ry="0" stroke="rgb(101, 161, 136)" stroke-opacity="0.939761082489" stroke-width="6" width="60.5757817933" x="398.282163219" y="851.992529664"/>""",
        """<rect fill="rgb(34, 174, 109)" height="14.2114293254" opacity="0.793732430519" rx="0" ry="0" stroke="rgb(70, 230, 137)" stroke-opacity="0.541985557936" stroke-width="8" width="197.809100378" x="580.929517835" y="971.46720175"/>""",
        """<rect fill="rgb(71, 247, 169)" height="36.1512938891" opacity="0.654594852183" rx="0" ry="0" stroke="rgb(53, 240, 219)" stroke-opacity="0.859966206903" stroke-width="3" width="105.101695287" x="783.316484433" y="810.564535923"/>""",
        """<rect fill="rgb(166, 121, 124)" height="34.9042004599" opacity="0.989738104444" rx="0" ry="0" stroke="rgb(67, 145, 83)" stroke-opacity="0.87128322404" stroke-width="10" width="119.607127411" x="794.790987725" y="578.272029484"/>""",
        """<rect fill="rgb(54, 107, 127)" height="9.40264604234" opacity="0.568381526788" rx="0" ry="0" stroke="rgb(218, 60, 203)" stroke-opacity="0.988468485633" stroke-width="10" width="130.229302544" x="493.190747889" y="454.318579496"/>""",
        """<rect fill="rgb(217, 72, 133)" height="163.518024282" opacity="0.540713273229" rx="0" ry="0" stroke="rgb(51, 93, 195)" stroke-opacity="0.871619528718" stroke-width="2" width="84.490330701" x="938.035473514" y="723.423614818"/>""",
        """<rect fill="rgb(44, 50, 169)" height="5.936891418" opacity="0.789621623031" rx="0" ry="0" stroke="rgb(156, 253, 182)" stroke-opacity="0.859460461678" stroke-width="6" width="29.9534741023" x="963.998222463" y="659.508598887"/>""",
        """<rect fill="rgb(7, 1, 163)" height="145.998646608" opacity="0.935374515793" rx="0" ry="0" stroke="rgb(195, 251, 35)" stroke-opacity="0.714156206205" stroke-width="9" width="120.038725735" x="561.582212293" y="736.255961995"/>""",
        """<rect fill="rgb(134, 202, 215)" height="42.609823121" opacity="0.952530667559" rx="0" ry="0" stroke="rgb(221, 47, 232)" stroke-opacity="0.720998402303" stroke-width="4" width="117.065301224" x="668.211368138" y="645.732624594"/>""",
        """<rect fill="rgb(214, 5, 15)" height="92.7390487304" opacity="0.822555613407" rx="0" ry="0" stroke="rgb(197, 149, 251)" stroke-opacity="0.628469672518" stroke-width="2" width="66.9554834274" x="485.14339645" y="109.642662111"/>""",
        """<rect fill="rgb(85, 179, 240)" height="121.753514999" opacity="0.695460902312" rx="0" ry="0" stroke="rgb(8, 64, 8)" stroke-opacity="0.549747867694" stroke-width="1" width="60.5932970572" x="510.727436869" y="200.774393771"/>""",
        """<rect fill="rgb(201, 182, 68)" height="25.795752672" opacity="0.609482127593" rx="0" ry="0" stroke="rgb(125, 149, 203)" stroke-opacity="0.545518211955" stroke-width="8" width="51.534709257" x="187.866383807" y="199.160333675"/>""",
        """<rect fill="rgb(43, 124, 248)" height="191.410037547" opacity="0.638394660714" rx="0" ry="0" stroke="rgb(153, 199, 36)" stroke-opacity="0.524145166786" stroke-width="3" width="146.282325943" x="590.806192557" y="526.675286831"/>""",
        """<rect fill="rgb(243, 123, 86)" height="184.397613128" opacity="0.910716900751" rx="0" ry="0" stroke="rgb(216, 56, 175)" stroke-opacity="0.650420172252" stroke-width="9" width="83.8362761393" x="128.826514534" y="856.508856456"/>""",
        """<rect fill="rgb(143, 137, 68)" height="124.724501757" opacity="0.568597624297" rx="0" ry="0" stroke="rgb(155, 164, 68)" stroke-opacity="0.818417497295" stroke-width="10" width="141.622646472" x="238.976733968" y="794.237348997"/>""",
        """<rect fill="rgb(38, 98, 204)" height="40.9094206461" opacity="0.965976640999" rx="0" ry="0" stroke="rgb(63, 230, 253)" stroke-opacity="0.874435162728" stroke-width="3" width="0.935029119992" x="123.747376395" y="430.949480553"/>""",
        """<rect fill="rgb(107, 79, 116)" height="182.860915293" opacity="0.732057759598" rx="0" ry="0" stroke="rgb(192, 121, 234)" stroke-opacity="0.762612954579" stroke-width="3" width="85.3528181032" x="597.218488351" y="399.180101185"/>""",
        """<rect fill="rgb(231, 111, 97)" height="88.1001354282" opacity="0.887491487565" rx="0" ry="0" stroke="rgb(221, 39, 92)" stroke-opacity="0.943250495104" stroke-width="1" width="99.9693260729" x="404.61456736" y="621.858614506"/>""",
        """<rect fill="rgb(154, 104, 160)" height="122.364127494" opacity="0.991179309259" rx="0" ry="0" stroke="rgb(3, 118, 223)" stroke-opacity="0.875359353996" stroke-width="2" width="41.6644641502" x="113.690393133" y="256.490948581"/>""",
        """<rect fill="rgb(44, 93, 236)" height="191.429048702" opacity="0.568804326866" rx="0" ry="0" stroke="rgb(117, 238, 82)" stroke-opacity="0.603022511198" stroke-width="3" width="172.247453123" x="534.095243849" y="509.325666608"/>""",
        """<rect fill="rgb(94, 89, 164)" height="37.7369054932" opacity="0.883276382905" rx="0" ry="0" stroke="rgb(195, 242, 99)" stroke-opacity="0.838729242487" stroke-width="7" width="89.1268400309" x="199.337326763" y="491.501819097"/>""",
        """<rect fill="rgb(19, 188, 177)" height="5.65687275798" opacity="0.705389749908" rx="0" ry="0" stroke="rgb(6, 15, 249)" stroke-opacity="0.725078908781" stroke-width="3" width="168.226551176" x="156.187838771" y="846.187914681"/>""",
        """<rect fill="rgb(240, 37, 149)" height="140.374784118" opacity="0.598421126559" rx="0" ry="0" stroke="rgb(243, 125, 152)" stroke-opacity="0.858703117345" stroke-width="2" width="135.203681303" x="981.053192173" y="376.22017128"/>""",
        """<rect fill="rgb(85, 216, 94)" height="125.30348986" opacity="0.925041391851" rx="0" ry="0" stroke="rgb(167, 149, 255)" stroke-opacity="0.837415769951" stroke-width="1" width="31.9472093049" x="321.14084094" y="947.69815084"/>""",
        """<rect fill="rgb(41, 233, 66)" height="82.5258062501" opacity="0.791417597925" rx="0" ry="0" stroke="rgb(244, 147, 28)" stroke-opacity="0.645499899615" stroke-width="10" width="149.286469015" x="862.733033585" y="925.056397381"/>""",
        """<rect fill="rgb(15, 22, 174)" height="56.933833366" opacity="0.709308468266" rx="0" ry="0" stroke="rgb(114, 69, 10)" stroke-opacity="0.829892869366" stroke-width="1" width="109.889286559" x="908.806257426" y="554.077163415"/>""",
        """<rect fill="rgb(117, 45, 75)" height="2.16460973619" opacity="0.679531775377" rx="0" ry="0" stroke="rgb(23, 171, 2)" stroke-opacity="0.5067083659" stroke-width="8" width="183.986790693" x="486.452604715" y="855.54730169"/>""",
        """<rect fill="rgb(204, 220, 140)" height="196.761352262" opacity="0.733323822065" rx="0" ry="0" stroke="rgb(12, 100, 159)" stroke-opacity="0.713673506643" stroke-width="7" width="174.48470351" x="397.63929119" y="533.800606393"/>""",
        """<rect fill="rgb(37, 142, 102)" height="81.0460157757" opacity="0.869044909442" rx="0" ry="0" stroke="rgb(158, 141, 174)" stroke-opacity="0.995309755488" stroke-width="8" width="121.492128176" x="675.222848721" y="779.011500191"/>""",
        """<rect fill="rgb(96, 113, 213)" height="129.628418069" opacity="0.891897539141" rx="0" ry="0" stroke="rgb(57, 109, 247)" stroke-opacity="0.621826788857" stroke-width="8" width="17.873875198" x="187.607752134" y="743.068578517"/>""",
        """<rect fill="rgb(171, 133, 88)" height="194.523534776" opacity="0.778976865721" rx="0" ry="0" stroke="rgb(200, 143, 50)" stroke-opacity="0.945249535313" stroke-width="7" width="21.5237930374" x="557.97940826" y="919.25803059"/>""",
        """<rect fill="rgb(85, 158, 53)" height="126.95235149" opacity="0.660202074715" rx="0" ry="0" stroke="rgb(240, 243, 50)" stroke-opacity="0.932888285144" stroke-width="8" width="150.06084616" x="949.891272813" y="232.463673352"/>""",
        """<rect fill="rgb(42, 119, 0)" height="29.139560601" opacity="0.874524208824" rx="0" ry="0" stroke="rgb(217, 251, 251)" stroke-opacity="0.646190727617" stroke-width="5" width="135.598367147" x="803.22282438" y="769.564173847"/>""",
        """<rect fill="rgb(134, 171, 130)" height="91.7500319564" opacity="0.552280024676" rx="0" ry="0" stroke="rgb(71, 89, 177)" stroke-opacity="0.877597376666" stroke-width="9" width="172.718501954" x="502.657287726" y="692.490215395"/>""",
        """<rect fill="rgb(15, 28, 97)" height="168.869635593" opacity="0.527763261574" rx="0" ry="0" stroke="rgb(230, 74, 216)" stroke-opacity="0.611001848585" stroke-width="1" width="176.437220067" x="523.085099117" y="889.100181333"/>""",
        """<rect fill="rgb(251, 23, 127)" height="140.060100374" opacity="0.670321604266" rx="0" ry="0" stroke="rgb(36, 99, 172)" stroke-opacity="0.686439870144" stroke-width="1" width="2.20336478283" x="430.448986966" y="336.11298117"/>""",
        """<rect fill="rgb(215, 143, 68)" height="37.7945617144" opacity="0.770865309429" rx="0" ry="0" stroke="rgb(26, 71, 85)" stroke-opacity="0.8685644513" stroke-width="7" width="5.42583228681" x="543.547328809" y="499.97854299"/>""",
        """<rect fill="rgb(232, 205, 31)" height="101.954678168" opacity="0.752969494511" rx="0" ry="0" stroke="rgb(185, 7, 3)" stroke-opacity="0.762241451932" stroke-width="2" width="160.499944898" x="588.828926314" y="248.761734385"/>""",
        """<rect fill="rgb(204, 13, 171)" height="154.123563863" opacity="0.572251067568" rx="0" ry="0" stroke="rgb(72, 107, 247)" stroke-opacity="0.705464712874" stroke-width="3" width="41.495723403" x="177.750961973" y="794.58160985"/>""",
        """<rect fill="rgb(100, 119, 228)" height="169.37123922" opacity="0.754473875408" rx="0" ry="0" stroke="rgb(106, 30, 225)" stroke-opacity="0.678508802306" stroke-width="2" width="141.64735543" x="510.645045815" y="131.633687601"/>""",
        """<rect fill="rgb(165, 158, 28)" height="65.622764192" opacity="0.591259214487" rx="0" ry="0" stroke="rgb(197, 30, 149)" stroke-opacity="0.804279767896" stroke-width="5" width="11.0060075602" x="735.317800282" y="503.123749501"/>""",
        """<rect fill="rgb(76, 43, 53)" height="62.1817311946" opacity="0.938053769346" rx="0" ry="0" stroke="rgb(200, 38, 26)" stroke-opacity="0.502493900886" stroke-width="8" width="21.0800215482" x="754.90300962" y="661.570506434"/>""",
)

    def test_rectangle_to_xml(self):
        """Rectangle: Object ---> XML"""
        assert len(self.rectangle_objects) == len(self.rectangle_xml_strings)
        for rectangle, xml in zip(self.rectangle_objects, self.rectangle_xml_strings): 
            self.assertEqual(rectangle.to_xml(), xml)

 
    def test_rectangle_from_xml(self):
        """Rectangle: XML ---> Object"""
        assert len(self.rectangle_objects) == len(self.rectangle_xml_strings)
        for rectangle, xml in zip(self.rectangle_objects, self.rectangle_xml_strings): 
            self.assertEqual(rectangle, object_from_xml(xml))



class CircleTest(unittest.TestCase):
    """Test For svgenesis.primitives.Circle"""
    ################################################
    # Circle Objects and XML Strings
    ################################################
    circle_objects = (
        Circle(opacity=0.803047795755, stroke_opacity=0.974727339295, stroke=rgb(161, 99, 214), stroke_width=3, cy=751.929294819, cx=532.100898758, r=3.91877294286, fill=rgb(223, 194, 105)),
        Circle(opacity=0.789488045365, stroke_opacity=0.590062235753, stroke=rgb(113, 151, 150), stroke_width=6, cy=469.88386332, cx=423.744374291, r=81.6414507973, fill=rgb(232, 52, 66)),
        Circle(opacity=0.673789815078, stroke_opacity=0.506855157853, stroke=rgb(231, 14, 172), stroke_width=5, cy=378.397041817, cx=235.623576346, r=64.1631521759, fill=rgb(36, 81, 77)),
        Circle(opacity=0.523718209198, stroke_opacity=0.922483012235, stroke=rgb(227, 97, 162), stroke_width=8, cy=742.637947958, cx=203.67441365, r=29.3920946945, fill=rgb(58, 185, 56)),
        Circle(opacity=0.717613300594, stroke_opacity=0.632021996338, stroke=rgb(6, 246, 233), stroke_width=1, cy=832.24876447, cx=669.745882639, r=63.8720999435, fill=rgb(31, 80, 202)),
        Circle(opacity=0.764172955286, stroke_opacity=0.660484604743, stroke=rgb(180, 224, 0), stroke_width=1, cy=832.792096448, cx=911.545857796, r=62.9240649357, fill=rgb(27, 156, 140)),
        Circle(opacity=0.988203741199, stroke_opacity=0.525483782415, stroke=rgb(58, 138, 194), stroke_width=10, cy=347.902369392, cx=767.797716064, r=51.7783515231, fill=rgb(46, 44, 250)),
        Circle(opacity=0.773076255834, stroke_opacity=0.999841404541, stroke=rgb(150, 201, 229), stroke_width=10, cy=868.357747257, cx=971.454578371, r=46.7462896541, fill=rgb(220, 19, 157)),
        Circle(opacity=0.513133991508, stroke_opacity=0.969069876857, stroke=rgb(89, 165, 220), stroke_width=3, cy=887.56324939, cx=497.083952082, r=9.7886830144, fill=rgb(156, 120, 143)),
        Circle(opacity=0.882125043966, stroke_opacity=0.984566391085, stroke=rgb(205, 160, 179), stroke_width=5, cy=483.653374379, cx=311.064993838, r=71.6705037518, fill=rgb(246, 22, 250)),
        Circle(opacity=0.754865721065, stroke_opacity=0.761044246365, stroke=rgb(38, 248, 199), stroke_width=7, cy=233.083321579, cx=998.4137214, r=74.6252446077, fill=rgb(2, 192, 67)),
        Circle(opacity=0.670848722027, stroke_opacity=0.655176123773, stroke=rgb(46, 150, 161), stroke_width=8, cy=372.261032631, cx=658.127114125, r=27.8022551483, fill=rgb(31, 196, 111)),
        Circle(opacity=0.634229263925, stroke_opacity=0.67320631743, stroke=rgb(68, 82, 73), stroke_width=9, cy=410.393811264, cx=269.751618563, r=72.814308847, fill=rgb(52, 230, 125)),
        Circle(opacity=0.532783930973, stroke_opacity=0.668206204894, stroke=rgb(65, 161, 51), stroke_width=3, cy=542.614905219, cx=513.995521867, r=60.7466726397, fill=rgb(173, 143, 253)),
        Circle(opacity=0.813893311055, stroke_opacity=0.805619555234, stroke=rgb(79, 70, 140), stroke_width=8, cy=127.326390916, cx=674.04066548, r=53.8626964663, fill=rgb(90, 209, 107)),
        Circle(opacity=0.874935416851, stroke_opacity=0.702515255858, stroke=rgb(0, 224, 178), stroke_width=8, cy=443.76829405, cx=511.324456858, r=11.0633771216, fill=rgb(157, 210, 20)),
        Circle(opacity=0.694880327201, stroke_opacity=0.962309595136, stroke=rgb(149, 115, 90), stroke_width=5, cy=497.722903396, cx=819.432682543, r=84.8233175071, fill=rgb(176, 116, 220)),
        Circle(opacity=0.659478050139, stroke_opacity=0.567401969186, stroke=rgb(182, 128, 88), stroke_width=6, cy=892.044571179, cx=755.594824196, r=32.4617189778, fill=rgb(75, 182, 84)),
        Circle(opacity=0.771434276978, stroke_opacity=0.890814846513, stroke=rgb(131, 175, 117), stroke_width=2, cy=415.506844886, cx=543.085520989, r=92.5199127547, fill=rgb(165, 39, 250)),
        Circle(opacity=0.882956467601, stroke_opacity=0.528801339452, stroke=rgb(179, 35, 132), stroke_width=1, cy=342.695309223, cx=700.034190341, r=61.4873703314, fill=rgb(213, 106, 12)),
        Circle(opacity=0.855644939046, stroke_opacity=0.51072813522, stroke=rgb(184, 61, 209), stroke_width=3, cy=831.129966107, cx=755.985621568, r=99.5794343285, fill=rgb(173, 248, 171)),
        Circle(opacity=0.801069443121, stroke_opacity=0.770837148102, stroke=rgb(140, 119, 115), stroke_width=7, cy=418.844032664, cx=248.484702361, r=96.6162625158, fill=rgb(215, 53, 72)),
        Circle(opacity=0.659444649082, stroke_opacity=0.977322232648, stroke=rgb(141, 231, 211), stroke_width=9, cy=496.402630862, cx=964.077841057, r=59.4763744102, fill=rgb(145, 234, 192)),
        Circle(opacity=0.502170491829, stroke_opacity=0.888603352001, stroke=rgb(178, 227, 91), stroke_width=10, cy=849.317280741, cx=981.690060317, r=25.6667019858, fill=rgb(206, 124, 211)),
        Circle(opacity=0.729738263085, stroke_opacity=0.948702224947, stroke=rgb(62, 23, 227), stroke_width=5, cy=479.000593924, cx=732.204322219, r=56.6950056989, fill=rgb(56, 109, 185)),
        Circle(opacity=0.901646039517, stroke_opacity=0.953015125701, stroke=rgb(115, 36, 18), stroke_width=5, cy=731.610742664, cx=575.82839487, r=78.1764121961, fill=rgb(146, 231, 227)),
        Circle(opacity=0.553375556824, stroke_opacity=0.6664156737, stroke=rgb(106, 8, 43), stroke_width=1, cy=338.63143971, cx=418.321607871, r=44.1764179335, fill=rgb(13, 109, 214)),
        Circle(opacity=0.878223940553, stroke_opacity=0.948402994162, stroke=rgb(29, 80, 169), stroke_width=2, cy=380.734472055, cx=756.000625092, r=80.5968748835, fill=rgb(243, 70, 148)),
        Circle(opacity=0.981230117191, stroke_opacity=0.52015047658, stroke=rgb(36, 16, 29), stroke_width=6, cy=533.017837294, cx=266.74924963, r=58.3587753733, fill=rgb(209, 181, 145)),
        Circle(opacity=0.802487505041, stroke_opacity=0.774848774336, stroke=rgb(239, 118, 78), stroke_width=10, cy=209.434917368, cx=582.054766422, r=82.2350404637, fill=rgb(116, 255, 132)),
        Circle(opacity=0.520042399173, stroke_opacity=0.752362071449, stroke=rgb(233, 122, 163), stroke_width=6, cy=166.5980034, cx=682.456831658, r=49.1735157602, fill=rgb(79, 167, 220)),
        Circle(opacity=0.755092231586, stroke_opacity=0.844739146296, stroke=rgb(151, 245, 17), stroke_width=2, cy=808.888461703, cx=844.849126956, r=11.2424303035, fill=rgb(249, 164, 86)),
        Circle(opacity=0.848477857746, stroke_opacity=0.729650045247, stroke=rgb(207, 111, 67), stroke_width=5, cy=790.215963174, cx=390.415352064, r=55.9470924601, fill=rgb(113, 197, 214)),
        Circle(opacity=0.564574887855, stroke_opacity=0.599288458743, stroke=rgb(191, 196, 140), stroke_width=10, cy=856.250929384, cx=162.427848124, r=30.0487981996, fill=rgb(35, 134, 90)),
        Circle(opacity=0.592070907814, stroke_opacity=0.502955387365, stroke=rgb(132, 85, 186), stroke_width=7, cy=336.736693296, cx=877.882148693, r=65.3020620526, fill=rgb(175, 92, 132)),
        Circle(opacity=0.963836008642, stroke_opacity=0.562374032533, stroke=rgb(36, 242, 224), stroke_width=9, cy=142.165864031, cx=883.460621851, r=73.9315884636, fill=rgb(20, 26, 135)),
        Circle(opacity=0.780040269967, stroke_opacity=0.603923326525, stroke=rgb(221, 148, 88), stroke_width=2, cy=326.658452236, cx=497.622162189, r=89.7834581473, fill=rgb(57, 95, 145)),
        Circle(opacity=0.897295015917, stroke_opacity=0.577460363226, stroke=rgb(245, 232, 31), stroke_width=7, cy=759.863782459, cx=687.812322466, r=65.1526762118, fill=rgb(194, 119, 142)),
        Circle(opacity=0.51649670769, stroke_opacity=0.966301746167, stroke=rgb(74, 142, 39), stroke_width=7, cy=728.522981925, cx=912.325714568, r=86.9707451987, fill=rgb(144, 122, 49)),
        Circle(opacity=0.551635553999, stroke_opacity=0.910071538839, stroke=rgb(132, 177, 208), stroke_width=3, cy=544.102697643, cx=611.04121167, r=28.2264001123, fill=rgb(242, 180, 220)),
        Circle(opacity=0.689737707836, stroke_opacity=0.503235219128, stroke=rgb(30, 224, 68), stroke_width=6, cy=546.683270599, cx=918.837893277, r=61.6409681807, fill=rgb(247, 250, 86)),
        Circle(opacity=0.660788743362, stroke_opacity=0.880079967409, stroke=rgb(39, 186, 78), stroke_width=10, cy=613.876300435, cx=877.868604272, r=63.1911012011, fill=rgb(201, 208, 23)),
        Circle(opacity=0.714547577889, stroke_opacity=0.560588863653, stroke=rgb(151, 71, 177), stroke_width=3, cy=698.259581702, cx=668.446543004, r=13.1474540052, fill=rgb(219, 90, 176)),
        Circle(opacity=0.814032002547, stroke_opacity=0.928337640478, stroke=rgb(35, 105, 209), stroke_width=3, cy=907.946747971, cx=164.181777334, r=76.4051640943, fill=rgb(226, 202, 30)),
        Circle(opacity=0.783060424714, stroke_opacity=0.98860052572, stroke=rgb(186, 221, 8), stroke_width=4, cy=640.778083932, cx=494.255401597, r=14.5563808722, fill=rgb(8, 234, 67)),
        Circle(opacity=0.844133860417, stroke_opacity=0.966089569535, stroke=rgb(2, 152, 187), stroke_width=2, cy=531.462076206, cx=314.728727424, r=22.1919289725, fill=rgb(66, 175, 167)),
        Circle(opacity=0.960968727462, stroke_opacity=0.91359352382, stroke=rgb(129, 84, 167), stroke_width=9, cy=573.34261096, cx=292.845461698, r=26.3050911236, fill=rgb(136, 147, 19)),
        Circle(opacity=0.571423660528, stroke_opacity=0.796380128683, stroke=rgb(209, 243, 29), stroke_width=1, cy=109.869399128, cx=565.16913329, r=3.4959761699, fill=rgb(246, 189, 53)),
        Circle(opacity=0.625839377084, stroke_opacity=0.830924133611, stroke=rgb(246, 64, 6), stroke_width=5, cy=995.013824162, cx=537.292597188, r=96.0680752143, fill=rgb(28, 56, 105)),
        Circle(opacity=0.587085226317, stroke_opacity=0.633253844879, stroke=rgb(26, 17, 169), stroke_width=3, cy=475.788938342, cx=266.245095526, r=95.8704492181, fill=rgb(121, 133, 188)),
        Circle(opacity=0.890780447751, stroke_opacity=0.738008250668, stroke=rgb(64, 166, 16), stroke_width=2, cy=402.765776833, cx=878.935539991, r=51.979843714, fill=rgb(23, 60, 118)),
        Circle(opacity=0.979843699357, stroke_opacity=0.731321711904, stroke=rgb(53, 235, 235), stroke_width=8, cy=369.578889724, cx=597.517043357, r=45.6355361135, fill=rgb(54, 130, 144)),
        Circle(opacity=0.983637619995, stroke_opacity=0.80050166045, stroke=rgb(177, 184, 156), stroke_width=10, cy=518.665306043, cx=665.673660955, r=64.9317639179, fill=rgb(61, 126, 179)),
        Circle(opacity=0.695079471282, stroke_opacity=0.678779615638, stroke=rgb(169, 92, 202), stroke_width=6, cy=817.052403657, cx=967.951972721, r=82.978267673, fill=rgb(34, 42, 185)),
        Circle(opacity=0.794972286667, stroke_opacity=0.737514225004, stroke=rgb(235, 179, 69), stroke_width=5, cy=826.38770012, cx=240.992208886, r=68.2972618362, fill=rgb(215, 51, 88)),
        Circle(opacity=0.745689887899, stroke_opacity=0.798857578313, stroke=rgb(53, 75, 61), stroke_width=5, cy=295.400100308, cx=601.658955544, r=82.2542659199, fill=rgb(94, 80, 43)),
        Circle(opacity=0.854673883622, stroke_opacity=0.837351773157, stroke=rgb(171, 155, 226), stroke_width=9, cy=805.044167941, cx=617.828615333, r=68.212411402, fill=rgb(210, 138, 61)),
        Circle(opacity=0.746143649967, stroke_opacity=0.56942737242, stroke=rgb(119, 111, 180), stroke_width=6, cy=231.9308613, cx=551.070722369, r=89.2775834214, fill=rgb(205, 86, 219)),
        Circle(opacity=0.724299375236, stroke_opacity=0.689276273229, stroke=rgb(47, 236, 96), stroke_width=9, cy=272.974941867, cx=895.518242493, r=60.0316157097, fill=rgb(130, 211, 87)),
        Circle(opacity=0.626433127263, stroke_opacity=0.785249940276, stroke=rgb(116, 226, 155), stroke_width=7, cy=661.533882949, cx=573.981170922, r=5.82514416731, fill=rgb(153, 117, 237)),
        Circle(opacity=0.753644814887, stroke_opacity=0.813374490797, stroke=rgb(192, 145, 100), stroke_width=5, cy=314.796802306, cx=622.316252827, r=59.4295555772, fill=rgb(137, 82, 139)),
        Circle(opacity=0.632070367976, stroke_opacity=0.807255960627, stroke=rgb(156, 141, 2), stroke_width=4, cy=330.149136302, cx=667.410840834, r=46.9434942474, fill=rgb(73, 143, 25)),
        Circle(opacity=0.523288236816, stroke_opacity=0.760583249548, stroke=rgb(29, 102, 32), stroke_width=10, cy=738.723633769, cx=666.07496452, r=44.564288818, fill=rgb(78, 105, 97)),
        Circle(opacity=0.903177109762, stroke_opacity=0.904740286711, stroke=rgb(225, 210, 215), stroke_width=6, cy=852.897871134, cx=950.915840308, r=6.81624466079, fill=rgb(235, 2, 155)),
        Circle(opacity=0.78395915123, stroke_opacity=0.559929180465, stroke=rgb(253, 242, 47), stroke_width=4, cy=995.947805118, cx=984.851082106, r=59.9834491775, fill=rgb(59, 226, 67)),
        Circle(opacity=0.780193378065, stroke_opacity=0.656642064772, stroke=rgb(64, 68, 36), stroke_width=7, cy=595.312248976, cx=369.08910313, r=36.4525254947, fill=rgb(25, 207, 216)),
        Circle(opacity=0.751978537422, stroke_opacity=0.794436607158, stroke=rgb(68, 251, 131), stroke_width=3, cy=547.175536211, cx=778.185790645, r=83.7746275475, fill=rgb(65, 99, 175)),
        Circle(opacity=0.951312169171, stroke_opacity=0.597594517219, stroke=rgb(40, 150, 32), stroke_width=10, cy=663.917900256, cx=249.510499816, r=8.1645908624, fill=rgb(250, 236, 77)),
        Circle(opacity=0.836299215033, stroke_opacity=0.953728165293, stroke=rgb(199, 130, 181), stroke_width=10, cy=910.88466703, cx=918.598031553, r=50.780810518, fill=rgb(48, 236, 20)),
        Circle(opacity=0.792638979298, stroke_opacity=0.800712927785, stroke=rgb(73, 62, 145), stroke_width=2, cy=280.913379354, cx=551.516955852, r=14.0581147595, fill=rgb(159, 10, 180)),
        Circle(opacity=0.778037980273, stroke_opacity=0.956763208977, stroke=rgb(11, 23, 19), stroke_width=9, cy=931.794259949, cx=776.16024893, r=8.59286913582, fill=rgb(180, 193, 188)),
        Circle(opacity=0.5496496617, stroke_opacity=0.67158525595, stroke=rgb(177, 51, 70), stroke_width=6, cy=589.176043029, cx=424.479906263, r=55.1730438199, fill=rgb(157, 199, 108)),
        Circle(opacity=0.898756921524, stroke_opacity=0.713012570084, stroke=rgb(35, 152, 4), stroke_width=10, cy=450.937693742, cx=890.774641645, r=86.0833437354, fill=rgb(155, 7, 203)),
        Circle(opacity=0.87248646509, stroke_opacity=0.605744261036, stroke=rgb(123, 169, 21), stroke_width=2, cy=812.920954323, cx=275.024446222, r=44.8564249009, fill=rgb(16, 35, 143)),
        Circle(opacity=0.954125485987, stroke_opacity=0.877651600723, stroke=rgb(197, 195, 200), stroke_width=1, cy=322.999807261, cx=454.375508281, r=84.7375318245, fill=rgb(96, 212, 105)),
        Circle(opacity=0.567652091457, stroke_opacity=0.957276202258, stroke=rgb(196, 37, 136), stroke_width=10, cy=635.508250508, cx=924.185067135, r=40.4341871562, fill=rgb(22, 246, 58)),
        Circle(opacity=0.716139837315, stroke_opacity=0.658746800049, stroke=rgb(216, 130, 99), stroke_width=3, cy=244.406952855, cx=725.7590226, r=97.8249933628, fill=rgb(192, 124, 130)),
        Circle(opacity=0.793601542884, stroke_opacity=0.694293773051, stroke=rgb(23, 177, 158), stroke_width=4, cy=767.147649896, cx=788.778947228, r=9.54796345745, fill=rgb(146, 238, 245)),
        Circle(opacity=0.802407112651, stroke_opacity=0.676145737462, stroke=rgb(222, 249, 31), stroke_width=6, cy=872.468066673, cx=957.929760832, r=6.77010376848, fill=rgb(75, 175, 100)),
        Circle(opacity=0.617081202298, stroke_opacity=0.508964082229, stroke=rgb(240, 213, 24), stroke_width=8, cy=958.154631439, cx=476.887589945, r=41.3475484169, fill=rgb(168, 175, 234)),
        Circle(opacity=0.639106755829, stroke_opacity=0.846518915291, stroke=rgb(59, 254, 191), stroke_width=10, cy=911.073970872, cx=267.320825756, r=73.3702153277, fill=rgb(145, 96, 74)),
        Circle(opacity=0.679546650359, stroke_opacity=0.541884325778, stroke=rgb(219, 140, 102), stroke_width=5, cy=604.707902314, cx=359.169865386, r=42.6684356157, fill=rgb(126, 116, 183)),
        Circle(opacity=0.644067979323, stroke_opacity=0.516713740668, stroke=rgb(244, 93, 133), stroke_width=2, cy=831.386720096, cx=303.75177485, r=38.8957138119, fill=rgb(145, 240, 208)),
        Circle(opacity=0.765455989683, stroke_opacity=0.985558315863, stroke=rgb(104, 38, 50), stroke_width=6, cy=265.351310683, cx=769.679684133, r=91.3814944447, fill=rgb(181, 60, 21)),
        Circle(opacity=0.914702512681, stroke_opacity=0.865073682369, stroke=rgb(70, 71, 13), stroke_width=7, cy=633.560782517, cx=468.293308161, r=67.6539438556, fill=rgb(219, 54, 242)),
        Circle(opacity=0.882279428282, stroke_opacity=0.741748817094, stroke=rgb(35, 36, 69), stroke_width=1, cy=792.5078207, cx=138.533715065, r=64.1027875048, fill=rgb(92, 247, 185)),
        Circle(opacity=0.516813767254, stroke_opacity=0.603320584586, stroke=rgb(55, 17, 37), stroke_width=6, cy=119.160840016, cx=872.480825566, r=13.8676176512, fill=rgb(94, 172, 106)),
        Circle(opacity=0.703716947763, stroke_opacity=0.75128592329, stroke=rgb(205, 210, 197), stroke_width=10, cy=909.068757906, cx=660.121966533, r=41.7391957335, fill=rgb(124, 214, 134)),
        Circle(opacity=0.755002045433, stroke_opacity=0.820245891985, stroke=rgb(166, 43, 93), stroke_width=3, cy=537.963061377, cx=118.310552033, r=90.3146343686, fill=rgb(103, 217, 203)),
        Circle(opacity=0.960927684937, stroke_opacity=0.658945536142, stroke=rgb(226, 75, 7), stroke_width=4, cy=593.479967913, cx=594.049081398, r=16.6787239733, fill=rgb(21, 172, 102)),
        Circle(opacity=0.993835667404, stroke_opacity=0.837961788955, stroke=rgb(232, 229, 121), stroke_width=2, cy=248.344231666, cx=452.657298909, r=24.1533451378, fill=rgb(48, 42, 24)),
        Circle(opacity=0.892314842586, stroke_opacity=0.923384948058, stroke=rgb(24, 175, 145), stroke_width=5, cy=541.577545753, cx=207.971457035, r=21.676585846, fill=rgb(68, 150, 129)),
        Circle(opacity=0.826347491009, stroke_opacity=0.725240446615, stroke=rgb(49, 131, 94), stroke_width=2, cy=879.7941829, cx=603.538831727, r=79.4539418966, fill=rgb(229, 86, 202)),
        Circle(opacity=0.585920391357, stroke_opacity=0.930214151718, stroke=rgb(197, 22, 203), stroke_width=4, cy=441.644508363, cx=871.448185548, r=52.6463460527, fill=rgb(207, 58, 98)),
        Circle(opacity=0.713897143229, stroke_opacity=0.891150805968, stroke=rgb(30, 214, 119), stroke_width=5, cy=584.487780661, cx=108.346718321, r=6.17447817943, fill=rgb(245, 199, 174)),
        Circle(opacity=0.909544904176, stroke_opacity=0.876260038152, stroke=rgb(214, 66, 184), stroke_width=3, cy=961.137635329, cx=437.239746766, r=18.3934997121, fill=rgb(169, 179, 45)),
        Circle(opacity=0.845753439732, stroke_opacity=0.913739245527, stroke=rgb(106, 61, 177), stroke_width=1, cy=697.416270748, cx=344.192791738, r=77.8840400366, fill=rgb(105, 166, 151)),
        Circle(opacity=0.616448403974, stroke_opacity=0.589961935696, stroke=rgb(0, 97, 65), stroke_width=7, cy=964.474347623, cx=208.196164241, r=79.0263486014, fill=rgb(140, 7, 124)),
        Circle(opacity=0.878857178886, stroke_opacity=0.714117455413, stroke=rgb(42, 89, 83), stroke_width=1, cy=313.029347355, cx=472.809085368, r=53.5851594587, fill=rgb(48, 67, 164)),
        Circle(opacity=0.776355406515, stroke_opacity=0.74306476976, stroke=rgb(237, 131, 232), stroke_width=10, cy=390.234828057, cx=944.576978919, r=98.0172328945, fill=rgb(254, 105, 176)),
        
)

    circle_xml_strings = (
        """<circle cx="532.100898758" cy="751.929294819" fill="rgb(223, 194, 105)" opacity="0.803047795755" r="3.91877294286" stroke="rgb(161, 99, 214)" stroke-opacity="0.974727339295" stroke-width="3"/>""",
        """<circle cx="423.744374291" cy="469.88386332" fill="rgb(232, 52, 66)" opacity="0.789488045365" r="81.6414507973" stroke="rgb(113, 151, 150)" stroke-opacity="0.590062235753" stroke-width="6"/>""",
        """<circle cx="235.623576346" cy="378.397041817" fill="rgb(36, 81, 77)" opacity="0.673789815078" r="64.1631521759" stroke="rgb(231, 14, 172)" stroke-opacity="0.506855157853" stroke-width="5"/>""",
        """<circle cx="203.67441365" cy="742.637947958" fill="rgb(58, 185, 56)" opacity="0.523718209198" r="29.3920946945" stroke="rgb(227, 97, 162)" stroke-opacity="0.922483012235" stroke-width="8"/>""",
        """<circle cx="669.745882639" cy="832.24876447" fill="rgb(31, 80, 202)" opacity="0.717613300594" r="63.8720999435" stroke="rgb(6, 246, 233)" stroke-opacity="0.632021996338" stroke-width="1"/>""",
        """<circle cx="911.545857796" cy="832.792096448" fill="rgb(27, 156, 140)" opacity="0.764172955286" r="62.9240649357" stroke="rgb(180, 224, 0)" stroke-opacity="0.660484604743" stroke-width="1"/>""",
        """<circle cx="767.797716064" cy="347.902369392" fill="rgb(46, 44, 250)" opacity="0.988203741199" r="51.7783515231" stroke="rgb(58, 138, 194)" stroke-opacity="0.525483782415" stroke-width="10"/>""",
        """<circle cx="971.454578371" cy="868.357747257" fill="rgb(220, 19, 157)" opacity="0.773076255834" r="46.7462896541" stroke="rgb(150, 201, 229)" stroke-opacity="0.999841404541" stroke-width="10"/>""",
        """<circle cx="497.083952082" cy="887.56324939" fill="rgb(156, 120, 143)" opacity="0.513133991508" r="9.7886830144" stroke="rgb(89, 165, 220)" stroke-opacity="0.969069876857" stroke-width="3"/>""",
        """<circle cx="311.064993838" cy="483.653374379" fill="rgb(246, 22, 250)" opacity="0.882125043966" r="71.6705037518" stroke="rgb(205, 160, 179)" stroke-opacity="0.984566391085" stroke-width="5"/>""",
        """<circle cx="998.4137214" cy="233.083321579" fill="rgb(2, 192, 67)" opacity="0.754865721065" r="74.6252446077" stroke="rgb(38, 248, 199)" stroke-opacity="0.761044246365" stroke-width="7"/>""",
        """<circle cx="658.127114125" cy="372.261032631" fill="rgb(31, 196, 111)" opacity="0.670848722027" r="27.8022551483" stroke="rgb(46, 150, 161)" stroke-opacity="0.655176123773" stroke-width="8"/>""",
        """<circle cx="269.751618563" cy="410.393811264" fill="rgb(52, 230, 125)" opacity="0.634229263925" r="72.814308847" stroke="rgb(68, 82, 73)" stroke-opacity="0.67320631743" stroke-width="9"/>""",
        """<circle cx="513.995521867" cy="542.614905219" fill="rgb(173, 143, 253)" opacity="0.532783930973" r="60.7466726397" stroke="rgb(65, 161, 51)" stroke-opacity="0.668206204894" stroke-width="3"/>""",
        """<circle cx="674.04066548" cy="127.326390916" fill="rgb(90, 209, 107)" opacity="0.813893311055" r="53.8626964663" stroke="rgb(79, 70, 140)" stroke-opacity="0.805619555234" stroke-width="8"/>""",
        """<circle cx="511.324456858" cy="443.76829405" fill="rgb(157, 210, 20)" opacity="0.874935416851" r="11.0633771216" stroke="rgb(0, 224, 178)" stroke-opacity="0.702515255858" stroke-width="8"/>""",
        """<circle cx="819.432682543" cy="497.722903396" fill="rgb(176, 116, 220)" opacity="0.694880327201" r="84.8233175071" stroke="rgb(149, 115, 90)" stroke-opacity="0.962309595136" stroke-width="5"/>""",
        """<circle cx="755.594824196" cy="892.044571179" fill="rgb(75, 182, 84)" opacity="0.659478050139" r="32.4617189778" stroke="rgb(182, 128, 88)" stroke-opacity="0.567401969186" stroke-width="6"/>""",
        """<circle cx="543.085520989" cy="415.506844886" fill="rgb(165, 39, 250)" opacity="0.771434276978" r="92.5199127547" stroke="rgb(131, 175, 117)" stroke-opacity="0.890814846513" stroke-width="2"/>""",
        """<circle cx="700.034190341" cy="342.695309223" fill="rgb(213, 106, 12)" opacity="0.882956467601" r="61.4873703314" stroke="rgb(179, 35, 132)" stroke-opacity="0.528801339452" stroke-width="1"/>""",
        """<circle cx="755.985621568" cy="831.129966107" fill="rgb(173, 248, 171)" opacity="0.855644939046" r="99.5794343285" stroke="rgb(184, 61, 209)" stroke-opacity="0.51072813522" stroke-width="3"/>""",
        """<circle cx="248.484702361" cy="418.844032664" fill="rgb(215, 53, 72)" opacity="0.801069443121" r="96.6162625158" stroke="rgb(140, 119, 115)" stroke-opacity="0.770837148102" stroke-width="7"/>""",
        """<circle cx="964.077841057" cy="496.402630862" fill="rgb(145, 234, 192)" opacity="0.659444649082" r="59.4763744102" stroke="rgb(141, 231, 211)" stroke-opacity="0.977322232648" stroke-width="9"/>""",
        """<circle cx="981.690060317" cy="849.317280741" fill="rgb(206, 124, 211)" opacity="0.502170491829" r="25.6667019858" stroke="rgb(178, 227, 91)" stroke-opacity="0.888603352001" stroke-width="10"/>""",
        """<circle cx="732.204322219" cy="479.000593924" fill="rgb(56, 109, 185)" opacity="0.729738263085" r="56.6950056989" stroke="rgb(62, 23, 227)" stroke-opacity="0.948702224947" stroke-width="5"/>""",
        """<circle cx="575.82839487" cy="731.610742664" fill="rgb(146, 231, 227)" opacity="0.901646039517" r="78.1764121961" stroke="rgb(115, 36, 18)" stroke-opacity="0.953015125701" stroke-width="5"/>""",
        """<circle cx="418.321607871" cy="338.63143971" fill="rgb(13, 109, 214)" opacity="0.553375556824" r="44.1764179335" stroke="rgb(106, 8, 43)" stroke-opacity="0.6664156737" stroke-width="1"/>""",
        """<circle cx="756.000625092" cy="380.734472055" fill="rgb(243, 70, 148)" opacity="0.878223940553" r="80.5968748835" stroke="rgb(29, 80, 169)" stroke-opacity="0.948402994162" stroke-width="2"/>""",
        """<circle cx="266.74924963" cy="533.017837294" fill="rgb(209, 181, 145)" opacity="0.981230117191" r="58.3587753733" stroke="rgb(36, 16, 29)" stroke-opacity="0.52015047658" stroke-width="6"/>""",
        """<circle cx="582.054766422" cy="209.434917368" fill="rgb(116, 255, 132)" opacity="0.802487505041" r="82.2350404637" stroke="rgb(239, 118, 78)" stroke-opacity="0.774848774336" stroke-width="10"/>""",
        """<circle cx="682.456831658" cy="166.5980034" fill="rgb(79, 167, 220)" opacity="0.520042399173" r="49.1735157602" stroke="rgb(233, 122, 163)" stroke-opacity="0.752362071449" stroke-width="6"/>""",
        """<circle cx="844.849126956" cy="808.888461703" fill="rgb(249, 164, 86)" opacity="0.755092231586" r="11.2424303035" stroke="rgb(151, 245, 17)" stroke-opacity="0.844739146296" stroke-width="2"/>""",
        """<circle cx="390.415352064" cy="790.215963174" fill="rgb(113, 197, 214)" opacity="0.848477857746" r="55.9470924601" stroke="rgb(207, 111, 67)" stroke-opacity="0.729650045247" stroke-width="5"/>""",
        """<circle cx="162.427848124" cy="856.250929384" fill="rgb(35, 134, 90)" opacity="0.564574887855" r="30.0487981996" stroke="rgb(191, 196, 140)" stroke-opacity="0.599288458743" stroke-width="10"/>""",
        """<circle cx="877.882148693" cy="336.736693296" fill="rgb(175, 92, 132)" opacity="0.592070907814" r="65.3020620526" stroke="rgb(132, 85, 186)" stroke-opacity="0.502955387365" stroke-width="7"/>""",
        """<circle cx="883.460621851" cy="142.165864031" fill="rgb(20, 26, 135)" opacity="0.963836008642" r="73.9315884636" stroke="rgb(36, 242, 224)" stroke-opacity="0.562374032533" stroke-width="9"/>""",
        """<circle cx="497.622162189" cy="326.658452236" fill="rgb(57, 95, 145)" opacity="0.780040269967" r="89.7834581473" stroke="rgb(221, 148, 88)" stroke-opacity="0.603923326525" stroke-width="2"/>""",
        """<circle cx="687.812322466" cy="759.863782459" fill="rgb(194, 119, 142)" opacity="0.897295015917" r="65.1526762118" stroke="rgb(245, 232, 31)" stroke-opacity="0.577460363226" stroke-width="7"/>""",
        """<circle cx="912.325714568" cy="728.522981925" fill="rgb(144, 122, 49)" opacity="0.51649670769" r="86.9707451987" stroke="rgb(74, 142, 39)" stroke-opacity="0.966301746167" stroke-width="7"/>""",
        """<circle cx="611.04121167" cy="544.102697643" fill="rgb(242, 180, 220)" opacity="0.551635553999" r="28.2264001123" stroke="rgb(132, 177, 208)" stroke-opacity="0.910071538839" stroke-width="3"/>""",
        """<circle cx="918.837893277" cy="546.683270599" fill="rgb(247, 250, 86)" opacity="0.689737707836" r="61.6409681807" stroke="rgb(30, 224, 68)" stroke-opacity="0.503235219128" stroke-width="6"/>""",
        """<circle cx="877.868604272" cy="613.876300435" fill="rgb(201, 208, 23)" opacity="0.660788743362" r="63.1911012011" stroke="rgb(39, 186, 78)" stroke-opacity="0.880079967409" stroke-width="10"/>""",
        """<circle cx="668.446543004" cy="698.259581702" fill="rgb(219, 90, 176)" opacity="0.714547577889" r="13.1474540052" stroke="rgb(151, 71, 177)" stroke-opacity="0.560588863653" stroke-width="3"/>""",
        """<circle cx="164.181777334" cy="907.946747971" fill="rgb(226, 202, 30)" opacity="0.814032002547" r="76.4051640943" stroke="rgb(35, 105, 209)" stroke-opacity="0.928337640478" stroke-width="3"/>""",
        """<circle cx="494.255401597" cy="640.778083932" fill="rgb(8, 234, 67)" opacity="0.783060424714" r="14.5563808722" stroke="rgb(186, 221, 8)" stroke-opacity="0.98860052572" stroke-width="4"/>""",
        """<circle cx="314.728727424" cy="531.462076206" fill="rgb(66, 175, 167)" opacity="0.844133860417" r="22.1919289725" stroke="rgb(2, 152, 187)" stroke-opacity="0.966089569535" stroke-width="2"/>""",
        """<circle cx="292.845461698" cy="573.34261096" fill="rgb(136, 147, 19)" opacity="0.960968727462" r="26.3050911236" stroke="rgb(129, 84, 167)" stroke-opacity="0.91359352382" stroke-width="9"/>""",
        """<circle cx="565.16913329" cy="109.869399128" fill="rgb(246, 189, 53)" opacity="0.571423660528" r="3.4959761699" stroke="rgb(209, 243, 29)" stroke-opacity="0.796380128683" stroke-width="1"/>""",
        """<circle cx="537.292597188" cy="995.013824162" fill="rgb(28, 56, 105)" opacity="0.625839377084" r="96.0680752143" stroke="rgb(246, 64, 6)" stroke-opacity="0.830924133611" stroke-width="5"/>""",
        """<circle cx="266.245095526" cy="475.788938342" fill="rgb(121, 133, 188)" opacity="0.587085226317" r="95.8704492181" stroke="rgb(26, 17, 169)" stroke-opacity="0.633253844879" stroke-width="3"/>""",
        """<circle cx="878.935539991" cy="402.765776833" fill="rgb(23, 60, 118)" opacity="0.890780447751" r="51.979843714" stroke="rgb(64, 166, 16)" stroke-opacity="0.738008250668" stroke-width="2"/>""",
        """<circle cx="597.517043357" cy="369.578889724" fill="rgb(54, 130, 144)" opacity="0.979843699357" r="45.6355361135" stroke="rgb(53, 235, 235)" stroke-opacity="0.731321711904" stroke-width="8"/>""",
        """<circle cx="665.673660955" cy="518.665306043" fill="rgb(61, 126, 179)" opacity="0.983637619995" r="64.9317639179" stroke="rgb(177, 184, 156)" stroke-opacity="0.80050166045" stroke-width="10"/>""",
        """<circle cx="967.951972721" cy="817.052403657" fill="rgb(34, 42, 185)" opacity="0.695079471282" r="82.978267673" stroke="rgb(169, 92, 202)" stroke-opacity="0.678779615638" stroke-width="6"/>""",
        """<circle cx="240.992208886" cy="826.38770012" fill="rgb(215, 51, 88)" opacity="0.794972286667" r="68.2972618362" stroke="rgb(235, 179, 69)" stroke-opacity="0.737514225004" stroke-width="5"/>""",
        """<circle cx="601.658955544" cy="295.400100308" fill="rgb(94, 80, 43)" opacity="0.745689887899" r="82.2542659199" stroke="rgb(53, 75, 61)" stroke-opacity="0.798857578313" stroke-width="5"/>""",
        """<circle cx="617.828615333" cy="805.044167941" fill="rgb(210, 138, 61)" opacity="0.854673883622" r="68.212411402" stroke="rgb(171, 155, 226)" stroke-opacity="0.837351773157" stroke-width="9"/>""",
        """<circle cx="551.070722369" cy="231.9308613" fill="rgb(205, 86, 219)" opacity="0.746143649967" r="89.2775834214" stroke="rgb(119, 111, 180)" stroke-opacity="0.56942737242" stroke-width="6"/>""",
        """<circle cx="895.518242493" cy="272.974941867" fill="rgb(130, 211, 87)" opacity="0.724299375236" r="60.0316157097" stroke="rgb(47, 236, 96)" stroke-opacity="0.689276273229" stroke-width="9"/>""",
        """<circle cx="573.981170922" cy="661.533882949" fill="rgb(153, 117, 237)" opacity="0.626433127263" r="5.82514416731" stroke="rgb(116, 226, 155)" stroke-opacity="0.785249940276" stroke-width="7"/>""",
        """<circle cx="622.316252827" cy="314.796802306" fill="rgb(137, 82, 139)" opacity="0.753644814887" r="59.4295555772" stroke="rgb(192, 145, 100)" stroke-opacity="0.813374490797" stroke-width="5"/>""",
        """<circle cx="667.410840834" cy="330.149136302" fill="rgb(73, 143, 25)" opacity="0.632070367976" r="46.9434942474" stroke="rgb(156, 141, 2)" stroke-opacity="0.807255960627" stroke-width="4"/>""",
        """<circle cx="666.07496452" cy="738.723633769" fill="rgb(78, 105, 97)" opacity="0.523288236816" r="44.564288818" stroke="rgb(29, 102, 32)" stroke-opacity="0.760583249548" stroke-width="10"/>""",
        """<circle cx="950.915840308" cy="852.897871134" fill="rgb(235, 2, 155)" opacity="0.903177109762" r="6.81624466079" stroke="rgb(225, 210, 215)" stroke-opacity="0.904740286711" stroke-width="6"/>""",
        """<circle cx="984.851082106" cy="995.947805118" fill="rgb(59, 226, 67)" opacity="0.78395915123" r="59.9834491775" stroke="rgb(253, 242, 47)" stroke-opacity="0.559929180465" stroke-width="4"/>""",
        """<circle cx="369.08910313" cy="595.312248976" fill="rgb(25, 207, 216)" opacity="0.780193378065" r="36.4525254947" stroke="rgb(64, 68, 36)" stroke-opacity="0.656642064772" stroke-width="7"/>""",
        """<circle cx="778.185790645" cy="547.175536211" fill="rgb(65, 99, 175)" opacity="0.751978537422" r="83.7746275475" stroke="rgb(68, 251, 131)" stroke-opacity="0.794436607158" stroke-width="3"/>""",
        """<circle cx="249.510499816" cy="663.917900256" fill="rgb(250, 236, 77)" opacity="0.951312169171" r="8.1645908624" stroke="rgb(40, 150, 32)" stroke-opacity="0.597594517219" stroke-width="10"/>""",
        """<circle cx="918.598031553" cy="910.88466703" fill="rgb(48, 236, 20)" opacity="0.836299215033" r="50.780810518" stroke="rgb(199, 130, 181)" stroke-opacity="0.953728165293" stroke-width="10"/>""",
        """<circle cx="551.516955852" cy="280.913379354" fill="rgb(159, 10, 180)" opacity="0.792638979298" r="14.0581147595" stroke="rgb(73, 62, 145)" stroke-opacity="0.800712927785" stroke-width="2"/>""",
        """<circle cx="776.16024893" cy="931.794259949" fill="rgb(180, 193, 188)" opacity="0.778037980273" r="8.59286913582" stroke="rgb(11, 23, 19)" stroke-opacity="0.956763208977" stroke-width="9"/>""",
        """<circle cx="424.479906263" cy="589.176043029" fill="rgb(157, 199, 108)" opacity="0.5496496617" r="55.1730438199" stroke="rgb(177, 51, 70)" stroke-opacity="0.67158525595" stroke-width="6"/>""",
        """<circle cx="890.774641645" cy="450.937693742" fill="rgb(155, 7, 203)" opacity="0.898756921524" r="86.0833437354" stroke="rgb(35, 152, 4)" stroke-opacity="0.713012570084" stroke-width="10"/>""",
        """<circle cx="275.024446222" cy="812.920954323" fill="rgb(16, 35, 143)" opacity="0.87248646509" r="44.8564249009" stroke="rgb(123, 169, 21)" stroke-opacity="0.605744261036" stroke-width="2"/>""",
        """<circle cx="454.375508281" cy="322.999807261" fill="rgb(96, 212, 105)" opacity="0.954125485987" r="84.7375318245" stroke="rgb(197, 195, 200)" stroke-opacity="0.877651600723" stroke-width="1"/>""",
        """<circle cx="924.185067135" cy="635.508250508" fill="rgb(22, 246, 58)" opacity="0.567652091457" r="40.4341871562" stroke="rgb(196, 37, 136)" stroke-opacity="0.957276202258" stroke-width="10"/>""",
        """<circle cx="725.7590226" cy="244.406952855" fill="rgb(192, 124, 130)" opacity="0.716139837315" r="97.8249933628" stroke="rgb(216, 130, 99)" stroke-opacity="0.658746800049" stroke-width="3"/>""",
        """<circle cx="788.778947228" cy="767.147649896" fill="rgb(146, 238, 245)" opacity="0.793601542884" r="9.54796345745" stroke="rgb(23, 177, 158)" stroke-opacity="0.694293773051" stroke-width="4"/>""",
        """<circle cx="957.929760832" cy="872.468066673" fill="rgb(75, 175, 100)" opacity="0.802407112651" r="6.77010376848" stroke="rgb(222, 249, 31)" stroke-opacity="0.676145737462" stroke-width="6"/>""",
        """<circle cx="476.887589945" cy="958.154631439" fill="rgb(168, 175, 234)" opacity="0.617081202298" r="41.3475484169" stroke="rgb(240, 213, 24)" stroke-opacity="0.508964082229" stroke-width="8"/>""",
        """<circle cx="267.320825756" cy="911.073970872" fill="rgb(145, 96, 74)" opacity="0.639106755829" r="73.3702153277" stroke="rgb(59, 254, 191)" stroke-opacity="0.846518915291" stroke-width="10"/>""",
        """<circle cx="359.169865386" cy="604.707902314" fill="rgb(126, 116, 183)" opacity="0.679546650359" r="42.6684356157" stroke="rgb(219, 140, 102)" stroke-opacity="0.541884325778" stroke-width="5"/>""",
        """<circle cx="303.75177485" cy="831.386720096" fill="rgb(145, 240, 208)" opacity="0.644067979323" r="38.8957138119" stroke="rgb(244, 93, 133)" stroke-opacity="0.516713740668" stroke-width="2"/>""",
        """<circle cx="769.679684133" cy="265.351310683" fill="rgb(181, 60, 21)" opacity="0.765455989683" r="91.3814944447" stroke="rgb(104, 38, 50)" stroke-opacity="0.985558315863" stroke-width="6"/>""",
        """<circle cx="468.293308161" cy="633.560782517" fill="rgb(219, 54, 242)" opacity="0.914702512681" r="67.6539438556" stroke="rgb(70, 71, 13)" stroke-opacity="0.865073682369" stroke-width="7"/>""",
        """<circle cx="138.533715065" cy="792.5078207" fill="rgb(92, 247, 185)" opacity="0.882279428282" r="64.1027875048" stroke="rgb(35, 36, 69)" stroke-opacity="0.741748817094" stroke-width="1"/>""",
        """<circle cx="872.480825566" cy="119.160840016" fill="rgb(94, 172, 106)" opacity="0.516813767254" r="13.8676176512" stroke="rgb(55, 17, 37)" stroke-opacity="0.603320584586" stroke-width="6"/>""",
        """<circle cx="660.121966533" cy="909.068757906" fill="rgb(124, 214, 134)" opacity="0.703716947763" r="41.7391957335" stroke="rgb(205, 210, 197)" stroke-opacity="0.75128592329" stroke-width="10"/>""",
        """<circle cx="118.310552033" cy="537.963061377" fill="rgb(103, 217, 203)" opacity="0.755002045433" r="90.3146343686" stroke="rgb(166, 43, 93)" stroke-opacity="0.820245891985" stroke-width="3"/>""",
        """<circle cx="594.049081398" cy="593.479967913" fill="rgb(21, 172, 102)" opacity="0.960927684937" r="16.6787239733" stroke="rgb(226, 75, 7)" stroke-opacity="0.658945536142" stroke-width="4"/>""",
        """<circle cx="452.657298909" cy="248.344231666" fill="rgb(48, 42, 24)" opacity="0.993835667404" r="24.1533451378" stroke="rgb(232, 229, 121)" stroke-opacity="0.837961788955" stroke-width="2"/>""",
        """<circle cx="207.971457035" cy="541.577545753" fill="rgb(68, 150, 129)" opacity="0.892314842586" r="21.676585846" stroke="rgb(24, 175, 145)" stroke-opacity="0.923384948058" stroke-width="5"/>""",
        """<circle cx="603.538831727" cy="879.7941829" fill="rgb(229, 86, 202)" opacity="0.826347491009" r="79.4539418966" stroke="rgb(49, 131, 94)" stroke-opacity="0.725240446615" stroke-width="2"/>""",
        """<circle cx="871.448185548" cy="441.644508363" fill="rgb(207, 58, 98)" opacity="0.585920391357" r="52.6463460527" stroke="rgb(197, 22, 203)" stroke-opacity="0.930214151718" stroke-width="4"/>""",
        """<circle cx="108.346718321" cy="584.487780661" fill="rgb(245, 199, 174)" opacity="0.713897143229" r="6.17447817943" stroke="rgb(30, 214, 119)" stroke-opacity="0.891150805968" stroke-width="5"/>""",
        """<circle cx="437.239746766" cy="961.137635329" fill="rgb(169, 179, 45)" opacity="0.909544904176" r="18.3934997121" stroke="rgb(214, 66, 184)" stroke-opacity="0.876260038152" stroke-width="3"/>""",
        """<circle cx="344.192791738" cy="697.416270748" fill="rgb(105, 166, 151)" opacity="0.845753439732" r="77.8840400366" stroke="rgb(106, 61, 177)" stroke-opacity="0.913739245527" stroke-width="1"/>""",
        """<circle cx="208.196164241" cy="964.474347623" fill="rgb(140, 7, 124)" opacity="0.616448403974" r="79.0263486014" stroke="rgb(0, 97, 65)" stroke-opacity="0.589961935696" stroke-width="7"/>""",
        """<circle cx="472.809085368" cy="313.029347355" fill="rgb(48, 67, 164)" opacity="0.878857178886" r="53.5851594587" stroke="rgb(42, 89, 83)" stroke-opacity="0.714117455413" stroke-width="1"/>""",
        """<circle cx="944.576978919" cy="390.234828057" fill="rgb(254, 105, 176)" opacity="0.776355406515" r="98.0172328945" stroke="rgb(237, 131, 232)" stroke-opacity="0.74306476976" stroke-width="10"/>"""
)

    def test_circle_to_xml(self):
        """Circle: Object ---> XML"""
        for circle, xml in zip(self.circle_objects, self.circle_xml_strings): 
            self.assertEqual(circle.to_xml(), xml)

 
    def test_circle_from_xml(self):
        """Circle: XML ---> Object"""
        assert len(self.circle_objects) == len(self.circle_xml_strings)
        for circle, xml in zip(self.circle_objects, self.circle_xml_strings): 
            self.assertEqual(circle, object_from_xml(xml))



class EllipseTest(unittest.TestCase):
    """Test For svgenesis.primitives.Ellipse"""
    ################################################
    # Ellipse Objects and XML Strings
    ################################################
    ellipse_objects = (
        Ellipse(opacity=0.705410661248, stroke_width=1, stroke_opacity=0.574398190769, rx=44.2857200543, cy=461.291327367, ry=18.1144013153, stroke=rgb(62, 17, 126), cx=589.764423367, fill=rgb(214, 252, 39)),
        Ellipse(opacity=0.612981448044, stroke_width=8, stroke_opacity=0.656249444639, rx=86.4880226858, cy=563.072366282, ry=78.9542838715, stroke=rgb(212, 197, 224), cx=460.959062566, fill=rgb(38, 105, 246)),
        Ellipse(opacity=0.542044730928, stroke_width=2, stroke_opacity=0.779612024267, rx=79.962135886, cy=444.851462344, ry=63.7660193567, stroke=rgb(117, 60, 133), cx=574.508717289, fill=rgb(83, 22, 132)),
        Ellipse(opacity=0.759006724582, stroke_width=10, stroke_opacity=0.571039033432, rx=20.7641447232, cy=570.49086008, ry=43.439248516, stroke=rgb(109, 156, 247), cx=722.039972243, fill=rgb(62, 194, 112)),
        Ellipse(opacity=0.684702057487, stroke_width=2, stroke_opacity=0.506387014083, rx=59.5211324358, cy=416.86328286, ry=40.4619359501, stroke=rgb(134, 161, 206), cx=509.90997924, fill=rgb(24, 168, 28)),
        Ellipse(opacity=0.698970572107, stroke_width=5, stroke_opacity=0.894447649921, rx=19.1723189175, cy=447.2099594, ry=17.5684599822, stroke=rgb(158, 74, 30), cx=235.170905307, fill=rgb(160, 166, 182)),
        Ellipse(opacity=0.555318095181, stroke_width=8, stroke_opacity=0.652792016068, rx=25.0276791297, cy=301.914372523, ry=57.1420252906, stroke=rgb(42, 225, 70), cx=748.306781258, fill=rgb(167, 103, 130)),
        Ellipse(opacity=0.566617850453, stroke_width=4, stroke_opacity=0.712262258254, rx=87.2793242333, cy=347.274417138, ry=10.1466553362, stroke=rgb(11, 89, 92), cx=338.078020073, fill=rgb(53, 49, 79)),
        Ellipse(opacity=0.565303925413, stroke_width=2, stroke_opacity=0.501880091657, rx=25.2199014261, cy=353.544639982, ry=41.8670869491, stroke=rgb(174, 254, 172), cx=217.366195605, fill=rgb(216, 108, 232)),
        Ellipse(opacity=0.790478157466, stroke_width=6, stroke_opacity=0.694103232746, rx=52.151099155, cy=315.976249366, ry=45.112771824, stroke=rgb(207, 25, 151), cx=204.769255332, fill=rgb(194, 202, 21)),
        Ellipse(opacity=0.699716908817, stroke_width=9, stroke_opacity=0.699652296151, rx=51.7216472728, cy=728.128436157, ry=25.4228199498, stroke=rgb(222, 235, 162), cx=464.469131409, fill=rgb(136, 148, 35)),
        Ellipse(opacity=0.964190565668, stroke_width=4, stroke_opacity=0.632383771268, rx=87.0569878973, cy=526.414208213, ry=92.3551444831, stroke=rgb(21, 135, 136), cx=745.404361941, fill=rgb(9, 134, 168)),
        Ellipse(opacity=0.969421995533, stroke_width=2, stroke_opacity=0.512652537442, rx=61.2413239068, cy=781.21469566, ry=88.7042239226, stroke=rgb(132, 251, 109), cx=275.623230093, fill=rgb(173, 233, 9)),
        Ellipse(opacity=0.902215467711, stroke_width=4, stroke_opacity=0.508398364807, rx=80.2095482954, cy=129.678278189, ry=12.2767838324, stroke=rgb(102, 104, 35), cx=633.99026056, fill=rgb(203, 186, 231)),
        Ellipse(opacity=0.851624337003, stroke_width=6, stroke_opacity=0.927054092135, rx=28.5302214555, cy=286.51382756, ry=61.952634316, stroke=rgb(88, 6, 52), cx=710.013917839, fill=rgb(46, 249, 124)),
        Ellipse(opacity=0.844247521055, stroke_width=5, stroke_opacity=0.751614029813, rx=55.5869204356, cy=139.844342923, ry=53.7438923046, stroke=rgb(178, 183, 48), cx=429.170368157, fill=rgb(183, 207, 90)),
        Ellipse(opacity=0.781494300849, stroke_width=2, stroke_opacity=0.93146533339, rx=30.9445519788, cy=454.792827947, ry=96.0864944793, stroke=rgb(144, 153, 60), cx=640.443570369, fill=rgb(242, 54, 151)),
        Ellipse(opacity=0.756847297513, stroke_width=4, stroke_opacity=0.877316256465, rx=83.8267339209, cy=546.458353582, ry=71.5333302936, stroke=rgb(94, 24, 67), cx=363.665793467, fill=rgb(221, 73, 45)),
        Ellipse(opacity=0.893252226431, stroke_width=3, stroke_opacity=0.996546986144, rx=77.4957393381, cy=241.484238677, ry=45.6682473743, stroke=rgb(48, 172, 207), cx=553.698580077, fill=rgb(230, 252, 155)),
        Ellipse(opacity=0.51276647726, stroke_width=3, stroke_opacity=0.797186730371, rx=34.2259314298, cy=744.201336359, ry=39.5404065106, stroke=rgb(40, 118, 199), cx=585.266453748, fill=rgb(20, 147, 198)),
        Ellipse(opacity=0.663900543262, stroke_width=8, stroke_opacity=0.505585794237, rx=71.2194269539, cy=349.169225269, ry=15.7955787305, stroke=rgb(122, 40, 79), cx=329.061459696, fill=rgb(115, 103, 194)),
        Ellipse(opacity=0.666221624642, stroke_width=9, stroke_opacity=0.84161761319, rx=8.23257401369, cy=400.231702653, ry=34.264233941, stroke=rgb(246, 193, 229), cx=256.112008812, fill=rgb(211, 79, 184)),
        Ellipse(opacity=0.771981139908, stroke_width=5, stroke_opacity=0.561295776342, rx=19.7955192155, cy=726.998076764, ry=14.9137147852, stroke=rgb(157, 178, 224), cx=841.816145766, fill=rgb(249, 8, 154)),
        Ellipse(opacity=0.964581437507, stroke_width=4, stroke_opacity=0.71291700827, rx=42.158104454, cy=536.279200413, ry=41.7995009364, stroke=rgb(169, 10, 246), cx=712.547977025, fill=rgb(34, 154, 145)),
        Ellipse(opacity=0.774741868989, stroke_width=3, stroke_opacity=0.86653478965, rx=86.7080696302, cy=657.258858229, ry=13.6657493152, stroke=rgb(156, 92, 77), cx=104.058262428, fill=rgb(148, 188, 235)),
        Ellipse(opacity=0.765224834667, stroke_width=7, stroke_opacity=0.894710989709, rx=62.7807537833, cy=857.949637498, ry=96.9829306382, stroke=rgb(19, 224, 9), cx=400.389223152, fill=rgb(85, 81, 174)),
        Ellipse(opacity=0.751771845979, stroke_width=6, stroke_opacity=0.982638158116, rx=84.0238869217, cy=176.276311735, ry=23.0743921413, stroke=rgb(176, 175, 8), cx=210.702906212, fill=rgb(14, 2, 210)),
        Ellipse(opacity=0.583698312149, stroke_width=8, stroke_opacity=0.508491851993, rx=40.7726450544, cy=165.510336564, ry=28.4551116765, stroke=rgb(153, 215, 149), cx=552.329951062, fill=rgb(60, 30, 159)),
        Ellipse(opacity=0.503855097238, stroke_width=5, stroke_opacity=0.518587016039, rx=34.3212309808, cy=330.064951329, ry=0.289832413703, stroke=rgb(90, 40, 100), cx=844.065924636, fill=rgb(181, 51, 157)),
        Ellipse(opacity=0.776013729997, stroke_width=1, stroke_opacity=0.671739210697, rx=58.2591251694, cy=587.082966003, ry=19.7803684385, stroke=rgb(135, 235, 166), cx=828.740646797, fill=rgb(19, 136, 126)),
        Ellipse(opacity=0.778187160205, stroke_width=6, stroke_opacity=0.764096508469, rx=46.304604524, cy=358.089565346, ry=74.8379925199, stroke=rgb(251, 98, 50), cx=696.287303479, fill=rgb(222, 148, 107)),
        Ellipse(opacity=0.503199711918, stroke_width=6, stroke_opacity=0.950620528461, rx=37.1015886205, cy=497.792769285, ry=74.3489799967, stroke=rgb(72, 141, 31), cx=958.142624447, fill=rgb(109, 47, 1)),
        Ellipse(opacity=0.873054297898, stroke_width=9, stroke_opacity=0.663150760991, rx=2.15342749092, cy=281.64708306, ry=4.32414122356, stroke=rgb(74, 179, 91), cx=914.453165148, fill=rgb(18, 177, 78)),
        Ellipse(opacity=0.683837624315, stroke_width=8, stroke_opacity=0.900056161927, rx=7.2165502063, cy=334.293710129, ry=45.5389426071, stroke=rgb(74, 235, 148), cx=960.134329467, fill=rgb(125, 64, 240)),
        Ellipse(opacity=0.525024206228, stroke_width=6, stroke_opacity=0.677147934264, rx=79.4645613723, cy=731.797592759, ry=93.0791967546, stroke=rgb(165, 84, 110), cx=244.707002669, fill=rgb(79, 49, 214)),
        Ellipse(opacity=0.667954820337, stroke_width=10, stroke_opacity=0.585993562782, rx=10.1423833821, cy=146.112560245, ry=26.5206413995, stroke=rgb(111, 27, 126), cx=883.869073927, fill=rgb(2, 192, 227)),
        Ellipse(opacity=0.92041429092, stroke_width=4, stroke_opacity=0.762614411056, rx=45.2183596137, cy=872.097571952, ry=69.7793821748, stroke=rgb(124, 218, 140), cx=872.126551978, fill=rgb(229, 3, 136)),
        Ellipse(opacity=0.929755472227, stroke_width=3, stroke_opacity=0.587474801074, rx=61.5562661749, cy=564.447970088, ry=14.5122060711, stroke=rgb(143, 8, 161), cx=817.564063826, fill=rgb(142, 136, 35)),
        Ellipse(opacity=0.567809446299, stroke_width=10, stroke_opacity=0.882506237784, rx=79.5109095388, cy=268.454782735, ry=71.5691444482, stroke=rgb(205, 252, 244), cx=345.892774289, fill=rgb(113, 36, 96)),
        Ellipse(opacity=0.516060323384, stroke_width=3, stroke_opacity=0.533404360551, rx=6.88313391822, cy=106.383185166, ry=52.0893558944, stroke=rgb(203, 219, 241), cx=253.571677428, fill=rgb(39, 245, 218)),
        Ellipse(opacity=0.534819827401, stroke_width=10, stroke_opacity=0.614366564332, rx=36.8478242846, cy=225.517695261, ry=32.5659724245, stroke=rgb(202, 91, 121), cx=785.150731637, fill=rgb(25, 1, 236)),
        Ellipse(opacity=0.60846640124, stroke_width=6, stroke_opacity=0.966900982604, rx=63.2500104969, cy=776.159038274, ry=79.9271802443, stroke=rgb(96, 33, 159), cx=347.292715373, fill=rgb(190, 235, 213)),
        Ellipse(opacity=0.697450350097, stroke_width=8, stroke_opacity=0.992146516077, rx=71.3982806361, cy=894.05761192, ry=56.2752336968, stroke=rgb(143, 175, 151), cx=790.058089041, fill=rgb(75, 145, 26)),
        Ellipse(opacity=0.580345569229, stroke_width=1, stroke_opacity=0.814639895544, rx=4.64583882993, cy=746.102639668, ry=56.0272288687, stroke=rgb(136, 205, 14), cx=172.767355798, fill=rgb(245, 232, 165)),
        Ellipse(opacity=0.561633716104, stroke_width=1, stroke_opacity=0.889009384923, rx=18.0032865972, cy=882.294140738, ry=45.4012847928, stroke=rgb(159, 50, 76), cx=159.772307245, fill=rgb(205, 178, 218)),
        Ellipse(opacity=0.656780548745, stroke_width=5, stroke_opacity=0.821620446631, rx=73.0762945979, cy=833.956411908, ry=34.5600839131, stroke=rgb(134, 217, 229), cx=678.938318123, fill=rgb(248, 178, 192)),
        Ellipse(opacity=0.547981846347, stroke_width=3, stroke_opacity=0.757875611002, rx=64.1848950883, cy=623.845857289, ry=75.7748937396, stroke=rgb(210, 179, 131), cx=651.235332704, fill=rgb(186, 45, 228)),
        Ellipse(opacity=0.889730038816, stroke_width=7, stroke_opacity=0.952760619275, rx=52.1262311081, cy=757.611807699, ry=5.44597798868, stroke=rgb(127, 239, 181), cx=477.070116231, fill=rgb(224, 142, 196)),
        Ellipse(opacity=0.739241565208, stroke_width=8, stroke_opacity=0.558222476278, rx=55.5894021644, cy=899.426297796, ry=23.8500014036, stroke=rgb(207, 185, 118), cx=462.949444698, fill=rgb(221, 32, 122)),
        Ellipse(opacity=0.575776767249, stroke_width=6, stroke_opacity=0.975486410925, rx=55.5103862515, cy=920.689773921, ry=18.9090215629, stroke=rgb(74, 4, 31), cx=495.65781271, fill=rgb(168, 241, 166)),
        Ellipse(opacity=0.767387123854, stroke_width=10, stroke_opacity=0.925101008763, rx=0.548882029964, cy=502.646941349, ry=43.1489366519, stroke=rgb(112, 217, 131), cx=726.230050501, fill=rgb(223, 139, 221)),
        Ellipse(opacity=0.967077821084, stroke_width=1, stroke_opacity=0.938784848086, rx=77.3906333049, cy=129.941544141, ry=10.3752688828, stroke=rgb(244, 109, 231), cx=499.334886425, fill=rgb(160, 114, 231)),
        Ellipse(opacity=0.681323280749, stroke_width=2, stroke_opacity=0.899196923278, rx=11.0486796255, cy=119.730112223, ry=6.80081879911, stroke=rgb(154, 29, 43), cx=338.468287287, fill=rgb(79, 252, 145)),
        Ellipse(opacity=0.886159445596, stroke_width=10, stroke_opacity=0.57037662039, rx=93.4384354161, cy=941.08124894, ry=52.4123077119, stroke=rgb(67, 63, 151), cx=825.087419801, fill=rgb(121, 232, 222)),
        Ellipse(opacity=0.885943279526, stroke_width=6, stroke_opacity=0.859002971112, rx=84.1492832122, cy=263.726638276, ry=86.3604309594, stroke=rgb(226, 137, 118), cx=426.672233977, fill=rgb(82, 104, 247)),
        Ellipse(opacity=0.934002934166, stroke_width=4, stroke_opacity=0.820128569403, rx=59.0360176931, cy=654.252459119, ry=75.9946399339, stroke=rgb(77, 158, 229), cx=741.03680314, fill=rgb(255, 161, 57)),
        Ellipse(opacity=0.695128203271, stroke_width=1, stroke_opacity=0.920810597184, rx=77.1288622877, cy=509.183858647, ry=13.7006329875, stroke=rgb(17, 222, 21), cx=678.987931308, fill=rgb(41, 128, 216)),
        Ellipse(opacity=0.991610221976, stroke_width=4, stroke_opacity=0.523818994172, rx=26.9544760667, cy=538.050326674, ry=38.5064167839, stroke=rgb(10, 124, 8), cx=127.39682239, fill=rgb(183, 38, 205)),
        Ellipse(opacity=0.820165794592, stroke_width=6, stroke_opacity=0.515128285509, rx=61.8030031348, cy=572.514044575, ry=91.4762284458, stroke=rgb(133, 166, 107), cx=751.805639286, fill=rgb(65, 60, 0)),
        Ellipse(opacity=0.623841459092, stroke_width=6, stroke_opacity=0.986951205921, rx=44.6995445375, cy=953.821429731, ry=28.8166869372, stroke=rgb(151, 91, 91), cx=365.706575898, fill=rgb(169, 121, 203)),
        Ellipse(opacity=0.658553632659, stroke_width=4, stroke_opacity=0.637149585809, rx=96.0251585237, cy=262.859883488, ry=0.327153447398, stroke=rgb(119, 226, 234), cx=692.910597675, fill=rgb(216, 5, 2)),
        Ellipse(opacity=0.990810478834, stroke_width=10, stroke_opacity=0.585919149867, rx=50.5631397452, cy=379.899771718, ry=93.7164914463, stroke=rgb(8, 171, 35), cx=620.77944186, fill=rgb(92, 161, 135)),
        Ellipse(opacity=0.647544351117, stroke_width=8, stroke_opacity=0.831151401975, rx=55.5804262276, cy=977.851089516, ry=60.6559179191, stroke=rgb(70, 55, 200), cx=250.197776422, fill=rgb(87, 156, 15)),
        Ellipse(opacity=0.802960055724, stroke_width=6, stroke_opacity=0.886026374044, rx=34.3087865573, cy=480.295406239, ry=30.3895820539, stroke=rgb(11, 214, 44), cx=226.112076749, fill=rgb(146, 141, 164)),
        Ellipse(opacity=0.726522742673, stroke_width=2, stroke_opacity=0.652771421829, rx=49.2061024174, cy=945.546674653, ry=70.7306506997, stroke=rgb(158, 96, 172), cx=871.551286598, fill=rgb(206, 2, 117)),
        Ellipse(opacity=0.738607759877, stroke_width=1, stroke_opacity=0.729082576218, rx=31.0648110571, cy=644.100449415, ry=98.118022117, stroke=rgb(42, 165, 16), cx=401.334736865, fill=rgb(57, 39, 2)),
        Ellipse(opacity=0.961471391372, stroke_width=1, stroke_opacity=0.565891728306, rx=8.3146827223, cy=814.19985736, ry=68.245549568, stroke=rgb(12, 158, 113), cx=895.281901198, fill=rgb(36, 187, 252)),
        Ellipse(opacity=0.87826944565, stroke_width=6, stroke_opacity=0.976732680846, rx=75.5233882006, cy=680.510673405, ry=40.8840740261, stroke=rgb(55, 44, 33), cx=142.204625277, fill=rgb(20, 118, 86)),
        Ellipse(opacity=0.575845845953, stroke_width=4, stroke_opacity=0.901502494921, rx=6.23439575374, cy=170.039565984, ry=12.046124548, stroke=rgb(35, 93, 136), cx=634.815411395, fill=rgb(64, 32, 226)),
        Ellipse(opacity=0.933888402896, stroke_width=4, stroke_opacity=0.857279936763, rx=31.902764982, cy=954.328162014, ry=91.3944917811, stroke=rgb(107, 188, 125), cx=269.996716312, fill=rgb(0, 133, 25)),
        Ellipse(opacity=0.959587581876, stroke_width=5, stroke_opacity=0.831196826906, rx=93.5726556265, cy=225.495927643, ry=9.90198958916, stroke=rgb(10, 12, 70), cx=928.639075078, fill=rgb(96, 114, 214)),
        Ellipse(opacity=0.819454653817, stroke_width=10, stroke_opacity=0.913634266863, rx=74.1290801281, cy=567.408780347, ry=84.9689756662, stroke=rgb(204, 11, 92), cx=352.606903722, fill=rgb(75, 123, 6)),
        Ellipse(opacity=0.768844913645, stroke_width=6, stroke_opacity=0.612060323395, rx=46.9954214682, cy=509.725274612, ry=94.3516435731, stroke=rgb(103, 235, 35), cx=706.442006462, fill=rgb(214, 215, 201)),
        Ellipse(opacity=0.716603769355, stroke_width=10, stroke_opacity=0.72053104948, rx=24.4348634875, cy=766.906281539, ry=39.9125353828, stroke=rgb(178, 213, 27), cx=334.036687363, fill=rgb(43, 207, 183)),
        Ellipse(opacity=0.758027672166, stroke_width=8, stroke_opacity=0.573087423402, rx=36.6626706768, cy=732.925756702, ry=53.8310819351, stroke=rgb(62, 116, 107), cx=602.637702359, fill=rgb(92, 9, 113)),
        Ellipse(opacity=0.973811924432, stroke_width=7, stroke_opacity=0.568229163388, rx=13.6924390157, cy=582.682632238, ry=77.6767997977, stroke=rgb(22, 4, 122), cx=634.976053293, fill=rgb(51, 49, 158)),
        Ellipse(opacity=0.620738129576, stroke_width=5, stroke_opacity=0.855015083623, rx=32.9864111884, cy=589.744418261, ry=60.1455997348, stroke=rgb(140, 195, 23), cx=593.781052698, fill=rgb(127, 99, 28)),
        Ellipse(opacity=0.628081219546, stroke_width=9, stroke_opacity=0.848694907986, rx=14.2295891327, cy=475.275573284, ry=70.1242878016, stroke=rgb(111, 125, 204), cx=777.1426386, fill=rgb(220, 140, 98)),
        Ellipse(opacity=0.968577230207, stroke_width=1, stroke_opacity=0.68500876803, rx=89.8936432853, cy=833.847359637, ry=39.3360320104, stroke=rgb(158, 18, 186), cx=203.888189178, fill=rgb(138, 168, 248)),
        Ellipse(opacity=0.617018701176, stroke_width=5, stroke_opacity=0.655494096126, rx=96.343883946, cy=578.656606461, ry=41.0847304317, stroke=rgb(46, 207, 193), cx=896.095422259, fill=rgb(34, 130, 50)),
        Ellipse(opacity=0.761241262164, stroke_width=2, stroke_opacity=0.761671921784, rx=76.4228355088, cy=991.234630639, ry=39.8685922573, stroke=rgb(166, 216, 142), cx=222.901040371, fill=rgb(151, 182, 82)),
        Ellipse(opacity=0.752742318504, stroke_width=10, stroke_opacity=0.692542833206, rx=14.3249554395, cy=737.359165647, ry=89.0524187604, stroke=rgb(21, 142, 29), cx=109.514372908, fill=rgb(194, 110, 223)),
        Ellipse(opacity=0.752231087803, stroke_width=9, stroke_opacity=0.795512432697, rx=22.8745641138, cy=144.786946993, ry=19.9949159442, stroke=rgb(20, 133, 151), cx=791.7163574, fill=rgb(240, 50, 101)),
        Ellipse(opacity=0.593155040622, stroke_width=6, stroke_opacity=0.794339558874, rx=3.9136848464, cy=713.503188526, ry=53.1681458434, stroke=rgb(239, 32, 254), cx=703.767057478, fill=rgb(122, 224, 101)),
        Ellipse(opacity=0.768824289793, stroke_width=1, stroke_opacity=0.769438212448, rx=32.5878288329, cy=386.913447808, ry=68.5402379212, stroke=rgb(167, 238, 149), cx=913.694374093, fill=rgb(49, 31, 231)),
        Ellipse(opacity=0.69602385221, stroke_width=4, stroke_opacity=0.699043596898, rx=96.2160881874, cy=887.523887824, ry=22.3753097026, stroke=rgb(21, 209, 232), cx=297.92004961, fill=rgb(41, 157, 164)),
        Ellipse(opacity=0.719792699297, stroke_width=6, stroke_opacity=0.588991732603, rx=30.1218557982, cy=672.928219556, ry=92.0518620853, stroke=rgb(198, 28, 185), cx=964.701805059, fill=rgb(78, 252, 203)),
        Ellipse(opacity=0.570031680129, stroke_width=7, stroke_opacity=0.71606220854, rx=76.6032767253, cy=793.917603198, ry=24.7217315936, stroke=rgb(152, 247, 27), cx=700.413605819, fill=rgb(70, 248, 174)),
        Ellipse(opacity=0.839200310957, stroke_width=2, stroke_opacity=0.805281952545, rx=96.7811563649, cy=259.559125426, ry=35.0544123722, stroke=rgb(181, 24, 250), cx=237.625238838, fill=rgb(150, 162, 190)),
        Ellipse(opacity=0.798484867916, stroke_width=10, stroke_opacity=0.673206011585, rx=78.9763950585, cy=336.134725216, ry=66.2122995096, stroke=rgb(82, 109, 247), cx=257.98666024, fill=rgb(15, 42, 70)),
        Ellipse(opacity=0.848336044408, stroke_width=6, stroke_opacity=0.509423779673, rx=46.8086892652, cy=816.85779554, ry=59.3497596094, stroke=rgb(159, 230, 214), cx=749.497959843, fill=rgb(118, 130, 214)),
        Ellipse(opacity=0.7253983869, stroke_width=4, stroke_opacity=0.721908558111, rx=23.8391551623, cy=245.030539874, ry=33.19507124, stroke=rgb(214, 227, 116), cx=285.907506423, fill=rgb(131, 64, 199)),
        Ellipse(opacity=0.651827505577, stroke_width=10, stroke_opacity=0.617911919123, rx=90.1202971069, cy=396.110803512, ry=95.8625036834, stroke=rgb(212, 190, 29), cx=132.662768235, fill=rgb(228, 217, 165)),
        Ellipse(opacity=0.760974426339, stroke_width=1, stroke_opacity=0.524233619994, rx=74.967672134, cy=865.241580083, ry=71.2827563406, stroke=rgb(130, 131, 58), cx=830.596608346, fill=rgb(136, 196, 145)),
        Ellipse(opacity=0.92143850995, stroke_width=8, stroke_opacity=0.590642283223, rx=16.4618338354, cy=599.541776089, ry=37.0128201785, stroke=rgb(118, 89, 164), cx=266.401965907, fill=rgb(114, 33, 127)),
        Ellipse(opacity=0.813954772525, stroke_width=9, stroke_opacity=0.513774789239, rx=56.8131259794, cy=571.270090801, ry=52.283297456, stroke=rgb(86, 125, 176), cx=398.975768139, fill=rgb(77, 183, 141)),
        Ellipse(opacity=0.600023678864, stroke_width=6, stroke_opacity=0.630048035228, rx=87.6631872008, cy=545.082805865, ry=27.3650906618, stroke=rgb(194, 96, 252), cx=874.698392264, fill=rgb(193, 195, 141)),
        Ellipse(opacity=0.764919430248, stroke_width=5, stroke_opacity=0.695779417396, rx=45.699143065, cy=671.720385176, ry=15.6797472398, stroke=rgb(165, 77, 205), cx=247.68242258, fill=rgb(132, 223, 190)),
        Ellipse(opacity=0.658333027855, stroke_width=7, stroke_opacity=0.799955933097, rx=22.1635410619, cy=360.25218695, ry=45.4887495572, stroke=rgb(66, 100, 28), cx=189.726918153, fill=rgb(212, 184, 110)),
        Ellipse(opacity=0.919258523279, stroke_width=9, stroke_opacity=0.603507479032, rx=36.527652285, cy=809.552326575, ry=24.0064725755, stroke=rgb(160, 235, 219), cx=360.189758933, fill=rgb(188, 13, 116)),
        )

    ellipse_xml_strings = (
        """<ellipse cx="589.764423367" cy="461.291327367" fill="rgb(214, 252, 39)" opacity="0.705410661248" rx="44.2857200543" ry="18.1144013153" stroke="rgb(62, 17, 126)" stroke-opacity="0.574398190769" stroke-width="1"/>""",
        """<ellipse cx="460.959062566" cy="563.072366282" fill="rgb(38, 105, 246)" opacity="0.612981448044" rx="86.4880226858" ry="78.9542838715" stroke="rgb(212, 197, 224)" stroke-opacity="0.656249444639" stroke-width="8"/>""",
        """<ellipse cx="574.508717289" cy="444.851462344" fill="rgb(83, 22, 132)" opacity="0.542044730928" rx="79.962135886" ry="63.7660193567" stroke="rgb(117, 60, 133)" stroke-opacity="0.779612024267" stroke-width="2"/>""",
        """<ellipse cx="722.039972243" cy="570.49086008" fill="rgb(62, 194, 112)" opacity="0.759006724582" rx="20.7641447232" ry="43.439248516" stroke="rgb(109, 156, 247)" stroke-opacity="0.571039033432" stroke-width="10"/>""",
        """<ellipse cx="509.90997924" cy="416.86328286" fill="rgb(24, 168, 28)" opacity="0.684702057487" rx="59.5211324358" ry="40.4619359501" stroke="rgb(134, 161, 206)" stroke-opacity="0.506387014083" stroke-width="2"/>""",
        """<ellipse cx="235.170905307" cy="447.2099594" fill="rgb(160, 166, 182)" opacity="0.698970572107" rx="19.1723189175" ry="17.5684599822" stroke="rgb(158, 74, 30)" stroke-opacity="0.894447649921" stroke-width="5"/>""",
        """<ellipse cx="748.306781258" cy="301.914372523" fill="rgb(167, 103, 130)" opacity="0.555318095181" rx="25.0276791297" ry="57.1420252906" stroke="rgb(42, 225, 70)" stroke-opacity="0.652792016068" stroke-width="8"/>""",
        """<ellipse cx="338.078020073" cy="347.274417138" fill="rgb(53, 49, 79)" opacity="0.566617850453" rx="87.2793242333" ry="10.1466553362" stroke="rgb(11, 89, 92)" stroke-opacity="0.712262258254" stroke-width="4"/>""",
        """<ellipse cx="217.366195605" cy="353.544639982" fill="rgb(216, 108, 232)" opacity="0.565303925413" rx="25.2199014261" ry="41.8670869491" stroke="rgb(174, 254, 172)" stroke-opacity="0.501880091657" stroke-width="2"/>""",
        """<ellipse cx="204.769255332" cy="315.976249366" fill="rgb(194, 202, 21)" opacity="0.790478157466" rx="52.151099155" ry="45.112771824" stroke="rgb(207, 25, 151)" stroke-opacity="0.694103232746" stroke-width="6"/>""",
        """<ellipse cx="464.469131409" cy="728.128436157" fill="rgb(136, 148, 35)" opacity="0.699716908817" rx="51.7216472728" ry="25.4228199498" stroke="rgb(222, 235, 162)" stroke-opacity="0.699652296151" stroke-width="9"/>""",
        """<ellipse cx="745.404361941" cy="526.414208213" fill="rgb(9, 134, 168)" opacity="0.964190565668" rx="87.0569878973" ry="92.3551444831" stroke="rgb(21, 135, 136)" stroke-opacity="0.632383771268" stroke-width="4"/>""",
        """<ellipse cx="275.623230093" cy="781.21469566" fill="rgb(173, 233, 9)" opacity="0.969421995533" rx="61.2413239068" ry="88.7042239226" stroke="rgb(132, 251, 109)" stroke-opacity="0.512652537442" stroke-width="2"/>""",
        """<ellipse cx="633.99026056" cy="129.678278189" fill="rgb(203, 186, 231)" opacity="0.902215467711" rx="80.2095482954" ry="12.2767838324" stroke="rgb(102, 104, 35)" stroke-opacity="0.508398364807" stroke-width="4"/>""",
        """<ellipse cx="710.013917839" cy="286.51382756" fill="rgb(46, 249, 124)" opacity="0.851624337003" rx="28.5302214555" ry="61.952634316" stroke="rgb(88, 6, 52)" stroke-opacity="0.927054092135" stroke-width="6"/>""",
        """<ellipse cx="429.170368157" cy="139.844342923" fill="rgb(183, 207, 90)" opacity="0.844247521055" rx="55.5869204356" ry="53.7438923046" stroke="rgb(178, 183, 48)" stroke-opacity="0.751614029813" stroke-width="5"/>""",
        """<ellipse cx="640.443570369" cy="454.792827947" fill="rgb(242, 54, 151)" opacity="0.781494300849" rx="30.9445519788" ry="96.0864944793" stroke="rgb(144, 153, 60)" stroke-opacity="0.93146533339" stroke-width="2"/>""",
        """<ellipse cx="363.665793467" cy="546.458353582" fill="rgb(221, 73, 45)" opacity="0.756847297513" rx="83.8267339209" ry="71.5333302936" stroke="rgb(94, 24, 67)" stroke-opacity="0.877316256465" stroke-width="4"/>""",
        """<ellipse cx="553.698580077" cy="241.484238677" fill="rgb(230, 252, 155)" opacity="0.893252226431" rx="77.4957393381" ry="45.6682473743" stroke="rgb(48, 172, 207)" stroke-opacity="0.996546986144" stroke-width="3"/>""",
        """<ellipse cx="585.266453748" cy="744.201336359" fill="rgb(20, 147, 198)" opacity="0.51276647726" rx="34.2259314298" ry="39.5404065106" stroke="rgb(40, 118, 199)" stroke-opacity="0.797186730371" stroke-width="3"/>""",
        """<ellipse cx="329.061459696" cy="349.169225269" fill="rgb(115, 103, 194)" opacity="0.663900543262" rx="71.2194269539" ry="15.7955787305" stroke="rgb(122, 40, 79)" stroke-opacity="0.505585794237" stroke-width="8"/>""",
        """<ellipse cx="256.112008812" cy="400.231702653" fill="rgb(211, 79, 184)" opacity="0.666221624642" rx="8.23257401369" ry="34.264233941" stroke="rgb(246, 193, 229)" stroke-opacity="0.84161761319" stroke-width="9"/>""",
        """<ellipse cx="841.816145766" cy="726.998076764" fill="rgb(249, 8, 154)" opacity="0.771981139908" rx="19.7955192155" ry="14.9137147852" stroke="rgb(157, 178, 224)" stroke-opacity="0.561295776342" stroke-width="5"/>""",
        """<ellipse cx="712.547977025" cy="536.279200413" fill="rgb(34, 154, 145)" opacity="0.964581437507" rx="42.158104454" ry="41.7995009364" stroke="rgb(169, 10, 246)" stroke-opacity="0.71291700827" stroke-width="4"/>""",
        """<ellipse cx="104.058262428" cy="657.258858229" fill="rgb(148, 188, 235)" opacity="0.774741868989" rx="86.7080696302" ry="13.6657493152" stroke="rgb(156, 92, 77)" stroke-opacity="0.86653478965" stroke-width="3"/>""",
        """<ellipse cx="400.389223152" cy="857.949637498" fill="rgb(85, 81, 174)" opacity="0.765224834667" rx="62.7807537833" ry="96.9829306382" stroke="rgb(19, 224, 9)" stroke-opacity="0.894710989709" stroke-width="7"/>""",
        """<ellipse cx="210.702906212" cy="176.276311735" fill="rgb(14, 2, 210)" opacity="0.751771845979" rx="84.0238869217" ry="23.0743921413" stroke="rgb(176, 175, 8)" stroke-opacity="0.982638158116" stroke-width="6"/>""",
        """<ellipse cx="552.329951062" cy="165.510336564" fill="rgb(60, 30, 159)" opacity="0.583698312149" rx="40.7726450544" ry="28.4551116765" stroke="rgb(153, 215, 149)" stroke-opacity="0.508491851993" stroke-width="8"/>""",
        """<ellipse cx="844.065924636" cy="330.064951329" fill="rgb(181, 51, 157)" opacity="0.503855097238" rx="34.3212309808" ry="0.289832413703" stroke="rgb(90, 40, 100)" stroke-opacity="0.518587016039" stroke-width="5"/>""",
        """<ellipse cx="828.740646797" cy="587.082966003" fill="rgb(19, 136, 126)" opacity="0.776013729997" rx="58.2591251694" ry="19.7803684385" stroke="rgb(135, 235, 166)" stroke-opacity="0.671739210697" stroke-width="1"/>""",
        """<ellipse cx="696.287303479" cy="358.089565346" fill="rgb(222, 148, 107)" opacity="0.778187160205" rx="46.304604524" ry="74.8379925199" stroke="rgb(251, 98, 50)" stroke-opacity="0.764096508469" stroke-width="6"/>""",
        """<ellipse cx="958.142624447" cy="497.792769285" fill="rgb(109, 47, 1)" opacity="0.503199711918" rx="37.1015886205" ry="74.3489799967" stroke="rgb(72, 141, 31)" stroke-opacity="0.950620528461" stroke-width="6"/>""",
        """<ellipse cx="914.453165148" cy="281.64708306" fill="rgb(18, 177, 78)" opacity="0.873054297898" rx="2.15342749092" ry="4.32414122356" stroke="rgb(74, 179, 91)" stroke-opacity="0.663150760991" stroke-width="9"/>""",
        """<ellipse cx="960.134329467" cy="334.293710129" fill="rgb(125, 64, 240)" opacity="0.683837624315" rx="7.2165502063" ry="45.5389426071" stroke="rgb(74, 235, 148)" stroke-opacity="0.900056161927" stroke-width="8"/>""",
        """<ellipse cx="244.707002669" cy="731.797592759" fill="rgb(79, 49, 214)" opacity="0.525024206228" rx="79.4645613723" ry="93.0791967546" stroke="rgb(165, 84, 110)" stroke-opacity="0.677147934264" stroke-width="6"/>""",
        """<ellipse cx="883.869073927" cy="146.112560245" fill="rgb(2, 192, 227)" opacity="0.667954820337" rx="10.1423833821" ry="26.5206413995" stroke="rgb(111, 27, 126)" stroke-opacity="0.585993562782" stroke-width="10"/>""",
        """<ellipse cx="872.126551978" cy="872.097571952" fill="rgb(229, 3, 136)" opacity="0.92041429092" rx="45.2183596137" ry="69.7793821748" stroke="rgb(124, 218, 140)" stroke-opacity="0.762614411056" stroke-width="4"/>""",
        """<ellipse cx="817.564063826" cy="564.447970088" fill="rgb(142, 136, 35)" opacity="0.929755472227" rx="61.5562661749" ry="14.5122060711" stroke="rgb(143, 8, 161)" stroke-opacity="0.587474801074" stroke-width="3"/>""",
        """<ellipse cx="345.892774289" cy="268.454782735" fill="rgb(113, 36, 96)" opacity="0.567809446299" rx="79.5109095388" ry="71.5691444482" stroke="rgb(205, 252, 244)" stroke-opacity="0.882506237784" stroke-width="10"/>""",
        """<ellipse cx="253.571677428" cy="106.383185166" fill="rgb(39, 245, 218)" opacity="0.516060323384" rx="6.88313391822" ry="52.0893558944" stroke="rgb(203, 219, 241)" stroke-opacity="0.533404360551" stroke-width="3"/>""",
        """<ellipse cx="785.150731637" cy="225.517695261" fill="rgb(25, 1, 236)" opacity="0.534819827401" rx="36.8478242846" ry="32.5659724245" stroke="rgb(202, 91, 121)" stroke-opacity="0.614366564332" stroke-width="10"/>""",
        """<ellipse cx="347.292715373" cy="776.159038274" fill="rgb(190, 235, 213)" opacity="0.60846640124" rx="63.2500104969" ry="79.9271802443" stroke="rgb(96, 33, 159)" stroke-opacity="0.966900982604" stroke-width="6"/>""",
        """<ellipse cx="790.058089041" cy="894.05761192" fill="rgb(75, 145, 26)" opacity="0.697450350097" rx="71.3982806361" ry="56.2752336968" stroke="rgb(143, 175, 151)" stroke-opacity="0.992146516077" stroke-width="8"/>""",
        """<ellipse cx="172.767355798" cy="746.102639668" fill="rgb(245, 232, 165)" opacity="0.580345569229" rx="4.64583882993" ry="56.0272288687" stroke="rgb(136, 205, 14)" stroke-opacity="0.814639895544" stroke-width="1"/>""",
        """<ellipse cx="159.772307245" cy="882.294140738" fill="rgb(205, 178, 218)" opacity="0.561633716104" rx="18.0032865972" ry="45.4012847928" stroke="rgb(159, 50, 76)" stroke-opacity="0.889009384923" stroke-width="1"/>""",
        """<ellipse cx="678.938318123" cy="833.956411908" fill="rgb(248, 178, 192)" opacity="0.656780548745" rx="73.0762945979" ry="34.5600839131" stroke="rgb(134, 217, 229)" stroke-opacity="0.821620446631" stroke-width="5"/>""",
        """<ellipse cx="651.235332704" cy="623.845857289" fill="rgb(186, 45, 228)" opacity="0.547981846347" rx="64.1848950883" ry="75.7748937396" stroke="rgb(210, 179, 131)" stroke-opacity="0.757875611002" stroke-width="3"/>""",
        """<ellipse cx="477.070116231" cy="757.611807699" fill="rgb(224, 142, 196)" opacity="0.889730038816" rx="52.1262311081" ry="5.44597798868" stroke="rgb(127, 239, 181)" stroke-opacity="0.952760619275" stroke-width="7"/>""",
        """<ellipse cx="462.949444698" cy="899.426297796" fill="rgb(221, 32, 122)" opacity="0.739241565208" rx="55.5894021644" ry="23.8500014036" stroke="rgb(207, 185, 118)" stroke-opacity="0.558222476278" stroke-width="8"/>""",
        """<ellipse cx="495.65781271" cy="920.689773921" fill="rgb(168, 241, 166)" opacity="0.575776767249" rx="55.5103862515" ry="18.9090215629" stroke="rgb(74, 4, 31)" stroke-opacity="0.975486410925" stroke-width="6"/>""",
        """<ellipse cx="726.230050501" cy="502.646941349" fill="rgb(223, 139, 221)" opacity="0.767387123854" rx="0.548882029964" ry="43.1489366519" stroke="rgb(112, 217, 131)" stroke-opacity="0.925101008763" stroke-width="10"/>""",
        """<ellipse cx="499.334886425" cy="129.941544141" fill="rgb(160, 114, 231)" opacity="0.967077821084" rx="77.3906333049" ry="10.3752688828" stroke="rgb(244, 109, 231)" stroke-opacity="0.938784848086" stroke-width="1"/>""",
        """<ellipse cx="338.468287287" cy="119.730112223" fill="rgb(79, 252, 145)" opacity="0.681323280749" rx="11.0486796255" ry="6.80081879911" stroke="rgb(154, 29, 43)" stroke-opacity="0.899196923278" stroke-width="2"/>""",
        """<ellipse cx="825.087419801" cy="941.08124894" fill="rgb(121, 232, 222)" opacity="0.886159445596" rx="93.4384354161" ry="52.4123077119" stroke="rgb(67, 63, 151)" stroke-opacity="0.57037662039" stroke-width="10"/>""",
        """<ellipse cx="426.672233977" cy="263.726638276" fill="rgb(82, 104, 247)" opacity="0.885943279526" rx="84.1492832122" ry="86.3604309594" stroke="rgb(226, 137, 118)" stroke-opacity="0.859002971112" stroke-width="6"/>""",
        """<ellipse cx="741.03680314" cy="654.252459119" fill="rgb(255, 161, 57)" opacity="0.934002934166" rx="59.0360176931" ry="75.9946399339" stroke="rgb(77, 158, 229)" stroke-opacity="0.820128569403" stroke-width="4"/>""",
        """<ellipse cx="678.987931308" cy="509.183858647" fill="rgb(41, 128, 216)" opacity="0.695128203271" rx="77.1288622877" ry="13.7006329875" stroke="rgb(17, 222, 21)" stroke-opacity="0.920810597184" stroke-width="1"/>""",
        """<ellipse cx="127.39682239" cy="538.050326674" fill="rgb(183, 38, 205)" opacity="0.991610221976" rx="26.9544760667" ry="38.5064167839" stroke="rgb(10, 124, 8)" stroke-opacity="0.523818994172" stroke-width="4"/>""",
        """<ellipse cx="751.805639286" cy="572.514044575" fill="rgb(65, 60, 0)" opacity="0.820165794592" rx="61.8030031348" ry="91.4762284458" stroke="rgb(133, 166, 107)" stroke-opacity="0.515128285509" stroke-width="6"/>""",
        """<ellipse cx="365.706575898" cy="953.821429731" fill="rgb(169, 121, 203)" opacity="0.623841459092" rx="44.6995445375" ry="28.8166869372" stroke="rgb(151, 91, 91)" stroke-opacity="0.986951205921" stroke-width="6"/>""",
        """<ellipse cx="692.910597675" cy="262.859883488" fill="rgb(216, 5, 2)" opacity="0.658553632659" rx="96.0251585237" ry="0.327153447398" stroke="rgb(119, 226, 234)" stroke-opacity="0.637149585809" stroke-width="4"/>""",
        """<ellipse cx="620.77944186" cy="379.899771718" fill="rgb(92, 161, 135)" opacity="0.990810478834" rx="50.5631397452" ry="93.7164914463" stroke="rgb(8, 171, 35)" stroke-opacity="0.585919149867" stroke-width="10"/>""",
        """<ellipse cx="250.197776422" cy="977.851089516" fill="rgb(87, 156, 15)" opacity="0.647544351117" rx="55.5804262276" ry="60.6559179191" stroke="rgb(70, 55, 200)" stroke-opacity="0.831151401975" stroke-width="8"/>""",
        """<ellipse cx="226.112076749" cy="480.295406239" fill="rgb(146, 141, 164)" opacity="0.802960055724" rx="34.3087865573" ry="30.3895820539" stroke="rgb(11, 214, 44)" stroke-opacity="0.886026374044" stroke-width="6"/>""",
        """<ellipse cx="871.551286598" cy="945.546674653" fill="rgb(206, 2, 117)" opacity="0.726522742673" rx="49.2061024174" ry="70.7306506997" stroke="rgb(158, 96, 172)" stroke-opacity="0.652771421829" stroke-width="2"/>""",
        """<ellipse cx="401.334736865" cy="644.100449415" fill="rgb(57, 39, 2)" opacity="0.738607759877" rx="31.0648110571" ry="98.118022117" stroke="rgb(42, 165, 16)" stroke-opacity="0.729082576218" stroke-width="1"/>""",
        """<ellipse cx="895.281901198" cy="814.19985736" fill="rgb(36, 187, 252)" opacity="0.961471391372" rx="8.3146827223" ry="68.245549568" stroke="rgb(12, 158, 113)" stroke-opacity="0.565891728306" stroke-width="1"/>""",
        """<ellipse cx="142.204625277" cy="680.510673405" fill="rgb(20, 118, 86)" opacity="0.87826944565" rx="75.5233882006" ry="40.8840740261" stroke="rgb(55, 44, 33)" stroke-opacity="0.976732680846" stroke-width="6"/>""",
        """<ellipse cx="634.815411395" cy="170.039565984" fill="rgb(64, 32, 226)" opacity="0.575845845953" rx="6.23439575374" ry="12.046124548" stroke="rgb(35, 93, 136)" stroke-opacity="0.901502494921" stroke-width="4"/>""",
        """<ellipse cx="269.996716312" cy="954.328162014" fill="rgb(0, 133, 25)" opacity="0.933888402896" rx="31.902764982" ry="91.3944917811" stroke="rgb(107, 188, 125)" stroke-opacity="0.857279936763" stroke-width="4"/>""",
        """<ellipse cx="928.639075078" cy="225.495927643" fill="rgb(96, 114, 214)" opacity="0.959587581876" rx="93.5726556265" ry="9.90198958916" stroke="rgb(10, 12, 70)" stroke-opacity="0.831196826906" stroke-width="5"/>""",
        """<ellipse cx="352.606903722" cy="567.408780347" fill="rgb(75, 123, 6)" opacity="0.819454653817" rx="74.1290801281" ry="84.9689756662" stroke="rgb(204, 11, 92)" stroke-opacity="0.913634266863" stroke-width="10"/>""",
        """<ellipse cx="706.442006462" cy="509.725274612" fill="rgb(214, 215, 201)" opacity="0.768844913645" rx="46.9954214682" ry="94.3516435731" stroke="rgb(103, 235, 35)" stroke-opacity="0.612060323395" stroke-width="6"/>""",
        """<ellipse cx="334.036687363" cy="766.906281539" fill="rgb(43, 207, 183)" opacity="0.716603769355" rx="24.4348634875" ry="39.9125353828" stroke="rgb(178, 213, 27)" stroke-opacity="0.72053104948" stroke-width="10"/>""",
        """<ellipse cx="602.637702359" cy="732.925756702" fill="rgb(92, 9, 113)" opacity="0.758027672166" rx="36.6626706768" ry="53.8310819351" stroke="rgb(62, 116, 107)" stroke-opacity="0.573087423402" stroke-width="8"/>""",
        """<ellipse cx="634.976053293" cy="582.682632238" fill="rgb(51, 49, 158)" opacity="0.973811924432" rx="13.6924390157" ry="77.6767997977" stroke="rgb(22, 4, 122)" stroke-opacity="0.568229163388" stroke-width="7"/>""",
        """<ellipse cx="593.781052698" cy="589.744418261" fill="rgb(127, 99, 28)" opacity="0.620738129576" rx="32.9864111884" ry="60.1455997348" stroke="rgb(140, 195, 23)" stroke-opacity="0.855015083623" stroke-width="5"/>""",
        """<ellipse cx="777.1426386" cy="475.275573284" fill="rgb(220, 140, 98)" opacity="0.628081219546" rx="14.2295891327" ry="70.1242878016" stroke="rgb(111, 125, 204)" stroke-opacity="0.848694907986" stroke-width="9"/>""",
        """<ellipse cx="203.888189178" cy="833.847359637" fill="rgb(138, 168, 248)" opacity="0.968577230207" rx="89.8936432853" ry="39.3360320104" stroke="rgb(158, 18, 186)" stroke-opacity="0.68500876803" stroke-width="1"/>""",
        """<ellipse cx="896.095422259" cy="578.656606461" fill="rgb(34, 130, 50)" opacity="0.617018701176" rx="96.343883946" ry="41.0847304317" stroke="rgb(46, 207, 193)" stroke-opacity="0.655494096126" stroke-width="5"/>""",
        """<ellipse cx="222.901040371" cy="991.234630639" fill="rgb(151, 182, 82)" opacity="0.761241262164" rx="76.4228355088" ry="39.8685922573" stroke="rgb(166, 216, 142)" stroke-opacity="0.761671921784" stroke-width="2"/>""",
        """<ellipse cx="109.514372908" cy="737.359165647" fill="rgb(194, 110, 223)" opacity="0.752742318504" rx="14.3249554395" ry="89.0524187604" stroke="rgb(21, 142, 29)" stroke-opacity="0.692542833206" stroke-width="10"/>""",
        """<ellipse cx="791.7163574" cy="144.786946993" fill="rgb(240, 50, 101)" opacity="0.752231087803" rx="22.8745641138" ry="19.9949159442" stroke="rgb(20, 133, 151)" stroke-opacity="0.795512432697" stroke-width="9"/>""",
        """<ellipse cx="703.767057478" cy="713.503188526" fill="rgb(122, 224, 101)" opacity="0.593155040622" rx="3.9136848464" ry="53.1681458434" stroke="rgb(239, 32, 254)" stroke-opacity="0.794339558874" stroke-width="6"/>""",
        """<ellipse cx="913.694374093" cy="386.913447808" fill="rgb(49, 31, 231)" opacity="0.768824289793" rx="32.5878288329" ry="68.5402379212" stroke="rgb(167, 238, 149)" stroke-opacity="0.769438212448" stroke-width="1"/>""",
        """<ellipse cx="297.92004961" cy="887.523887824" fill="rgb(41, 157, 164)" opacity="0.69602385221" rx="96.2160881874" ry="22.3753097026" stroke="rgb(21, 209, 232)" stroke-opacity="0.699043596898" stroke-width="4"/>""",
        """<ellipse cx="964.701805059" cy="672.928219556" fill="rgb(78, 252, 203)" opacity="0.719792699297" rx="30.1218557982" ry="92.0518620853" stroke="rgb(198, 28, 185)" stroke-opacity="0.588991732603" stroke-width="6"/>""",
        """<ellipse cx="700.413605819" cy="793.917603198" fill="rgb(70, 248, 174)" opacity="0.570031680129" rx="76.6032767253" ry="24.7217315936" stroke="rgb(152, 247, 27)" stroke-opacity="0.71606220854" stroke-width="7"/>""",
        """<ellipse cx="237.625238838" cy="259.559125426" fill="rgb(150, 162, 190)" opacity="0.839200310957" rx="96.7811563649" ry="35.0544123722" stroke="rgb(181, 24, 250)" stroke-opacity="0.805281952545" stroke-width="2"/>""",
        """<ellipse cx="257.98666024" cy="336.134725216" fill="rgb(15, 42, 70)" opacity="0.798484867916" rx="78.9763950585" ry="66.2122995096" stroke="rgb(82, 109, 247)" stroke-opacity="0.673206011585" stroke-width="10"/>""",
        """<ellipse cx="749.497959843" cy="816.85779554" fill="rgb(118, 130, 214)" opacity="0.848336044408" rx="46.8086892652" ry="59.3497596094" stroke="rgb(159, 230, 214)" stroke-opacity="0.509423779673" stroke-width="6"/>""",
        """<ellipse cx="285.907506423" cy="245.030539874" fill="rgb(131, 64, 199)" opacity="0.7253983869" rx="23.8391551623" ry="33.19507124" stroke="rgb(214, 227, 116)" stroke-opacity="0.721908558111" stroke-width="4"/>""",
        """<ellipse cx="132.662768235" cy="396.110803512" fill="rgb(228, 217, 165)" opacity="0.651827505577" rx="90.1202971069" ry="95.8625036834" stroke="rgb(212, 190, 29)" stroke-opacity="0.617911919123" stroke-width="10"/>""",
        """<ellipse cx="830.596608346" cy="865.241580083" fill="rgb(136, 196, 145)" opacity="0.760974426339" rx="74.967672134" ry="71.2827563406" stroke="rgb(130, 131, 58)" stroke-opacity="0.524233619994" stroke-width="1"/>""",
        """<ellipse cx="266.401965907" cy="599.541776089" fill="rgb(114, 33, 127)" opacity="0.92143850995" rx="16.4618338354" ry="37.0128201785" stroke="rgb(118, 89, 164)" stroke-opacity="0.590642283223" stroke-width="8"/>""",
        """<ellipse cx="398.975768139" cy="571.270090801" fill="rgb(77, 183, 141)" opacity="0.813954772525" rx="56.8131259794" ry="52.283297456" stroke="rgb(86, 125, 176)" stroke-opacity="0.513774789239" stroke-width="9"/>""",
        """<ellipse cx="874.698392264" cy="545.082805865" fill="rgb(193, 195, 141)" opacity="0.600023678864" rx="87.6631872008" ry="27.3650906618" stroke="rgb(194, 96, 252)" stroke-opacity="0.630048035228" stroke-width="6"/>""",
        """<ellipse cx="247.68242258" cy="671.720385176" fill="rgb(132, 223, 190)" opacity="0.764919430248" rx="45.699143065" ry="15.6797472398" stroke="rgb(165, 77, 205)" stroke-opacity="0.695779417396" stroke-width="5"/>""",
        """<ellipse cx="189.726918153" cy="360.25218695" fill="rgb(212, 184, 110)" opacity="0.658333027855" rx="22.1635410619" ry="45.4887495572" stroke="rgb(66, 100, 28)" stroke-opacity="0.799955933097" stroke-width="7"/>""",
        """<ellipse cx="360.189758933" cy="809.552326575" fill="rgb(188, 13, 116)" opacity="0.919258523279" rx="36.527652285" ry="24.0064725755" stroke="rgb(160, 235, 219)" stroke-opacity="0.603507479032" stroke-width="9"/>""",

)

    def test_ellipse_to_xml(self):
        """Ellipse: Object ---> XML"""
        for ellipse, xml in zip(self.ellipse_objects, self.ellipse_xml_strings): 
            self.assertEqual(ellipse.to_xml(), xml)

 
    def test_ellipse_from_xml(self):
        """Ellipse: XML ---> Object"""
        assert len(self.ellipse_objects) == len(self.ellipse_xml_strings)
        for ellipse, xml in zip(self.ellipse_objects, self.ellipse_xml_strings): 
            self.assertEqual(ellipse, object_from_xml(xml))



class PolylineTest(unittest.TestCase):
    """Test For svgenesis.primitives.Polyline"""
    ################################################
    # Polyline Objects and XML Strings
    ################################################
    polyline_objects = ()

    polyline_xml_strings = ()

    def test_polyline_to_xml(self):
        """Polyline: Object ---> XML"""
        for polyline, xml in zip(self.polyline_objects, self.polyline_xml_strings): 
            self.assertEqual(polyline.to_xml(), xml)

 
    def test_polyline_from_xml(self):
        """Polyline: XML ---> Object"""
        assert len(self.polyline_objects) == len(self.polyline_xml_strings)
        for polyline, xml in zip(self.polyline_objects, self.polyline_xml_strings): 
            self.assertEqual(polyline, object_from_xml(xml))
        
        
        pass




class PolygonTest(unittest.TestCase):
    """Test For svgenesis.primitives.Polygon"""
    ################################################
    # Polygon Objects and XML Strings
    ################################################
    polygon_objects = ()

    polygon_xml_strings = ()

    def test_polygon_to_xml(self):
        """Polygon: Object ---> XML"""
        for polygon, xml in zip(self.polygon_objects, self.polygon_xml_strings): 
            self.assertEqual(polygon.to_xml(), xml)

 
    def test_polygon_from_xml(self):
        """Polygon: XML ---> Object"""
        assert len(self.polygon_objects) == len(self.polygon_xml_strings)
        for polygon, xml in zip(self.polygon_objects, self.polygon_xml_strings): 
            self.assertEqual(polygon, object_from_xml(xml))

        pass



class PathTest(unittest.TestCase):
    """Test For svgenesis.primitives.Path"""
    ################################################
    # Path Objects and XML Strings
    ################################################
    path_objects = ()

    path_xml_strings = ()

    def test_path_to_xml(self):
        """Path: Object ---> XML"""
        for path, xml in zip(self.path_objects, self.path_xml_strings): 
            self.assertEqual(path.to_xml(), xml)

 
    def test_path_from_xml(self):
        """Path: XML ---> Object"""
        assert len(self.path_objects) == len(self.path_xml_strings)
        for path, xml in zip(self.path_objects, self.path_xml_strings): 
            self.assertEqual(path, object_from_xml(xml))


def main():
    import textstyle as style
    import sys

    print
    print style.bold_blue_text("Testing: `svgenesis.primitives'")
    print 

    unittest.main()


if __name__ == "__main__":
    main()
