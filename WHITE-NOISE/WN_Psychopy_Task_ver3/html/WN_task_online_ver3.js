/**************************** 
 * Wn_Task_Online_Ver3 Test *
 ****************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'WN_task_online_ver3';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(set_sessionRoutineBegin());
flowScheduler.add(set_sessionRoutineEachFrame());
flowScheduler.add(set_sessionRoutineEnd());
flowScheduler.add(Instr_StaircaseRoutineBegin());
flowScheduler.add(Instr_StaircaseRoutineEachFrame());
flowScheduler.add(Instr_StaircaseRoutineEnd());
const hear_staircase_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(hear_staircase_loopLoopBegin, hear_staircase_loopLoopScheduler);
flowScheduler.add(hear_staircase_loopLoopScheduler);
flowScheduler.add(hear_staircase_loopLoopEnd);
flowScheduler.add(set_sound_volumeRoutineBegin());
flowScheduler.add(set_sound_volumeRoutineEachFrame());
flowScheduler.add(set_sound_volumeRoutineEnd());
flowScheduler.add(Instr_expRoutineBegin());
flowScheduler.add(Instr_expRoutineEachFrame());
flowScheduler.add(Instr_expRoutineEnd());
const RT1_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RT1_trialsLoopBegin, RT1_trialsLoopScheduler);
flowScheduler.add(RT1_trialsLoopScheduler);
flowScheduler.add(RT1_trialsLoopEnd);
flowScheduler.add(Instr_stim_preRoutineBegin());
flowScheduler.add(Instr_stim_preRoutineEachFrame());
flowScheduler.add(Instr_stim_preRoutineEnd());
flowScheduler.add(Stim_preRoutineBegin());
flowScheduler.add(Stim_preRoutineEachFrame());
flowScheduler.add(Stim_preRoutineEnd());
const Stim_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Stim_trialsLoopBegin, Stim_trialsLoopScheduler);
flowScheduler.add(Stim_trialsLoopScheduler);
flowScheduler.add(Stim_trialsLoopEnd);
flowScheduler.add(Stim_postRoutineBegin());
flowScheduler.add(Stim_postRoutineEachFrame());
flowScheduler.add(Stim_postRoutineEnd());
flowScheduler.add(Instr_comp2RoutineBegin());
flowScheduler.add(Instr_comp2RoutineEachFrame());
flowScheduler.add(Instr_comp2RoutineEnd());
const RT2_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(RT2_trialsLoopBegin, RT2_trialsLoopScheduler);
flowScheduler.add(RT2_trialsLoopScheduler);
flowScheduler.add(RT2_trialsLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var set_sessionClock;
var session_nr;
var subject_nr;
var counterb_list;
var tot_levels;
var k;
var my_session;
var ExpList;
var Instr_StaircaseClock;
var Instr_staircase_txt;
var key_resp_5;
var Instr_staircaseClock;
var hear_sc_fix;
var stair_sound;
var hear_sc_resp;
var ini_volume;
var curr_volume;
var last_response;
var tot_sc_trials;
var volumes_array;
var hear_sc_ntrial;
var hc_instr1;
var hc_instr2;
var set_sound_volumeClock;
var Instr_expClock;
var Instr_comp1_txt;
var Instr_task_key;
var RTcompClock;
var RTcomp_fix;
var RTcomp_poly;
var RTcomp_resp;
var RTcomp_sound;
var Instr_stim_preClock;
var Instr_stim_pre_txt;
var Instr_stim_pre_resp;
var Stim_preClock;
var PreStim_fix;
var background_sound_pre;
var PreStim_key;
var RTStimClock;
var RTstim_fix;
var RTStim_poly;
var RTStim_resp;
var polystart_array;
var Stim_postClock;
var PostStim_fix;
var PostStim_key;
var Instr_comp2Clock;
var Instr_comp2_txt;
var Instr_comp2_key;
var EndClock;
var End_txt;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "set_session"
  set_sessionClock = new util.Clock();
  var ExpList, counterb_list, k, my_session, session_nr, subject_nr, tot_levels;
  session_nr = Number.parseInt(expInfo["session"]);
  subject_nr = Number.parseInt(expInfo["participant"]);
  counterb_list = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]];
  tot_levels = counterb_list.length;
  k = ((subject_nr - (tot_levels * Math.floor((subject_nr / tot_levels)))) - 1);
  my_session = counterb_list[k][(session_nr - 1)];
  if ((my_session === 1)) {
      ExpList = "WN_RTblock1_ExpList.xlsx";
  }
  if ((my_session === 2)) {
      ExpList = "WN_RTblock2_ExpList.xlsx";
  }
  if ((my_session === 3)) {
      ExpList = "WN_RTblock3_ExpList.xlsx";
  }
  // Initialize components for Routine "Instr_Staircase"
  Instr_StaircaseClock = new util.Clock();
  Instr_staircase_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instr_staircase_txt',
    text: 'Benvenuto!\n\nIn questo esperimento dovrai ascoltare alcuni suoni ed effettuare alcuni compiti.\nCome prima cosa ti chiediamo di impostare il volume del tuo computer al massimo.\nCi sarà una breve sessione in cui ti chiederemo di premere i tasti "freccia su" e "freccia giù" \nin base a delle istruzioni sullo schermo.\n\nPremi il tasto "c" per continuare',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instr_staircase"
  Instr_staircaseClock = new util.Clock();
  hear_sc_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'hear_sc_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  stair_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'sound_cue.wav',
    secs: (- 1),
    });
  stair_sound.setVolume(1.0);
  hear_sc_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ini_volume = 0.2;
  curr_volume = ini_volume;
  last_response = "up";
  tot_sc_trials = 100;
  volumes_array = new Array(tot_sc_trials);
  hear_sc_ntrial = 1;
  
  hc_instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'hc_instr1',
    text: 'Premi "freccia giù" se hai sentito il suono ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  hc_instr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'hc_instr2',
    text: 'Premi "freccia su" se non hai sentito il suono',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "set_sound_volume"
  set_sound_volumeClock = new util.Clock();
  // Initialize components for Routine "Instr_exp"
  Instr_expClock = new util.Clock();
  Instr_comp1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instr_comp1_txt',
    text: 'Adesso comincerà il compito vero e proprio.\nSiediti normalmente al computer come se dovessi scrivere.\nVedrai al centro dello schermo una croce nera. \nTieni lo sguardo sulla croce. \nA intervalli casuali comparirà un cerchio rosso oppure potrai sentire un breve suono. \nIn entrambi i casi dovrai rispondere premendo la Barra Spaziatrice il più velocemente possibile appena uno dei due stimoli (cerchio o suono) comparirà. \n\nTerminato questo compito riceverai ulteriori istruzioni. \n\nPremi il tasto "c" per continuare.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  Instr_task_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RTcomp"
  RTcompClock = new util.Clock();
  RTcomp_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'RTcomp_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  RTcomp_poly = new visual.Polygon ({
    win: psychoJS.window, name: 'RTcomp_poly', 
    edges: 50, size:[0.09, 0.09],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 0, 0]),
    fillColor: new util.Color([1, 0, 0]),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  RTcomp_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  RTcomp_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  RTcomp_sound.setVolume(1.0);
  // Initialize components for Routine "Instr_stim_pre"
  Instr_stim_preClock = new util.Clock();
  Instr_stim_pre_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instr_stim_pre_txt',
    text: 'Ben fatto! \nOra vedrai di nuovo la croce nera. \nTieni lo sguardo sulla croce e rilassati. \nSentirai una traccia audio in sottofondo per qualche minuto ma non dovrai fare nulla. \nAd un certo punto vedrai ricomparire il cerchio rosso. \nOgni volta che comparirà, dovrai premere la Barra Spaziatrice il più velocemente possibile, come nel task precedente. \n\nQuando il cerchio smetterà di comparire, dovrai rilassarti e continuare ad ascoltare la traccia audio, per qualche minuto. \nTerminata quella sessione ti daremo nuove istruzioni\n\nPremi il tasto "c" per continuare.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  Instr_stim_pre_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Stim_pre"
  Stim_preClock = new util.Clock();
  PreStim_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'PreStim_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  if (my_session == 1){
  background_sound_pre = new sound.Sound({     win: psychoJS.window,     value: 'white_noise_bg.wav',     secs: -1,     });
  }
  
  if (my_session == 2){
  background_sound_pre = new sound.Sound({     win: psychoJS.window,     value: 'white_int_noise_bg2.wav',     secs: -1,     });
  }
  
  if (my_session == 3){
  background_sound_pre = new sound.Sound({     win: psychoJS.window,     value: 'pink_noise_bg.wav',     secs: -1,     });
  }
  PreStim_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RTStim"
  RTStimClock = new util.Clock();
  RTstim_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'RTstim_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  RTStim_poly = new visual.Polygon ({
    win: psychoJS.window, name: 'RTStim_poly', 
    edges: 50, size:[0.09, 0.09],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 0, 0]),
    fillColor: new util.Color([1, 0, 0]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  RTStim_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  polystart_array = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7];
  
  // Initialize components for Routine "Stim_post"
  Stim_postClock = new util.Clock();
  PostStim_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'PostStim_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  PostStim_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instr_comp2"
  Instr_comp2Clock = new util.Clock();
  Instr_comp2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instr_comp2_txt',
    text: 'Quasi finito! \nOra dovrai rifare lo stesso task che hai completato per primo: cerchio e suono compariranno ad intervalli casuali. \nRispondi il più veloce possibile con la Barra Spaziatrice. \n\nPremi il tasto "c" per continuare.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  Instr_comp2_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "RTcomp"
  RTcompClock = new util.Clock();
  RTcomp_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'RTcomp_fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  RTcomp_poly = new visual.Polygon ({
    win: psychoJS.window, name: 'RTcomp_poly', 
    edges: 50, size:[0.09, 0.09],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 0, 0]),
    fillColor: new util.Color([1, 0, 0]),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  RTcomp_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  RTcomp_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  RTcomp_sound.setVolume(1.0);
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  End_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'End_txt',
    text: 'Grazie della partecipazione!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var set_sessionComponents;
function set_sessionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'set_session'-------
    t = 0;
    set_sessionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    set_sessionComponents = [];
    
    for (const thisComponent of set_sessionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function set_sessionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'set_session'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = set_sessionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of set_sessionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function set_sessionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'set_session'-------
    for (const thisComponent of set_sessionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "set_session" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var Instr_StaircaseComponents;
function Instr_StaircaseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instr_Staircase'-------
    t = 0;
    Instr_StaircaseClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    Instr_StaircaseComponents = [];
    Instr_StaircaseComponents.push(Instr_staircase_txt);
    Instr_StaircaseComponents.push(key_resp_5);
    
    for (const thisComponent of Instr_StaircaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Instr_StaircaseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instr_Staircase'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr_StaircaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instr_staircase_txt* updates
    if (t >= 0.0 && Instr_staircase_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_staircase_txt.tStart = t;  // (not accounting for frame time here)
      Instr_staircase_txt.frameNStart = frameN;  // exact frame index
      
      Instr_staircase_txt.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['c'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_StaircaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr_StaircaseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instr_Staircase'-------
    for (const thisComponent of Instr_StaircaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Instr_Staircase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var hear_staircase_loop;
var currentLoop;
function hear_staircase_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  hear_staircase_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: tot_sc_trials, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'hear_staircase_loop'
  });
  psychoJS.experiment.addLoop(hear_staircase_loop); // add the loop to the experiment
  currentLoop = hear_staircase_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisHear_staircase_loop of hear_staircase_loop) {
    const snapshot = hear_staircase_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(Instr_staircaseRoutineBegin(snapshot));
    thisScheduler.add(Instr_staircaseRoutineEachFrame(snapshot));
    thisScheduler.add(Instr_staircaseRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function hear_staircase_loopLoopEnd() {
  psychoJS.experiment.removeLoop(hear_staircase_loop);

  return Scheduler.Event.NEXT;
}


var RT1_trials;
function RT1_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  RT1_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'WN_RT_ExpList.xlsx',
    seed: undefined, name: 'RT1_trials'
  });
  psychoJS.experiment.addLoop(RT1_trials); // add the loop to the experiment
  currentLoop = RT1_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisRT1_trial of RT1_trials) {
    const snapshot = RT1_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(RTcompRoutineBegin(snapshot));
    thisScheduler.add(RTcompRoutineEachFrame(snapshot));
    thisScheduler.add(RTcompRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function RT1_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(RT1_trials);

  return Scheduler.Event.NEXT;
}


var Stim_trials;
function Stim_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Stim_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'WN_RTblock1_ExpList.xlsx',
    seed: undefined, name: 'Stim_trials'
  });
  psychoJS.experiment.addLoop(Stim_trials); // add the loop to the experiment
  currentLoop = Stim_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisStim_trial of Stim_trials) {
    const snapshot = Stim_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(RTStimRoutineBegin(snapshot));
    thisScheduler.add(RTStimRoutineEachFrame(snapshot));
    thisScheduler.add(RTStimRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function Stim_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(Stim_trials);

  return Scheduler.Event.NEXT;
}


var RT2_trials;
function RT2_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  RT2_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'WN_RT_ExpList.xlsx',
    seed: undefined, name: 'RT2_trials'
  });
  psychoJS.experiment.addLoop(RT2_trials); // add the loop to the experiment
  currentLoop = RT2_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisRT2_trial of RT2_trials) {
    const snapshot = RT2_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(RTcompRoutineBegin(snapshot));
    thisScheduler.add(RTcompRoutineEachFrame(snapshot));
    thisScheduler.add(RTcompRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function RT2_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(RT2_trials);

  return Scheduler.Event.NEXT;
}


var _hear_sc_resp_allKeys;
var Instr_staircaseComponents;
function Instr_staircaseRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instr_staircase'-------
    t = 0;
    Instr_staircaseClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    stair_sound.setVolume(curr_volume);
    hear_sc_resp.keys = undefined;
    hear_sc_resp.rt = undefined;
    _hear_sc_resp_allKeys = [];
    // keep track of which components have finished
    Instr_staircaseComponents = [];
    Instr_staircaseComponents.push(hear_sc_fix);
    Instr_staircaseComponents.push(stair_sound);
    Instr_staircaseComponents.push(hear_sc_resp);
    Instr_staircaseComponents.push(hc_instr1);
    Instr_staircaseComponents.push(hc_instr2);
    
    for (const thisComponent of Instr_staircaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Instr_staircaseRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instr_staircase'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr_staircaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *hear_sc_fix* updates
    if (t >= 0.2 && hear_sc_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hear_sc_fix.tStart = t;  // (not accounting for frame time here)
      hear_sc_fix.frameNStart = frameN;  // exact frame index
      
      hear_sc_fix.setAutoDraw(true);
    }

    // start/stop stair_sound
    if (t >= 0.2 && stair_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stair_sound.tStart = t;  // (not accounting for frame time here)
      stair_sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stair_sound.play(); });  // screen flip
      stair_sound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stair_sound.getDuration() + stair_sound.tStart)     && stair_sound.status === PsychoJS.Status.STARTED) {
      stair_sound.stop();  // stop the sound (if longer than duration)
      stair_sound.status = PsychoJS.Status.FINISHED;
    }
    
    // *hear_sc_resp* updates
    if (t >= 0.0 && hear_sc_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hear_sc_resp.tStart = t;  // (not accounting for frame time here)
      hear_sc_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { hear_sc_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { hear_sc_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { hear_sc_resp.clearEvents(); });
    }

    if (hear_sc_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = hear_sc_resp.getKeys({keyList: ['up', 'down'], waitRelease: false});
      _hear_sc_resp_allKeys = _hear_sc_resp_allKeys.concat(theseKeys);
      if (_hear_sc_resp_allKeys.length > 0) {
        hear_sc_resp.keys = _hear_sc_resp_allKeys[0].name;  // just the first key pressed
        hear_sc_resp.rt = _hear_sc_resp_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *hc_instr1* updates
    if (t >= 0 && hc_instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hc_instr1.tStart = t;  // (not accounting for frame time here)
      hc_instr1.frameNStart = frameN;  // exact frame index
      
      hc_instr1.setAutoDraw(true);
    }

    
    // *hc_instr2* updates
    if (t >= 0 && hc_instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hc_instr2.tStart = t;  // (not accounting for frame time here)
      hc_instr2.frameNStart = frameN;  // exact frame index
      
      hc_instr2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_staircaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var curr_response;
var vol_ind;
function Instr_staircaseRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instr_staircase'-------
    for (const thisComponent of Instr_staircaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stair_sound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('hear_sc_resp.keys', hear_sc_resp.keys);
    if (typeof hear_sc_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('hear_sc_resp.rt', hear_sc_resp.rt);
        routineTimer.reset();
        }
    
    hear_sc_resp.stop();
    curr_response = hear_sc_resp.keys;
    vol_ind = (hear_sc_ntrial - 1);
    volumes_array[vol_ind] = curr_volume;
    if ((curr_response === "up")) {
        curr_volume = (curr_volume + (curr_volume * 0.25));
    }
    if ((curr_response === "down")) {
        curr_volume = (curr_volume - (curr_volume * 0.25));
    }
    if (((curr_response !== last_response) && (hear_sc_ntrial !== 1))) {
        curr_volume = ini_volume;
    }
    last_response = curr_response;
    hear_sc_ntrial = (hear_sc_ntrial + 1);
    
    // the Routine "Instr_staircase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var set_sound_volumeComponents;
function set_sound_volumeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'set_sound_volume'-------
    t = 0;
    set_sound_volumeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    set_sound_volumeComponents = [];
    
    for (const thisComponent of set_sound_volumeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function set_sound_volumeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'set_sound_volume'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = set_sound_volumeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of set_sound_volumeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var max_vol;
var min_vol;
var sound_vol;
function set_sound_volumeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'set_sound_volume'-------
    for (const thisComponent of set_sound_volumeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    max_vol = Math.max.apply(Math, volumes_array)
    min_vol = Math.min.apply(Math, volumes_array)
    sound_vol = ((max_vol - min_vol) / 3);
    
    psychoJS.experiment.addData("Final_Volume", sound_vol)
    // the Routine "set_sound_volume" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Instr_task_key_allKeys;
var curr_block;
var Instr_expComponents;
function Instr_expRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instr_exp'-------
    t = 0;
    Instr_expClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    Instr_task_key.keys = undefined;
    Instr_task_key.rt = undefined;
    _Instr_task_key_allKeys = [];
    curr_block = "PreStim";
    
    // keep track of which components have finished
    Instr_expComponents = [];
    Instr_expComponents.push(Instr_comp1_txt);
    Instr_expComponents.push(Instr_task_key);
    
    for (const thisComponent of Instr_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Instr_expRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instr_exp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instr_comp1_txt* updates
    if (t >= 0.0 && Instr_comp1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_comp1_txt.tStart = t;  // (not accounting for frame time here)
      Instr_comp1_txt.frameNStart = frameN;  // exact frame index
      
      Instr_comp1_txt.setAutoDraw(true);
    }

    
    // *Instr_task_key* updates
    if (t >= 0.0 && Instr_task_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_task_key.tStart = t;  // (not accounting for frame time here)
      Instr_task_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instr_task_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instr_task_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instr_task_key.clearEvents(); });
    }

    if (Instr_task_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instr_task_key.getKeys({keyList: ['c'], waitRelease: false});
      _Instr_task_key_allKeys = _Instr_task_key_allKeys.concat(theseKeys);
      if (_Instr_task_key_allKeys.length > 0) {
        Instr_task_key.keys = _Instr_task_key_allKeys[_Instr_task_key_allKeys.length - 1].name;  // just the last key pressed
        Instr_task_key.rt = _Instr_task_key_allKeys[_Instr_task_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_expComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr_expRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instr_exp'-------
    for (const thisComponent of Instr_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Instr_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _RTcomp_resp_allKeys;
var stimstart_temp;
var stimstart;
var stop_draw_stim;
var ISI_temp;
var RTISI_dur;
var RTcompComponents;
function RTcompRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'RTcomp'-------
    t = 0;
    RTcompClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    RTcomp_poly.setOpacity(VisOpacity);
    RTcomp_resp.keys = undefined;
    RTcomp_resp.rt = undefined;
    _RTcomp_resp_allKeys = [];
    RTcomp_sound = new sound.Sound({
    win: psychoJS.window,
    value: SoundFileName,
    secs: -1,
    });
    RTcomp_sound.setVolume(sound_vol);
    function getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    }
    
    stimstart_temp = getRandomInt(300, 700)
    stimstart = stimstart_temp/1000
    
    stop_draw_stim = false;
    
    function getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    }
    
    ISI_temp = getRandomInt(1500, 2500)
    RTISI_dur = ISI_temp/1000
    
    // keep track of which components have finished
    RTcompComponents = [];
    RTcompComponents.push(RTcomp_fix);
    RTcompComponents.push(RTcomp_poly);
    RTcompComponents.push(RTcomp_resp);
    RTcompComponents.push(RTcomp_sound);
    
    for (const thisComponent of RTcompComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function RTcompRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'RTcomp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = RTcompClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RTcomp_fix* updates
    if (t >= 0.0 && RTcomp_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTcomp_fix.tStart = t;  // (not accounting for frame time here)
      RTcomp_fix.frameNStart = frameN;  // exact frame index
      
      RTcomp_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RTcomp_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RTcomp_fix.setAutoDraw(false);
    }
    
    // *RTcomp_poly* updates
    if (t >= stimstart && RTcomp_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTcomp_poly.tStart = t;  // (not accounting for frame time here)
      RTcomp_poly.frameNStart = frameN;  // exact frame index
      
      RTcomp_poly.setAutoDraw(true);
    }

    if (RTcomp_poly.status === PsychoJS.Status.STARTED && Boolean(stop_draw_stim)) {
      RTcomp_poly.setAutoDraw(false);
    }
    
    // *RTcomp_resp* updates
    if (t >= 0 && RTcomp_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTcomp_resp.tStart = t;  // (not accounting for frame time here)
      RTcomp_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { RTcomp_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { RTcomp_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { RTcomp_resp.clearEvents(); });
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RTcomp_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RTcomp_resp.status = PsychoJS.Status.FINISHED;
  }

    if (RTcomp_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = RTcomp_resp.getKeys({keyList: ['space'], waitRelease: false});
      _RTcomp_resp_allKeys = _RTcomp_resp_allKeys.concat(theseKeys);
      if (_RTcomp_resp_allKeys.length > 0) {
        RTcomp_resp.keys = _RTcomp_resp_allKeys[0].name;  // just the first key pressed
        RTcomp_resp.rt = _RTcomp_resp_allKeys[0].rt;
      }
    }
    
    // start/stop RTcomp_sound
    if (t >= stimstart && RTcomp_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTcomp_sound.tStart = t;  // (not accounting for frame time here)
      RTcomp_sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ RTcomp_sound.play(); });  // screen flip
      RTcomp_sound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (RTcomp_sound.getDuration() + RTcomp_sound.tStart)     && RTcomp_sound.status === PsychoJS.Status.STARTED) {
      RTcomp_sound.stop();  // stop the sound (if longer than duration)
      RTcomp_sound.status = PsychoJS.Status.FINISHED;
    }
    if ((t > (stimstart + 1))) {
        stop_draw_stim = true;
    }
    if ((RTcomp_resp.status === PsychoJS.Status.STARTED)) {
        if ((RTcomp_resp.keys === "space")) {
            stop_draw_stim = true;
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RTcompComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RTcompRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'RTcomp'-------
    for (const thisComponent of RTcompComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RTcomp_resp.keys', RTcomp_resp.keys);
    if (typeof RTcomp_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('RTcomp_resp.rt', RTcomp_resp.rt);
        }
    
    RTcomp_resp.stop();
    RTcomp_sound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData("block", curr_block);
    psychoJS.experiment.addData("stimstart", stimstart);
    
    // the Routine "RTcomp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Instr_stim_pre_resp_allKeys;
var Instr_stim_preComponents;
function Instr_stim_preRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instr_stim_pre'-------
    t = 0;
    Instr_stim_preClock.reset(); // clock
    frameN = -1;
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    Instr_stim_pre_resp.keys = undefined;
    Instr_stim_pre_resp.rt = undefined;
    _Instr_stim_pre_resp_allKeys = [];
    // keep track of which components have finished
    Instr_stim_preComponents = [];
    Instr_stim_preComponents.push(Instr_stim_pre_txt);
    Instr_stim_preComponents.push(Instr_stim_pre_resp);
    
    for (const thisComponent of Instr_stim_preComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Instr_stim_preRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instr_stim_pre'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr_stim_preClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instr_stim_pre_txt* updates
    if (t >= 0.0 && Instr_stim_pre_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_stim_pre_txt.tStart = t;  // (not accounting for frame time here)
      Instr_stim_pre_txt.frameNStart = frameN;  // exact frame index
      
      Instr_stim_pre_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instr_stim_pre_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instr_stim_pre_txt.setAutoDraw(false);
    }
    
    // *Instr_stim_pre_resp* updates
    if (t >= 0.0 && Instr_stim_pre_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_stim_pre_resp.tStart = t;  // (not accounting for frame time here)
      Instr_stim_pre_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instr_stim_pre_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instr_stim_pre_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instr_stim_pre_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instr_stim_pre_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instr_stim_pre_resp.status = PsychoJS.Status.FINISHED;
  }

    if (Instr_stim_pre_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instr_stim_pre_resp.getKeys({keyList: ['c'], waitRelease: false});
      _Instr_stim_pre_resp_allKeys = _Instr_stim_pre_resp_allKeys.concat(theseKeys);
      if (_Instr_stim_pre_resp_allKeys.length > 0) {
        Instr_stim_pre_resp.keys = _Instr_stim_pre_resp_allKeys[_Instr_stim_pre_resp_allKeys.length - 1].name;  // just the last key pressed
        Instr_stim_pre_resp.rt = _Instr_stim_pre_resp_allKeys[_Instr_stim_pre_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_stim_preComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr_stim_preRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instr_stim_pre'-------
    for (const thisComponent of Instr_stim_preComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _PreStim_key_allKeys;
var Stim_preComponents;
function Stim_preRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Stim_pre'-------
    t = 0;
    Stim_preClock.reset(); // clock
    frameN = -1;
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    background_sound_pre.setVolume(sound_vol);
    background_sound_pre.play();
    
    PreStim_key.keys = undefined;
    PreStim_key.rt = undefined;
    _PreStim_key_allKeys = [];
    // keep track of which components have finished
    Stim_preComponents = [];
    Stim_preComponents.push(PreStim_fix);
    Stim_preComponents.push(PreStim_key);
    
    for (const thisComponent of Stim_preComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Stim_preRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Stim_pre'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Stim_preClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PreStim_fix* updates
    if (t >= 0.0 && PreStim_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreStim_fix.tStart = t;  // (not accounting for frame time here)
      PreStim_fix.frameNStart = frameN;  // exact frame index
      
      PreStim_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PreStim_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PreStim_fix.setAutoDraw(false);
    }
    
    // *PreStim_key* updates
    if (t >= 0.0 && PreStim_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PreStim_key.tStart = t;  // (not accounting for frame time here)
      PreStim_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PreStim_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PreStim_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PreStim_key.clearEvents(); });
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PreStim_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PreStim_key.status = PsychoJS.Status.FINISHED;
  }

    if (PreStim_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = PreStim_key.getKeys({keyList: ['q'], waitRelease: false});
      _PreStim_key_allKeys = _PreStim_key_allKeys.concat(theseKeys);
      if (_PreStim_key_allKeys.length > 0) {
        PreStim_key.keys = _PreStim_key_allKeys[_PreStim_key_allKeys.length - 1].name;  // just the last key pressed
        PreStim_key.rt = _PreStim_key_allKeys[_PreStim_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Stim_preComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Stim_preRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Stim_pre'-------
    for (const thisComponent of Stim_preComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    /*
    if my_session==2:
    background_sound_pre.stop()
    */
    
    return Scheduler.Event.NEXT;
  };
}


