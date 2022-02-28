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
SSP(end).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '1';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

SSP(end+1).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '2';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

%%  first element
SSP(end+1).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '3';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

SSP(end+1).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '4';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

SSP(end+1).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '5';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

SSP(end+1).Subject = 'MAP001'; % note that here is just 'end'. For the other elements is 'end+1'
SSP(end).run = '6';
SSP(end).cardiac = [1];
SSP(end).blink = [1];
SSP(end).cardiac_comment = '';
SSP(end).Comment = 'lil blink e un po strano come topografia probabilmente per gli occhi semichiusi del soggetto';

