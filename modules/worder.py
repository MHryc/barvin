import numpy as np
import random, string, os

CURRENT_PATH = (os.path.dirname(__file__)) + "/data"

class Worder():
    def __init__(self):
        self.trait_arr = None
        self.name1_arr = None
        self.name2_arr = None

    @classmethod
    def coder(self, length: int=4) -> str:
        """
        Returns an upper case alpha-numeric k-long code. Used for "unique"
        object naming.
        """
        return ''.join(
            random.choices(string.ascii_letters + string.digits, k=length)
            ).upper()
    
    def word_pool(self, k: int=100):
        """
        Sets the trait and names arrays of size k, used to create scientific
        names and trait combinations.
        """
        with open(CURRENT_PATH + "/cechy_polskie.txt", "r") as file:
            self.trait_arr = np.array(
                [trait.strip() for trait in random.choices(file.readlines(), k=k)]
                )

        with open(CURRENT_PATH + "/gat_1.txt", "r") as file:
            self.name1_arr = np.array(
                [name.strip() for name in random.choices(file.readlines(), k=k)]
                )

        with open(CURRENT_PATH + "/gat_2.txt", "r") as file:
            self.name2_arr = np.array(
                [name.strip() for name in random.choices(file.readlines(), k=k)]
                )

    def christen(self) -> str:
        """
        Returns a two part faux scientific insect name.
        """
        return f"{np.random.choice(self.name1_arr).capitalize()} {np.random.choice(self.name2_arr)}"

if __name__ == "__main__":
    pass
#for i in range(10):
#    gatunek = Individual()
#    print(gatunek.name)
#    for gene in gatunek.genome.keys():
#        val = round(gatunek.genome[gene], 3)
#        if val <= 0.5:
#            if val <= 0.25:
#                umiej = "licha"
#            else:
#                umiej = "pospolita"
#        else:
#            if val <= 0.75:
#                umiej = "solidna"
#            else:
#                umiej = "wybitna"
#
#        print(f"- {umiej} : {gene}")
#    print()