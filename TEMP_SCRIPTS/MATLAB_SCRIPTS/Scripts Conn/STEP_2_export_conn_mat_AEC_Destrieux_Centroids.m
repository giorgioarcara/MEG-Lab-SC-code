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
    'Subject01_A/S001_ISRRestingEC_20170220_01_resample/timefreq_connectn_aec_180213_2349_pre_CentrDestr.mat', ...
    'Subject01_A/S001_ISRRestingEC_20170220_02_resample/timefreq_connectn_aec_180213_2356_post_CentrDestr.mat', ...
    'Subject01_B/TDCSS001_ISRRestingEC_20170221_01_resample/timefreq_connectn_aec_180214_0004_pre_CentrDestr.mat', ...
    'Subject01_B/TDCSS001_ISRRestingEC_20170221_02_resample/timefreq_connectn_aec_180214_0011_post_CentrDestr.mat', ...
    'Subject02_A/TDCSS002_ISRRestingEC_20170220_01_resample/timefreq_connectn_aec_180214_0018_pre_CentrDestr.mat', ...
    'Subject02_A/TDCSS002_ISRRestingEC_20170220_02_resample/timefreq_connectn_aec_180214_0026_post_CentrDestr.mat', ...
    'Subject02_B/TDCSS002_ISRRestingEC_20170220_03_resample/timefreq_connectn_aec_180214_0033_pre_CentrDestr.mat', ...
    'Subject02_B/TDCSS002_ISRRestingEC_20170220_04_resample/timefreq_connectn_aec_180214_0040_post_CentrDestr.mat', ...
    'Subject04_A/TDCSS004_ISRRestingEC_20170222_01_resample_02/timefreq_connectn_aec_180214_0048_pre_CentrDestr.mat', ...
    'Subject04_A/TDCSS004_ISRRestingEC_20170222_02_resample_02/timefreq_connectn_aec_180214_0055_post_CentrDestr.mat', ...
    'Subject04_B/TDCSS004_ISRRestingEC_20170222_03_resample_02/timefreq_connectn_aec_180214_0103_pre_CentrDestr.mat', ...
    'Subject04_B/TDCSS004_ISRRestingEC_20170222_04_resample/timefreq_connectn_aec_180214_0110_post_CentrDestr.mat', ...
    'Subject05_A/TDCSS005_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180214_0118_pre_CentrDestr.mat', ...
    'Subject05_A/TDCSS005_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180214_0123_post_CentrDestr.mat', ...
    'Subject05_B/TDCSS005_ISRRestingEC_20170301_01_resample/timefreq_connectn_aec_180214_0130_pre_CentrDestr.mat', ...
    'Subject05_B/TDCSS005_ISRRestingEC_20170301_02_resample/timefreq_connectn_aec_180214_0138_post_CentrDestr.mat', ...
    'Subject06_A/TDCSS006_ISRRestingEC_20170223_01_resample/timefreq_connectn_aec_180214_0145_pre_CentrDestr.mat', ...
    'Subject06_A/TDCSS006_ISRRestingEC_20170223_02_resample/timefreq_connectn_aec_180214_0153_post_CentrDestr.mat', ...
    'Subject06_B/TDCSS006_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180214_0200_pre_CentrDestr.mat', ...
    'Subject06_B/TDCSS006_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180214_0208_post_CentrDestr.mat', ...
    'Subject07_A/TDCSS007_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180214_0216_pre_CentrDestr.mat', ...
    'Subject07_A/TDCSS007_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180214_0223_post_CentrDestr.mat', ...
    'Subject07_B/TDCSS007_ISRRestingEC_20170303_01_resample/timefreq_connectn_aec_180214_0231_pre_CentrDestr.mat', ...
    'Subject07_B/TDCSS007_ISRRestingEC_20170303_02_resample/timefreq_connectn_aec_180214_0238_post_CentrDestr.mat', ...
    'Subject08_A/TDCSS008_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180214_0245_pre_CentrDestr.mat', ...
    'Subject08_A/TDCSS008_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180214_0253_post_CentrDestr.mat', ...
    'Subject08_B/TDCSS008_ISRRestingEC_20170227_03_resample/timefreq_connectn_aec_180214_0300_pre_CentrDestr.mat', ...
    'Subject08_B/TDCSS008_ISRRestingEC_20170227_04_resample/timefreq_connectn_aec_180214_0308_post_CentrDestr.mat', ...
    'Subject09_A/TDCSS009_ISRRestingEC_20170227_01_resample/timefreq_connectn_aec_180214_0314_pre_CentrDestr.mat', ...
    'Subject09_A/TDCSS009_ISRRestingEC_20170227_02_resample/timefreq_connectn_aec_180214_0322_post_CentrDestr.mat', ...
    'Subject09_B/TDCSS009_ISRRestingEC_20170302_01_resample/timefreq_connectn_aec_180214_0329_pre_CentrDestr.mat', ...
    'Subject09_B/TDCSS009_ISRRestingEC_20170302_02_resample/timefreq_connectn_aec_180214_0336_post_CentrDestr.mat', ...
    'Subject10_A/TDCSS010_ISRRestingEC_20170228_01_resample/timefreq_connectn_aec_180214_0344_pre_CentrDestr.mat', ...
    'Subject10_A/TDCSS010_ISRRestingEC_20170228_02_resample/timefreq_connectn_aec_180214_0351_post_CentrDestr.mat', ...
    'Subject10_B/TDCSS010_ISRRestingEC_20170420_01_resample/timefreq_connectn_aec_180214_0359_pre_CentrDestr.mat', ...
    'Subject10_B/TDCSS010_ISRRestingEC_20170420_02_resample/timefreq_connectn_aec_180214_0406_post_CentrDestr.mat', ...
    'Subject11_A/TDCSS011_ISRRestingEC_20170301_01_resample/timefreq_connectn_aec_180214_0414_pre_CentrDestr.mat', ...
    'Subject11_A/TDCSS011_ISRRestingEC_20170301_02_resample/timefreq_connectn_aec_180214_0422_post_CentrDestr.mat', ...
    'Subject11_B/TDCSS011_ISRRestingEC_20170306_01_resample/timefreq_connectn_aec_180214_0429_pre_CentrDestr.mat', ...
    'Subject11_B/TDCSS011_ISRRestingEC_20170306_02_resample/timefreq_connectn_aec_180214_0435_post_CentrDestr.mat', ...
    'Subject12_A/TDCSS012_ISRRestingEC_20170410_01_resample/timefreq_connectn_aec_180214_0442_pre_CentrDestr.mat', ...
    'Subject12_A/TDCSS012_ISRRestingEC_20170410_02_resample/timefreq_connectn_aec_180214_0450_post_CentrDestr.mat', ...
    'Subject12_B/TDCSS012_ISRRestingEC_20170411_01_resample/timefreq_connectn_aec_180214_0457_pre_CentrDestr.mat', ...
    'Subject12_B/TDCSS012_ISRRestingEC_20170411_02_resample/timefreq_connectn_aec_180214_0505_post_CentrDestr.mat', ...
    'Subject13_A/TDCSS013_ISRRestingEC_20170411_01_resample/timefreq_connectn_aec_180214_0512_pre_CentrDestr.mat', ...
    'Subject13_A/TDCSS013_ISRRestingEC_20170411_02_resample/timefreq_connectn_aec_180214_0520_post_CentrDestr.mat', ...
    'Subject13_B/TDCSS013_ISRRestingEC_20170412_01_resample/timefreq_connectn_aec_180214_0527_pre_CentrDestr.mat', ...
    'Subject13_B/TDCSS013_ISRRestingEC_20170412_02_resample/timefreq_connectn_aec_180214_0534_post_CentrDestr.mat', ...
    'Subject14_A/TDCSS014_ISRRestingEC_20170420_01_resample/timefreq_connectn_aec_180214_0542_pre_CentrDestr.mat', ...
    'Subject14_A/TDCSS014_ISRRestingEC_20170420_02_resample/timefreq_connectn_aec_180214_0550_post_CentrDestr.mat', ...
    'Subject14_B/TDCSS014_ISRRestingEC_20170421_01_resample/timefreq_connectn_aec_180214_0558_pre_CentrDestr.mat', ...
    'Subject14_B/TDCSS014_ISRRestingEC_20170421_02_resample/timefreq_connectn_aec_180214_0605_post_CentrDestr.mat', ...
    'Subject15_A/TDCSS015_ISRRestingEC_20170424_01_resample/timefreq_connectn_aec_180214_0612_pre_CentrDestr.mat', ...
    'Subject15_A/TDCSS015_ISRRestingEC_20170424_02_resample/timefreq_connectn_aec_180214_0620_post_CentrDestr.mat', ...
    'Subject15_B/TDCSS015_ISRRestingEC_20170426_01_resample/timefreq_connectn_aec_180214_0628_pre_CentrDestr.mat', ...
    'Subject15_B/TDCSS015_ISRRestingEC_20170426_02_resample/timefreq_connectn_aec_180214_0634_post_CentrDestr.mat'};


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
