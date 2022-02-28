#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue May 19 10:51:22 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'WN_task_online_ver3'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/giorgioarcara/Documents/Lavori collaborazioni/Giovanni Pellegrino/White Noise/White Noise Psychopy/WN_Psychopy_Task_ver3/WN_task_online_ver3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "set_session"
set_sessionClock = core.Clock()
from math import floor
session_nr = int(expInfo['session'])
subject_nr = int(expInfo['participant'])

counterb_list = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
tot_levels = len(counterb_list)

k = subject_nr - (tot_levels*floor(subject_nr/tot_levels)) - 1;

my_session = counterb_list[k][session_nr-1]



if my_session == 1:
    ExpList = 'WN_RTblock1_ExpList.xlsx'

if my_session == 2:
    ExpList = 'WN_RTblock2_ExpList.xlsx'

if my_session == 3:
    ExpList = 'WN_RTblock3_ExpList.xlsx'

# Initialize components for Routine "Instr_Staircase"
Instr_StaircaseClock = core.Clock()
Instr_staircase_txt = visual.TextStim(win=win, name='Instr_staircase_txt',
    text='Benvenuto!\n\nIn questo esperimento dovrai ascoltare alcuni suoni ed effettuare alcuni compiti.\nCome prima cosa ti chiediamo di impostare il volume del tuo computer al massimo.\nCi sarà una breve sessione in cui ti chiederemo di premere i tasti "freccia su" e "freccia giù" \nin base a delle istruzioni sullo schermo.\n\nPremi il tasto "c" per continuare',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Instr_staircase"
Instr_staircaseClock = core.Clock()
hear_sc_fix = visual.TextStim(win=win, name='hear_sc_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stair_sound = sound.Sound('sound_cue.wav', secs=-1, stereo=True, hamming=True,
    name='stair_sound')
stair_sound.setVolume(1.0)
hear_sc_resp = keyboard.Keyboard()
# here intialize some variables
ini_volume=0.2
curr_volume=ini_volume
last_response='up'
tot_sc_trials=100
volumes_array=[1]*tot_sc_trials
hear_sc_ntrial=1

hc_instr1 = visual.TextStim(win=win, name='hc_instr1',
    text='Premi "freccia giù" se hai sentito il suono ',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
hc_instr2 = visual.TextStim(win=win, name='hc_instr2',
    text='Premi "freccia su" se non hai sentito il suono',
    font='Arial',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "set_sound_volume"
set_sound_volumeClock = core.Clock()

# Initialize components for Routine "Instr_exp"
Instr_expClock = core.Clock()
Instr_comp1_txt = visual.TextStim(win=win, name='Instr_comp1_txt',
    text='Adesso comincerà il compito vero e proprio.\nSiediti normalmente al computer come se dovessi scrivere.\nVedrai al centro dello schermo una croce nera. \nTieni lo sguardo sulla croce. \nA intervalli casuali comparirà un cerchio rosso oppure potrai sentire un breve suono. \nIn entrambi i casi dovrai rispondere premendo la Barra Spaziatrice il più velocemente possibile appena uno dei due stimoli (cerchio o suono) comparirà. \n\nTerminato questo compito riceverai ulteriori istruzioni. \n\nPremi il tasto "c" per continuare.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instr_task_key = keyboard.Keyboard()

# Initialize components for Routine "RTcomp"
RTcompClock = core.Clock()
RTcomp_fix = visual.TextStim(win=win, name='RTcomp_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RTcomp_poly = visual.Polygon(
    win=win, name='RTcomp_poly',
    edges=50, size=(0.09, 0.09),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
RTcomp_resp = keyboard.Keyboard()
RTcomp_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='RTcomp_sound')
RTcomp_sound.setVolume(1.0)
stimstart_array=[0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]
import random
RTISIarray=[1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

# Initialize components for Routine "Instr_stim_pre"
Instr_stim_preClock = core.Clock()
Instr_stim_pre_txt = visual.TextStim(win=win, name='Instr_stim_pre_txt',
    text='Ben fatto! \nOra vedrai di nuovo la croce nera. \nTieni lo sguardo sulla croce e rilassati. \nSentirai una traccia audio in sottofondo per qualche minuto ma non dovrai fare nulla. \nAd un certo punto vedrai ricomparire il cerchio rosso. \nOgni volta che comparirà, dovrai premere la Barra Spaziatrice il più velocemente possibile, come nel task precedente. \n\nQuando il cerchio smetterà di comparire, dovrai rilassarti e continuare ad ascoltare la traccia audio, per qualche minuto. \nTerminata quella sessione ti daremo nuove istruzioni\n\nPremi il tasto "c" per continuare.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instr_stim_pre_resp = keyboard.Keyboard()

# Initialize components for Routine "Stim_pre"
Stim_preClock = core.Clock()
PreStim_fix = visual.TextStim(win=win, name='PreStim_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
if my_session==1:
    background_sound_pre = sound.Sound('white_noise_bg.wav')

if my_session==2:
    background_sound_pre = sound.Sound('white_int_noise_bg2.wav')

if my_session==3:
    background_sound_pre = sound.Sound('pink_noise_bg.wav')


PreStim_key = keyboard.Keyboard()

# Initialize components for Routine "RTStim"
RTStimClock = core.Clock()
RTstim_fix = visual.TextStim(win=win, name='RTstim_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RTStim_poly = visual.Polygon(
    win=win, name='RTStim_poly',
    edges=50, size=(0.09, 0.09),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
RTStim_resp = keyboard.Keyboard()
polystart_array=[0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]
import random
StimISIarray=[1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

# Initialize components for Routine "Stim_post"
Stim_postClock = core.Clock()
PostStim_fix = visual.TextStim(win=win, name='PostStim_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PostStim_key = keyboard.Keyboard()

# Initialize components for Routine "Instr_comp2"
Instr_comp2Clock = core.Clock()
Instr_comp2_txt = visual.TextStim(win=win, name='Instr_comp2_txt',
    text='Quasi finito! \nOra dovrai rifare lo stesso task che hai completato per primo: cerchio e suono compariranno ad intervalli casuali. \nRispondi il più veloce possibile con la Barra Spaziatrice. \n\nPremi il tasto "c" per continuare.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instr_comp2_key = keyboard.Keyboard()

# Initialize components for Routine "RTcomp"
RTcompClock = core.Clock()
RTcomp_fix = visual.TextStim(win=win, name='RTcomp_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RTcomp_poly = visual.Polygon(
    win=win, name='RTcomp_poly',
    edges=50, size=(0.09, 0.09),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
RTcomp_resp = keyboard.Keyboard()
RTcomp_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='RTcomp_sound')
RTcomp_sound.setVolume(1.0)
stimstart_array=[0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]
import random
RTISIarray=[1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

# Initialize components for Routine "End"
EndClock = core.Clock()
End_txt = visual.TextStim(win=win, name='End_txt',
    text='Grazie della partecipazione!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "set_session"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
set_sessionComponents = []
for thisComponent in set_sessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
set_sessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "set_session"-------
while continueRoutine:
    # get current time
    t = set_sessionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=set_sessionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in set_sessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "set_session"-------
for thisComponent in set_sessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "set_session" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_Staircase"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Instr_StaircaseComponents = [Instr_staircase_txt, key_resp_5]
for thisComponent in Instr_StaircaseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_StaircaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_Staircase"-------
while continueRoutine:
    # get current time
    t = Instr_StaircaseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_StaircaseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_staircase_txt* updates
    if Instr_staircase_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_staircase_txt.frameNStart = frameN  # exact frame index
        Instr_staircase_txt.tStart = t  # local t and not account for scr refresh
        Instr_staircase_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_staircase_txt, 'tStartRefresh')  # time at next scr refresh
        Instr_staircase_txt.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['c'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_StaircaseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_Staircase"-------
for thisComponent in Instr_StaircaseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_staircase_txt.started', Instr_staircase_txt.tStartRefresh)
thisExp.addData('Instr_staircase_txt.stopped', Instr_staircase_txt.tStopRefresh)
# the Routine "Instr_Staircase" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
hear_staircase_loop = data.TrialHandler(nReps=tot_sc_trials, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='hear_staircase_loop')
thisExp.addLoop(hear_staircase_loop)  # add the loop to the experiment
thisHear_staircase_loop = hear_staircase_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHear_staircase_loop.rgb)
if thisHear_staircase_loop != None:
    for paramName in thisHear_staircase_loop:
        exec('{} = thisHear_staircase_loop[paramName]'.format(paramName))

for thisHear_staircase_loop in hear_staircase_loop:
    currentLoop = hear_staircase_loop
    # abbreviate parameter names if possible (e.g. rgb = thisHear_staircase_loop.rgb)
    if thisHear_staircase_loop != None:
        for paramName in thisHear_staircase_loop:
            exec('{} = thisHear_staircase_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instr_staircase"-------
    continueRoutine = True
    # update component parameters for each repeat
    stair_sound.setSound('sound_cue.wav', hamming=True)
    stair_sound.setVolume(curr_volume, log=False)
    hear_sc_resp.keys = []
    hear_sc_resp.rt = []
    _hear_sc_resp_allKeys = []
    # keep track of which components have finished
    Instr_staircaseComponents = [hear_sc_fix, stair_sound, hear_sc_resp, hc_instr1, hc_instr2]
    for thisComponent in Instr_staircaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instr_staircaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instr_staircase"-------
    while continueRoutine:
        # get current time
        t = Instr_staircaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instr_staircaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hear_sc_fix* updates
        if hear_sc_fix.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            hear_sc_fix.frameNStart = frameN  # exact frame index
            hear_sc_fix.tStart = t  # local t and not account for scr refresh
            hear_sc_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hear_sc_fix, 'tStartRefresh')  # time at next scr refresh
            hear_sc_fix.setAutoDraw(True)
        # start/stop stair_sound
        if stair_sound.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            stair_sound.frameNStart = frameN  # exact frame index
            stair_sound.tStart = t  # local t and not account for scr refresh
            stair_sound.tStartRefresh = tThisFlipGlobal  # on global time
            stair_sound.play(when=win)  # sync with win flip
        
        # *hear_sc_resp* updates
        waitOnFlip = False
        if hear_sc_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hear_sc_resp.frameNStart = frameN  # exact frame index
            hear_sc_resp.tStart = t  # local t and not account for scr refresh
            hear_sc_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hear_sc_resp, 'tStartRefresh')  # time at next scr refresh
            hear_sc_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(hear_sc_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(hear_sc_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if hear_sc_resp.status == STARTED and not waitOnFlip:
            theseKeys = hear_sc_resp.getKeys(keyList=['up', 'down'], waitRelease=False)
            _hear_sc_resp_allKeys.extend(theseKeys)
            if len(_hear_sc_resp_allKeys):
                hear_sc_resp.keys = _hear_sc_resp_allKeys[0].name  # just the first key pressed
                hear_sc_resp.rt = _hear_sc_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *hc_instr1* updates
        if hc_instr1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            hc_instr1.frameNStart = frameN  # exact frame index
            hc_instr1.tStart = t  # local t and not account for scr refresh
            hc_instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hc_instr1, 'tStartRefresh')  # time at next scr refresh
            hc_instr1.setAutoDraw(True)
        
        # *hc_instr2* updates
        if hc_instr2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            hc_instr2.frameNStart = frameN  # exact frame index
            hc_instr2.tStart = t  # local t and not account for scr refresh
            hc_instr2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hc_instr2, 'tStartRefresh')  # time at next scr refresh
            hc_instr2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instr_staircaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instr_staircase"-------
    for thisComponent in Instr_staircaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    hear_staircase_loop.addData('hear_sc_fix.started', hear_sc_fix.tStartRefresh)
    hear_staircase_loop.addData('hear_sc_fix.stopped', hear_sc_fix.tStopRefresh)
    stair_sound.stop()  # ensure sound has stopped at end of routine
    hear_staircase_loop.addData('stair_sound.started', stair_sound.tStartRefresh)
    hear_staircase_loop.addData('stair_sound.stopped', stair_sound.tStopRefresh)
    # check responses
    if hear_sc_resp.keys in ['', [], None]:  # No response was made
        hear_sc_resp.keys = None
    hear_staircase_loop.addData('hear_sc_resp.keys',hear_sc_resp.keys)
    if hear_sc_resp.keys != None:  # we had a response
        hear_staircase_loop.addData('hear_sc_resp.rt', hear_sc_resp.rt)
    hear_staircase_loop.addData('hear_sc_resp.started', hear_sc_resp.tStartRefresh)
    hear_staircase_loop.addData('hear_sc_resp.stopped', hear_sc_resp.tStopRefresh)
    curr_response = hear_sc_resp.keys
    vol_ind=hear_sc_ntrial-1
    volumes_array[vol_ind]=curr_volume
    
    if curr_response=='up':
        curr_volume=curr_volume+curr_volume*0.25
    
    if curr_response=='down':
        curr_volume=curr_volume-curr_volume*0.25
    
    if  (curr_response!=last_response) and hear_sc_ntrial!=1:
         curr_volume=ini_volume
    
    last_response = curr_response
    hear_sc_ntrial=hear_sc_ntrial+1
    
    hear_staircase_loop.addData('hc_instr1.started', hc_instr1.tStartRefresh)
    hear_staircase_loop.addData('hc_instr1.stopped', hc_instr1.tStopRefresh)
    hear_staircase_loop.addData('hc_instr2.started', hc_instr2.tStartRefresh)
    hear_staircase_loop.addData('hc_instr2.stopped', hc_instr2.tStopRefresh)
    # the Routine "Instr_staircase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed tot_sc_trials repeats of 'hear_staircase_loop'


# ------Prepare to start Routine "set_sound_volume"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
set_sound_volumeComponents = []
for thisComponent in set_sound_volumeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
set_sound_volumeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "set_sound_volume"-------
while continueRoutine:
    # get current time
    t = set_sound_volumeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=set_sound_volumeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in set_sound_volumeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "set_sound_volume"-------
for thisComponent in set_sound_volumeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
max_vol = max(volumes_array)
min_vol = min(volumes_array)
sound_vol=(max_vol-min_vol)/3

thisExp.addData('Final_Volume', sound_vol)
# the Routine "set_sound_volume" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_exp"-------
continueRoutine = True
# update component parameters for each repeat
Instr_task_key.keys = []
Instr_task_key.rt = []
_Instr_task_key_allKeys = []
curr_block="PreStim"
# keep track of which components have finished
Instr_expComponents = [Instr_comp1_txt, Instr_task_key]
for thisComponent in Instr_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_exp"-------
while continueRoutine:
    # get current time
    t = Instr_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_comp1_txt* updates
    if Instr_comp1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_comp1_txt.frameNStart = frameN  # exact frame index
        Instr_comp1_txt.tStart = t  # local t and not account for scr refresh
        Instr_comp1_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_comp1_txt, 'tStartRefresh')  # time at next scr refresh
        Instr_comp1_txt.setAutoDraw(True)
    
    # *Instr_task_key* updates
    waitOnFlip = False
    if Instr_task_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_task_key.frameNStart = frameN  # exact frame index
        Instr_task_key.tStart = t  # local t and not account for scr refresh
        Instr_task_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_task_key, 'tStartRefresh')  # time at next scr refresh
        Instr_task_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instr_task_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instr_task_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instr_task_key.status == STARTED and not waitOnFlip:
        theseKeys = Instr_task_key.getKeys(keyList=['c'], waitRelease=False)
        _Instr_task_key_allKeys.extend(theseKeys)
        if len(_Instr_task_key_allKeys):
            Instr_task_key.keys = _Instr_task_key_allKeys[-1].name  # just the last key pressed
            Instr_task_key.rt = _Instr_task_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_exp"-------
for thisComponent in Instr_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_comp1_txt.started', Instr_comp1_txt.tStartRefresh)
thisExp.addData('Instr_comp1_txt.stopped', Instr_comp1_txt.tStopRefresh)
# the Routine "Instr_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RT1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WN_RT_ExpList.xlsx'),
    seed=None, name='RT1_trials')
thisExp.addLoop(RT1_trials)  # add the loop to the experiment
thisRT1_trial = RT1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRT1_trial.rgb)
if thisRT1_trial != None:
    for paramName in thisRT1_trial:
        exec('{} = thisRT1_trial[paramName]'.format(paramName))

for thisRT1_trial in RT1_trials:
    currentLoop = RT1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisRT1_trial.rgb)
    if thisRT1_trial != None:
        for paramName in thisRT1_trial:
            exec('{} = thisRT1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RTcomp"-------
    continueRoutine = True
    # update component parameters for each repeat
    RTcomp_poly.setOpacity(VisOpacity)
    RTcomp_resp.keys = []
    RTcomp_resp.rt = []
    _RTcomp_resp_allKeys = []
    RTcomp_sound.setSound(SoundFileName, hamming=True)
    RTcomp_sound.setVolume(sound_vol, log=False)
    stimstart = random.choice(polystart_array)
    stop_draw_stim=False
    RTISI_dur=random.choice(StimISIarray)
    # keep track of which components have finished
    RTcompComponents = [RTcomp_fix, RTcomp_poly, RTcomp_resp, RTcomp_sound]
    for thisComponent in RTcompComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RTcompClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RTcomp"-------
    while continueRoutine:
        # get current time
        t = RTcompClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RTcompClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RTcomp_fix* updates
        if RTcomp_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_fix.frameNStart = frameN  # exact frame index
            RTcomp_fix.tStart = t  # local t and not account for scr refresh
            RTcomp_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_fix, 'tStartRefresh')  # time at next scr refresh
            RTcomp_fix.setAutoDraw(True)
        if RTcomp_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RTcomp_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                RTcomp_fix.tStop = t  # not accounting for scr refresh
                RTcomp_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_fix, 'tStopRefresh')  # time at next scr refresh
                RTcomp_fix.setAutoDraw(False)
        
        # *RTcomp_poly* updates
        if RTcomp_poly.status == NOT_STARTED and tThisFlip >= stimstart-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_poly.frameNStart = frameN  # exact frame index
            RTcomp_poly.tStart = t  # local t and not account for scr refresh
            RTcomp_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_poly, 'tStartRefresh')  # time at next scr refresh
            RTcomp_poly.setAutoDraw(True)
        if RTcomp_poly.status == STARTED:
            if bool(stop_draw_stim):
                # keep track of stop time/frame for later
                RTcomp_poly.tStop = t  # not accounting for scr refresh
                RTcomp_poly.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_poly, 'tStopRefresh')  # time at next scr refresh
                RTcomp_poly.setAutoDraw(False)
        
        # *RTcomp_resp* updates
        waitOnFlip = False
        if RTcomp_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_resp.frameNStart = frameN  # exact frame index
            RTcomp_resp.tStart = t  # local t and not account for scr refresh
            RTcomp_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_resp, 'tStartRefresh')  # time at next scr refresh
            RTcomp_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RTcomp_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RTcomp_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RTcomp_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                RTcomp_resp.tStop = t  # not accounting for scr refresh
                RTcomp_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_resp, 'tStopRefresh')  # time at next scr refresh
                RTcomp_resp.status = FINISHED
        if RTcomp_resp.status == STARTED and not waitOnFlip:
            theseKeys = RTcomp_resp.getKeys(keyList=['space'], waitRelease=False)
            _RTcomp_resp_allKeys.extend(theseKeys)
            if len(_RTcomp_resp_allKeys):
                RTcomp_resp.keys = _RTcomp_resp_allKeys[0].name  # just the first key pressed
                RTcomp_resp.rt = _RTcomp_resp_allKeys[0].rt
        # start/stop RTcomp_sound
        if RTcomp_sound.status == NOT_STARTED and tThisFlip >= stimstart-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_sound.frameNStart = frameN  # exact frame index
            RTcomp_sound.tStart = t  # local t and not account for scr refresh
            RTcomp_sound.tStartRefresh = tThisFlipGlobal  # on global time
            RTcomp_sound.play(when=win)  # sync with win flip
        if t > (stimstart+1):
            stop_draw_stim=True
            
        
        if RTcomp_resp.status == STARTED:
            if RTcomp_resp.keys=="space":
                stop_draw_stim=True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RTcompComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RTcomp"-------
    for thisComponent in RTcompComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT1_trials.addData('RTcomp_fix.started', RTcomp_fix.tStartRefresh)
    RT1_trials.addData('RTcomp_fix.stopped', RTcomp_fix.tStopRefresh)
    RT1_trials.addData('RTcomp_poly.started', RTcomp_poly.tStartRefresh)
    RT1_trials.addData('RTcomp_poly.stopped', RTcomp_poly.tStopRefresh)
    # check responses
    if RTcomp_resp.keys in ['', [], None]:  # No response was made
        RTcomp_resp.keys = None
    RT1_trials.addData('RTcomp_resp.keys',RTcomp_resp.keys)
    if RTcomp_resp.keys != None:  # we had a response
        RT1_trials.addData('RTcomp_resp.rt', RTcomp_resp.rt)
    RT1_trials.addData('RTcomp_resp.started', RTcomp_resp.tStartRefresh)
    RT1_trials.addData('RTcomp_resp.stopped', RTcomp_resp.tStopRefresh)
    RTcomp_sound.stop()  # ensure sound has stopped at end of routine
    RT1_trials.addData('RTcomp_sound.started', RTcomp_sound.tStartRefresh)
    RT1_trials.addData('RTcomp_sound.stopped', RTcomp_sound.tStopRefresh)
    thisExp.addData("block", curr_block)
    thisExp.addData("stimstart", stimstart)
    # the Routine "RTcomp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'RT1_trials'


# ------Prepare to start Routine "Instr_stim_pre"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
Instr_stim_pre_resp.keys = []
Instr_stim_pre_resp.rt = []
_Instr_stim_pre_resp_allKeys = []
# keep track of which components have finished
Instr_stim_preComponents = [Instr_stim_pre_txt, Instr_stim_pre_resp]
for thisComponent in Instr_stim_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_stim_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_stim_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Instr_stim_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_stim_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_stim_pre_txt* updates
    if Instr_stim_pre_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_stim_pre_txt.frameNStart = frameN  # exact frame index
        Instr_stim_pre_txt.tStart = t  # local t and not account for scr refresh
        Instr_stim_pre_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_stim_pre_txt, 'tStartRefresh')  # time at next scr refresh
        Instr_stim_pre_txt.setAutoDraw(True)
    if Instr_stim_pre_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instr_stim_pre_txt.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Instr_stim_pre_txt.tStop = t  # not accounting for scr refresh
            Instr_stim_pre_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instr_stim_pre_txt, 'tStopRefresh')  # time at next scr refresh
            Instr_stim_pre_txt.setAutoDraw(False)
    
    # *Instr_stim_pre_resp* updates
    waitOnFlip = False
    if Instr_stim_pre_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_stim_pre_resp.frameNStart = frameN  # exact frame index
        Instr_stim_pre_resp.tStart = t  # local t and not account for scr refresh
        Instr_stim_pre_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_stim_pre_resp, 'tStartRefresh')  # time at next scr refresh
        Instr_stim_pre_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instr_stim_pre_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instr_stim_pre_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instr_stim_pre_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instr_stim_pre_resp.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Instr_stim_pre_resp.tStop = t  # not accounting for scr refresh
            Instr_stim_pre_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instr_stim_pre_resp, 'tStopRefresh')  # time at next scr refresh
            Instr_stim_pre_resp.status = FINISHED
    if Instr_stim_pre_resp.status == STARTED and not waitOnFlip:
        theseKeys = Instr_stim_pre_resp.getKeys(keyList=['c'], waitRelease=False)
        _Instr_stim_pre_resp_allKeys.extend(theseKeys)
        if len(_Instr_stim_pre_resp_allKeys):
            Instr_stim_pre_resp.keys = _Instr_stim_pre_resp_allKeys[-1].name  # just the last key pressed
            Instr_stim_pre_resp.rt = _Instr_stim_pre_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_stim_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_stim_pre"-------
