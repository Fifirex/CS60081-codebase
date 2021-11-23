# creating pipal analysis file

import numpy as np
import pandas as pd

def prepPipal(dat = None):
    if dat is None:
        passwords = pd.read_csv('database/clean.csv', index_col = 0)["Passwords"].tolist()
    else:
        print("got dat yay!")
        passwords = dat["Passwords"].tolist()
    np.savetxt("database/pipalInput.txt", passwords, fmt="%s")

if __name__ == "__main__":
    prepPipal()