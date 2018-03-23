import numpy as np
import pandas as pd
import os
from deck import *

class spanish21:
    def __init__(self, n_p = 1):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.hard = np.genfromtxt((os.path.dirname(self.dir_path)+'/inputs/spanish21_hard.csv'), delimiter=',')
        self.min_bet = 10
        self.stack = 1000
        self.num_pots = n_p
        self.hit_dict = {
            1.0 : 'hit', 2.0 : 'stand', 3.0 : 'double', 4.0 : 'surrender', 5.0 : 'split'
        }
        self.dealers = []
        self.sum_dealers = []
        self.players = dict.fromkeys(np.arange(self.num_pots))
        self.sum_players = dict.fromkeys(np.arange(self.num_pots))
        self.bet = dict.fromkeys(np.arange(self.num_pots), self.min_bet)
        self.deck = pro_deck().spanish21(6)
        self.cut =np.random.randint(30,high=50)
        self.one_deck_flow()

    def draw(self):
        tmp = self.deck[0]
        self.deck = self.deck[1:]
        return tmp

    def start(self):
        for i in range(self.num_pots):
            self.players[i] = self.draw()
        self.dealers = self.draw()
        for i in range(self.num_pots):
            self.players[i] = np.append(self.players[i], self.draw())
        self.dealers = np.append(self.dealers, self.draw())

    def pre_stage(self):
        for i in range(self.num_pots):
            if self.sum_players[i]==(11,1):
                print('pot '+str(i)+' blackjack')
        if self.sum_dealers==(11,1):
                print('dealer blackjack')

    def print_debug(self):
        for i in range(self.num_pots):
            print(self.players[i],self.sum_players[i])
        print(self.dealers,self.sum_dealers)
        
    def hit(self, i):
        self.players[i] = np.append(self.players[i], self.draw())
        self.sum_players[i] = deck_parser().sum(self.players[i])
        if deck_parser().busted(self.players[i]):
            print('pot '+str(i)+' busted')
            self.bet[i] = 0
        elif deck_parser().hit21(self.players[i]):
            print('pot '+str(i)+' hit 21')
            self.bet[i] = self.bet[i] * 2
        else:
            self.players_run(i)

    def double_hit(self, i):
        self.players[i] = np.append(self.players[i], self.draw())
        self.sum_players[i] = deck_parser().sum(self.players[i])
        if deck_parser().busted(self.players[i]):
            print('pot '+str(i)+' busted')
            self.bet[i] = 0
        elif deck_parser().hit21(self.players[i]):
            print('pot '+str(i)+' hit 21')
            self.bet[i] = self.bet[i] * 2
        else:
            self.players_run(i, double_flag = 1)

    def action(self, i):
        tmp = deck_parser().sum(self.players[i])
        tmp2 = deck_parser().general_rank_parser(self.dealers[0])
        if tmp2 > 10: tmp2-=1
        # if tmp1[1] == 1:
        return self.hit_dict[self.hard[tmp[0]-2][tmp2-2]]

    def players_run(self, i, double_flag = 0):
        if self.action(i) == 'hit' and double_flag == 0:
            self.hit(i)
        elif self.action(i) == 'double':
            print('pot '+str(i)+' double')
            self.bet[i] = self.bet[i] * 2
            self.stack -= self.bet[i]
            self.double_hit(i)
        elif self.action(i) == 'surrender':
            pass
        elif self.action(i) == 'split':
            pass
        else:   # self.action(i) == 'split' and double stand
            pass

    def one_pot_flow(self):
        for i in range(self.num_pots):
            if self.sum_dealers==(11,1):
                if self.sum_players[i]!=(11,1):
                    print('pot '+str(i)+' lost')
                    self.bet[i] = 0
                else:
                    print('pot '+str(i)+' win')
                    self.bet[i] = self.bet[i] * 2.5
            else:
                if self.sum_players[i]==(11,1):
                    print('pot '+str(i)+' win')
                    self.bet[i] = self.bet[i] * 2.5
                else:
                    self.players_run(i)
                    

    def one_deck_flow(self):
        print(self.deck)
        while len(self.deck) > self.cut:
            self.start()
            for i in range(self.num_pots):
                self.sum_players[i] = deck_parser().sum(self.players[i])
            self.sum_dealers = deck_parser().sum(self.dealers)            
            self.pre_stage()
            self.one_pot_flow()
            self.print_debug()
            print('')

        # print(len(self.deck),self.cut)

if __name__ == '__main__':
    spanish21(1)