for thisComponent in Instr_stim_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_stim_pre_txt.started', Instr_stim_pre_txt.tStartRefresh)
thisExp.addData('Instr_stim_pre_txt.stopped', Instr_stim_pre_txt.tStopRefresh)

# ------Prepare to start Routine "Stim_pre"-------
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
background_sound_pre.setVolume(sound_vol)
background_sound_pre.play()
PreStim_key.keys = []
PreStim_key.rt = []
_PreStim_key_allKeys = []
# keep track of which components have finished
Stim_preComponents = [PreStim_fix, PreStim_key]
for thisComponent in Stim_preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Stim_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stim_pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stim_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stim_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PreStim_fix* updates
    if PreStim_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PreStim_fix.frameNStart = frameN  # exact frame index
        PreStim_fix.tStart = t  # local t and not account for scr refresh
        PreStim_fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PreStim_fix, 'tStartRefresh')  # time at next scr refresh
        PreStim_fix.setAutoDraw(True)
    if PreStim_fix.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PreStim_fix.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            PreStim_fix.tStop = t  # not accounting for scr refresh
            PreStim_fix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PreStim_fix, 'tStopRefresh')  # time at next scr refresh
            PreStim_fix.setAutoDraw(False)
    
    # *PreStim_key* updates
    waitOnFlip = False
    if PreStim_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PreStim_key.frameNStart = frameN  # exact frame index
        PreStim_key.tStart = t  # local t and not account for scr refresh
        PreStim_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PreStim_key, 'tStartRefresh')  # time at next scr refresh
        PreStim_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PreStim_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PreStim_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PreStim_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PreStim_key.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            PreStim_key.tStop = t  # not accounting for scr refresh
            PreStim_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PreStim_key, 'tStopRefresh')  # time at next scr refresh
            PreStim_key.status = FINISHED
    if PreStim_key.status == STARTED and not waitOnFlip:
        theseKeys = PreStim_key.getKeys(keyList=['q'], waitRelease=False)
        _PreStim_key_allKeys.extend(theseKeys)
        if len(_PreStim_key_allKeys):
            PreStim_key.keys = _PreStim_key_allKeys[-1].name  # just the last key pressed
            PreStim_key.rt = _PreStim_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stim_preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stim_pre"-------
