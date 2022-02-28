%% ASSR (version 2.0)

% Authors: Matteo, Maran, Giorgio Arcara, Giovanni Pellegrino.
% Standard settings 
Fs = 44100; 
Fc = 1000; 
Fm = 40; 
modulation_depth = 0;


length_sound = 1; %Duration of sound = 1 sec 
ISI = 1;                      %ISI = 1 sec       
t = [1/Fs:1/Fs:length_sound]-1/Fs; 

ASSR(1:Fs.*length_sound) = 0;
ASSR(1:Fs.*length_sound) = sin(2 .*pi .*Fc .*t) .*(1 + modulation_depth .* cos(2 .*pi .* Fm .*t));

%Fade in and fade out of 6 ms
faded_ASSR = ASSR;
fade_duration = .006;
fade_in=linspace(0,1,fade_duration .*Fs);
fade_out=linspace(1,0,(fade_duration .*Fs));
faded_ASSR(1:length(fade_in))= faded_ASSR(1:length(fade_in)).*fade_in;
faded_ASSR(end-length(fade_out)+1:end)= faded_ASSR(end-length(fade_out)+1:end).*fade_out;

%My sound = ASSR (1 sec) + 1 sec of silence
my_sound(1:(Fs.*(length_sound+ISI))) = 0;% Initialize variable
my_sound(1:length_sound*Fs) = faded_ASSR;

% %Remove clipping
my_sound_no_clip= my_sound./(max(abs(my_sound(:))));

% Write file
file_name = strcat('ASSR_1000Hz_',num2str(Fc),'_',num2str(Fm),'_',num2str(modulation_depth),'.wav');
audiowrite(file_name, my_sound_no_clip, Fs);