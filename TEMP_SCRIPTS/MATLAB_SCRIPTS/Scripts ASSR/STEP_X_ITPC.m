%% Time Frequency
% 1) Calculate ITC


%% PRELIMINARY PREPARATION
clear



working_folder = '/storages/LDATA/Code/Scripts ASSR';
addpath(genpath(working_folder));


% launch brainstorm, with no gui (but only if is not already running)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_folder='Reports';


if ~exist([working_folder, '/' export_folder])
    mkdir([working_folder, '/' export_folder]) % create folder if it does not exist
end;


%% GET CURRENT SCRIPT NAME

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

%%


%% SET PROTOCOL
ProtocolName = 'ASSR_tDCS_wMEM';

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
    'tag',           'Sound_adj', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);



%% SPECIFY HERE THE FILES AND THE SUBJECTS TO BE PROCESSED.

%my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'Second_adj');
%my_sFiles = sel_files_bst(my_sFiles, 'S008_tDCS');

my_sFiles = {my_sFiles_ini.FileName};


%% GROUP BY SUBJECTS
SubjectNames={my_subjects.Subject.Name};
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames);

%% GROUP BY CONDITION
cond_names = {'_PRE', '_POST'};

for iSubj=1:length(SubjectNames)
    Subj_cond{iSubj}=group_by_str_bst(Subj_grouped{iSubj}, cond_names);
end;




% TO EXCLUDE SOME SUBJECTS
% my_sFiles = sel_files_bst(my_sFiles, '.', 'S001_|S002_');



% loop over subjects
for iSubj = 2:length(Subj_cond)
    
    for iCond = 1:length(cond_names);
        
        
        curr_files=Subj_cond{iSubj}{iCond};
        
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
        
        % Process: Time-frequency (Morlet wavelets)
        Res = bst_process('CallProcess', 'process_timefreq', link_files, [], ...
            'clusters',  {}, ...
            'scoutfunc', 1, ...  % Mean
            'edit',      struct(...
            'Comment',         'Avg, ITPC,38-42Hz', ...
            'TimeBands',       [], ...
            'Freqs',           [38, 39, 40, 41, 42], ...
            'MorletFc',        1, ...
            'MorletFwhmTc',    3, ...
            'ClusterFuncTime', 'none', ...
            'Measure',         'power', ...
            'Output',          'average', ...
            'RemoveEvoked',    0, ...
            'SaveKernel',      0), ...
            'normalize', 'none');  % None: Save non-standardized time-frequency maps
        
        
        
        % Process: Add tag:
        Res = bst_process('CallProcess', 'process_add_tag', Res, [], ...
            'tag',    ['ITPC', cond_names{iCond}], ...
            'output', 2);  % Add to file name
        
        
        % Save and display report
        ReportFile = bst_report('Save', Res);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [working_folder, '/', export_folder]);
        
        
        
        
        
        
    end;% end loop over conditions
end; % end loop over Subjects



%% BACKUP SCRIPT AND OBJECT WITH DATA


export_script(script_name, my_sFiles_ini)