for thisComponent in Stim_preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PreStim_fix.started', PreStim_fix.tStartRefresh)
thisExp.addData('PreStim_fix.stopped', PreStim_fix.tStopRefresh)
'''
if my_session==2:
    background_sound_pre.stop()
    '''

# set up handler to look after randomisation of conditions etc
Stim_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WN_RTblock1_ExpList.xlsx'),
    seed=None, name='Stim_trials')
thisExp.addLoop(Stim_trials)  # add the loop to the experiment
thisStim_trial = Stim_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStim_trial.rgb)
if thisStim_trial != None:
    for paramName in thisStim_trial:
        exec('{} = thisStim_trial[paramName]'.format(paramName))

for thisStim_trial in Stim_trials:
    currentLoop = Stim_trials
    # abbreviate parameter names if possible (e.g. rgb = thisStim_trial.rgb)
    if thisStim_trial != None:
        for paramName in thisStim_trial:
            exec('{} = thisStim_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RTStim"-------
    continueRoutine = True
    # update component parameters for each repeat
    RTStim_resp.keys = []
    RTStim_resp.rt = []
    _RTStim_resp_allKeys = []
    polystart = random.choice(polystart_array)
    stop_draw_pol=False
    StimISI_dur=random.choice(StimISIarray)
    # keep track of which components have finished
    RTStimComponents = [RTstim_fix, RTStim_poly, RTStim_resp]
    for thisComponent in RTStimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RTStimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RTStim"-------
    while continueRoutine:
        # get current time
        t = RTStimClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RTStimClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RTstim_fix* updates
        if RTstim_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RTstim_fix.frameNStart = frameN  # exact frame index
            RTstim_fix.tStart = t  # local t and not account for scr refresh
            RTstim_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTstim_fix, 'tStartRefresh')  # time at next scr refresh
            RTstim_fix.setAutoDraw(True)
        if RTstim_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RTstim_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                RTstim_fix.tStop = t  # not accounting for scr refresh
                RTstim_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTstim_fix, 'tStopRefresh')  # time at next scr refresh
                RTstim_fix.setAutoDraw(False)
        
        # *RTStim_poly* updates
        if RTStim_poly.status == NOT_STARTED and tThisFlip >= polystart-frameTolerance:
            # keep track of start time/frame for later
            RTStim_poly.frameNStart = frameN  # exact frame index
            RTStim_poly.tStart = t  # local t and not account for scr refresh
            RTStim_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTStim_poly, 'tStartRefresh')  # time at next scr refresh
            RTStim_poly.setAutoDraw(True)
        if RTStim_poly.status == STARTED:
            if bool(stop_draw_pol):
                # keep track of stop time/frame for later
                RTStim_poly.tStop = t  # not accounting for scr refresh
                RTStim_poly.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTStim_poly, 'tStopRefresh')  # time at next scr refresh
                RTStim_poly.setAutoDraw(False)
        
        # *RTStim_resp* updates
        waitOnFlip = False
        if RTStim_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RTStim_resp.frameNStart = frameN  # exact frame index
            RTStim_resp.tStart = t  # local t and not account for scr refresh
            RTStim_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTStim_resp, 'tStartRefresh')  # time at next scr refresh
            RTStim_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RTStim_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RTStim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RTStim_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                RTStim_resp.tStop = t  # not accounting for scr refresh
                RTStim_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTStim_resp, 'tStopRefresh')  # time at next scr refresh
                RTStim_resp.status = FINISHED
        if RTStim_resp.status == STARTED and not waitOnFlip:
            theseKeys = RTStim_resp.getKeys(keyList=['space'], waitRelease=False)
            _RTStim_resp_allKeys.extend(theseKeys)
            if len(_RTStim_resp_allKeys):
                RTStim_resp.keys = _RTStim_resp_allKeys[0].name  # just the first key pressed
                RTStim_resp.rt = _RTStim_resp_allKeys[0].rt
        if t > (polystart+1):
            stop_draw_pol=True
            
        
        if RTStim_resp.status == STARTED:
            if RTStim_resp.keys=="space":
                stop_draw_pol=True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RTStimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RTStim"-------
    for thisComponent in RTStimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Stim_trials.addData('RTstim_fix.started', RTstim_fix.tStartRefresh)
    Stim_trials.addData('RTstim_fix.stopped', RTstim_fix.tStopRefresh)
    Stim_trials.addData('RTStim_poly.started', RTStim_poly.tStartRefresh)
    Stim_trials.addData('RTStim_poly.stopped', RTStim_poly.tStopRefresh)
    # check responses
    if RTStim_resp.keys in ['', [], None]:  # No response was made
        RTStim_resp.keys = None
    Stim_trials.addData('RTStim_resp.keys',RTStim_resp.keys)
    if RTStim_resp.keys != None:  # we had a response
        Stim_trials.addData('RTStim_resp.rt', RTStim_resp.rt)
    Stim_trials.addData('RTStim_resp.started', RTStim_resp.tStartRefresh)
    Stim_trials.addData('RTStim_resp.stopped', RTStim_resp.tStopRefresh)
    thisExp.addData("block", "DuringStim")
    thisExp.addData("stimstart", polystart)
    # the Routine "RTStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Stim_trials'


