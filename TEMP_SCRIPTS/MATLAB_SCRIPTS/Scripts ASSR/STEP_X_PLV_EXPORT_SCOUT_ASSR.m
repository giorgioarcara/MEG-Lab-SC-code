% launch brainstorm, with no gui (but only if is not already running)
clear

if ~brainstorm('status')
    brainstorm %nogui
end


%% SET EXPORT FOLDER FOR REPORTS
export_main_folder='/storages/LDATA/Code/Scripts ASSR';
export_folder='Reports';


if ~exist([export_main_folder, '/' export_folder])
    mkdir([export_main_folder, '/' export_folder]) % create folder if it does not exist
end;


addpath('/storages/LDATA/Code/Scripts ASSR/functions')


script_name = mfilename('fullpath')
%% BACKUP SCRIPT AND OBJECT WITH DATA


if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end


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

%% FIRST SELECTION ON TAG
% as the seeds information is stored in the Comment.
% I use this loop with bst selection (based on comment) to retrieve all
% files.


% NOTE!!! There is small typo in some comments with a space.
my_Seeds = {'Right_SM1_normalized', 'Left_SM1_normalized', 'ASSR_Left _normalized', 'ASSR_Right _normalized'};
my_Seeds_names = {'Right_SM1', 'Left_SM1', 'Left_ASSR', 'Right_ASSR'};


for iSeed = 1: length(my_Seeds)
    % Process: Select results (i.e., select source data)
    my_sFiles_ini{iSeed}= bst_process('CallProcess', 'process_select_files_timefreq', [], [], ...
        'subjectname',   'All', ...
        'condition',     [], ...
        'tag',           my_Seeds{iSeed}, ...
        'includebad',    0, ...
        'includeintra',  1, ... % include intra as I select average of runs
        'includecommon', 1);
    
end;




%% DIVIDE BY SEED (storing in a cell in the more common name I use)
% furthermore, select by measure

my_measure = 'plv';

for iSeed = 1:length(my_Seeds)
    Seed_grouped{iSeed} = sel_files_bst({my_sFiles_ini{iSeed}.FileName}, my_measure);
end


my_Conds = {'/REAL_POST/', '/REAL_PRE/', '/SHAM_POST/', '/SHAM_PRE/'};
my_Conds_names = {'REAL_POST', 'REAL_PRE', 'SHAM_POST', 'SHAM_PRE'};


%% SELECT ONLY SOME FILES
my_sel = 'Group_analysis';

for iSeed=1:length(my_Seeds)
    Seed_Cond{iSeed} = group_by_str_bst( sel_files_bst(Seed_grouped{iSeed}, my_sel), my_Conds);
end

%% ORDER BY SUBJECT NAMES (just to be sure they are on the right order).
for iSeed = 1:length(my_Seeds)
    for iCond = 1:length(my_Conds)
        
        Seed_Cond{iSeed}{iCond} = sort_by_fragment(Seed_Cond{iSeed}{iCond}, 'Subject..');
    end
end


% SET EXPORT FOLDER

export_txt_folder='PLV_export_files';


if ~exist([export_main_folder, '/' export_txt_folder])
    mkdir([export_main_folder, '/' export_txt_folder]) % create folder if it does not exist
end;


cd([export_main_folder, '/' export_txt_folder])




%% EXPORT TO ERPR

% loop over seeds
for iSeed = 1:length(my_Seeds)
    
    % loop over conditions
    for iCond = 1:length(my_Conds)
        
        % select current files
        curr_files = Seed_Cond{iSeed}{iCond}
        
        % loop over files
        for iFile = 1: length(curr_files)
            
            % Start a new report
            bst_report('Start', curr_files);
            
            % Process: Scouts time series: Cortex L Cortex R
            Res1 = bst_process('CallProcess', 'process_extract_scout', curr_files{iFile}, [], ...
                'timewindow',     [], ...
                'scouts',         {'Desikan-Killiany', {'bankssts L', 'bankssts R', 'caudalanteriorcingulate L', 'caudalanteriorcingulate R', 'caudalmiddlefrontal L', 'caudalmiddlefrontal R', 'cuneus L', 'cuneus R', 'entorhinal L', 'entorhinal R', 'frontalpole L', 'frontalpole R', 'fusiform L', 'fusiform R', 'inferiorparietal L', 'inferiorparietal R', 'inferiortemporal L', 'inferiortemporal R', 'insula L', 'insula R', 'isthmuscingulate L', 'isthmuscingulate R', 'lateraloccipital L', 'lateraloccipital R', 'lateralorbitofrontal L', 'lateralorbitofrontal R', 'lingual L', 'lingual R', 'medialorbitofrontal L', 'medialorbitofrontal R', 'middletemporal L', 'middletemporal R', 'paracentral L', 'paracentral R', 'parahippocampal L', 'parahippocampal R', 'parsopercularis L', 'parsopercularis R', 'parsorbitalis L', 'parsorbitalis R', 'parstriangularis L', 'parstriangularis R', 'pericalcarine L', 'pericalcarine R', 'postcentral L', 'postcentral R', 'posteriorcingulate L', 'posteriorcingulate R', 'precentral L', 'precentral R', 'precuneus L', 'precuneus R', 'rostralanteriorcingulate L', 'rostralanteriorcingulate R', 'rostralmiddlefrontal L', 'rostralmiddlefrontal R', 'superiorfrontal L', 'superiorfrontal R', 'superiorparietal L', 'superiorparietal R', 'superiortemporal L', 'superiortemporal R', 'supramarginal L', 'supramarginal R', 'temporalpole L', 'temporalpole R', 'transversetemporal L', 'transversetemporal R'}}, ...
                'scoutfunc',      1, ...  % Mean
                'concatenate',    1, ...
                'save',           1, ...
                'addrowcomment',  0, ...
                'addfilecomment', 0);
            
            
            % Process: export to erpR
            Res2 = bst_process('CallProcess', 'process_export_erpR', Res1, [], ...
                'chars',        10, ...
                'base',         [my_measure, '_', my_Seeds_names{iSeed}, '_', my_Conds_names{iCond}, '_', num2str(iFile)], ...
                'Num',          0, ...
                'BadChans',     1);
            
            % NOTE: as the intermediate files are of different kind (matrix
            % and results) I have to make two separate calls to delete the
            % files.
            
            % Process: Delete selected files
            Res1 = bst_process('CallProcess', 'process_delete', Res1, [], ...
                'target', 1);  % Delete selected files
            
            
            
            % Save and display report
            ReportFile = bst_report('Save', Res2);
            bst_report('Open', ReportFile);
            bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
            
            
            
        end;
    end;
end;


cd(export_main_folder)

%% EXPORT SCRIPT
export_script(script_name, my_sFiles_ini)


