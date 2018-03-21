clear all; close all; clc;

disp ('---------------')
% A=testbusted(1000000);
% writetable(A,'bustedtable.xls')
A=xlsread('bustedtable.xls');
n=20000;
% a=[8;5;5;2;3;2;7;7;8;7];
% a=.5;
ev=player(A,n,0);
% astore=a;
evstore=ev;
max=sum(ev)/13;
% while 1
%     a=a+.01;
%     ev=player(A,n,a);
%     if sum(ev)/13>max
%         max=sum(ev)/13;
%         astore=a;
%         evstore=ev;
%     else
%         a=a-.01;
%         break
%     end
% end
% while 1
%     a=a-.01;
%     ev=player(A,n,a);
%     if sum(ev)/13>max
%         max=sum(ev)/13;
%         astore=a;
%         evstore=ev;
%     else
%         a=a+.01;
%         break
%     end
% end
% max=sum(ev)/13;
% p1=1;
% while p1<11
%     a(p1)=a(p1)+1;
%     ev=player(A,n,a);
%     if sum(ev)/13>max
%         max=sum(ev)/13;
%         astore=a;
%         evstore=ev;
%     else
%         a(p1)=a(p1)-1;
%         p1=p1+1;
%     end
% end
% p1=1;
% while p1<11
%     a(p1)=a(p1)-1;
%     ev=player(A,n,a);
%     if sum(ev)/13>max
%         max=sum(ev)/13;
%         astore=a;
%         evstore=ev;
%     else
%         a(p1)=a(p1)+1;
%         p1=p1+1;
%     end
% end
for i=1:13
    fprintf([card(i),'  ',num2str(evstore(i)),'\n'])
end
fprintf('---\n')
fprintf(num2str(sum(evstore)/13))
fprintf('\n')

function ev=player(A,n,a)

evs=zeros(13,n);
for i=1:13
% i=10;
    for j=1:n
        p=zeros(1,11);
        pv=zeros(1,11);
        p(1)=drawdeck;
        p(2)=drawdeck;
        pv(2)=value(p(2));
        pv(1)=value(p(1));
        if bjack(pv(pv>0))
%             ps=card(p(p~=0));
%             disp (['player: ',ps,' BLACKJACK'])
            evs(i,j)=1*A(i,1)+2.5*(1-A(i,1));
        else
            surrender=0;
            t=3;
            while sumup(pv)<=11
                p(t)=drawdeck;
                pv(t)=value(p(t));
                t=t+1;
            end
            if i>9
                while sumup(pv)<=16 || sumup2(pv)<=7
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==9
                while sumup(pv)<=16 || sumup2(pv)<=8
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==8
                while sumup(pv)<=16 || sumup2(pv)<=7
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==7
                while sumup(pv)<=16 || sumup2(pv)<=7
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==6
                while sumup(pv)<=12 || sumup2(pv)<=2
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==5
                while sumup(pv)<=13 || sumup2(pv)<=3
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==4
                while sumup(pv)<=12 || sumup2(pv)<=2
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==3
                while sumup(pv)<=13 || sumup2(pv)<=5
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==2
                while sumup(pv)<=13 || sumup2(pv)<=5
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            elseif i==1
                while sumup(pv)<=17 || sumup2(pv)<=8
                    p(t)=drawdeck;
                    pv(t)=value(p(t));
                    t=t+1;
                end
            end
%             ps=card(p(p~=0));
%             disp (['player: ',ps,' sum=',num2str(sumup(pv))])
            if surrender==1
                evs(i,j)=.5;
            else
                if sumup(pv)>21
%                 disp('busted')
                    evs(i,j)=0;
                elseif sumup(pv)==21
                    evs(i,j)=2*(sum(A(i,2:5))+A(i,7))+1*A(i,6);
                elseif sumup(pv)==20
                    evs(i,j)=2*(sum(A(i,2:4))+A(i,7))+1*A(i,5);
                elseif sumup(pv)==19
                    evs(i,j)=2*(sum(A(i,2:3))+A(i,7))+1*A(i,4);
                elseif sumup(pv)==18
                    evs(i,j)=2*(A(i,2)+A(i,7))+1*A(i,3);
                elseif sumup(pv)==17
                    evs(i,j)=2*A(i,7)+1*A(i,2);
                elseif sumup(pv)<17
                    evs(i,j)=2*A(i,7);
                end
            end
            switch i
                case 1
                    evs(i,j)=evs(i,j)+a*12/13*2;
                case 2
                    evs(i,j)=evs(i,j)*(1+a*11/13)+a*11/13;
                case 3
                    evs(i,j)=evs(i,j)*(1+a*10/13)+a*10/13;
                case 4
                    evs(i,j)=evs(i,j)*(1+a*9/13)+a*9/13;
                case 5
                    evs(i,j)=evs(i,j)*(1+a*8/13)+a*8/13;
                case 6
                    evs(i,j)=evs(i,j)*(1+a*7/13)+a*7/13;
                case 7
                    evs(i,j)=evs(i,j)+a*6/13*2;
                case 8
                    evs(i,j)=evs(i,j)+a*5/13*2;
                case 9
                    evs(i,j)=evs(i,j)+a*4/13*2;
                case 10
                    evs(i,j)=evs(i,j)+a*3/13*2;
                case 11
                    evs(i,j)=evs(i,j)+a*2/13*2;
                case 12
                    evs(i,j)=evs(i,j)+a*1/13*2;           
                case 13
                    evs(i,j)=evs(i,j);          
            end
        end
    end
