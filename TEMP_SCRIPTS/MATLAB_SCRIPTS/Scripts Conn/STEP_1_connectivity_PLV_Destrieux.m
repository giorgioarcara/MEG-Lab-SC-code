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
            'scouts',     {'Destrieux', {'G_Ins_lg_and_S_cent_ins L', 'G_Ins_lg_and_S_cent_ins R', 'G_and_S_cingul-Ant L', 'G_and_S_cingul-Ant R', 'G_and_S_cingul-Mid-Ant L', 'G_and_S_cingul-Mid-Ant R', 'G_and_S_cingul-Mid-Post L', 'G_and_S_cingul-Mid-Post R', 'G_and_S_frontomargin L', 'G_and_S_frontomargin R', 'G_and_S_occipital_inf L', 'G_and_S_occipital_inf R', 'G_and_S_paracentral L', 'G_and_S_paracentral R', 'G_and_S_subcentral L', 'G_and_S_subcentral R', 'G_and_S_transv_frontopol L', 'G_and_S_transv_frontopol R', 'G_cingul-Post-dorsal L', 'G_cingul-Post-dorsal R', 'G_cingul-Post-ventral L', 'G_cingul-Post-ventral R', 'G_cuneus L', 'G_cuneus R', 'G_front_inf-Opercular L', 'G_front_inf-Opercular R', 'G_front_inf-Orbital L', 'G_front_inf-Orbital R', 'G_front_inf-Triangul L', 'G_front_inf-Triangul R', 'G_front_middle L', 'G_front_middle R', 'G_front_sup L', 'G_front_sup R', 'G_insular_short L', 'G_insular_short R', 'G_oc-temp_lat-fusifor L', 'G_oc-temp_lat-fusifor R', 'G_oc-temp_med-Lingual L', 'G_oc-temp_med-Lingual R', 'G_oc-temp_med-Parahip L', 'G_oc-temp_med-Parahip R', 'G_occipital_middle L', 'G_occipital_middle R', 'G_occipital_sup L', 'G_occipital_sup R', 'G_orbital L', 'G_orbital R', 'G_pariet_inf-Angular L', 'G_pariet_inf-Angular R', 'G_pariet_inf-Supramar L', 'G_pariet_inf-Supramar R', 'G_parietal_sup L', 'G_parietal_sup R', 'G_postcentral L', 'G_postcentral R', 'G_precentral L', 'G_precentral R', 'G_precuneus L', 'G_precuneus R', 'G_rectus L', 'G_rectus R', 'G_subcallosal L', 'G_subcallosal R', 'G_temp_sup-G_T_transv L', 'G_temp_sup-G_T_transv R', 'G_temp_sup-Lateral L', 'G_temp_sup-Lateral R', 'G_temp_sup-Plan_polar L', 'G_temp_sup-Plan_polar R', 'G_temp_sup-Plan_tempo L', 'G_temp_sup-Plan_tempo R', 'G_temporal_inf L', 'G_temporal_inf R', 'G_temporal_middle L', 'G_temporal_middle R', 'Lat_Fis-ant-Horizont L', 'Lat_Fis-ant-Horizont R', 'Lat_Fis-ant-Vertical L', 'Lat_Fis-ant-Vertical R', 'Lat_Fis-post L', 'Lat_Fis-post R', 'Pole_occipital L', 'Pole_occipital R', 'Pole_temporal L', 'Pole_temporal R', 'S_calcarine L', 'S_calcarine R', 'S_central L', 'S_central R', 'S_cingul-Marginalis L', 'S_cingul-Marginalis R', 'S_circular_insula_ant L', 'S_circular_insula_ant R', 'S_circular_insula_inf L', 'S_circular_insula_inf R', 'S_circular_insula_sup L', 'S_circular_insula_sup R', 'S_collat_transv_ant L', 'S_collat_transv_ant R', 'S_collat_transv_post L', 'S_collat_transv_post R', 'S_front_inf L', 'S_front_inf R', 'S_front_middle L', 'S_front_middle R', 'S_front_sup L', 'S_front_sup R', 'S_interm_prim-Jensen L', 'S_interm_prim-Jensen R', 'S_intrapariet_and_P_trans L', 'S_intrapariet_and_P_trans R', 'S_oc-temp_lat L', 'S_oc-temp_lat R', 'S_oc-temp_med_and_Lingual L', 'S_oc-temp_med_and_Lingual R', 'S_oc_middle_and_Lunatus L', 'S_oc_middle_and_Lunatus R', 'S_oc_sup_and_transversal L', 'S_oc_sup_and_transversal R', 'S_occipital_ant L', 'S_occipital_ant R', 'S_orbital-H_Shaped L', 'S_orbital-H_Shaped R', 'S_orbital_lateral L', 'S_orbital_lateral R', 'S_orbital_med-olfact L', 'S_orbital_med-olfact R', 'S_parieto_occipital L', 'S_parieto_occipital R', 'S_pericallosal L', 'S_pericallosal R', 'S_postcentral L', 'S_postcentral R', 'S_precentral-inf-part L', 'S_precentral-inf-part R', 'S_precentral-sup-part L', 'S_precentral-sup-part R', 'S_suborbital L', 'S_suborbital R', 'S_subparietal L', 'S_subparietal R', 'S_temporal_inf L', 'S_temporal_inf R', 'S_temporal_sup L', 'S_temporal_sup R', 'S_temporal_transverse L', 'S_temporal_transverse R'}}, ...
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
            'tag',    [CondNames{iCond}, '_Destrieux'], ...
            'output', 2);  % Add to file name
        
        % Process: Add tag:
        Conn_files = bst_process('CallProcess', 'process_add_tag', Conn_files, [], ...
            'tag',   [CondNames{iCond}, '_Destrieux'], ...
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

