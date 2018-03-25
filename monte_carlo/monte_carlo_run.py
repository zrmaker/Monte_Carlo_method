import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))+'/functions/')
from game_flow import spanish21

class monte_carlo_method:
    def __init__(self, num_runs = 10000):
        self.num_runs = num_runs
        self.stack = 1000.
        self.stack_record = np.array(self.stack)
        self.ev_record = []
        self.ev = 0
        self.run()
    
    def run(self):
        for i in range(self.num_runs):
            one_run_stack = spanish21(1).one_deck_flow()
            self.stack += (one_run_stack - 1000.)
            ev = one_run_stack / 1000
            self.ev_record = np.append(self.ev_record,ev)
            self.ev = np.mean(self.ev_record)
            self.stack_record = np.append(self.stack_record,self.stack)
        print(self.ev_record,self.stack_record,self.ev)

if __name__ == '__main__':
    monte_carlo_method(100)