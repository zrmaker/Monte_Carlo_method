import numpy as np

class blackjack:
    def __init__(self):
        self.n=100
        self.stack=1000
        self.minimum=10
        # self.

    def drawdeck(self):
        return np.random.randint(1,14)

    def value(self,a):
        return 10 if a>=10 else a

    def testbusted(self):
        return 1

    def monte_carlo_bj(self):
        df=self.drawdeck()
        p1=self.drawdeck()
        p2=self.drawdeck()
        print(p2,self.value(p2))

    def main(self):
        for i in range(self.n):
            self.monte_carlo_bj()

if __name__=='__main__':
    blackjack().main()