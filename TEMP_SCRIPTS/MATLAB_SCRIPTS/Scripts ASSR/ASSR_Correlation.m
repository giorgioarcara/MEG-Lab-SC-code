%Correlation
path_data='/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data/';
fnames = dir('/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data/Sub*');
my_seeds = {'Left_SM1', 'Right_SM1', 'ASSR_Right', 'ASSR_Left'};

for gg=1:length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/REAL_*']);
    for hh=1:length(runs_names)
        [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
        display (run)
        trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
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
        Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
        for rr=1:length(sFiles_new)
            sFiles_last{1,rr}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,rr).FileName]);
        end
        
        for pp=1:length(my_seeds)
            
            sFiles = bst_process('CallProcess', 'process_corr1', sFiles_last, [], ...
                'timewindow', [0, 1], ...
                'scouts',     {'User scouts', my_seeds(pp)}, ...
                'scoutfunc',  1, ...  % Mean
                'scouttime',  2, ...  % After
                'scalarprod', 0, ...
                'outputmode', 2);  % Save average connectivity matrix (one file)
            
            % Process: Add tag: _baseline
            sFiles = bst_process('CallProcess', 'process_add_tag', sFiles, [], ...
                'tag',    '_active', ...
                'output', 1);  % Add to comment
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        clear sFiles_last sFiles_TF Common_operator_file sFiles_new sFiles trial_names sFiles_backup
    end
end


for gg=1:length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/REAL_*']);
    for hh=1:length(runs_names)
        [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
        display (run)
        trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
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
        Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
        for rr=1:length(sFiles_new)
            sFiles_last{1,rr}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,rr).FileName]);
        end
        
        for pp=1:length(my_seeds)
            
            sFiles = bst_process('CallProcess', 'process_corr1', sFiles_last, [], ...
                'timewindow', [-1, 0], ...
                'scouts',     {'User scouts', my_seeds(pp)}, ...
                'scoutfunc',  1, ...  % Mean
                'scouttime',  2, ...  % After
                'scalarprod', 0, ...
                'outputmode', 2);  % Save average connectivity matrix (one file)
            
            % Process: Add tag: _baseline
            sFiles = bst_process('CallProcess', 'process_add_tag', sFiles, [], ...
                'tag',    '_baseline', ...
                'output', 1);  % Add to comment
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        clear sFiles_last sFiles_TF Common_operator_file sFiles_new sFiles trial_names sFiles_backup
    end
end


for gg=1:length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/SHAM_*']);
    for hh=1:length(runs_names)
        [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
        display (run)
        trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
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
        Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
        for rr=1:length(sFiles_new)
            sFiles_last{1,rr}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,rr).FileName]);
        end
        
        for pp=1:length(my_seeds)
            
            sFiles = bst_process('CallProcess', 'process_corr1', sFiles_last, [], ...
                'timewindow', [0, 1], ...
                'scouts',     {'User scouts', my_seeds(pp)}, ...
                'scoutfunc',  1, ...  % Mean
                'scouttime',  2, ...  % After
                'scalarprod', 0, ...
                'outputmode', 2);  % Save average connectivity matrix (one file)
            
            % Process: Add tag: _baseline
            sFiles = bst_process('CallProcess', 'process_add_tag', sFiles, [], ...
                'tag',    '_active', ...
                'output', 1);  % Add to comment
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        clear sFiles_last sFiles_TF Common_operator_file sFiles_new sFiles trial_names sFiles_backup
    end
end


for gg=1:length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/SHAM_*']);
    for hh=1:length(runs_names)
        [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
        display (run)
        trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
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
        Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data');
        for rr=1:length(sFiles_new)
            sFiles_last{1,rr}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,rr).FileName]);
        end
        
        for pp=1:length(my_seeds)
            
            sFiles = bst_process('CallProcess', 'process_corr1', sFiles_last, [], ...
                'timewindow', [-1, 0], ...
                'scouts',     {'User scouts', my_seeds(pp)}, ...
                'scoutfunc',  1, ...  % Mean
                'scouttime',  2, ...  % After
                'scalarprod', 0, ...
                'outputmode', 2);  % Save average connectivity matrix (one file)
            
            % Process: Add tag: _baseline
            sFiles = bst_process('CallProcess', 'process_add_tag', sFiles, [], ...
                'tag',    '_baseline', ...
                'output', 1);  % Add to comment
        end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        clear sFiles_last sFiles_TF Common_operator_file sFiles_new sFiles trial_names sFiles_backup
    end
end