end
ev=sum(evs,2)/n/(1+a);
end

function A=testbusted(n)
bt=zeros(13,7);
for i=1:13
    for j=1:n
        t=2;
        d=zeros(1,11);
        dv=zeros(1,11);
        d(1)=i;
        dv(1)=value(d(1));
        while 1
            d(t)=drawdeck;
            dv(t)=value(d(t));
            if sumup(dv)<17
                t=t+1;
            else
                break
            end
        end
        
        if sumup(dv)==17
            bt(i,2)=bt(i,2)+1;
        elseif sumup(dv)==18
            bt(i,3)=bt(i,3)+1;
        elseif sumup(dv)==19
            bt(i,4)=bt(i,4)+1;
        elseif sumup(dv)==20
            bt(i,5)=bt(i,5)+1;
        elseif sumup(dv)==21
            if bjack(dv(dv>0))
                bt(i,1)=bt(i,1)+1;
            else
                bt(i,6)=bt(i,6)+1;
            end
        elseif sumup(dv)>21
            bt(i,7)=bt(i,7)+1;
        end
    end
end
bt=bt/n;
A=array2table(bt,'variablenames',{'BLACKJACK','SUM17','SUM18','SUM19','SUM20','SUM21','BUSTED'});
end

function normal
for i=1:13
    d=zeros(1,11);
    p=zeros(1,11);
    dv=zeros(1,11);
    pv=zeros(1,11);
    ev=0;
    d(1)=i;
	dv(1)=value(d(1));
    p(1)=drawdeck;
    p(2)=drawdeck;
    pv(2)=value(p(2));
    pv(1)=value(p(1));
    ds=card(d(d~=0));
    ps=card(p(p~=0));
    if bjack(pv(pv>0))
        d(2)=drawdeck;
        dv(2)=value(d(2));
        ds=card(d(d~=0));
        disp (['player: ',ps,' BLACKJACK'])
        if bjack(dv(dv>0))
            disp (['dealer: ',ds,' BLACKJACK'])
            ev=1;
        else
            disp (['dealer: ',ds])
            ev=2.5;
        end
    else
        disp (['player: ',ps,' sum=',num2str(sumup(pv))])
        t=2;
        while 1
            d(t)=drawdeck;
            dv(t)=value(d(t));
            if sumup(dv)<17
                t=t+1;
            else
                break
            end
        end
        ds=card(d(d~=0));
        fprintf (['dealer: ',ds,' sum=',num2str(sumup(dv)),'\n'])
        if sumup(dv)>21
            fprintf('Dealer Busted.\n')
            ev=2;
        elseif sumup(dv)>sumup(pv)
            fprintf('Dealer Win.\n')
            ev=0;
        elseif sumup(dv)<sumup(pv)
            fprintf('Player Win.\n')
            ev=2;
        elseif sumup(dv)==sumup(pv)    
            fprintf('Even.\n')
            ev=1;
        end
       
    end
    disp (['EV: ',num2str(ev)])
    disp ('---------------')
end
end

function a=drawdeck
    a=floor(rand*13+1);
end

function a=value(b)
    if b>=10
        a=10;
    else
        a=b;
    end
end

function a=sumup(b)
    if length(b(b==1))>0
        a=sum(b);
        if a<=11
            a=a+10;
        end
    else
        a=sum(b);
    end
end

function a=sumup2(b)
    a=sum(b);
end

function t=bjack(a)
    if length(a)==2 && ((a(1)==1 && a(2)==10) || (a(2)==1 && a(1)==10))
        t=1;
    else
        t=0;
    end
end

function s=card(a)
    s=[];
    for i=1:length(a)
        switch a(i)
            case 10
                s(i)='T';
            case 11
                s(i)='J';
            case 12
                s(i)='Q';
            case 13
                s(i)='K';
            case 1
                s(i)='A';
            otherwise
                s(i)=num2str(a(i));
        end
    end
end