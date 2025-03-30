import numpy as np
import random

"""
A module with functions for DNA sequence generation and mutation
"""

NUCLEOTIDES = np.array(['A', 'C', 'T', 'G'])

def get_seq(k: int=10) -> np.ndarray:
    return np.array([random.choice(NUCLEOTIDES) for i in range(k)])

def mutate(in_seq: np.ndarray) -> np.ndarray:
    """
    Depreciated
    """
    modifier = np.random.rand()
    out_seq = np.copy(in_seq)
    for i in range(in_seq.size):
        if np.random.rand() * modifier > 0.35:
            out_seq[i] = random.choice(NUCLEOTIDES)
    
    return out_seq

def mutate2(in_seq: np.ndarray, fraction = 0.3) -> np.ndarray:
    """
    Takes a ndarray of nucleotides and returns an array with roughly k fraction
    mutated. Since A->A type mutations are not forbiden real fraqtion of mutated
    nucleotides will be slightly lower.
    """
    size = in_seq.size
    count = np.round(size * fraction).astype(int)
    indices = random.choices([*range(size)], k=count)

    out_seq = np.copy(in_seq)
    for i in indices:
        out_seq[i] = random.choice(NUCLEOTIDES)
    
    return out_seq