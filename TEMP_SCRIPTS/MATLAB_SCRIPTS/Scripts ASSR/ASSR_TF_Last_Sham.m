%%% On 7
path_data='/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data/';
fnames = dir('/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data/Sub*');

for gg=9:28%7:16%30%length(fnames) %da fare da xx a 16
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/SHAM_*']);
    for hh=1:length(runs_names)
        [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
        display (run)
        trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data');
        sFiles=cell(1,length(trial_names));
        for qq=1:length(trial_names)
            sFiles{1,qq}=(trial_names(qq,1).name);
        end
        sFiles_backup=sFiles;
        sFiles_new = bst_process('CallProcess', 'process_select_tag', sFiles, [], ...
            'tag',    'baseline', ...
            'search', 2, ...  % Search the file comments
            'select', 2);  % Select only the files without the tag
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data');
        for qq=1:length(sFiles_new)
            sFiles_last{1,qq}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,qq).FileName]);
        end
       
        
     sFiles = bst_process('CallProcess', 'process_timefreq', sFiles_last, [], ...
            'clusters',  {}, ...
            'scoutfunc', 1, ...  % Mean
            'edit',      struct(...
            'Comment',         'Avg, TF,38-42Hz', ...
            'TimeBands',       [], ...
            'Freqs',           [38, 39, 40, 41, 42], ...
            'MorletFc',        1, ...
            'MorletFwhmTc',    3, ...
            'ClusterFuncTime', 'none', ...
            'Measure',         'magnitude', ...
            'Output',          'average', ...
            'RemoveEvoked',    0, ...
            'SaveKernel',      0), ...
            'normalize', 'none');  % None: Save non-standardized time-frequency maps
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        clear sFiles_last sFiles_TF Common_operator_file sFiles_new sFiles trial_names sFiles_backup
    end
end