var _RTStim_resp_allKeys;
var polystart_temp;
var polystart;
var stop_draw_pol;
var StimISI_dur;
var RTStimComponents;
function RTStimRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'RTStim'-------
    t = 0;
    RTStimClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    RTStim_resp.keys = undefined;
    RTStim_resp.rt = undefined;
    _RTStim_resp_allKeys = [];
    function getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    }
    
    polystart_temp = getRandomInt(300, 700)
    polystart = polystart_temp/1000
    
    stop_draw_pol = false;
    
    function getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
    }
    
    ISI_temp = getRandomInt(1500, 2500)
    StimISI_dur = ISI_temp/1000
    
    // keep track of which components have finished
    RTStimComponents = [];
    RTStimComponents.push(RTstim_fix);
    RTStimComponents.push(RTStim_poly);
    RTStimComponents.push(RTStim_resp);
    
    for (const thisComponent of RTStimComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function RTStimRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'RTStim'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = RTStimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RTstim_fix* updates
    if (t >= 0.0 && RTstim_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTstim_fix.tStart = t;  // (not accounting for frame time here)
      RTstim_fix.frameNStart = frameN;  // exact frame index
      
      RTstim_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RTstim_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RTstim_fix.setAutoDraw(false);
    }
    
    // *RTStim_poly* updates
    if (t >= polystart && RTStim_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTStim_poly.tStart = t;  // (not accounting for frame time here)
      RTStim_poly.frameNStart = frameN;  // exact frame index
      
      RTStim_poly.setAutoDraw(true);
    }

    if (RTStim_poly.status === PsychoJS.Status.STARTED && Boolean(stop_draw_pol)) {
      RTStim_poly.setAutoDraw(false);
    }
    
    // *RTStim_resp* updates
    if (t >= 0 && RTStim_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RTStim_resp.tStart = t;  // (not accounting for frame time here)
      RTStim_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { RTStim_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { RTStim_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { RTStim_resp.clearEvents(); });
    }

    frameRemains = 2  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RTStim_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RTStim_resp.status = PsychoJS.Status.FINISHED;
  }

    if (RTStim_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = RTStim_resp.getKeys({keyList: ['space'], waitRelease: false});
      _RTStim_resp_allKeys = _RTStim_resp_allKeys.concat(theseKeys);
      if (_RTStim_resp_allKeys.length > 0) {
        RTStim_resp.keys = _RTStim_resp_allKeys[0].name;  // just the first key pressed
        RTStim_resp.rt = _RTStim_resp_allKeys[0].rt;
      }
    }
    
    if ((t > (polystart + 1))) {
        stop_draw_pol = true;
    }
    if ((RTStim_resp.status === PsychoJS.Status.STARTED)) {
        if ((RTStim_resp.keys === "space")) {
            stop_draw_pol = true;
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RTStimComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RTStimRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'RTStim'-------
    for (const thisComponent of RTStimComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RTStim_resp.keys', RTStim_resp.keys);
    if (typeof RTStim_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('RTStim_resp.rt', RTStim_resp.rt);
        }
    
    RTStim_resp.stop();
    psychoJS.experiment.addData("block", "DuringStim")
    psychoJS.experiment.addData("stimstart", polystart)
    
    // the Routine "RTStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _PostStim_key_allKeys;
var Stim_postComponents;
function Stim_postRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Stim_post'-------
    t = 0;
    Stim_postClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    PostStim_key.keys = undefined;
    PostStim_key.rt = undefined;
    _PostStim_key_allKeys = [];
    // keep track of which components have finished
    Stim_postComponents = [];
    Stim_postComponents.push(PostStim_fix);
    Stim_postComponents.push(PostStim_key);
    
    for (const thisComponent of Stim_postComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Stim_postRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Stim_post'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Stim_postClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PostStim_fix* updates
    if (t >= 0.0 && PostStim_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PostStim_fix.tStart = t;  // (not accounting for frame time here)
      PostStim_fix.frameNStart = frameN;  // exact frame index
      
      PostStim_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PostStim_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PostStim_fix.setAutoDraw(false);
    }
    
    // *PostStim_key* updates
    if (t >= 0.0 && PostStim_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PostStim_key.tStart = t;  // (not accounting for frame time here)
      PostStim_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PostStim_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PostStim_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PostStim_key.clearEvents(); });
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PostStim_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PostStim_key.status = PsychoJS.Status.FINISHED;
  }

    if (PostStim_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = PostStim_key.getKeys({keyList: ['q'], waitRelease: false});
      _PostStim_key_allKeys = _PostStim_key_allKeys.concat(theseKeys);
      if (_PostStim_key_allKeys.length > 0) {
        PostStim_key.keys = _PostStim_key_allKeys[_PostStim_key_allKeys.length - 1].name;  // just the last key pressed
        PostStim_key.rt = _PostStim_key_allKeys[_PostStim_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Stim_postComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Stim_postRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Stim_post'-------
    for (const thisComponent of Stim_postComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    background_sound_pre.stop();
    
    return Scheduler.Event.NEXT;
  };
}


var _Instr_comp2_key_allKeys;
var Instr_comp2Components;
function Instr_comp2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Instr_comp2'-------
    t = 0;
    Instr_comp2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(60.000000);
    // update component parameters for each repeat
    Instr_comp2_key.keys = undefined;
    Instr_comp2_key.rt = undefined;
    _Instr_comp2_key_allKeys = [];
    curr_block = "PostStim";
    
    // keep track of which components have finished
    Instr_comp2Components = [];
    Instr_comp2Components.push(Instr_comp2_txt);
    Instr_comp2Components.push(Instr_comp2_key);
    
    for (const thisComponent of Instr_comp2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Instr_comp2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Instr_comp2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr_comp2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instr_comp2_txt* updates
    if (t >= 0.0 && Instr_comp2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_comp2_txt.tStart = t;  // (not accounting for frame time here)
      Instr_comp2_txt.frameNStart = frameN;  // exact frame index
      
      Instr_comp2_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instr_comp2_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instr_comp2_txt.setAutoDraw(false);
    }
    
    // *Instr_comp2_key* updates
    if (t >= 0.0 && Instr_comp2_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr_comp2_key.tStart = t;  // (not accounting for frame time here)
      Instr_comp2_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Instr_comp2_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Instr_comp2_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Instr_comp2_key.clearEvents(); });
    }

    frameRemains = 0.0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instr_comp2_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instr_comp2_key.status = PsychoJS.Status.FINISHED;
  }

    if (Instr_comp2_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = Instr_comp2_key.getKeys({keyList: ['c'], waitRelease: false});
      _Instr_comp2_key_allKeys = _Instr_comp2_key_allKeys.concat(theseKeys);
      if (_Instr_comp2_key_allKeys.length > 0) {
        Instr_comp2_key.keys = _Instr_comp2_key_allKeys[_Instr_comp2_key_allKeys.length - 1].name;  // just the last key pressed
        Instr_comp2_key.rt = _Instr_comp2_key_allKeys[_Instr_comp2_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_comp2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr_comp2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Instr_comp2'-------
    for (const thisComponent of Instr_comp2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var EndComponents;
function EndRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(End_txt);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EndRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *End_txt* updates
    if (t >= 0.0 && End_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      End_txt.tStart = t;  // (not accounting for frame time here)
      End_txt.frameNStart = frameN;  // exact frame index
      
      End_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (End_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      End_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'End'-------
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
