%% Time Frequency
% 1) Calculate run average
% 2) ERSD
% 3) add tag
% 4) average time 400 ms - 1000 ms


%% PRELIMINARY PREPARATION
clear


addpath('/storages/LDATA/Giorgio Mapping/Parlog Analysis/functions');

% launch brainstorm, with no gui (but only if is not already running)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='/storages/LDATA/Giorgio Mapping/Parlog Analysis/';
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


%%


%% SET PROTOCOL
ProtocolName = 'ARCARA_Mapping';

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
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_timefreq', [], [], ...
    'subjectname',   SubjectNames{1}, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);


%% SELECT HERE THE CORRECT FILES


%% SPECIFY HERE THE FILES AND THE SUBJECTS TO BE PROCESSED.

my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'morlet'); %% IMPORTANT. with this I select the sensors
my_sFiles = sel_files_bst(my_sFiles, 'MAP001');



%% DIVIDE BY SUBJECTS
SubjectNames=sel_files_bst({my_subjects.Subject.Name}, 'MAP001');
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames);


%% DIVIDE BY RUN
% suboptimal, set task according to trial order
tasks_subj_runs = {1:3, 4:6}
tasks_subj_runs_name={'naming' 'wordrep'}
% TO EXCLUDE SOME SUBJECTS
% my_sFiles = sel_files_bst(my_sFiles, '.', 'S001_|S002_');


for iSubj = 1:length(Subj_grouped)
    
    for iTask = 1:length(tasks_subj_runs);
        
        curr_files=Subj_grouped{iSubj}(tasks_subj_runs{iTask});
        
        
        % Start a new report
        bst_report('Start', curr_files);
        
        
        % Process: Average: Everything
        Res = bst_process('CallProcess', 'process_average', curr_files, [], ...
            'avgtype',   1, ...  % Everything
            'avg_func',  1, ...  % Arithmetic average:  mean(x)
            'weighted',  0, ...
            'matchrows', 0, ...
            'iszerobad', 1);
        
        % Process: Event-related perturbation (ERS/ERD): [-500ms,-300ms]
        Res = bst_process('CallProcess', 'process_baseline_norm', Res, [], ...
            'baseline',  [-0.5, -0.3], ...
            'method',    'ersd', ...  % Event-related perturbation (ERS/ERD):    x_std = (x - &mu;) / &mu; * 100
            'overwrite', 1);
        
        % Process: Add tag: SubjectName
        Res = bst_process('CallProcess', 'process_add_tag', Res, [], ...
            'tag',    [SubjectNames{iSubj}, '| ',tasks_subj_runs_name{iTask}, '| sensors'] , ...
            'output', 1);  % Add to comment
        
        % Process: Add tag: SubjectName
        Res = bst_process('CallProcess', 'process_add_tag', Res, [], ...
            'tag',     [SubjectNames{iSubj}, '_',tasks_subj_runs_name{iTask}, '_sensors'], ...
            'output', 2);  % Add to filename
        
        
        % Save and display report
        ReportFile = bst_report('Save', Res);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
        
        
        
    end;
end;


%% BACKUP SCRIPT AND OBJECT WITH DATA


export_script(script_name, my_sFiles_ini)