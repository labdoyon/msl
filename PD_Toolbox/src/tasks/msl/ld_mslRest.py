# -*- coding: utf-8 -*-
#
# ld_rest: show a white cross

from psychopy import event, visual
from ld_utils import createWindow

currWindow = createWindow(True)

cross = visual.ShapeStim(currWindow, units='cm',
    vertices=((0, -2), (0, 2), (0,0), (-2,0), (2, 0)),
    lineWidth=900,
    closeShape=False,
    lineColor='white')

cross.draw()
currWindow.flip()

k = ['']
while k[0] not in ['escape', 'esc','q']:
    k = event.waitKeys()
	
currWindow.close()
print 'End Rest'