%% NOISE COVARIANCE
% this script generate noise covariance for the selected data.
% Importantly, run this code AFTER having created the last conditions
% (i.e., data folder containing the data on which the sources are computed) 
% so the noise is immediatly copied to the folder in
% which is needed

%% STEP 1 
% This script starts from a protocol (already created)
% with all files of all subjects
% 0) Convert epoched to continuos
% 1) Apply CTF compensation
% 2) resample at 600 Hz
% 3) calculate noise covariance
% 4) create snapshot.

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
ProtocolName = 'mapping_clinical';

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

% Input files
sFiles = [];
SubjectNames = {...
    'All'};

% Start a new report

% Process: Select data files in: */*
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_data', [], [], ...
    'subjectname',   SubjectNames{1}, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);



my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'SysTest|ArcaraNoise');

%% SPECIFY HERE THE FILES AND THE SUBJECTS TO BE PROCESSED.


my_sFiles = sort_by_fragment(my_sFiles, 'Subject..');
my_sFiles = sel_files_bst(my_sFiles, 'AF|BO|EM');




%% PART 1 CONVERT EPOCHED FILES TO CONTINOUS

% Start a new report
bst_report('Start', my_sFiles);

for i=1:length(my_sFiles);
    
    curr_file = in_bst_data(my_sFiles{i}, 'F');
    
    if (regexpi(curr_file.F.format, '^CTF$')) % when F.format is CTF, the data are epoched
        
        % Process: Convert to continuous (CTF): Continuous
        Temp = bst_process('CallProcess', 'process_ctf_convert', my_sFiles{i}, [], ...
            'rectype', 2);  % Continuous
    end;
    
end;


Noise_files=my_sFiles;


% APPLY COMPENSATION AND CALCULATE COVARIANCE

% Start a new report
bst_report('Start', Noise_files);

% Process: Apply SSP & CTF compensation
sNoiseFiles = bst_process('CallProcess', 'process_ssp_apply', Noise_files, []);

% Process: Resample: 600Hz
sNoiseFiles = bst_process('CallProcess', 'process_resample', sNoiseFiles, [], ...
    'freq',      600, ...
    'overwrite', 0);

%% NOTE!!! I use from 8s because at 7 there is a jump in some squid (strongly affecting the covariance)

sNoiseFiles = bst_process('CallProcess', 'process_noisecov', sNoiseFiles, [], ...
    'baseline',       [1,119], ...
    'datatimewindow', [1, 119], ...
    'sensortypes',    'MEG', ...
    'target',         1, ...  % Noise covariance     (covariance over baseline time window)
    'dcoffset',       1, ...  % Block by block, to avoid effects of slow shifts in data
    'identity',       0, ...
    'copycond',       1, ... % copy directly to other conditions
    'copysubj',       0, ...
    'replacefile',    1);  % Replace


% Process: Snapshot: Noise covariance
sNoiseFiles = bst_process('CallProcess', 'process_snapshot', sNoiseFiles, [], ...
    'target',         3, ...  % Noise covariance
    'modality',       1, ...  % MEG (All)
    'orient',         1, ...  % left
    'time',           0, ...
    'contact_time',   [0, 0.1], ...
    'contact_nimage', 12, ...
    'threshold',      30, ...
    'Comment',        '');

% Save and display report
ReportFile = bst_report('Save', sNoiseFiles);
bst_report('Open', ReportFile);
bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);

% USEFUL CODE to copy noie to other conditions (i.e., o other folders of
% the same subject)
% for iNoise=1:length(sNoiseFiles)
%     
%     OutputFiles = db_set_noisecov(sNoiseFiles(iNoise).iStudy, 'AllConditions')
%     
% end;


%% BACKUP SCRIPT AND OBJECT WITH DATA

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

export_script(script_name, my_sFiles_ini)

