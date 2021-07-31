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

    rotation = ElementTree.SubElement(properties, "vector3")
    rotation.attrib = {"name": "rotation"}

    rX = ElementTree.SubElement(rotation, "X")
    rX.text = str(part["Rotation"]["X"])

    rY = ElementTree.SubElement(rotation, "Y")
    rY.text = str(part["Rotation"]["Y"])

    rZ = ElementTree.SubElement(rotation, "Z")
    rZ.text = str(part["Rotation"]["Z"])
    
    scale = ElementTree.SubElement(properties, "vector3")
    scale.attrib = {"name": "scale"}

    sX = ElementTree.SubElement(scale, "X")
    sX.text = str(part["Size"]["X"])

    sY = ElementTree.SubElement(scale, "Y")
    sY.text = str(part["Size"]["Y"])

    sZ = ElementTree.SubElement(scale, "Z")
    sZ.text = str(part["Size"]["Z"])

    color = ElementTree.SubElement(properties, "string")
    color.attrib = {"name": "color"}
    color.text = "#000000"

    shape = ElementTree.SubElement(properties, "string")
    shape.attrib = {"name": "shape"}
    shape.text = "cube"

    material = ElementTree.SubElement(properties, "int")
    material.attrib = {"name": "material"}
    material.text = "0"

    bool = ElementTree.SubElement(properties, "boolean")
    bool.attrib = {"name": "anchored"}
    bool.text = "true"

    bool = ElementTree.SubElement(properties, "boolean")
    bool.attrib = {"name": "canCollide"}
    bool.text = "true"

    bool = ElementTree.SubElement(properties, "boolean")
    bool.attrib = {"name": "isSpawn"}
    bool.text = "false"

    bool = ElementTree.SubElement(properties, "boolean")
    bool.attrib = {"name": "hideStuds"}
    bool.text = "true"



tree.write('out/result.spm')