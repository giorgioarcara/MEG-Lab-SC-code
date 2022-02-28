%% Time Frequency
% 1) Calculate avereage on ERSD in newly defined time win


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
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_timefreq', [], [], ...
    'subjectname',   SubjectNames{1}, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  1, ...
    'includecommon', 0);


%% SELECT HERE THE CORRECT FILES


%% SPECIFY HERE THE FILES AND THE SUBJECTS TO BE PROCESSED.

my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'hilbert', 'avg');
my_sFiles = sel_files_bst(my_sFiles, 'ersd');
my_sFiles = sel_files_bst(my_sFiles, 'AF|BO|EM');




%% DIVIDE BY SUBJECTS
SubjectNames={my_subjects.Subject.Name};
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames);



% TO EXCLUDE SOME SUBJECTS
% my_sFiles = sel_files_bst(my_sFiles, '.', 'S001_|S002_');
time_windows = {[0.080 0.200], [0.201 0.500], [0.501 1]};

for iSubj = 1:length(Subj_grouped)
    
    for iTimewin=1:length(time_windows)
        
        % Process: Average time: [400ms,1000ms]
        Res1 = bst_process('CallProcess', 'process_average_time', Subj_grouped{iSubj}, [], ...
            'timewindow', [time_windows{iTimewin}(1), time_windows{iTimewin}(2)], ...
            'isstd',      0, ...
            'overwrite',  0);
    end;
    
    
    % Save and display report
    ReportFile = bst_report('Save', Res1);
    bst_report('Open', ReportFile);
    bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
    
    
    
    
end;


%% BACKUP SCRIPT AND OBJECT WITH DATA


export_script(script_name, my_sFiles_ini)
