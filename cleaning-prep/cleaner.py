# pure cleaning

import pandas as pd
import numpy as np
import re
from frequency import exportFrequency

def masterClean(findFreq = True):
    file = open("database/raw.txt", "r")
    file3 = open("database/whitelist-domains.txt", "r")

    whitelist = []
    for line in file3:
        whitelist.append(line.strip())

    ctrRaw = 0
    ctrClean = 0
    ctrEmpty = 0
    ctrInvalid = 0
    accList = []
    passList = []
    domainList = []

    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

    for line in file:
        ctrRaw += 1
        empty = False
        if line.find(':') == -1:
            continue
        acc = line.split(':')[0].lower()
        passw = line.split(':')[1][:-1].lower()
        if passw == " ":
            ctrEmpty += 1
            empty = True
        if not email_regex.match(acc):
            ctrInvalid += 1
            empty = True
        if not empty:
            domain = acc.split('@')[1]
            if domain in whitelist:
                ctrClean += 1
                accList.append(acc)
                passList.append(passw)
                domainList.append(domain)
            # accList.append(acc)
            # passList.append(passw)
            # domainList.append(domain)
            # ctrClean += 1

    data = pd.DataFrame({"Accounts":accList, "Passwords":passList, "Domains":domainList})

    # dropping all the rows that are pure duplicates
    data = data.drop_duplicates()

    data.to_csv("database/clean.csv")

    print ("Raw count        : %d" % (ctrRaw))                                                       #398669
    print ("Clean count      : %d (%d eliminated)" % (len(data.index), ctrRaw - len(data.index)))    #357452 (41217 eliminated)
    print ("duplicates       : %d" % (ctrClean - len(data.index)))                                   #34698
    print ("null pass        : %d" % (ctrEmpty))                                                     #5572
    print ("invalid email id : %d" % (ctrInvalid))                                                   #952

    if findFreq:
        exportFrequency(data)
    
    file.close()
    # file3.close()

    if __name__ != "__main__":
        return data

if __name__ == "__main__":
    masterClean(findFreq = False)