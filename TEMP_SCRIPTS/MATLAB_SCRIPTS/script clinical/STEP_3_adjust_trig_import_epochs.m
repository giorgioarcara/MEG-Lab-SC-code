%% IMPORT EPOCHS
% 1) import epochs with -2.5 2.5 of First Adj
% 2) baseline corection -200 - 0

% 1) adjust events with photodiod


%% PRELIMINARY PREPARATION
clear


addpath('/storages/LDATA/Giorgio/mapping_clinical_Analyses/Scripts/functions');
addpath('/storages/LDATA/Giorgio/mapping_clinical_Analyses/Scripts/');

% launch brainstorm, with no gui (but only if is not already running)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='/storages/LDATA/Giorgio/mapping_clinical_Analyses/';
export_folder='Reports';


if ~exist([export_main_folder, '/' export_folder])
    mkdir([export_main_folder, '/' export_folder]) % create folder if it does not exist
end;


%% GET CURRENT SCRIPT NAME

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

%%


%% SET PROTOCOL
ProtocolName = 'mapping_clinical_DB';

% get the protocol index, knowing the name
iProtocol = bst_get('Protocol', ProtocolName);

% set the current protocol
gui_brainstorm('SetCurrentProtocol', iProtocol);

% check info
ProtocolInfo=bst_get('ProtocolInfo')

% get the subject list
my_subjects = bst_get('ProtocolSubjects')


%% SELECT FILES WITH BRAINSTORM FUNCTION
% select all files
% Start a new report
% Input files
sFiles = [];
SubjectNames = {...
    'All'};

% Process: Select data files in: */*
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_data', [], [], ...
    'subjectname',   SubjectNames{1}, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);


%% SELECT HERE THE CORRECT FILES


%% SPECIFY HERE THE FILES AND THE SUBJECTS TO BE PROCESSED.

my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'LanguageTasks|ArcaraMapping');
my_sFiles = sel_files_bst(my_sFiles, 'AF|BO|EM', '_04'); % exclude _04 BO that is a run aborted after few trials.





%% DIVIDE BY SUBJECTS
SubjectNames={my_subjects.Subject.Name};
Subj_files_grouped = group_by_str_bst(my_sFiles, SubjectNames);

% create cell with corespondence sFiles with task (can be used if each
% subjet perform just one type of task.
tasks_subj = {'verbgen', 'naming', 'verbgen'}


% TO EXCLUDE SOME SUBJECTS
% my_sFiles = sel_files_bst(my_sFiles, '.', 'S001_|S002_');


for iSubj = 1:length(Subj_files_grouped)
    
    % Start a new report
    bst_report('Start', Subj_files_grouped{iSubj});
    
    
    %% CASE verbgen
    if strcmp( tasks_subj{iSubj} , 'verbgen')
        
        Res = bst_process('CallProcess', 'process_evt_detect_analog', Subj_files_grouped{iSubj}, [], ...
            'eventname',   'First_adj', ...
            'channelname', 'UADC002', ...
            'timewindow',  [], ...
            'threshold',   2, ...
            'blanking',    2, ...
            'highpass',    0, ...
            'lowpass',     0, ...
            'refevent',    'First', ...
            'isfalling',   0, ...
            'ispullup',    1, ...
            'isclassify',  0);
        
    end;
    
    
    
    %% CASE naming
    if strcmp( tasks_subj{iSubj} , 'naming')
        
        Res = bst_process('CallProcess', 'process_evt_detect_analog', Subj_files_grouped{iSubj}, [], ...
            'eventname',   'First_adj', ...
            'channelname', 'UADC001', ...
            'timewindow',  [], ...
            'threshold',   2, ...
            'blanking',    2, ...
            'highpass',    0, ...
            'lowpass',     0, ...
            'refevent',    'First', ...
            'isfalling',   0, ...
            'ispullup',    1, ...
            'isclassify',  0);
        
    end;
    
        Res = bst_process('CallProcess', 'process_import_data_event', Res, [], ...
        'subjectname', SubjectNames{iSubj}, ...
        'condition',   '', ...
        'eventname',   'First_adj', ...
        'timewindow',  [], ...
        'epochtime',   [-2.5, 2.5], ...
        'createcond',  0, ...
        'ignoreshort', 1, ...
        'usectfcomp',  1, ...
        'usessp',      1, ...
        'freq',        [600], ...
        'baseline',    [-0.2, 0]);
    
    
    
    % Save and display report
    ReportFile = bst_report('Save', Res);
    bst_report('Open', ReportFile);
    bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
    
end;

%% BACKUP SCRIPT AND OBJECT WITH DATA

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

export_script(script_name, my_sFiles_ini)
