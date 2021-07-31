import math
from xml.etree import ElementTree

tree = ElementTree.parse('parse.rbxlx')
robloxCore = tree.getroot()

game = {}
workspaceParts = []

def degree(radian):
    pi = math.pi
    deg = (radian*180)/pi
    return deg

def add_part(item):
    Properties = list(item)[0]

    p = {}

    for property in list(Properties):
        p[property.attrib["name"]] = property

    CFrame = p['CFrame']

    CValues = {}

    for CFrameProp in list(CFrame):
        CValues[CFrameProp.tag] = CFrameProp

    X, Y, Z = CValues["X"].text, CValues["Y"].text, CValues["Z"].text
    X, Y, Z = float(X), float(Y), float(Z)

    R00, R01, R02, R12, R22 = CValues["R00"].text, CValues["R01"].text, CValues["R02"].text, CValues["R12"].text, CValues["R22"].text

    ry = degree(math.asin(float(R02)))
    rx = degree(math.atan2(-float(R12), float(R22)))
    rz = degree(math.atan2(-float(R01), float(R00)))

    Size = p["size"]
    SizeChildren = list(Size)

    sX, sY, sZ = float(SizeChildren[0].text), float(SizeChildren[1].text), float(SizeChildren[2].text)

    workspaceParts.append({
        "element": item,
        "Position": {
            "X": X,
            "Y": Y,
            "Z": Z
        },
        "Rotation": {
            "X": rx,
            "Y": ry,
            "Z": rz
        },
        "Size": {
            "X": sX,
            "Y": sY,
            "Z": sZ
        }

    })

def convert():
    for child in list(robloxCore):
        tagName = child.tag
        attributes = child.attrib

        if "class" in attributes:
            game[attributes["class"]] = child


    for item in list(game['Workspace']):
        attributes = item.attrib

        if "class" in attributes:
            className = attributes["class"] 

            if className == "Part":
                add_part(item)

    return workspaceParts