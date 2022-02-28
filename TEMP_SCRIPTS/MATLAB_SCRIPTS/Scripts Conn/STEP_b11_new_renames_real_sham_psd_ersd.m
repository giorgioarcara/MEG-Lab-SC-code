%% RENAME REAL SHAM
% This script start from an initial selection of files.
% then it add the tag (in both FileName and Comment) according to a segment
% of the FileName. In this specific case, the Segment of the FileName is
% the Name of the Subjects.
% This script is necessary (and I cannot use simpler function) cause each
% Subject had a different combination of "real" and "sham"

%% PRELIMINARY PREPARATION
clear


addpath('/storages/LDATA/Analyses tDCS-MEG - 03 2017')

% launch brainstorm, with no gui (but only if is not already condning)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='/storages/LDATA/Analyses tDCS-MEG - 03 2017';
export_folder='Reports';


if ~exist([export_main_folder, '/' export_folder])
    mkdir([export_main_folder, '/' export_folder]) % create folder if it does not exist
end;



%% SET PROTOCOL
ProtocolName = 'sticazzi';

% get the protocol index, knowing the name
iProtocol = bst_get('Protocol', ProtocolName);

% set the current protocol
gui_brainstorm('SetCurrentProtocol', iProtocol);

% check info
ProtocolInfo=bst_get('ProtocolInfo')

% get the subject list
my_subjects = bst_get('ProtocolSubjects')


%% SELECT FILES
% select all files

% Input files
sFiles = [];
SubjectNames = {...
    'All'};


my_measure='psd'

% Start a new report

% Process: Select data files in: */*
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_timefreq', [], [], ...
    'subjectname',   SubjectNames{1}, ...
    'condition',     '', ...
    'tag',           my_measure, ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);



my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'ersd');

%check files
my_sFiles = sort_by_fragment(my_sFiles, 'Subject..');


%% CREATE OBJECT WITH KEYS
keys=struct()
keys.Subject = 'NewSubject01_A';;
keys.session= 'real';
keys(end+1).Subject = 'NewSubject01_B';;
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject02_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject02_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject03_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject03_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject04_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject04_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject05_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject05_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject06_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject06_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject07_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject07_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject08_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject08_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject09_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject09_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject10_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject10_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject11_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject11_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject12_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject12_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject13_A';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject13_B';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject14_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject14_B';
keys(end).session= 'real';
keys(end+1).Subject = 'Subject15_A';
keys(end).session= 'sham';
keys(end+1).Subject = 'Subject15_B';
keys(end).session= 'real';

% suboptimal, but I don't know final lenght of object
% so I cannot initialize the matrix with the correct length.
real_indices = [];
sham_indices = [];

for iFile = 1:length(my_sFiles);
    curr_file = my_sFiles{iFile};
    file_split = strsplit(my_sFiles{iFile}, '/');
    curr_Subj_name = file_split{1};
    
    [ ~, curr_key_ind] = sel_files_bst({keys.Subject}, curr_Subj_name);
    
    if (strcmpi(keys(curr_key_ind).session, 'real'))
        real_indices = [real_indices, iFile];
    end;
    
    if (strcmpi(keys(curr_key_ind).session, 'sham'))
        sham_indices = [sham_indices, iFile];
    end;
    
end;


%% RETRIEVE ACCORDIG TO THE CREATE INDICES
% SORT AGAIN (just to be sure);
real_files = sort_by_fragment(my_sFiles(real_indices), 'Subject..');
sham_files = sort_by_fragment(my_sFiles(sham_indices), 'Subject..');


%%
% RENAME "REAL" FILES

bst_report('Start', real_files);

% Process: Add tag:
Res1 = bst_process('CallProcess', 'process_add_tag', real_files, [], ...
    'tag',    ['_real' ], ...
    'output', 2);  % Add to file name

% Process: Add tag:
Res1 = bst_process('CallProcess', 'process_add_tag', Res1, [], ...
    'tag',   [ 'real' ], ...
    'output', 1);  % Add to comment


% Save and display report
ReportFile = bst_report('Save', Res1);
bst_report('Open', ReportFile);
bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);


%%
% RENAME "SHAM" FILES

bst_report('Start', sham_files);

% Process: Add tag:
Res2 = bst_process('CallProcess', 'process_add_tag', sham_files, [], ...
    'tag',    ['_sham' ], ...
    'output', 2);  % Add to file name

% Process: Add tag:
Res2 = bst_process('CallProcess', 'process_add_tag', Res2, [], ...
    'tag',   [ 'sham' ], ...
    'output', 1);  % Add to comment


% Save and display report
ReportFile = bst_report('Save', Res2);
bst_report('Open', ReportFile);
bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);






