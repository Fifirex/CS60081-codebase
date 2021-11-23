import pandas as pd
import numpy as np

def exportFrequency(data = None):
    if data is None:
        data = pd.read_csv("database/clean.csv", index_col=0)

    # saving frequency of domains
    freqDomain = data['Domains'].value_counts()
    freqDomain.to_csv("database/domainFreq.csv")

    # saving frequency of emails
    freqEmail = data['Accounts'].value_counts()
    freqEmail.to_csv("database/emailFreq.csv")

    # saving frequency of passwords
    freqPass = data['Passwords'].value_counts()
    freqPass.to_csv("database/passwordFreq.csv")

    # cumulative analysis of domains
    ofile = open("database/domainCumulative.txt", "w")
    sum = 0
    cumulative = np.column_stack((freqDomain.index.to_numpy(), freqDomain.to_numpy()))
    for i in range(len(freqDomain)):
        sum += cumulative[i][1]
        cumulative[i][1] = float(sum/data.shape[0]) * 100.0
        ofile.write(str(cumulative[i][0]) + ", " + str(round(cumulative[i][1], 3)) + "%\n")
    ofile.close()

    # cumulative worked yay!
    assert sum == data.shape[0]

    print("Frequency analysis complete.")

if __name__ == "__main__":
    exportFrequency()