# ------Prepare to start Routine "Stim_post"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
PostStim_key.keys = []
PostStim_key.rt = []
_PostStim_key_allKeys = []
# keep track of which components have finished
Stim_postComponents = [PostStim_fix, PostStim_key]
for thisComponent in Stim_postComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Stim_postClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stim_post"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stim_postClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stim_postClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PostStim_fix* updates
    if PostStim_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PostStim_fix.frameNStart = frameN  # exact frame index
        PostStim_fix.tStart = t  # local t and not account for scr refresh
        PostStim_fix.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PostStim_fix, 'tStartRefresh')  # time at next scr refresh
        PostStim_fix.setAutoDraw(True)
    if PostStim_fix.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PostStim_fix.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            PostStim_fix.tStop = t  # not accounting for scr refresh
            PostStim_fix.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PostStim_fix, 'tStopRefresh')  # time at next scr refresh
            PostStim_fix.setAutoDraw(False)
    
    # *PostStim_key* updates
    waitOnFlip = False
    if PostStim_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PostStim_key.frameNStart = frameN  # exact frame index
        PostStim_key.tStart = t  # local t and not account for scr refresh
        PostStim_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PostStim_key, 'tStartRefresh')  # time at next scr refresh
        PostStim_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PostStim_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PostStim_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PostStim_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PostStim_key.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            PostStim_key.tStop = t  # not accounting for scr refresh
            PostStim_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PostStim_key, 'tStopRefresh')  # time at next scr refresh
            PostStim_key.status = FINISHED
    if PostStim_key.status == STARTED and not waitOnFlip:
        theseKeys = PostStim_key.getKeys(keyList=['q'], waitRelease=False)
        _PostStim_key_allKeys.extend(theseKeys)
        if len(_PostStim_key_allKeys):
            PostStim_key.keys = _PostStim_key_allKeys[-1].name  # just the last key pressed
            PostStim_key.rt = _PostStim_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stim_postComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stim_post"-------
