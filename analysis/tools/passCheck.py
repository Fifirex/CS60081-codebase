import pandas as pd
import numpy as np

data = pd.read_csv('database/clean.csv', index_col=0).to_numpy()

passw = input('Enter password (:q to exit): ')
ctr = 0

while (passw != ":q"):
    for row in data:
        if row[1] == passw:
            print(row[0])
            ctr += 1
            # if ctr == 20:
            #     break
    passw = input('Enter password (:q to exit): ')