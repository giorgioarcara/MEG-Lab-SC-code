%% CONNECTIVITY (ver 2)

% This script launch connectivity (mean after) on the data already
% pre-processed for the Neural Plasticity Paper (the original
% brainstorm_db was tdcs_neural_plasticity_merge)
% it compute connectivity on specific bands with AEC

% NOTE beta and gamma band taken from Hipp, 2012 (Nature Neuroscience)

%% PRELIMINARY PREPARATION
clear


%% GET CURRENT SCRIPT NAME

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

%%


addpath('/storages/LDATA/Giorgio/TDCS MEG Exp1 Graph Theory analysis/Scripts/functions')

% launch brainstorm, with no gui (but only if is not already condning)
if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='storages/LDATA/Giorgio/TDCS MEG Exp1 Graph Theory analysis/';
export_folder='Reports_new';


if ~exist([export_main_folder, '/' export_folder])
    mkdir([export_main_folder, '/' export_folder]) % create folder if it does not exist
end;


%% SET PROTOCOL
ProtocolName = 'tDCS_MEG_Exp1_GraphTheory';

% get the protocol index, knowing the name
iProtocol = bst_get('Protocol', ProtocolName);

% set the current protocol
gui_brainstorm('SetCurrentProtocol', iProtocol);

% check info
ProtocolInfo=bst_get('ProtocolInfo')

% get the subject list
my_subjects = bst_get('ProtocolSubjects')

%% SELECT SUBJECTS

SubjectNames = sel_files_bst({my_subjects.Subject.Name}, '.', 'Group_analysis');
SubjectNames_sel = SubjectNames; % all subjects are ok
% SubjectNames_sel = sel_files_bst(SubjectNames, 'Subject01_A'); % all subjects are ok
SubjectNames_sel = SubjectNames;



%% SELECT FILES
% select all files

% Input files
sFiles = [];


% Start a new report

