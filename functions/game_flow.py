import numpy as np
import pandas as pd
import os
from deck import pro_deck

class spanish21:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.strategy = np.genfromtxt((os.path.dirname(self.dir_path)+'/inputs/hardway.csv'), delimiter=',')
        print(self.strategy)
        self.dealer = []
        self.players = []
        self.deck = pro_deck().spanish21(6)
        self.cut =np.random.randint(30,high=50)

    def draw(self):
        tmp = self.deck[0]
        self.deck = self.deck[1:]
        return tmp

    def start(self):
        self.players = self.draw()
        self.dealer = self.draw()
        self.players = np.append(self.players, self.draw())
        self.dealer = np.append(self.dealer, self.draw())

    def flow(self):
        print(self.deck)
        while len(self.deck) > self.cut:
            self.start()
            print(self.players,self.dealer)
        print(len(self.deck),self.cut)

if __name__ == '__main__':
    spanish21().flow()
