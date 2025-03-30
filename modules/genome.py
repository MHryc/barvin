import numpy as np
import random

"""
A module with functions for DNA sequence generation and mutation
"""

NUCLEOTIDES = np.array(['A', 'C', 'T', 'G'])

def get_seq(k: int=10) -> np.ndarray:
    """
    Outputs a k-long array of nucleotides (ACTG). Each nucleotide has equal
    probability.

    Args:
        k (int): length of the output array (default is 10).
    
    Returns:
        np.ndarray: a k-long 1D array of nucleotides.

    Args:
        k (int): length of the output array (default is 10).
    
    Returns:
        np.ndarray: a k-long 1D array of nucleotides.
    """
    return np.array([random.choice(NUCLEOTIDES) for i in range(k)])

def mutate(in_seq: np.ndarray) -> np.ndarray:
    """
    Depreciated (I don't like it)

    Takes an np.ndarray of ATCG and returns a mutated copy. Each time this
    function is run a random float between 0 and 1 is assigned to `modifier`.
    For each nucleotide if `modifier` * np.random.rand() is greater than 0.35,
    nucleotide is mutated.

    It was supposed to simulate varying molecular clock but in current for it's
    too ridgid for my taste.

    Args:
        in_seq (np.ndarray): an array of ATCG.

    Returns:
        np.ndarray: copied and mutated original string (no in-place mutation).
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

    Args:
        in_seq (np.ndarray): array of ACTG.
        fraction (float): the fraction of the sequence that will be mutated.

    Returns:
        np.ndarray: copied and mutated original string (no in-place mutation).
    """
    size = in_seq.size
    count = np.round(size * fraction).astype(int)
    indices = random.choices([*range(size)], k=count)

    out_seq = np.copy(in_seq)
    for i in indices:
        out_seq[i] = random.choice(NUCLEOTIDES)
    
    return out_seq

if __name__ == "__main__":
    print(
        mutate2.__doc__
    )