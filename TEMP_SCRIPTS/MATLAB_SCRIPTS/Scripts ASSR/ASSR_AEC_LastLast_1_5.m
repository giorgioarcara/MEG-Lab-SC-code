%AEC_ASSR
path_data='/storages/LDATA/BrainstormDB/NewProcedure_OtherConnectivityMetrics/data/';
fnames = dir('/storages/LDATA/BrainstormDB/NewProcedure_OtherConnectivityMetrics/data/Sub*');
my_seeds = {'Left_SM1', 'Right_SM1', 'ASSR_Right', 'ASSR_Left'};
my_bands = {[2, 4], [5, 7], [8, 12], [15, 29], [39, 41]};
my_bands_names = {'delta', 'theta', 'alpha', 'beta', 'ASSR'};
my_time_window = {[0, 1], [0.4, 0.7]};
my_time_window_tag = {'_0-1', '_0.4-0.7'};

for gg=1:5%length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/*']);
    for hh=1:length(runs_names)
        if strcmp(runs_names(hh,1).name, 'REAL_PRE') || strcmp(runs_names(hh,1).name, 'REAL_POST') || strcmp(runs_names(hh,1).name, 'SHAM_PRE') || strcmp(runs_names(hh,1).name, 'SHAM_POST')
            [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
            display (run)
            trial_names=rdir([path_data name '/' run '/data*.mat'], '', '/storages/LDATA/BrainstormDB/NewProcedure_OtherConnectivityMetrics/data');
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
            Common_operator_file=rdir([path_data name '/' run '/results_MN_MEG_KERNEL*.mat'], '', '/storages/LDATA/BrainstormDB/NewProcedure_OtherConnectivityMetrics/data');
            for rr=1:length(sFiles_new)
                sFiles_last{1,rr}=(['link|' Common_operator_file(1,1).name '|' sFiles_new(1,rr).FileName]);
            end
            
            for pp=1:length(my_seeds)
                for iband=1:length(my_bands)
                    for iTime=1:length(my_time_window)
                        TagToAdd=['AEC: ' my_seeds{pp} '_' my_bands_names{iband} my_time_window_tag{iTime}];
                        display(['working on...' name '...' runs_names(hh,1).name '...' TagToAdd])
                        
                        % Process: Amplitude Envelope Correlation 1xN
                        sFiles = bst_process('CallProcess', 'process_aec1', sFiles_last, [], ...
                            'timewindow', my_time_window{iTime}, ...
                            'scouts',     {'User scouts', my_seeds(pp)}, ...
                            'scoutfunc',  1, ...  % Mean
                            'scouttime',  2, ...  % After
                            'freqbands',  {my_bands_names{iband}, [num2str(my_bands{iband}(1)), ',', num2str(my_bands{iband}(2))], 'mean'}, ...
                            'isorth',     1, ...
                            'outputmode', 3);  % Save average connectivity matrix (one file)
                        
                        % Process: Set comment
                        sFiles = bst_process('CallProcess', 'process_set_comment', sFiles, [], ...
                            'tag',    TagToAdd, ...
                            'isindex', 0);
                        
                        % Process: Extract values: [all]
                        sFiles = bst_process('CallProcess', 'process_extract_values', sFiles, [], ...
                            'timewindow', [], ...
                            'freqrange',  [], ...
                            'rows',       '', ...
                            'isabs',      0, ...
                            'avgtime',    0, ...
                            'avgrow',     0, ...
                            'avgfreq',    1, ...
                            'matchrows',  0, ...
                            'dim',        2, ...  % Concatenate time (dimension 2)
                            'Comment',    '');
                        % Process: Set comment
                        sFiles = bst_process('CallProcess', 'process_set_comment', sFiles, [], ...
                            'tag',    [TagToAdd '| Extracted'], ...
                            'isindex', 0);
                        % Process: Project on default anatomy: surface
                        sFiles = bst_process('CallProcess', 'process_project_sources', sFiles, [], ...
                            'headmodeltype', 'surface');  % Cortex surface
                        
                        % Process: Add tag
                        sFiles = bst_process('CallProcess', 'process_add_tag', sFiles, [], ...
                            'tag',    'Projected_AEC', ...
                            'output', 1);  % Add to comment
                        % Process: Spatial smoothing (20.00)
                        sFiles = bst_process('CallProcess', 'process_ssmooth_surfstat', sFiles, [], ...
                            'fwhm',      10, ...
                            'overwrite', 0);
                        
                    end
                end
            end
            clear sFiles_last Common_operator_file sFiles_new sFiles trial_names sFiles_backup
            
        end
    end
end
