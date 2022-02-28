%% THIS IS A SCRIPT TO BE DONE MANUALLY, marking the removed components.
%% NOT DONE

%% 

% Mapping_clinical_DB
% 
% PSD: artefatto da 0 hz a 8 hz. Visibile con stessa topografia a 50 hz. Generic necessaria
% SSP cardiac = ok, rimossa component 1.
% SSP generic = [0-40s, 0-8 hz]. Rimossa component 1.
% Commento: dati abbastanza brutti.


%Meglio usare questa struttura

SSP = struct()

%%  first element
SSP(end).Subject = 'AF_01'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';

SSP(end+1).Subject = 'AF_02'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';

SSP(end+1).Subject = 'AF_03'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';


SSP(end).Subject = 'BO_01'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';

SSP(end+1).Subject = 'BO_02'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';

SSP(end+1).Subject = 'BO_03'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'nessun commento generale';



SSP(end+1).Subject = 'EM_01'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [0];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'cardiaco strano. non tolto. Oculare un po strano';

SSP(end+1).Subject = 'EM_02'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [0];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'cardiaco strano. non tolto. Oculare un po strano';

SSP(end+1).Subject = 'EM_03'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).cardiac = [0];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'cardiaco strano. non tolto. Oculare un po strano';

