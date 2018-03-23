import numpy as np
import pandas as pd
import os
from deck import *

class spanish21:
    def __init__(self, n_p = 1):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.hard = np.genfromtxt((os.path.dirname(self.dir_path)+'/inputs/spanish21_hard.csv'), delimiter=',')
        self.num_pots = n_p
        self.dealers = []
        self.sum_dealers = []
        self.players = dict.fromkeys(np.arange(self.num_pots))
        self.sum_players = dict.fromkeys(np.arange(self.num_pots))
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
        print('')

    def one_deck_flow(self):
        print(self.deck)
        while len(self.deck) > self.cut:
            self.start()
            for i in range(self.num_pots):
                self.sum_players[i] = deck_parser().sum(self.players[i])
            self.sum_dealers = deck_parser().sum(self.dealers)            
            self.pre_stage()
            self.print_debug()
            for i in range(self.num_pots):
                if self.sum_dealers==(11,1):
            
        # print(len(self.deck),self.cut)

if __name__ == '__main__':
    spanish21(1)
