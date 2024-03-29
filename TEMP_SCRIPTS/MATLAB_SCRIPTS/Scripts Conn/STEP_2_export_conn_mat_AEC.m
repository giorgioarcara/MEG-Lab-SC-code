% Script generated by Brainstorm (10-Jan-2018)
%% PRELIMINARY PREPARATION
clear

%% ADD FUNCTIONS
addpath('/storages/LDATA/Giorgio/TDCS MEG Exp1 Graph Theory analysis/Scripts/functions')


%% GET CURRENT SCRIPT NAME

script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

%%
% Input files
my_sFiles_ini = {...
    'Subject01_A/S001_ISRRestingEC_20170220_01_resample/timefreq_connectn_aec_180125_1156_pre.mat', ...
    'Subject01_A/S001_ISRRestingEC_20170220_02_resample/timefreq_connectn_aec_180125_1202_post.mat', ...
    'Subject01_B/TDCSS001_ISRRestingEC_20170221_01_resample/timefreq_connectn_aec_180125_1207_pre.mat', ...
    'Subject01_B/TDCSS001_ISRRestingEC_20170221_02_resample/timefreq_connectn_aec_180125_1213_post.mat', ...
    'Subject02_A/TDCSS002_ISRRestingEC_20170220_01_resample/timefreq_connectn_aec_180125_1219_pre.mat', ...
    'Subject02_A/TDCSS002_ISRRestingEC_20170220_02_resample/timefreq_connectn_aec_180125_1225_post.mat', ...
    'Subject02_B/TDCSS002_ISRRestingEC_20170220_03_resample/timefreq_connectn_aec_180125_1231_pre.mat', ...
    'Subject02_B/TDCSS002_ISRRestingEC_20170220_04_resample/timefreq_connectn_aec_180125_1236_post.mat', ...
    'Subject03_A/TDCSS003_ISRRestingEC_20170221_01_resample_02/timefreq_connectn_aec_180125_1242_pre.mat', ...
    'Subject03_A/TDCSS003_ISRRestingEC_20170221_02_resample_02/timefreq_connectn_aec_180125_1248_post.mat', ...
    'Subject03_B/TDCSS003_ISRRestingEC_20170222_01_resample_02/timefreq_connectn_aec_180125_1254_pre.mat', ...
    'Subject03_B/TDCSS003_ISRRestingEC_20170222_02_resample_02/timefreq_connectn_aec_180125_1300_post.mat', ...
    'Subject04_A/TDCSS004_ISRRestingEC_20170222_01_resample_02/timefreq_connectn_aec_180125_1305_pre.mat', ...
    'Subject04_A/TDCSS004_ISRRestingEC_20170222_02_resample_02/timefreq_connectn_aec_180125_1311_post.mat', ...
    'Subject04_B/TDCSS004_ISRRestingEC_20170222_03_resample_02/timefreq_connectn_aec_180125_1317_pre.mat', ...
    'Subject04_B/TDCSS004_ISRRestingEC_20170222_04_resample/timefreq_connectn_aec_180125_1323_post.mat', ...
    'Subject05_A/TDCSS005_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180125_1328_pre.mat', ...
    'Subject05_A/TDCSS005_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180125_1333_post.mat', ...
    'Subject05_B/TDCSS005_ISRRestingEC_20170301_01_resample/timefreq_connectn_aec_180125_1338_pre.mat', ...
    'Subject05_B/TDCSS005_ISRRestingEC_20170301_02_resample/timefreq_connectn_aec_180125_1344_post.mat', ...
    'Subject06_A/TDCSS006_ISRRestingEC_20170223_01_resample/timefreq_connectn_aec_180125_1350_pre.mat', ...
    'Subject06_A/TDCSS006_ISRRestingEC_20170223_02_resample/timefreq_connectn_aec_180125_1356_post.mat', ...
    'Subject06_B/TDCSS006_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180125_1402_pre.mat', ...
    'Subject06_B/TDCSS006_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180125_1407_post.mat', ...
    'Subject07_A/TDCSS007_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180125_1413_pre.mat', ...
    'Subject07_A/TDCSS007_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180125_1418_post.mat', ...
    'Subject07_B/TDCSS007_ISRRestingEC_20170303_01_resample/timefreq_connectn_aec_180125_1425_pre.mat', ...
    'Subject07_B/TDCSS007_ISRRestingEC_20170303_02_resample/timefreq_connectn_aec_180125_1432_post.mat', ...
    'Subject08_A/TDCSS008_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180125_1438_pre.mat', ...
    'Subject08_A/TDCSS008_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180125_1445_post.mat', ...
    'Subject08_B/TDCSS008_ISRRestingEC_20170227_03_resample/timefreq_connectn_aec_180125_1452_pre.mat', ...
    'Subject08_B/TDCSS008_ISRRestingEC_20170227_04_resample/timefreq_connectn_aec_180124_0959.mat', ...
    'Subject08_B/TDCSS008_ISRRestingEC_20170227_04_resample/timefreq_connectn_aec_180125_1459_post.mat', ...
    'Subject09_A/TDCSS009_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180125_1505_pre.mat', ...
    'Subject09_A/TDCSS009_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180125_1513_post.mat', ...
    'Subject09_B/TDCSS009_ISRRestingEC_20170302_01_resample/timefreq_connectn_aec_180125_1520_pre.mat', ...
    'Subject09_B/TDCSS009_ISRRestingEC_20170302_02_resample/timefreq_connectn_aec_180125_1526_post.mat', ...
    'Subject10_A/TDCSS010_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180125_1533_pre.mat', ...
    'Subject10_A/TDCSS010_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180125_1539_post.mat', ...
    'Subject10_B/TDCSS010_ISRRestingEC_20170420_01_resample/timefreq_connectn_aec_180125_1546_pre.mat', ...
    'Subject10_B/TDCSS010_ISRRestingEC_20170420_02_resample/timefreq_connectn_aec_180125_1552_post.mat', ...
    'Subject11_A/TDCSS011_ISRRestingEC_20170301_01_resample/timefreq_connectn_aec_180125_1559_pre.mat', ...
    'Subject11_A/TDCSS011_ISRRestingEC_20170301_02_resample/timefreq_connectn_aec_180125_1607_post.mat', ...
    'Subject11_B/TDCSS011_ISRRestingEC_20170306_01_resample/timefreq_connectn_aec_180125_1614_pre.mat', ...
    'Subject11_B/TDCSS011_ISRRestingEC_20170306_02_resample/timefreq_connectn_aec_180125_1619_post.mat', ...
    'Subject12_A/TDCSS012_ISRRestingEC_20170410_01_resample/timefreq_connectn_aec_180125_1626_pre.mat', ...
    'Subject12_A/TDCSS012_ISRRestingEC_20170410_02_resample/timefreq_connectn_aec_180125_1633_post.mat', ...
    'Subject12_B/TDCSS012_ISRRestingEC_20170411_01_resample/timefreq_connectn_aec_180125_1639_pre.mat', ...
    'Subject12_B/TDCSS012_ISRRestingEC_20170411_02_resample/timefreq_connectn_aec_180125_1644_post.mat', ...
    'Subject13_A/TDCSS013_ISRRestingEC_20170411_01_resample/timefreq_connectn_aec_180125_1649_pre.mat', ...
    'Subject13_A/TDCSS013_ISRRestingEC_20170411_02_resample/timefreq_connectn_aec_180125_1655_post.mat', ...
    'Subject13_B/TDCSS013_ISRRestingEC_20170412_01_resample/timefreq_connectn_aec_180125_1700_pre.mat', ...
    'Subject13_B/TDCSS013_ISRRestingEC_20170412_02_resample/timefreq_connectn_aec_180125_1706_post.mat', ...
    'Subject14_A/TDCSS014_ISRRestingEC_20170420_01_resample/timefreq_connectn_aec_180125_1711_pre.mat', ...
    'Subject14_A/TDCSS014_ISRRestingEC_20170420_02_resample/timefreq_connectn_aec_180125_1717_post.mat', ...
    'Subject14_B/TDCSS014_ISRRestingEC_20170421_01_resample/timefreq_connectn_aec_180125_1722_pre.mat', ...
    'Subject14_B/TDCSS014_ISRRestingEC_20170421_02_resample/timefreq_connectn_aec_180125_1727_post.mat', ...
    'Subject15_A/TDCSS015_ISRRestingEC_20170424_01_resample/timefreq_connectn_aec_180125_1733_pre.mat', ...
    'Subject15_A/TDCSS015_ISRRestingEC_20170424_02_resample/timefreq_connectn_aec_180125_1738_post.mat', ...
    'Subject15_B/TDCSS015_ISRRestingEC_20170426_01_resample/timefreq_connectn_aec_180125_1744_pre.mat', ...
    'Subject15_B/TDCSS015_ISRRestingEC_20170426_02_resample/timefreq_connectn_aec_180125_1749_post.mat'};


sFiles = my_sFiles_ini;

cd('/storages/LDATA/Giorgio/TDCS MEG Exp1 Graph Theory analysis/Conn_mat')
% Start a new report
bst_report('Start', sFiles);

% Process: export connectivity matrix in .mat format
sFiles = bst_process('CallProcess', 'process_export_conn_mat', sFiles, [], ...
    'chars',        50, ...
    'base',         '', ...
    'BaseOver',     0, ...
    'Num',          1);

% Save and display report
ReportFile = bst_report('Save', sFiles);
bst_report('Open', ReportFile);
% bst_report('Export', ReportFile, ExportDir);


script_name = mfilename('fullpath')

if (length(script_name) == 0)
    error('You must run this script by calling it from the prompt or clicking the Run button!')
end

export_script(script_name, my_sFiles_ini)

