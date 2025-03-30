import random, sys, argparse
import numpy as np

# Define constants for transition and emission matrices
TRANSITION_MATRIX = {
    'A': {'A': 0.999, 'B': 0.001},
    'B': {'A': 0.001, 'B': 0.999}
}
EMISSION_MATRIX = {
    'A': {
        'A': {'A': 0.25, 'C': 0.25, 'T': 0.25, 'G': 0.25},
        'C': {'A': 0.25, 'C': 0.25, 'T': 0.25, 'G': 0.25},
        'T': {'A': 0.25, 'C': 0.25, 'T': 0.25, 'G': 0.25},
        'G': {'A': 0.25, 'C': 0.25, 'T': 0.25, 'G': 0.25},
    },
    'B': {
        'A': {'A': 0.1, 'C': 0.1, 'T': 0.7, 'G': 0.1},
        'C': {'A': 0.4, 'C': 0.1, 'T': 0.4, 'G': 0.1},
        'T': {'A': 0.7, 'C': 0.1, 'T': 0.1, 'G': 0.1},
        'G': {'A': 0.4, 'C': 0.1, 'T': 0.4, 'G': 0.1}
    }
}
NUCLEOTIDES = ('A', 'C', 'T', 'G')
STATES = ('A', 'B')

def random_seq(transition_matrix: dict, emission_matrix: dict, n: int) -> np.ndarray:
    """
    Generate a synthetic DNA sequence and its corresponding hidden state
    sequence.

    Args:
        transition_matrix (dict): Transition probability matrix for hidden
        states.
        emission_matrix (dict): Emission probability matrix for observed
        nucleotides.
        n (int): Length of the generated sequence.

    Returns:
        np.ndarray: 2D array containing sequence and hidden state arrays.
    """
    seq = np.empty((n,), dtype='U1')
    seq[0] = random.choice(NUCLEOTIDES)
    hidden = np.empty((n,), dtype='U1')
    hidden[0] = random.choice(STATES)

    for i in range(n - 1):
        seq_wgh = np.array([wgh for wgh in emission_matrix[hidden[i]][seq[i]].values()])
        hid_wgh = np.array([wgh for wgh in transition_matrix[hidden[i]].values()])

        seq[i + 1] = np.array(random.choices(NUCLEOTIDES, seq_wgh, k=1))[0]
        hidden[i + 1] = np.array(random.choices(STATES, hid_wgh, k=1))[0]
    return np.array([''.join(seq), ''.join(hidden)])

if __name__ == "__main__":
    print(
        random_seq(TRANSITION_MATRIX, EMISSION_MATRIX, 10)
    )