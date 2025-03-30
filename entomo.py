#!/bin/python

import random, string, os
import numpy as np
# my modules
from genome import *
from worder import *

# Instantiate Worder and initialize the list of words
wd = Worder()
wd.word_pool()

class Species:
    def __init__(self):
        self.name = wd.christen()
        self.genome = get_seq()
        self.ancestor = None
        self.L_descent = None
        self.R_descent = None
        self.extinct = False
    
    def recreate_genome(self):
        self.genome = get_seq()
    
    def cladgen(self):
        if self.L_descent:
            raise Exception("Thise species is extinct!")

        L, R = Species(), Species()
        L.ancestor, R.ancestor = self, self
        L.genome, R.genome = mutate2(self.genome), mutate2(self.genome)
        self.L_descent, self.R_descent = L, R
        self.extinct = True

beetle = Species()
beetle.cladgen()

print(
    f"{beetle.genome}\t{beetle.name}\n"
    f"{beetle.L_descent.genome}\t{beetle.L_descent.name}\n"
    f"{beetle.R_descent.genome}\t{beetle.R_descent.name}\n"
)