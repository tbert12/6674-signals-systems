% Primer programa en Matlab

% ** Curso 1 Seniales y Sistemas - FIUBA **


clc,clear all % Limpiamos la pantalla y borramos todas las variables


%% Coseno discreto

n = 0:19;
Omega = 2*pi/5;
y1 = cos(Omega*n); % Frec Omega=2pi/5

figure
stem(n,y1)



%% Coseno continuo muestreado

fs = 20;        % frec de muestreo
f0 = 2;         % frec coseno [Hz]
T = 5;          % duracion del coseno [s]
t = 0:1/fs:T;   % eje temporal. El paso es 1/fs

y2 = cos(2*pi*f0*t); % señal muestreada

% Ploteo señales superpuestas usando stem y plot

figure,stem(t,y2)
hold on,plot(t,y2,'r')
xlabel 'Tiempo [s]'
legend('Stem','Plot')



%% DFT del coseno

Y = fft(y1);    % hago la DFT (muestras de la T.F entre 0 y 2pi)
Y_abs = abs(Y); % tomo el valor absoluto de la DFT (es compleja)
Y_eje = 0:2*pi/20:2*pi*19/20; % defino el eje x para el grafico

figure,stem(Y_eje,Y_abs)


%% Espectrograma


% Defino 2 cosenos con frecuencias f1 y f2 y duracion T, y
% los concateno en el vector y

T = 10;
fs = 1000; % elijo fs suficientemente alta
t = 0:1/fs:T;

f1 = 100;
y1 = cos(2*pi*f1*t);

f2 = 200;
y2 = cos(2*pi*f2*t);

y = [y1,y2];  % concateno ambos vectores

% Realizo el espectrograma
% S = SPECTROGRAM(X,WINDOW,NOVERLAP,NFFT,Fs) 
%   X: vector con muestras de la senial
%   WINDOW: ventana del espectrograma (vector o numero de muestras)
%   NOVERLAP: cant de muestras q se solapan las ventanas
%   NFFT: cant de muestras con las que hace la FFT (poner [] para default)
%   FS: frecuencia de muestreo del vector X (pone el eje horizontal del
%       espectrograma en [s] y el vertical en [Hz]

%   Nota: poner 'yaxis' como ultimo argumento pone el eje de tiempo como
%   horizontal. Si no, queda es vertical por defaut.

w1 = hamming(400);  % ventana hamming

figure, SPECTROGRAM(y,w1,200,[],fs,'yaxis') %EN OCTAVE ES OTRA
title 'Espectrograma con Hamming'
caxis([-60 0])      % modifico el color axis para verlo mejor

w2 = boxcar(400);   % ventana cuadrada

figure, spectrogram(y,w2,200,[],fs,'yaxis')

title 'Espectrograma con Boxcar'

caxis([-60 0])

% Nota: explorar los espectrogramas con el boton Rotate 3D de la ventana
% de la figura

% Visualizo la senial y su espectro para comparar

figure,plot(y)

Y = fft(y);

Y_eje = linspace(0,2*pi,length(Y));

figure,plot(Y_eje,abs(Y))





%% Otros espectrogramas (ejemplo tomado de "help spectrogram")



% Spectrogram of linear chirp

t=0:0.001:2;                    % 2 secs @ 1kHz sample rate

y=chirp(t,100,1,200);       % Start @ 100Hz, cross 200Hz at t=1sec

spectrogram(y,kaiser(128,18),120,128,1E3,'yaxis');

title('Linear Chirp: start at 100Hz and cross 200Hz at t=1sec');



% Waterfall display of the PSD of each segment of a VCO

Fs = 10e3;

t = 0:1/Fs:2;

x1 = vco(sawtooth(2*pi*t,0.5),[0.1 0.4]*Fs,Fs);

spectrogram(x1,kaiser(256,5),220,512,Fs);

view(-45,65)

colormap bone



% Ejemplos de imagenes embebidas en espectrogramas de canciones:

%   http://twistedsifter.com/2013/01/hidden-images-embedded-into-songs-spectrographs/



%% Espectros de ventanas

% Otras ventanas que trae el Matlab:

%    bartlett, blackman, boxcar, chebwin, hamming, hann, kaiser, triang.



Nw = 200;    % cant de puntos de la ventana

nfft = 1024; % cant de puntos con que hago la fft (>Nw)



w = hanning(Nw);

W_dB = 20*log10(fftshift(abs(fft(w,nfft)))); % espectro en [dB]



w_eje = linspace(-1,1,nfft); % eje de frecuencias normalizado de -1 a 1 en vez de -pi a pi



figure

subplot(1,2,1),plot(w), xlabel 'Muestras',title 'Ventana'

subplot(1,2,2),plot(w_eje,W_dB), xlabel 'Frec normalizada',title 'Espectro [dB]'



% FIN DEL CODIGO