I chose to use Python for this assignment due to my familiarity with the language and the ease with which I could use other libraries. The flexibility of Python also allowed me to write the code for this assignemnt faster.

The steps I took to solve the problem were: First, parsing the XML tree to find the leaf GUI elements. After finding the leaf elements, I recorded the coordinates of their bounding boxes in a list. This list of boundary coordinates was used to draw rectangles over the GUI elements in the corresponding png image. This process was repeated for each XML-png pair in the provided folder.

In order to parse the XML tree hierarchy, I chose to use the ElementTree module. In order to find the leaf elements, I used a recursive algorithm to search for nodes that had no children.

I used the pillow module to draw the rectangles on the annotated images. 