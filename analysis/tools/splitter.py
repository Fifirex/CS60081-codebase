import pandas as pd

SAMPLE_SIZE = 100
NUMBER_OF_SAMPLES = 3

data = pd.read_csv("database/clean.csv", index_col=0)

for i in range(NUMBER_OF_SAMPLES):
    shuffled = data.sample(n=SAMPLE_SIZE)
    shuffled.to_csv("tools/sample" + str(i+1) + ".csv")