% Process: Select data files in: */*
my_sFiles_ini = bst_process('CallProcess', 'process_select_files_data', [], [], ...
    'subjectname',   SubjectNames_sel, ...
    'condition',     '', ...
    'tag',           '', ...
    'includebad',    0, ...
    'includeintra',  0, ...
    'includecommon', 0);


%% SELECT FILES HERE

my_sFiles = sel_files_bst({my_sFiles_ini.FileName}, 'resample');
my_sFiles = sel_files_bst(my_sFiles, 'bl', 'ASSR');

%check files
my_sFiles = sort_by_fragment(my_sFiles, 'Subject..');



%% DIVIDE BY SUJECTS
Subj_grouped = group_by_str_bst(my_sFiles, SubjectNames_sel);



%% GROUP BY cond

% get study names for each file
study_names = cell (1, length(Subj_grouped));
for iSubj = 1: length(Subj_grouped);
    for iFile = 1:length(Subj_grouped{iSubj});
        study_names{iSubj}{iFile} = bst_fileparts(Subj_grouped{iSubj}{iFile});
    end;
end;

% get unique and divide in cond
Subj_cond=cell (1, length(Subj_grouped));
for iSubj = 1: length(Subj_grouped);
    Subj_cond{iSubj} = group_by_str_bst(Subj_grouped{iSubj}, unique(study_names{iSubj}));
end




% COMPUTE CONNECTIVITY

CondNames = {'pre', 'post'};



tic
% loop over subj
for iSubj=1:length(SubjectNames_sel);
    
    for iCond = 1:length(Subj_cond{iSubj})
        
        curr_files =  Subj_cond{iSubj}{iCond};
        
        bst_report('Start', curr_files);
        
        
        %%  --------------- PLV ------------------------------
        % RETRIEVE SOURCE (LINK) FILES
        % retrieve condition path
        curr_study=bst_get('StudyWithCondition', bst_fileparts(curr_files{1}));
        
        % exclude with the following steps the empty filenames, in the
        % ResultFile, otherwise cannot use intersect
        no_empty_DataFile_ind=find(~cellfun(@isempty, {curr_study.Result.DataFile}));
        no_empty_Resultfile=curr_study.Result(no_empty_DataFile_ind);
        
        % find intersection between curr-files (the data to be processed)
        % and the non-empty Resultfile names
        [ind_no_empty_Resultfile]=ismember({no_empty_Resultfile.DataFile}, curr_files);
        
        % retrieve link_files
        link_files={no_empty_Resultfile(ind_no_empty_Resultfile).FileName};
        
        %% SELECT only those with volume (tag added before), in the filename
        % link_files = sel_files_bst(link_files, 'volume');
        
        
        bst_report('Start', link_files);
        
        % Process: Amplitude Envelope Correlation NxN
        Conn_files = bst_process('CallProcess', 'process_plv1n', link_files, [], ...
            'timewindow', [,], ...
            'scouts',     {'Desikan-Killiany - centroid', {'bankssts L', 'bankssts R', 'caudalanteriorcingulate L', 'caudalanteriorcingulate R', 'caudalmiddlefrontal L', 'caudalmiddlefrontal R', 'cuneus L', 'cuneus R', 'entorhinal L', 'entorhinal R', 'frontalpole L', 'frontalpole R', 'fusiform L', 'fusiform R', 'inferiorparietal L', 'inferiorparietal R', 'inferiortemporal L', 'inferiortemporal R', 'insula L', 'insula R', 'isthmuscingulate L', 'isthmuscingulate R', 'lateraloccipital L', 'lateraloccipital R', 'lateralorbitofrontal L', 'lateralorbitofrontal R', 'lingual L', 'lingual R', 'medialorbitofrontal L', 'medialorbitofrontal R', 'middletemporal L', 'middletemporal R', 'paracentral L', 'paracentral R', 'parahippocampal L', 'parahippocampal R', 'parsopercularis L', 'parsopercularis R', 'parsorbitalis L', 'parsorbitalis R', 'parstriangularis L', 'parstriangularis R', 'pericalcarine L', 'pericalcarine R', 'postcentral L', 'postcentral R', 'posteriorcingulate L', 'posteriorcingulate R', 'precentral L', 'precentral R', 'precuneus L', 'precuneus R', 'rostralanteriorcingulate L', 'rostralanteriorcingulate R', 'rostralmiddlefrontal L', 'rostralmiddlefrontal R', 'superiorfrontal L', 'superiorfrontal R', 'superiorparietal L', 'superiorparietal R', 'superiortemporal L', 'superiortemporal R', 'supramarginal L', 'supramarginal R', 'temporalpole L', 'temporalpole R', 'transversetemporal L', 'transversetemporal R'}}, ...
            'scoutfunc',  3, ...  % PCA
            'scouttime',  1, ...  % Before
            'freqbands',  { 'alpha', '8, 12', 'mean'; 'beta', '15, 23', 'mean'; 'gamma1', '32, 45', 'mean'}, ...
            'mirror',     0, ...
            'keeptime',   0, ...
            'plvmeasure', 2, ...  % Magnitude
            'outputmode', 3);  % Save average connectivity matrix (one file)
        ;  % Save average connectivity matrix (one file)
        
        % Process: Add tag:
        Conn_files = bst_process('CallProcess', 'process_add_tag', Conn_files, [], ...
            'tag',    [CondNames{iCond}, '_CentrDesikan'], ...
            'output', 2);  % Add to file name
        
        % Process: Add tag:
        Conn_files = bst_process('CallProcess', 'process_add_tag', Conn_files, [], ...
            'tag',   [CondNames{iCond}, '_CentrDesikan'], ...
            'output', 1);  % Add to comment
        
        
        % Save and display report
        ReportFile = bst_report('Save', Conn_files);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
        
    end;
end;
toc


script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

export_script(script_name, my_sFiles_ini)

