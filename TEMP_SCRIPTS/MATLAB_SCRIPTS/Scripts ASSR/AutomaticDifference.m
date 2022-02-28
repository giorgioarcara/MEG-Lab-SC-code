% Automatic Difference
addpath ('/storages/LDATA/Code/brainstorm3')
addpath ('/storages/LDATA/Code/Scripts ASSR')

if ~brainstorm('status')
    brainstorm nogui
end
ProtocolName = 'OtherConnectivityMetrics_tDCS_ASSR';
% Get the protocol index
iProtocol = bst_get('Protocol', ProtocolName);
if isempty(iProtocol)
    error(['Unknown protocol: ' ProtocolName]);
end
% Select the current procotol
gui_brainstorm('SetCurrentProtocol', iProtocol);

path_data='/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data/';
fnames = dir('/storages/LDATA/BrainstormDB/OtherConnectivityMetrics_tDCS_ASSR/data/Subject*');

Labels={...
    'AEC: Left_SM1, mean after | _active | matlab', ...
    'AEC: Right_SM1, mean after | _active | matlab', ...
    'AEC: ASSR_Right, mean after | _active | matlab', ...
    'AEC: ASSR_Left, mean after | _active | matlab', ...
    'Corr: Left_SM1, mean after | _active | matlab', ...
    'Corr: Right_SM1, mean after | _active | matlab', ...
    'Corr: ASSR_Right, mean after | _active | matlab', ...
    'Corr: ASSR_Left, mean after | _active | matlab', ...
    'Envelope: Left_SM1, mean after | _active | matlab', ...
    'Envelope: Right_SM1, mean after | _active | matlab', ...
    'Envelope: ASSR_Right, mean after | _active | matlab', ...
    'Envelope: ASSR_Left, mean after | _active | matlab', ...
    'PLV: Left_SM1, mean after | _active | matlab', ...
    'PLV: Right_SM1, mean after | _active | matlab', ...
    'PLV: ASSR_Right, mean after | _active | matlab', ...
    'PLV: ASSR_Left, mean after | _active | matlab'};

%SHAM
for gg=1:length(fnames) %run over patients
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runnames = dir([path_data name '/SHAM_P*']);
    for zz=1:length(runnames)
        if runnames(zz).name=='REAL_POST' || runnames(zz)=='SHAM_POST'
            runs_names_A = dir([path_data name '/*_POST']);
        end
             if runnames(zz).name=='REAL_PRE' || runnames(zz)=='SHAM_PRE'
            runs_names_A = dir([path_data name '/*_POST']);
             end

    end
    runs_names_B = dir([path_data name '/*_PRE']);
    [pathstr_run_A,run_A,ext_run_A] = fileparts(runs_names_A.name);
    [pathstr_run_B,run_B,ext_run_B] = fileparts(runs_names_B.name);
    display(run_A)
    display(run_B)
    data_names_A=dir([path_data name '/' run_A '/timefreq_connect1*']); %find all timefrequency files of the run
    data_names_B=dir([path_data name '/' run_B '/timefreq_connect1*']); %find all timefrequency files of the run
        for ff=1:size(data_names_A,1)
            sFiles_A(1,ff)={['/' name '/' run_A '/' data_names_A(ff,1).name]};
        end
        for hh=1:size(data_names_B,1)
            sFiles_B(1,hh)={['/' name '/' run_B '/' data_names_B(hh,1).name]};
        end
    for pp=1:length(Labels)
        
        % Select files
        try
            GroupA = bst_process('CallProcess', 'process_select_tag', sFiles_A, [], ...
                'tag',    Labels{1,pp}, ...
                'search', 2, ...  % Search the file comments
                'select', 1);
            FilesGroupA={GroupA(1,:).FileName};
        catch
            warning(['Problem with GroupA files...' name ' ' run_A ' ' Labels{1,pp}]);
        end
        try
            GroupB = bst_process('CallProcess', 'process_select_tag', sFiles_B, [], ...
                'tag',    Labels{1,pp}, ...
                'search', 2, ...  % Search the file comments
                'select', 1);
            FilesGroupB={GroupB(1,:).FileName};
        catch
            warning(['Problem with GroupB files' name ' ' run ' ' Labels{1,pp}]);
        end
        try
            % Difference
            sFiles = bst_process('CallProcess', 'process_diff_ab', FilesGroupA, FilesGroupB);
        catch
            warning(['Problem with difference...' name run_A]);
        end
        clear FilesGroupA FilesGroupB GroupA GroupB sFiles
    end
    clear sFiles_A sFiles_B 
end

%REAL
for gg=1:length(fnames) %run over patients
    [pathstr,name,ext] = fileparts(fnames(gg,1).name);
    display(name)
    runnames = dir([path_data name '/SHAM_P*']);
    for zz=1:length(runnames)
        if runnames(zz).name=='REAL_POST' || runnames(zz)=='SHAM_POST'
            runs_names_A = dir([path_data name '/*_POST']);
        end
             if runnames(zz).name=='REAL_PRE' || runnames(zz)=='SHAM_PRE'
            runs_names_A = dir([path_data name '/*_POST']);
             end

    end
    runs_names_B = dir([path_data name '/*_PRE']);
    [pathstr_run_A,run_A,ext_run_A] = fileparts(runs_names_A.name);
    [pathstr_run_B,run_B,ext_run_B] = fileparts(runs_names_B.name);
    display(run_A)
    display(run_B)
    data_names_A=dir([path_data name '/' run_A '/timefreq_connect1*']); %find all timefrequency files of the run
    data_names_B=dir([path_data name '/' run_B '/timefreq_connect1*']); %find all timefrequency files of the run
        for ff=1:size(data_names_A,1)
            sFiles_A(1,ff)={['/' name '/' run_A '/' data_names_A(ff,1).name]};
        end
        for hh=1:size(data_names_B,1)
            sFiles_B(1,hh)={['/' name '/' run_B '/' data_names_B(hh,1).name]};
        end
    for pp=1:length(Labels)
        
        % Select files
        try
            GroupA = bst_process('CallProcess', 'process_select_tag', sFiles_A, [], ...
                'tag',    Labels{1,pp}, ...
                'search', 2, ...  % Search the file comments
                'select', 1);
            FilesGroupA={GroupA(1,:).FileName};
        catch
            warning(['Problem with GroupA files...' name ' ' run_A ' ' Labels{1,pp}]);
        end
        try
            GroupB = bst_process('CallProcess', 'process_select_tag', sFiles_B, [], ...
                'tag',    Labels{1,pp}, ...
                'search', 2, ...  % Search the file comments
                'select', 1);
            FilesGroupB={GroupB(1,:).FileName};
        catch
            warning(['Problem with GroupB files' name ' ' run ' ' Labels{1,pp}]);
        end
        try
            % Difference
            sFiles = bst_process('CallProcess', 'process_diff_ab', FilesGroupA, FilesGroupB);
        catch
            warning(['Problem with difference...' name run_A]);
        end
        clear FilesGroupA FilesGroupB GroupA GroupB sFiles
    end
    clear sFiles_A sFiles_B 
end


