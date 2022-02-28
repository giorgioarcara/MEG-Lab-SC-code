#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu May  7 16:14:16 2020
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
    originPath='/Users/giorgioarcara/Documents/Lavori collaborazioni/Giovanni Pellegrino/White Noise/White Noise Psychopy/WN_Psychopy_Task_ver3/WN_task_online_ver3.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "Instr1"
Instr1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Istruzioni task 1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
my_session = int(expInfo['session'])
if my_session == 1:
    ExpList = 'WN_RTblock1_ExpList.xlsx'

if my_session == 2:
    ExpList = 'WN_RTblock2_ExpList.xlsx'


# Initialize components for Routine "RT_comp"
RT_compClock = core.Clock()
trial_fix = visual.TextStim(win=win, name='trial_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=50, size=(0.06, 0.06),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
RTvis_resp = keyboard.Keyboard()
RT_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='RT_sound')
RT_sound.setVolume(1)

# Initialize components for Routine "RT_ISI"
RT_ISIClock = core.Clock()
import random
ISIarray=[2.1, 2.2, 2.3, 2.4, 2.5] 
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
Instr_text = visual.TextStim(win=win, name='Instr_text',
    text='Instruction here',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Stim_pre"
Stim_preClock = core.Clock()
Fix_pre = visual.TextStim(win=win, name='Fix_pre',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
if my_session==1:
    background_sound = sound.Sound('white_noise_bg.wav')
    
if my_session==2:
    background_sound = sound.Sound('white_int_noise_bg.wav')

key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "RTStim"
RTStimClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',
    edges=50, size=(0.06, 0.06),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Stim_resp = keyboard.Keyboard()
Stim_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Stim_sound')
Stim_sound.setVolume(1)
polystart_array=[0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]

# Initialize components for Routine "RTStim_ISI"
RTStim_ISIClock = core.Clock()
import random
StimISIarray=[2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Stim_post"
Stim_postClock = core.Clock()
Fix_post = visual.TextStim(win=win, name='Fix_post',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
if my_session==2:
    background_sound.play()

# Initialize components for Routine "RT_comp"
RT_compClock = core.Clock()
trial_fix = visual.TextStim(win=win, name='trial_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=50, size=(0.06, 0.06),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
RTvis_resp = keyboard.Keyboard()
RT_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='RT_sound')
RT_sound.setVolume(1)

# Initialize components for Routine "RT_ISI"
RT_ISIClock = core.Clock()
import random
ISIarray=[2.1, 2.2, 2.3, 2.4, 2.5] 
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Instr1Components = [text_2, key_resp]
for thisComponent in Instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr1"-------
while continueRoutine:
    # get current time
    t = Instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr1"-------
for thisComponent in Instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RT1_trials = data.TrialHandler(nReps=0, method='random', 
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
    
    # ------Prepare to start Routine "RT_comp"-------
    continueRoutine = True
    # update component parameters for each repeat
    polygon.setOpacity(VisOpacity)
    RTvis_resp.keys = []
    RTvis_resp.rt = []
    _RTvis_resp_allKeys = []
    RT_sound.setSound(SoundFileName, hamming=True)
    RT_sound.setVolume(1, log=False)
    # keep track of which components have finished
    RT_compComponents = [trial_fix, polygon, RTvis_resp, RT_sound]
    for thisComponent in RT_compComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RT_compClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RT_comp"-------
    while continueRoutine:
        # get current time
        t = RT_compClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RT_compClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_fix* updates
        if trial_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_fix.frameNStart = frameN  # exact frame index
            trial_fix.tStart = t  # local t and not account for scr refresh
            trial_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fix, 'tStartRefresh')  # time at next scr refresh
            trial_fix.setAutoDraw(True)
        if trial_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trial_fix.tStop = t  # not accounting for scr refresh
                trial_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_fix, 'tStopRefresh')  # time at next scr refresh
                trial_fix.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # *RTvis_resp* updates
        waitOnFlip = False
        if RTvis_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RTvis_resp.frameNStart = frameN  # exact frame index
            RTvis_resp.tStart = t  # local t and not account for scr refresh
            RTvis_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTvis_resp, 'tStartRefresh')  # time at next scr refresh
            RTvis_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RTvis_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RTvis_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RTvis_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RTvis_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                RTvis_resp.tStop = t  # not accounting for scr refresh
                RTvis_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTvis_resp, 'tStopRefresh')  # time at next scr refresh
                RTvis_resp.status = FINISHED
        if RTvis_resp.status == STARTED and not waitOnFlip:
            theseKeys = RTvis_resp.getKeys(keyList=['space'], waitRelease=False)
            _RTvis_resp_allKeys.extend(theseKeys)
            if len(_RTvis_resp_allKeys):
                RTvis_resp.keys = _RTvis_resp_allKeys[0].name  # just the first key pressed
                RTvis_resp.rt = _RTvis_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop RT_sound
        if RT_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RT_sound.frameNStart = frameN  # exact frame index
            RT_sound.tStart = t  # local t and not account for scr refresh
            RT_sound.tStartRefresh = tThisFlipGlobal  # on global time
            RT_sound.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RT_compComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RT_comp"-------
    for thisComponent in RT_compComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT1_trials.addData('trial_fix.started', trial_fix.tStartRefresh)
    RT1_trials.addData('trial_fix.stopped', trial_fix.tStopRefresh)
    RT1_trials.addData('polygon.started', polygon.tStartRefresh)
    RT1_trials.addData('polygon.stopped', polygon.tStopRefresh)
    # check responses
    if RTvis_resp.keys in ['', [], None]:  # No response was made
        RTvis_resp.keys = None
    RT1_trials.addData('RTvis_resp.keys',RTvis_resp.keys)
    if RTvis_resp.keys != None:  # we had a response
        RT1_trials.addData('RTvis_resp.rt', RTvis_resp.rt)
    RT1_trials.addData('RTvis_resp.started', RTvis_resp.tStartRefresh)
    RT1_trials.addData('RTvis_resp.stopped', RTvis_resp.tStopRefresh)
    RT_sound.stop()  # ensure sound has stopped at end of routine
    RT1_trials.addData('RT_sound.started', RT_sound.tStartRefresh)
    RT1_trials.addData('RT_sound.stopped', RT_sound.tStopRefresh)
    # the Routine "RT_comp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RT_ISI"-------
    continueRoutine = True
    # update component parameters for each repeat
    RTISI_dur=random.choice(ISIarray) 
    # keep track of which components have finished
    RT_ISIComponents = [text_3]
    for thisComponent in RT_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RT_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RT_ISI"-------
    while continueRoutine:
        # get current time
        t = RT_ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RT_ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + RTISI_dur-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RT_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RT_ISI"-------
    for thisComponent in RT_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT1_trials.addData('text_3.started', text_3.tStartRefresh)
    RT1_trials.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "RT_ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'RT1_trials'


# ------Prepare to start Routine "Instr2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instr2Components = [Instr_text, key_resp_3]
for thisComponent in Instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr2"-------
while continueRoutine:
    # get current time
    t = Instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_text* updates
    if Instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_text.frameNStart = frameN  # exact frame index
        Instr_text.tStart = t  # local t and not account for scr refresh
        Instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_text, 'tStartRefresh')  # time at next scr refresh
        Instr_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr2"-------
