# conducts basic analysis of the data

import pandas as pd
import numpy as np
from zipf import Zipf
from pipal import prepPipal

def basicAn(data = None, prepZipf = False, Pipal = False):
    ctrClean = 0
    ctrProfilepass = 0
    ctrPhonenum = 0
    ctrSmall = 0
    # ctrUnique = 0

    if data is None:
        data = pd.read_csv("database/clean.csv", index_col=0)

    # vectorizing for faster iteration
    dataArr = data.to_numpy()

    for row in dataArr:
        # testing for if password string is completely present in the mail ID
        if row[0].find(row[1]) != -1:
            ctrProfilepass += 1

        # testing for if password is a phone number
        if len(row[1]) == 10 and row[1].isnumeric() == True:
            ctrPhonenum += 1

        # testing for if password is of length < 8
        if len(row[1]) < 8:
            ctrSmall += 1

    # finding duplicate email ids
    # accFreq = data['Accounts'].value_counts()
    # for i in range(len(accFreq)):
    #     if accFreq[i] == 1:
    #         ctrUnique += 1

    # print(data.loc[data.Accounts == "maries1@mailweb.stars-and-glory.stars-and-glory.top"])
    # print("\nNumber of unique entries : " + str(ctrUnique))

    ctrClean = np.shape(dataArr)[0]
    print ("\nAcc count    : %d" % (ctrClean))                                                      #357586
    print ("Passw in acc : %d (%0.2f %%)" % (ctrProfilepass, float(ctrProfilepass/ctrClean*100)))   #4789
    print ("Phone num    : %d (%0.2f %%)" % (ctrPhonenum, float(ctrPhonenum/ctrClean*100)))         #158816
    print ("Small Passw  : %d (%0.2f %%)" % (ctrSmall, float(ctrSmall/ctrClean*100)))               #33912

    if (prepZipf):
        Zipf()
    if (Pipal):
        prepPipal(dat = data)

if __name__ == "__main__":
    basicAn()