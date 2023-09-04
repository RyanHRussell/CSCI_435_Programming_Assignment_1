import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import sys, os


def findAndRecordBounds(node: ET.Element, bounds):
    """ Recursive method to find the leaf nodes in the XML tree and store the
    bounds of the corresponding GUI element """

    if len(node) == 0:

        cur_bound_str = node.get("bounds")
        # cur_bound_str has the form "[x1,y1][x2,y2]"

        cur_bound = cur_bound_str.split(",")
        # now cur_bound has 3 elements of the form ["[x1",   "y1][x2",   "y2]"]

        cur_bound[1] = cur_bound[1].split("]")
        # now cur_bound has 3 elements of the form ["[x1",   [ "y1", "[x2" ],   "y2]"]

        cur_bound[0] = int(cur_bound[0][1:])

        cur_bound[1][0] = int(cur_bound[1][0])
        cur_bound[1][1] = int(cur_bound[1][1][1:])

        cur_bound[2] = int(cur_bound[2][:-1])
        # now cur_bound has 3 elements of the form [x1,   [y1, x2],   y2]

        bounds.append( (cur_bound[0], cur_bound[1][0], cur_bound[1][1], cur_bound[2]) )


    else:
        for child in node:
            findAndRecordBounds(child, bounds)



def parseTreeForBounds (xmlFile):
    """ Returns a list of the bounds of all GUI elements in the XML file """

    tree = ET.parse(xmlFile)

    root = tree.getroot()

    bounds = [] # bounds is a list of 4-tuples that each contain the coordinates of the
                # top left and lower right corners of the bounds of a GUI object in the
                # form (x1, y1, x2, y2)

    findAndRecordBounds(root, bounds)

    return bounds




def drawRectangles(pngFile, bounds):
    """ Draws rectangles in the positions specified by the bounds on a copy of the provided png file """

    with Image.open(pngFile) as image:

        draw = ImageDraw.Draw(image)

        for coords in bounds:

            draw.rectangle( coords, outline="yellow", width=5 )

        filename = pngFile[:-3] + "annotated.png"

        image.save(filename)





if __name__ == '__main__':

    path = sys.argv[1]

    ls = os.listdir(path)

    for file in ls:

        if file[-4:] == ".xml":

            filePath = path + "/" + file

            bnds = parseTreeForBounds(filePath)

            filePath = filePath[:-3] + "png"

            drawRectangles(filePath, bnds)