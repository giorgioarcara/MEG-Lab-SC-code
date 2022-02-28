%Select and Extract Values
path_data='/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data/';
fnames = dir('/storages/LDATA/BrainstormDB/ASSR_tDCS_wMEM/data/Sub*');

for gg=1:length(fnames)
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runs_names = dir([path_data name '/*']);
    for hh=1:length(runs_names)
        if strcmp(runs_names(hh,1).name, 'REAL_PRE') || strcmp(runs_names(hh,1).name, 'REAL_POST') || strcmp(runs_names(hh,1).name, 'SHAM_PRE') || strcmp(runs_names(hh,1).name, 'SHAM_POST')
            [pathstr_run,run,ext_run] = fileparts(runs_names(hh,1).name);
            display (run)
            trial_names=rdir([path_data name '/' run '/timefreq_morlet*.mat'], '', '/storages/LDATA/BrainstormDB/NewProcedure_OtherConnectivityMetrics/data');
            sFiles=cell(1,length(trial_names));
            for qq=1:length(trial_names)
                sFiles{1,qq}=(trial_names(qq,1).name);
            end
            sFiles_backup=sFiles;
            sFiles_new = bst_process('CallProcess', 'process_select_tag', sFiles, [], ...
                'tag',    'zscore', ...
                'search', 2, ...  % Search the file comments
                'select', 2);  % Select only the files without the tag
            sFiles_new = bst_process('CallProcess', 'process_select_tag', sFiles_new, [], ...
                'tag',    'ITPC', ...
                'search', 2, ...  % Search the file comments
                'select', 2);  % Select only the files without the tag
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            TagToAdd=['TF_Absolute_300_700'];
            display(['working on...' name '...' runs_names(hh,1).name '...' TagToAdd])
            
            % Start a new report
            bst_report('Start', sFiles);
            % Process: Extract values: [300ms,700ms] 38-42Hz
            sFiles = bst_process('CallProcess', 'process_extract_values', sFiles, [], ...
                'timewindow', [0.3, 0.7], ...
                'freqrange',  [38, 42], ...
                'rows',       '', ...
                'isabs',      0, ...
                'avgtime',    1, ...
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
                'tag',    'Projected_TF_Absolute', ...
                'output', 1);  % Add to comment
            % Process: Spatial smoothing (10.00)
            sFiles = bst_process('CallProcess', 'process_ssmooth_surfstat', sFiles, [], ...
                'fwhm',      10, ...
                'overwrite', 0);
            % Save and display report
            ReportFile = bst_report('Save', sFiles);
            bst_report('Open', ReportFile);
            % bst_report('Export', ReportFile, ExportDir);
        end
    end
end
