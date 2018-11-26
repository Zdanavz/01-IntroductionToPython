"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zack Zdanavicius.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
########################################################################
#
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window=rg.TurtleWindow()
blue=rg.SimpleTurtle('turtle')
blue.pen=rg.Pen('Blue', 5)
blue.speed=25

size = 150

for k in range(8):
    blue.draw_circle(size)
    blue.pen_up()
    blue.right(50)
    blue.pen_down()
    size=size-5

#########################################################################

window.tracer(100)

red=rg.SimpleTurtle('turtle')
red.pen=rg.Pen('red', 1)
red.speed=25

for k in range(500):
    red.left(91)
    red.forward(k)


window.close_on_mouse_click()