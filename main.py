from converter import convert
from xml.etree import ElementTree

parts = convert()

tree = ElementTree.parse('template.xml')
game = tree.getroot()
environment = list(game)[0]

for part in parts:
    Part = ElementTree.SubElement(environment, "Item")
    Part.attrib = {'class': 'Part'}

    properties = ElementTree.SubElement(Part, "Properties")

    name = ElementTree.SubElement(properties, "string")
    name.attrib = {"name": "name"}
    name.text = "Part"

    position = ElementTree.SubElement(properties, "vector3")
    position.attrib = {"name": "position"}

    pX = ElementTree.SubElement(position, "X")
    pX.text = str(part["Position"]["X"])

    pY = ElementTree.SubElement(position, "Y")
    pY.text = str(part["Position"]["Y"])

    pZ = ElementTree.SubElement(position, "Z")
    pZ.text = str(part["Position"]["Z"])
    


tree.write('out/result.spm')