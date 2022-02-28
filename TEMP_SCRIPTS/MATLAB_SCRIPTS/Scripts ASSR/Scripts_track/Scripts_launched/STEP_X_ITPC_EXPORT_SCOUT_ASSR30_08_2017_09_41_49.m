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
my_measure = 'ITPC';


my_sFiles_ini= bst_process('CallProcess', 'process_select_files_timefreq', [], [], ...
    'subjectname',   'All', ...
    'condition',     [], ...
    'tag',           my_measure, ...
    'includebad',    0, ...
    'includeintra',  1, ... % include intra as I select average of runs
    'includecommon', 1);


my_sFiles = {my_sFiles_ini.FileName};



%% DIVIDE BY SEED (storing in a cell in the more common name I use)
% furthermore, select by measure

my_Conds = {'/REAL_POST/', '/REAL_PRE/', '/SHAM_POST/', '/SHAM_PRE/'};
my_Conds_names = {'REAL_POST', 'REAL_PRE', 'SHAM_POST', 'SHAM_PRE'};


%% SELECT ONLY SOME FILES
my_sel = 'Group_analysis';

Cond_grouped = group_by_str_bst( sel_files_bst( my_sFiles, my_sel), my_Conds);

%% ORDER BY SUBJECT NAMES (just to be sure they are on the right order).

for iCond = 1:length(my_Conds)
    Cond_grouped{iCond} = sort_by_fragment(Cond_grouped{iCond}, 'Subject..');
end;


% SET EXPORT FOLDER

export_txt_folder='ITPC_export_files';


if ~exist([export_main_folder, '/' export_txt_folder])
    mkdir([export_main_folder, '/' export_txt_folder]) % create folder if it does not exist
end;


cd([export_main_folder, '/' export_txt_folder])




%% EXPORT TO ERPR


% loop over conditions
for iCond = 1:length(my_Conds)
    
    % select current files
    curr_files = Cond_grouped{iCond}
    
    % loop over files
    for iFile = 1: length(curr_files)
        
        % Start a new report
        bst_report('Start', curr_files);
        
        
        % Process: Extract values: [300ms,700ms] 38-42Hz
        Res1 = bst_process('CallProcess', 'process_extract_values', curr_files{iFile}, [], ...
            'timewindow', [0.3, 0.7], ...
            'freqrange',  [38, 42], ...
            'rows',       '', ...
            'isabs',      0, ...
            'avgtime',    0, ...
            'avgrow',     0, ...
            'avgfreq',    1, ...
            'matchrows',  0, ...
            'dim',        2, ...  % Concatenate time (dimension 2)
            'Comment',    '');
        
        % Process: Scouts time series: Cortex L Cortex R
        Res2 = bst_process('CallProcess', 'process_extract_scout', Res1, [], ...
            'timewindow',     [], ...
            'scouts',         {'Structures', {'Cortex L', 'Cortex R'}}, ...
            'scoutfunc',      1, ...  % Mean
            'concatenate',    1, ...
            'save',           1, ...
            'addrowcomment',  0, ...
            'addfilecomment', 0);
        
        
        % Process: export to erpR
        Res3 = bst_process('CallProcess', 'process_export_erpR', Res2, [], ...
            'chars',        10, ...
            'base',         [my_measure, '_', my_Conds_names{iCond}, '_', num2str(iFile)], ...
            'Num',          0, ...
            'BadChans',     1);
        
        % NOTE: as the intermediate files are of different kind (matrix
        % and results) I have to make two separate calls to delete the
        % files.
        
        % Process: Delete selected files
        Res1 = bst_process('CallProcess', 'process_delete', Res1, [], ...
            'target', 1);  % Delete selected files
        
        
        % Process: Delete selected files
        Res2 = bst_process('CallProcess', 'process_delete', Res2, [], ...
            'target', 1);  % Delete selected files
        
        
        % Save and display report
        ReportFile = bst_report('Save', Res3);
        bst_report('Open', ReportFile);
        bst_report('Export', ReportFile, [export_main_folder, '/', export_folder]);
        
        
        
    end;
end;


cd(export_main_folder)

%% EXPORT SCRIPT
export_script(script_name, my_sFiles_ini)


