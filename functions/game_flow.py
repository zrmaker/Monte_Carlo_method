import numpy as np
import pandas as pd
import os
from deck import *

class spanish21:
    def __init__(self, num_playing_pots = 1):
        self.dealer_hit_soft_17 = 1
        self.min_bet = 10.
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.hard = np.genfromtxt((os.path.dirname(self.dir_path)+'/inputs/spanish21_hard.csv'), delimiter=',')
        self.soft = np.genfromtxt((os.path.dirname(self.dir_path)+'/inputs/spanish21_soft.csv'), delimiter=',')
        self.num_pots = num_playing_pots
        self.hit_dict = {
            1.0 : 'hit', 2.0 : 'stand', 3.0 : 'double', 4.0 : 'surrender', 5.0 : 'split'
        }
        self.dealers = []
        self.sum_dealers = []
        self.players = dict.fromkeys(np.arange(self.num_pots))
        self.sum_players = dict.fromkeys(np.arange(self.num_pots))
        self.pot_flag = dict.fromkeys(np.arange(self.num_pots))
        self.bet = dict.fromkeys(np.arange(self.num_pots), self.min_bet)
        self.stack = 1000.
        self.back = 0
        self.deck = pro_deck().spanish21(6)
        self.cut =np.random.randint(30,high=50)

    def draw(self):
        tmp = self.deck[0]
        self.deck = self.deck[1:]
        return tmp

    def start(self):
        for i in range(self.num_pots):
            self.bet[i] = self.min_bet
            self.stack -= self.bet[i]
            self.players[i] = self.draw()
        self.dealers = self.draw()
        for i in range(self.num_pots):
            self.players[i] = np.append(self.players[i], self.draw())
            self.sum_players[i] = deck_parser().sum(self.players[i])
        self.dealers = np.append(self.dealers, self.draw())    
        self.sum_dealers = deck_parser().sum(self.dealers)

    def print_debug(self):
        for i in range(self.num_pots):
            print(self.players[i],self.sum_players[i][0]+self.sum_players[i][1]*10)
        print(self.dealers,self.sum_dealers[0]+self.sum_dealers[1]*10)
        
    def hit(self, i):
        self.players[i] = np.append(self.players[i], self.draw())
        self.sum_players[i] = deck_parser().sum(self.players[i])
        if deck_parser().busted(self.players[i]):
            print('pot '+str(i)+' busted')
            self.bet[i] = 0
            self.pot_flag[i] = 'closed'
        elif deck_parser().hit21(self.players[i]):
            print('pot '+str(i)+' hit 21')
            self.back += self.bet[i] * 2
            self.pot_flag[i] = 'closed'
        else:
            self.players_run(i)

    def double_hit(self, i):
        self.players[i] = np.append(self.players[i], self.draw())
        self.sum_players[i] = deck_parser().sum(self.players[i])
        if deck_parser().busted(self.players[i]):
            print('pot '+str(i)+' busted')
            self.bet[i] = 0
            self.pot_flag[i] = 'closed'
        elif deck_parser().hit21(self.players[i]):
            print('pot '+str(i)+' hit 21')
            self.back += self.bet[i] * 2
            self.pot_flag[i] = 'closed'
        else:
            self.players_run(i, double_flag = 1)

    def action(self, i):
        tmp1 = deck_parser().sum(self.players[i])
        tmp2 = deck_parser().general_rank_parser(self.dealers[0])
        if tmp2 > 10: tmp2-=1
        if tmp1[1] == 1:
            return self.hit_dict[self.soft[tmp1[0]-2][tmp2-2]]
        else:
            return self.hit_dict[self.hard[tmp1[0]-2][tmp2-2]]

    def players_run(self, i, double_flag = 0):
        if self.action(i) == 'hit' and double_flag == 0:
            self.hit(i)
        elif self.action(i) == 'double':
            print('pot '+str(i)+' double')
            self.stack -= self.bet[i]
            self.bet[i] = self.bet[i] * 2
            self.double_hit(i)
        elif self.action(i) == 'surrender' and len(self.players[i]) == 2:
            print('pot '+str(i)+' surrender')
            self.back += self.bet[i] / 2
            self.pot_flag[i] = 'closed'
        elif self.action(i) == 'split':
            pass
        else:   # self.action(i) == 'split', double stand, hit 15/16 surrender
            pass
    
    def dealers_run(self):
        tmp = deck_parser().sum(self.dealers)
        while not (tmp[0] > 16 or tmp[0] + 10 * tmp[1] > 16 + self.dealer_hit_soft_17):
            self.dealers = np.append(self.dealers, self.draw())
            tmp = deck_parser().sum(self.dealers)
        self.sum_dealers = tmp

    def player_dealer_flow(self):
        for i in range(self.num_pots):
            if self.sum_dealers==(11,1):
                print('dealer blackjack')
                if self.sum_players[i]!=(11,1):
                    print('pot '+str(i)+' lost')
                    self.bet[i] = 0
                else:
                    print('pot '+str(i)+' blackjack')
                    print('pot '+str(i)+' win')
                    self.back += self.bet[i] * 2.5
                    self.bet[i] = 0
                return 1
            else:
                if self.sum_players[i]==(11,1):
                    print('pot '+str(i)+' blackjack')
                    print('pot '+str(i)+' win')
                    self.back += self.bet[i] * 2.5
                    self.bet[i] = 0
                    return 1
                else:
                    self.players_run(i)
        dealer_run_flag = 0
        for i in range(self.num_pots):
            if self.pot_flag[i] != 'closed': dealer_run_flag = 1
        if dealer_run_flag == 1: 
            self.dealers_run()
            return 0
        else:
            return 1

    def who_win(self):
        if deck_parser().busted(self.dealers):
            print('dealer busted')
            for i in range(self.num_pots):
                if self.pot_flag[i] != 'closed':
                    print('pot '+str(i)+' win')
                    self.back += self.bet[i] * 2
        else:
            for i in range(self.num_pots):
                if self.pot_flag[i] != 'closed':
                    sum_over_players = self.sum_players[i][0] + self.sum_players[i][1] * 10
                    sum_over_dealers = self.sum_dealers[0] + self.sum_dealers[1] * 10
                    if  sum_over_players < 22 and sum_over_players > sum_over_dealers:
                        print('pot '+str(i)+' win')
                        self.back += self.bet[i] * 2
                    elif sum_over_players == sum_over_dealers:
                        print('pot '+str(i)+' push')
                        self.back += self.bet[i]
                    elif sum_over_players < sum_over_dealers:
                        print('pot '+str(i)+' lost')

    def one_deck_flow(self):
        print(self.deck)
        while len(self.deck) > self.cut:
            self.back = 0
            prev_stack = self.stack
            self.pot_flag = dict.fromkeys(np.arange(self.num_pots))
            self.start()
            over_flag = self.player_dealer_flow()
            self.print_debug()
            if not over_flag:
                self.who_win()
            self.stack += self.back
            print('stack change return:',self.stack,self.stack-prev_stack,self.back)
            print('---')
        print(len(self.deck),self.cut)
        return self.stack

if __name__ == '__main__':
    spanish21(1).one_deck_flow()