for thisComponent in Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_text.started', Instr_text.tStartRefresh)
thisExp.addData('Instr_text.stopped', Instr_text.tStopRefresh)
# the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stim_pre"-------
continueRoutine = True
# update component parameters for each repeat
background_sound.play()
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Stim_preComponents = [Fix_pre, key_resp_2]
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
while continueRoutine:
    # get current time
    t = Stim_preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stim_preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Fix_pre* updates
    if Fix_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fix_pre.frameNStart = frameN  # exact frame index
        Fix_pre.tStart = t  # local t and not account for scr refresh
        Fix_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fix_pre, 'tStartRefresh')  # time at next scr refresh
        Fix_pre.setAutoDraw(True)
    if Fix_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Fix_pre.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            Fix_pre.tStop = t  # not accounting for scr refresh
            Fix_pre.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fix_pre, 'tStopRefresh')  # time at next scr refresh
            Fix_pre.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
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
thisExp.addData('Fix_pre.started', Fix_pre.tStartRefresh)
thisExp.addData('Fix_pre.stopped', Fix_pre.tStopRefresh)
# the Routine "Stim_pre" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(ExpList, selection='1:10'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "RTStim"-------
    continueRoutine = True
    # update component parameters for each repeat
    Stim_resp.keys = []
    Stim_resp.rt = []
    _Stim_resp_allKeys = []
    Stim_sound.setSound(SoundFileName, hamming=True)
    Stim_sound.setVolume(1, log=False)
    stop_draw_pol=False
    polystart = random.choice(polystart_array)
    # keep track of which components have finished
    RTStimComponents = [text_6, polygon_2, Stim_resp, Stim_sound]
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
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2.3-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= polystart-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            if bool(stop_draw_pol):
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # *Stim_resp* updates
        waitOnFlip = False
        if Stim_resp.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            Stim_resp.frameNStart = frameN  # exact frame index
            Stim_resp.tStart = t  # local t and not account for scr refresh
            Stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim_resp, 'tStartRefresh')  # time at next scr refresh
            Stim_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Stim_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Stim_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Stim_resp.tStop = t  # not accounting for scr refresh
                Stim_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stim_resp, 'tStopRefresh')  # time at next scr refresh
                Stim_resp.status = FINISHED
        if Stim_resp.status == STARTED and not waitOnFlip:
            theseKeys = Stim_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _Stim_resp_allKeys.extend(theseKeys)
            if len(_Stim_resp_allKeys):
                Stim_resp.keys = _Stim_resp_allKeys[-1].name  # just the last key pressed
                Stim_resp.rt = _Stim_resp_allKeys[-1].rt
        # start/stop Stim_sound
        if Stim_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stim_sound.frameNStart = frameN  # exact frame index
            Stim_sound.tStart = t  # local t and not account for scr refresh
            Stim_sound.tStartRefresh = tThisFlipGlobal  # on global time
            Stim_sound.play(when=win)  # sync with win flip
        if t > 2:
            stop_draw_pol=True
            
        
        if Stim_resp.status == STARTED:
            if Stim_resp.keys=="space":
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
    trials.addData('text_6.started', text_6.tStartRefresh)
    trials.addData('text_6.stopped', text_6.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # check responses
    if Stim_resp.keys in ['', [], None]:  # No response was made
        Stim_resp.keys = None
    trials.addData('Stim_resp.keys',Stim_resp.keys)
    if Stim_resp.keys != None:  # we had a response
        trials.addData('Stim_resp.rt', Stim_resp.rt)
    trials.addData('Stim_resp.started', Stim_resp.tStartRefresh)
    trials.addData('Stim_resp.stopped', Stim_resp.tStopRefresh)
    Stim_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('Stim_sound.started', Stim_sound.tStartRefresh)
    trials.addData('Stim_sound.stopped', Stim_sound.tStopRefresh)
    # the Routine "RTStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RTStim_ISI"-------
    continueRoutine = True
    routineTimer.add(0.700000)
    # update component parameters for each repeat
    StimISI_dur=random.choice(StimISIarray)
    # keep track of which components have finished
    RTStim_ISIComponents = [text_5]
    for thisComponent in RTStim_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RTStim_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RTStim_ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RTStim_ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RTStim_ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RTStim_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RTStim_ISI"-------
    for thisComponent in RTStim_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Stim_post"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Stim_postComponents = [Fix_post, key_resp_4]
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
while continueRoutine:
    # get current time
    t = Stim_postClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stim_postClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Fix_post* updates
    if Fix_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fix_post.frameNStart = frameN  # exact frame index
        Fix_post.tStart = t  # local t and not account for scr refresh
        Fix_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fix_post, 'tStartRefresh')  # time at next scr refresh
        Fix_post.setAutoDraw(True)
    if Fix_post.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Fix_post.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            Fix_post.tStop = t  # not accounting for scr refresh
            Fix_post.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fix_post, 'tStopRefresh')  # time at next scr refresh
            Fix_post.setAutoDraw(False)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
