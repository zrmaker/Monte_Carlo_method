clear all; close all; clc;

deck=ones(52,1)*1:52;

n=1:15;
x=n./(47-2.*n);
y=n.*(1+2.*x)./(46-2.*n);
y1=n./(46-2.*n);
xtext=cellstr(num2str(x','%.4f'));

plot(n,x);
hold on;
scatter(n,x,10,'filled','MarkerEdgeColor',[0    0.4470    0.7410],'MarkerFaceColor',[0    0.4470    0.7410]);
% plot(n,y);
% plot(n,y1);
grid on;
grid minor;
text(n+.1,x-.01,xtext);