for thisComponent in Stim_postComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PostStim_fix.started', PostStim_fix.tStartRefresh)
thisExp.addData('PostStim_fix.stopped', PostStim_fix.tStopRefresh)
background_sound_pre.stop()


# ------Prepare to start Routine "Instr_comp2"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
Instr_comp2_key.keys = []
Instr_comp2_key.rt = []
_Instr_comp2_key_allKeys = []
curr_block="PostStim"
# keep track of which components have finished
Instr_comp2Components = [Instr_comp2_txt, Instr_comp2_key]
for thisComponent in Instr_comp2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_comp2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_comp2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Instr_comp2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_comp2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_comp2_txt* updates
    if Instr_comp2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_comp2_txt.frameNStart = frameN  # exact frame index
        Instr_comp2_txt.tStart = t  # local t and not account for scr refresh
        Instr_comp2_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_comp2_txt, 'tStartRefresh')  # time at next scr refresh
        Instr_comp2_txt.setAutoDraw(True)
    if Instr_comp2_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instr_comp2_txt.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Instr_comp2_txt.tStop = t  # not accounting for scr refresh
            Instr_comp2_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instr_comp2_txt, 'tStopRefresh')  # time at next scr refresh
            Instr_comp2_txt.setAutoDraw(False)
    
    # *Instr_comp2_key* updates
    waitOnFlip = False
    if Instr_comp2_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_comp2_key.frameNStart = frameN  # exact frame index
        Instr_comp2_key.tStart = t  # local t and not account for scr refresh
        Instr_comp2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_comp2_key, 'tStartRefresh')  # time at next scr refresh
        Instr_comp2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instr_comp2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instr_comp2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instr_comp2_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instr_comp2_key.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Instr_comp2_key.tStop = t  # not accounting for scr refresh
            Instr_comp2_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Instr_comp2_key, 'tStopRefresh')  # time at next scr refresh
            Instr_comp2_key.status = FINISHED
    if Instr_comp2_key.status == STARTED and not waitOnFlip:
        theseKeys = Instr_comp2_key.getKeys(keyList=['c'], waitRelease=False)
        _Instr_comp2_key_allKeys.extend(theseKeys)
        if len(_Instr_comp2_key_allKeys):
            Instr_comp2_key.keys = _Instr_comp2_key_allKeys[-1].name  # just the last key pressed
            Instr_comp2_key.rt = _Instr_comp2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_comp2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_comp2"-------
