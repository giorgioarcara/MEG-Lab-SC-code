%% Time Frequency
% 1) Calculate TF


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
my_sFiles = sel_files_bst(my_sFiles, 'First');
my_sFiles = sel_files_bst(my_sFiles, 'AF|BO|EM');




%% DIVIDE BY SUBJECTS
SubjectNames={my_subjects.Subject.Name};
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames);

%% DIVIDE BY RUN (i.e. SESSION)

% get study names for each file
study_names = cell (1, length(Subj_grouped));
for iSubj = 1: length(Subj_grouped);
    for iFile = 1:length(Subj_grouped{iSubj});
        study_names{iSubj}{iFile} = bst_fileparts(Subj_grouped{iSubj}{iFile});
    end;
end;

% get unique and divide in
Subj_cond=cell (1, length(Subj_grouped));
for iSubj = 1: length(Subj_grouped);
    Subj_cond{iSubj} = group_by_str_bst(Subj_grouped{iSubj}, unique(study_names{iSubj}));
end

% TO EXCLUDE SOME SUBJECTS
% my_sFiles = sel_files_bst(my_sFiles, '.', 'S001_|S002_');


for iSubj = 1:length(Subj_cond)
    
    nRuns = length(Subj_cond{iSubj})
    
    for iRun = 1:nRuns
        
        curr_files=Subj_cond{iSubj}{iRun};
        
        
        % Start a new report
        bst_report('Start', curr_files);
        
        
        %% RETRIEVE SOURCE (LINK) FILES
        % retrieve condition path
        curr_study=bst_get('StudyWithCondition', bst_fileparts(curr_files{1}));
        
        % exclude with the following steps the empty filenames, in the
        % ResultFile, otherwise cannot use intersect
        no_empty_DataFile_ind=find(~cellfun(@isempty, {curr_study.Result.DataFile}));
        no_empty_Resultfile=curr_study.Result(no_empty_DataFile_ind);
        
        % find intersection between curr-files (the data to be processed)
        % and the non-empty Resultfile names
        [a ind_curr_files ind_no_empty_Resultfile]=intersect(curr_files, {no_empty_Resultfile.DataFile});
        
        % retrieve link_files
        link_files={no_empty_Resultfile(ind_no_empty_Resultfile).FileName};
        
        
        
        % Start a new report
        bst_report('Start', link_files);
        
        my_tag='beta'
        
        % Process: Hilbert transform
        link_files = bst_process('CallProcess', 'process_hilbert', link_files, [], ...
            'clusters',  {}, ...
            'scoutfunc', 1, ...  % Mean
            'edit',      struct(...
            'Comment',         ['Avg,Power, ', my_tag], ...
            'TimeBands',       [], ...
            'Freqs',           {{'beta', '15, 25', 'mean'}}, ...
            'ClusterFuncTime', 'none', ...
            'Measure',         'power', ...
            'Output',          'average', ...
            'RemoveEvoked',    0, ...
            'SaveKernel',      0), ...
            'normalize', 'none', ...  % None: Save non-standardized time-frequency maps
            'mirror',    0);
         
        
        
        % Save and display report
        ReportFile = bst_report('Save', link_files);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
        
    end;
    
end;

%% BACKUP SCRIPT AND OBJECT WITH DATA


export_script(script_name, my_sFiles_ini)
