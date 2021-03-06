import numpy as np

class pro_deck:
    def __init__(self):
        self.deck = []
        self.rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        self.suit = ['S','H','D','C']

    def blackjack(self,num_decks):
        for i in range(len(self.rank)):
            for j in range(len(self.suit)):
                self.deck = np.append(self.deck,self.rank[i]+self.suit[j])
        self.deck = np.repeat(self.deck,num_decks)
        np.random.shuffle(self.deck)
        return self.deck

    def spanish21(self,num_decks):
        for i in [x for x in range(len(self.rank)) if x != 4]:
            for j in range(len(self.suit)):
                self.deck = np.append(self.deck,self.rank[i]+self.suit[j])
        self.deck = np.repeat(self.deck,num_decks)
        np.random.shuffle(self.deck)
        return self.deck

class deck_parser:
    def __init__(self):
        self.dict = {
        'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10,
        '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5,
        '4' : 4, '3' : 3, '2' : 2
        }
        
    def blackjack_rank_parser(self,card):
        tmp = self.dict[card[0]]
        flag = 0
        if tmp == 14:
            tmp = 1
            flag = 1
        if tmp > 10: tmp = 10
        return tmp, flag

    def general_rank_parser(self,card):
        return self.dict[card[0]]

    def sum(self, cards):
        tmp = 0
        flag = 0
        for i in range(len(cards)):
            tmp2,tmp3 = deck_parser().blackjack_rank_parser(cards[i])
            tmp += tmp2
            if tmp3 == 1: flag = 1
        if tmp > 11 : flag = 0
        return tmp, flag
    
    def busted(self, cards):
        if self.sum(cards)[0] > 21: return 1
        else: return 0

    def hit21(self, cards):
        if self.sum(cards) == (21,0) or self.sum(cards) == (11,1): return 1
        else: return 0

if __name__ == '__main__':
    tmp = pro_deck().blackjack(6)[0]
    print(tmp, deck_parser().rank_parser(tmp,'spanish21'))