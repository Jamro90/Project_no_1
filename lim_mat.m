clear
clc

%% dziedzina i wzór ciągu
x = (0:1:999);                      % wyznaczenie dziedziny
data = load("data.dat");            % załadowanie danych
y = data;

%% wykres a_n
plot(x,y,"ob");
title("wykres");

%% configuracja wykresu
xlabel("oś x");
ylabel("oś y");

%% ciąg zmierza do 
disp(["lim a_n = " + num2str(max(y)) + "\n"]);  % wynik granicy

