from svgenesis.core import *

class Group(SVGElement):
    """
    
    """
    SVG_TAG_NAME = 'g'

    @staticmethod
    def xml_parse_handler(group_node):
        pass

    def __init__(self, id=None, elements=[]):
        self.id = id
        self._elements = elements
        
    def __repr__(self):
        cls_name = self.__class__.__name__
        elems = []
        for e in self._elements:
            elems.append(repr(e))
        elems = ', '.join(elems)
        return '%s(%s)' % (cls_name, elems)

    def __str__(self):
        group_str =  ''
        for elem in self._elements: 
            group_str += str(elem)
        if not self.id is None:
            id_str = "id=\"%s\"" % self.id
        else:
            id_str = ''

        return self.SVG_TEMPLATE_STR % dict(GROUPING=group_str,
                                       ID=id_str)

    def to_node(self):
        node = minidom.Element(self.SVG_TAG_NAME)        
        if not self.id is None:
            node.setAttribute('id', str(self.id))
        for elem in self._elements:
            node.appendChild(elem.to_node())
        return node

    def to_xml(self):
        return self.to_node().toxml()