thisExp.addData('Fix_post.started', Fix_post.tStartRefresh)
thisExp.addData('Fix_post.stopped', Fix_post.tStopRefresh)
background_sound.stop()
# the Routine "Stim_post" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # ------Prepare to start Routine "RT_comp"-------
    continueRoutine = True
    # update component parameters for each repeat
    polygon.setOpacity(VisOpacity)
    RTvis_resp.keys = []
    RTvis_resp.rt = []
    _RTvis_resp_allKeys = []
    RT_sound.setSound(SoundFileName, hamming=True)
    RT_sound.setVolume(1, log=False)
    # keep track of which components have finished
    RT_compComponents = [trial_fix, polygon, RTvis_resp, RT_sound]
    for thisComponent in RT_compComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RT_compClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RT_comp"-------
    while continueRoutine:
        # get current time
        t = RT_compClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RT_compClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_fix* updates
        if trial_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_fix.frameNStart = frameN  # exact frame index
            trial_fix.tStart = t  # local t and not account for scr refresh
            trial_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fix, 'tStartRefresh')  # time at next scr refresh
            trial_fix.setAutoDraw(True)
        if trial_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_fix.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                trial_fix.tStop = t  # not accounting for scr refresh
                trial_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_fix, 'tStopRefresh')  # time at next scr refresh
                trial_fix.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # *RTvis_resp* updates
        waitOnFlip = False
        if RTvis_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RTvis_resp.frameNStart = frameN  # exact frame index
            RTvis_resp.tStart = t  # local t and not account for scr refresh
            RTvis_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RTvis_resp, 'tStartRefresh')  # time at next scr refresh
            RTvis_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RTvis_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RTvis_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RTvis_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RTvis_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                RTvis_resp.tStop = t  # not accounting for scr refresh
                RTvis_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RTvis_resp, 'tStopRefresh')  # time at next scr refresh
                RTvis_resp.status = FINISHED
        if RTvis_resp.status == STARTED and not waitOnFlip:
            theseKeys = RTvis_resp.getKeys(keyList=['space'], waitRelease=False)
            _RTvis_resp_allKeys.extend(theseKeys)
            if len(_RTvis_resp_allKeys):
                RTvis_resp.keys = _RTvis_resp_allKeys[0].name  # just the first key pressed
                RTvis_resp.rt = _RTvis_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop RT_sound
        if RT_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RT_sound.frameNStart = frameN  # exact frame index
            RT_sound.tStart = t  # local t and not account for scr refresh
            RT_sound.tStartRefresh = tThisFlipGlobal  # on global time
            RT_sound.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RT_compComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RT_comp"-------
    for thisComponent in RT_compComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT2_trials.addData('trial_fix.started', trial_fix.tStartRefresh)
    RT2_trials.addData('trial_fix.stopped', trial_fix.tStopRefresh)
    RT2_trials.addData('polygon.started', polygon.tStartRefresh)
    RT2_trials.addData('polygon.stopped', polygon.tStopRefresh)
    # check responses
    if RTvis_resp.keys in ['', [], None]:  # No response was made
        RTvis_resp.keys = None
    RT2_trials.addData('RTvis_resp.keys',RTvis_resp.keys)
    if RTvis_resp.keys != None:  # we had a response
        RT2_trials.addData('RTvis_resp.rt', RTvis_resp.rt)
    RT2_trials.addData('RTvis_resp.started', RTvis_resp.tStartRefresh)
    RT2_trials.addData('RTvis_resp.stopped', RTvis_resp.tStopRefresh)
    RT_sound.stop()  # ensure sound has stopped at end of routine
    RT2_trials.addData('RT_sound.started', RT_sound.tStartRefresh)
    RT2_trials.addData('RT_sound.stopped', RT_sound.tStopRefresh)
    # the Routine "RT_comp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RT_ISI"-------
    continueRoutine = True
    # update component parameters for each repeat
    RTISI_dur=random.choice(ISIarray) 
    # keep track of which components have finished
    RT_ISIComponents = [text_3]
    for thisComponent in RT_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RT_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RT_ISI"-------
    while continueRoutine:
        # get current time
        t = RT_ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RT_ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + RTISI_dur-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RT_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RT_ISI"-------
    for thisComponent in RT_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RT2_trials.addData('text_3.started', text_3.tStartRefresh)
    RT2_trials.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "RT_ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'RT2_trials'


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
