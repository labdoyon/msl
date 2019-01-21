# -*- coding: utf-8 -*-
# 
# ld_intro: Learn the sequence

from psychopy import visual, core, event
from ld_utils import createWindow
from ld_messages import introMessage1, introMessage2, readyMessage
from numpy import inf
from ld_mslMenu import getParamMenu
import numpy as np
import sys

#Menu
infos = getParamMenu('intro')

#Create Window @TODO Check multiple monitor and flip
currWindow = createWindow(infos['fullScreen'])

# Presentation - wait for TRIGGER
taskStim1 = visual.TextStim(currWindow, text=introMessage1[infos['language']], color='gold',wrapWidth=100, pos=(0,.5))
taskStim2 = visual.TextStim(currWindow, text=introMessage2[infos['language']], color='gold',wrapWidth=100, pos=(0,.3))
taskStim3 = visual.TextStim(currWindow, text=infos['seq'], color='gold',wrapWidth=100, pos=(0,0))
waitStim = visual.TextStim(currWindow, text=readyMessage[infos['language']], color='gold',wrapWidth=100, pos=(0,-.7))

#Draw messages
taskStim1.draw()
taskStim2.draw()
taskStim3.draw()
waitStim.draw()
currWindow.flip()

#Reformat SEQ
infos['seq'] = infos['seq'].replace(' - ','')

# Create Cross before starting the experiment 
cross = visual.ShapeStim(currWindow, units='cm',
    vertices=((0, -2), (0, 2), (0,0), (-2,0), (2, 0)),
    lineWidth=900,
    closeShape=False,
    lineColor='red')

# Wait for trigger
out = event.waitKeys(maxWait=inf, keyList=['5'], timeStamped=True)

#First RED Cross
cross.draw()
currWindow.flip()
core.wait(infos['durRest'])

NbSeqOK = 0

while (NbSeqOK < infos['introNbSeq']):
    
    seqOK = 0;
    keyTmp = [];
    
    # Green cross
    cross.setLineColor('green')
    cross.draw()
    currWindow.flip()
    
    while seqOK == 0:
        keyTmp.append(event.waitKeys(maxWait=inf, keyList=['1','2','3','4','escape']))

        keyStr = [i[0] for i in keyTmp]
        keyStr = [i[0] for i in keyStr]
        keyStr = ''.join(keyStr)
                
        if len(keyStr) == len(infos['seq']):
            if keyStr == infos['seq']:
                keyTmp = []
                seqOK = 1
                NbSeqOK += 1
            else:
                del keyTmp[0]
                NbSeqOK = 0

currWindow.close()
print 'End Intro'