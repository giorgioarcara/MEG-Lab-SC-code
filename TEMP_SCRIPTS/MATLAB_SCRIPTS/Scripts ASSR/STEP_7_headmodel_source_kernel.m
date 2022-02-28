
%% IMPORTANT:
% This script was not sent due to an error. Selecting all the files it
% returns an error. It works if only one subject at the time is processed.
% Data were obtained by sending the script separately for each subject
% Uncomment to see the actual script.




%% GENERATE HEAD MODEL AND CALCULATE SOURCE KERNEL
% This script generate the head model and then calculate the source kernel
% 1) generate head model (BEM)
% 2) calculate source inversion kernel (wMNE).

%% PRELIMINARY PREPARATION
clear


addpath('/storages/LDATA/Giorgio/Mapping_pre_post_Analyses/Scripts/functions');
addpath('/storages/LDATA/Giorgio/Mapping_pre_post_Analyses/Scripts/');

% launch brainstorm, with no gui (but only if is not already running)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='/storages/LDATA/Giorgio/Mapping_pre_post_Analyses/';
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
ProtocolName = 'mapping_pre_post';

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


%% SELECT SUBJECT NAMES (note that only subject names are used to calculate bem).
SubjectNames = sel_files_bst({my_subjects.Subject.Name}, 'MC_pre|MC_post|PC_pre|PC_post|SL_pre|SL_post');

%% SELECT FILES
% select all files

% Input files
sFiles = [];
% SubjectNames = {...
%     'All'};

% Start a new report

% Process: Select data files in: */*
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_data', [], [], ...
    'subjectname',   SubjectNames, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);



my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'First');
my_sFiles = sel_files_bst(my_sFiles, 'MC_pre|MC_post|PC_pre|PC_post|SL_pre|SL_post');

%% DIVIDE BY SUBJECTS
SubjectNames={my_subjects.Subject.Name};
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames);

%%% !! LEAVE THIS IN CASE I WANT TO DIVIDE BY RUN
% %% DIVIDE BY RUN
% % get study names for each file
% study_names = cell (1, length(Subj_grouped));
% for iSubj = 1: length(Subj_grouped);
%     for iFile = 1:length(Subj_grouped{iSubj});
%         study_names{iSubj}{iFile} = bst_fileparts(Subj_grouped{iSubj}{iFile});
%     end;
% end;
% 
% % get unique and divide in
% Subj_cond=cell (1, length(Subj_grouped));
% for iSubj = 1: length(Subj_grouped);
%     Subj_cond{iSubj} = group_by_str_bst(Subj_grouped{iSubj}, unique(study_names{iSubj}));
% end


for iSubj=1:length(Subj_grouped)
    
%     nruns = length(Subj_grouped{iSubj})
%     
%     for iRun = 1:nruns
        
        curr_files = Subj_grouped{iSubj} %{iRun};
        
        bst_report('Start', curr_files);
        
%         %COMPUTE HEAD MODEL (BEM)
%         Res = bst_process('CallProcess', 'process_headmodel', curr_files, [], ...
%             'Comment',     'OpenMEEG BEM', ...
%             'sourcespace', 2, ...  % MRI volume
%             'volumegrid',  2, ...
%             'meg',         4, ...  % OpenMEEG BEM
%             'eeg',         0, ...  %
%             'ecog',        0, ...  %
%             'seeg',        0, ...  %
%             'openmeeg',    struct(...
%             'BemSelect',    [1, 1, 1], ...
%             'BemCond',      [1, 0.0125, 1], ...
%             'BemNames',     {{'Scalp', 'Skull', 'Brain'}}, ...
%             'BemFiles',     {{}}, ...
%             'isAdjoint',    0, ...
%             'isAdaptative', 1, ...
%             'isSplit',      0, ...
%             'SplitLength',  4000));
%         
        
        
        
        % Process: Compute sources
        Res2 = bst_process('CallProcess', 'process_inverse', curr_files, [], ...
            'Comment',     '', ...
            'method',      1, ...  % Minimum norm estimates (wMNE)
            'wmne',        struct(...
            'SourceOrient', {{'free'}}, ...
            'loose',        0.2, ...
            'SNR',          3, ...
            'pca',          1, ...
            'diagnoise',    0, ...
            'regnoise',     1, ...
            'magreg',       0.1, ...
            'gradreg',      0.1, ...
            'eegreg',       0.1, ...
            'depth',        1, ...
            'weightexp',    0.5, ...
            'weightlimit',  10), ...
            'sensortypes', 'MEG', ...
            'output',      1);  % Kernel only: shared % Kernel only: shared
        
        
        % Save and display report
        ReportFile = bst_report('Save', Res2);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
        
    end;
%end;


%% BACKUP SCRIPT AND OBJECT WITH DATA



export_script(script_name, SubjectNames)
