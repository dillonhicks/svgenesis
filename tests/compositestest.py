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
from svgenesis.core import *
from svgenesis.composites import *
import unittest

class TriangleTest(unittest.TestCase):
    """Test For svgenesis.composites.Triangle"""

    triangle_objects = (
        Triangle(stroke=rgb(56, 52, 31), points=((1011, 662), (1808, 1926), (1605, 1372)), stroke_width=9, fill=rgb(103, 126, 255)),
        Triangle(stroke=rgb(155, 174, 77), points=((1320, 1048), (979, 1449), (1562, 1742)), stroke_width=4, fill=rgb(7, 240, 26)),
        Triangle(stroke=rgb(155, 118, 191), points=((42, 1510), (467, 38), (1748, 599)), stroke_width=3, fill=rgb(155, 220, 35)),
        Triangle(stroke=rgb(114, 78, 227), points=((1574, 954), (1894, 866), (1817, 1355)), stroke_width=10, fill=rgb(252, 93, 6)),
        Triangle(stroke=rgb(11, 123, 87), points=((1397, 1097), (173, 717), (1156, 846)), stroke_width=5, fill=rgb(182, 224, 230)),
        Triangle(stroke=rgb(95, 80, 175), points=((642, 1614), (1016, 618), (1717, 461)), stroke_width=1, fill=rgb(212, 1, 16)),
        Triangle(stroke=rgb(94, 100, 217), points=((307, 213), (1378, 1832), (172, 1425)), stroke_width=3, fill=rgb(39, 65, 112)),
        Triangle(stroke=rgb(62, 124, 66), points=((375, 1537), (1006, 139), (1951, 321)), stroke_width=10, fill=rgb(228, 97, 60)),
        Triangle(stroke=rgb(164, 247, 118), points=((1494, 673), (1125, 1107), (756, 1026)), stroke_width=3, fill=rgb(61, 183, 44)),
        Triangle(stroke=rgb(198, 218, 5), points=((1896, 244), (1624, 231), (1213, 1912)), stroke_width=9, fill=rgb(73, 93, 190)),
)
    triangle_xml_strings = (
	"""<polygon fill="rgb(103, 126, 255)" points="1011,662 1808,1926 1605,1372 " stroke="rgb(56, 52, 31)" stroke-width="9" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(7, 240, 26)" points="1320,1048 979,1449 1562,1742 " stroke="rgb(155, 174, 77)" stroke-width="4" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(155, 220, 35)" points="42,1510 467,38 1748,599 " stroke="rgb(155, 118, 191)" stroke-width="3" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(252, 93, 6)" points="1574,954 1894,866 1817,1355 " stroke="rgb(114, 78, 227)" stroke-width="10" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(182, 224, 230)" points="1397,1097 173,717 1156,846 " stroke="rgb(11, 123, 87)" stroke-width="5" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(212, 1, 16)" points="642,1614 1016,618 1717,461 " stroke="rgb(95, 80, 175)" stroke-width="1" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(39, 65, 112)" points="307,213 1378,1832 172,1425 " stroke="rgb(94, 100, 217)" stroke-width="3" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(228, 97, 60)" points="375,1537 1006,139 1951,321 " stroke="rgb(62, 124, 66)" stroke-width="10" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(61, 183, 44)" points="1494,673 1125,1107 756,1026 " stroke="rgb(164, 247, 118)" stroke-width="3" svgenesis:type="Triangle"/>""",
	"""<polygon fill="rgb(73, 93, 190)" points="1896,244 1624,231 1213,1912 " stroke="rgb(198, 218, 5)" stroke-width="9" svgenesis:type="Triangle"/>""")

    def test_triangle_to_xml(self):
        """Triangle: Object ---> XML"""
        assert len(self.triangle_objects) == len(self.triangle_xml_strings)
        for triangle, xml in zip(self.triangle_objects, 
                                 self.triangle_xml_strings): 
            self.assertEqual(triangle.to_xml(), xml)

 
    def test_triangle_from_xml(self):
        """Triangle: XML ---> Object"""
        assert len(self.triangle_objects) == len(self.triangle_xml_strings)
        for triangle, xml in zip(self.triangle_objects, self.triangle_xml_strings): 
            self.assertEqual(triangle, object_from_xml(xml))


class EquilateralTriangleTest(unittest.TestCase):
    """Test For svgenesis.composites.EquilateralTriangle"""
    triangle_objects = ()
    triangle_xml_strings = ()
    def test_triangle_to_xml(self):
        """EquilateralTriangle: Object ---> XML"""
        assert len(self.triangle_objects) == len(self.triangle_xml_strings)
        for triangle, xml in zip(self.triangle_objects, 
                                 self.triangle_xml_strings): 
            self.assertEqual(triangle.to_xml(), xml)

 
    def test_triangle_from_xml(self):
        """EquilateralTriangle: XML ---> Object"""
        assert len(self.triangle_objects) == len(self.triangle_xml_strings)
        for triangle, xml in zip(self.triangle_objects, self.triangle_xml_strings): 
            self.assertEqual(triangle, object_from_xml(xml))
    


class EquilateralPentagonTest(unittest.TestCase):
    """Test For svgenesis.composites.EquilateralPentagon"""
    pentagon_objects = ()
    pentagon_xml_strings = ()

    def test_pentagon_to_xml(self):
        """EquilateralPentagon: Object ---> XML"""
        assert len(self.pentagon_objects) == len(self.pentagon_xml_strings)
        for pentagon, xml in zip(self.pentagon_objects, 
                                 self.pentagon_xml_strings): 
            self.assertEqual(pentagon.to_xml(), xml)

 
    def test_pentagon_from_xml(self):
        """EquilateralPentagon: XML ---> Object"""
        assert len(self.pentagon_objects) == len(self.pentagon_xml_strings)
        for pentagon, xml in zip(self.pentagon_objects, self.pentagon_xml_strings): 
            self.assertEqual(pentagon, object_from_xml(xml))
    



class EquilateralHexagonTest(unittest.TestCase):
    """Test For svgenesis.composites.EquilateralTriangle"""
    hexagon_objects = ()
    hexagon_xml_strings = ()

    def test_hexagon_to_xml(self):
        """EquilateralHexagon: Object ---> XML"""
        assert len(self.hexagon_objects) == len(self.hexagon_xml_strings)
        for hexagon, xml in zip(self.hexagon_objects, 
                                 self.hexagon_xml_strings): 
            self.assertEqual(hexagon.to_xml(), xml)

 
    def test_hexagon_from_xml(self):
        """EquilateralHexagon: XML ---> Object"""
        assert len(self.hexagon_objects) == len(self.hexagon_xml_strings)
        for hexagon, xml in zip(self.hexagon_objects, self.hexagon_xml_strings): 
            self.assertEqual(hexagon, object_from_xml(xml))
    



if __name__ == "__main__":
    import textstyle as style
    import sys

    print
    print style.bold_blue_text("Testing: `svgenesis.composites'")
    print 

    unittest.main()