for thisComponent in Instr_comp2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_comp2_txt.started', Instr_comp2_txt.tStartRefresh)
thisExp.addData('Instr_comp2_txt.stopped', Instr_comp2_txt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
RT2_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('WN_RT_ExpList.xlsx'),
    seed=None, name='RT2_trials')
thisExp.addLoop(RT2_trials)  # add the loop to the experiment
thisRT2_trial = RT2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRT2_trial.rgb)
if thisRT2_trial != None:
    for paramName in thisRT2_trial:
        exec('{} = thisRT2_trial[paramName]'.format(paramName))

for thisRT2_trial in RT2_trials:
    currentLoop = RT2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisRT2_trial.rgb)
    if thisRT2_trial != None:
        for paramName in thisRT2_trial:
            exec('{} = thisRT2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RTcomp"-------
    continueRoutine = True
    # update component parameters for each repeat
    RTcomp_poly.setOpacity(VisOpacity)
    RTcomp_resp.keys = []
    RTcomp_resp.rt = []
    _RTcomp_resp_allKeys = []
    RTcomp_sound.setSound(SoundFileName, hamming=True)
    RTcomp_sound.setVolume(sound_vol, log=False)
    stimstart = random.choice(polystart_array)
    stop_draw_stim=False
    RTISI_dur=random.choice(StimISIarray)
    # keep track of which components have finished
    RTcompComponents = [RTcomp_fix, RTcomp_poly, RTcomp_resp, RTcomp_sound]
    for thisComponent in RTcompComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RTcompClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RTcomp"-------
    while continueRoutine:
        # get current time
        t = RTcompClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RTcompClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RTcomp_fix* updates
        if RTcomp_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_fix.frameNStart = frameN  # exact frame index
            RTcomp_fix.tStart = t  # local t and not account for scr refresh
            RTcomp_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_fix, 'tStartRefresh')  # time at next scr refresh
            RTcomp_fix.setAutoDraw(True)
        if RTcomp_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RTcomp_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                RTcomp_fix.tStop = t  # not accounting for scr refresh
                RTcomp_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_fix, 'tStopRefresh')  # time at next scr refresh
                RTcomp_fix.setAutoDraw(False)
        
        # *RTcomp_poly* updates
        if RTcomp_poly.status == NOT_STARTED and tThisFlip >= stimstart-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_poly.frameNStart = frameN  # exact frame index
            RTcomp_poly.tStart = t  # local t and not account for scr refresh
            RTcomp_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_poly, 'tStartRefresh')  # time at next scr refresh
            RTcomp_poly.setAutoDraw(True)
        if RTcomp_poly.status == STARTED:
            if bool(stop_draw_stim):
                # keep track of stop time/frame for later
                RTcomp_poly.tStop = t  # not accounting for scr refresh
                RTcomp_poly.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_poly, 'tStopRefresh')  # time at next scr refresh
                RTcomp_poly.setAutoDraw(False)
        
        # *RTcomp_resp* updates
        waitOnFlip = False
        if RTcomp_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_resp.frameNStart = frameN  # exact frame index
            RTcomp_resp.tStart = t  # local t and not account for scr refresh
            RTcomp_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTcomp_resp, 'tStartRefresh')  # time at next scr refresh
            RTcomp_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RTcomp_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RTcomp_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RTcomp_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                RTcomp_resp.tStop = t  # not accounting for scr refresh
                RTcomp_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTcomp_resp, 'tStopRefresh')  # time at next scr refresh
                RTcomp_resp.status = FINISHED
        if RTcomp_resp.status == STARTED and not waitOnFlip:
            theseKeys = RTcomp_resp.getKeys(keyList=['space'], waitRelease=False)
            _RTcomp_resp_allKeys.extend(theseKeys)
            if len(_RTcomp_resp_allKeys):
                RTcomp_resp.keys = _RTcomp_resp_allKeys[0].name  # just the first key pressed
                RTcomp_resp.rt = _RTcomp_resp_allKeys[0].rt
        # start/stop RTcomp_sound
        if RTcomp_sound.status == NOT_STARTED and tThisFlip >= stimstart-frameTolerance:
            # keep track of start time/frame for later
            RTcomp_sound.frameNStart = frameN  # exact frame index
            RTcomp_sound.tStart = t  # local t and not account for scr refresh
            RTcomp_sound.tStartRefresh = tThisFlipGlobal  # on global time
            RTcomp_sound.play(when=win)  # sync with win flip
        if t > (stimstart+1):
            stop_draw_stim=True
            
        
        if RTcomp_resp.status == STARTED:
            if RTcomp_resp.keys=="space":
                stop_draw_stim=True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RTcompComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RTcomp"-------
    for thisComponent in RTcompComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT2_trials.addData('RTcomp_fix.started', RTcomp_fix.tStartRefresh)
    RT2_trials.addData('RTcomp_fix.stopped', RTcomp_fix.tStopRefresh)
    RT2_trials.addData('RTcomp_poly.started', RTcomp_poly.tStartRefresh)
    RT2_trials.addData('RTcomp_poly.stopped', RTcomp_poly.tStopRefresh)
    # check responses
    if RTcomp_resp.keys in ['', [], None]:  # No response was made
        RTcomp_resp.keys = None
    RT2_trials.addData('RTcomp_resp.keys',RTcomp_resp.keys)
    if RTcomp_resp.keys != None:  # we had a response
        RT2_trials.addData('RTcomp_resp.rt', RTcomp_resp.rt)
    RT2_trials.addData('RTcomp_resp.started', RTcomp_resp.tStartRefresh)
    RT2_trials.addData('RTcomp_resp.stopped', RTcomp_resp.tStopRefresh)
    RTcomp_sound.stop()  # ensure sound has stopped at end of routine
    RT2_trials.addData('RTcomp_sound.started', RTcomp_sound.tStartRefresh)
    RT2_trials.addData('RTcomp_sound.stopped', RTcomp_sound.tStopRefresh)
    thisExp.addData("block", curr_block)
    thisExp.addData("stimstart", stimstart)
    # the Routine "RTcomp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'RT2_trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [End_txt]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_txt* updates
    if End_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_txt.frameNStart = frameN  # exact frame index
        End_txt.tStart = t  # local t and not account for scr refresh
        End_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_txt, 'tStartRefresh')  # time at next scr refresh
        End_txt.setAutoDraw(True)
    if End_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > End_txt.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            End_txt.tStop = t  # not accounting for scr refresh
            End_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(End_txt, 'tStopRefresh')  # time at next scr refresh
            End_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('End_txt.started', End_txt.tStartRefresh)
thisExp.addData('End_txt.stopped', End_txt.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
