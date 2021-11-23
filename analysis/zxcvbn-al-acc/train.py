from zxcvbn import zxcvbn as zx
from zxcvbn.matching import add_frequency_lists
import math
import pandas as pd

def train_zxcvbn(k_value):
    ctr = 0
    base_words = []
    base2entropy = []
    passwords = []

    if k_value != 0:
        base = open('documentation/pipal-analysis/base-words.txt')
        for lines in base:
            ctr += 1
            if ctr < 3:
                continue
            base_words.append(lines.split('=')[0].strip())
            if (ctr > (k_value * 1000 + 1)):
                break

        add_frequency_lists({
            'my_list': base_words
        })

        assert len(base_words) == k_value * 1000
        print(base_words[:10])

    # user input prep
    acc = pd.read_csv("database/clean.csv", index_col=0)["Accounts"].to_list()
    ctr = 0

    fileIn = open("database/pipalInput.txt", "r")
    for line in fileIn:
        passwords.append(line.strip())

    with open("analysis/zxcvbn-al-acc/zxcvbn-cumulative-" + str(k_value) + "k.txt", 'w') as file:
        for password in passwords:
            result = zx(password, user_inputs=acc[ctr])
            base2entropy.append(math.log(result["guesses"], 2))
            file.write(password + ": " + str(base2entropy[-1]) + "\n")
            ctr += 1

    fileIn.close()
    base.close()

if __name__ == "__main__":
    # train_zxcvbn(10)
    f1 = open("analysis/zxcvbn-al-acc/zxcvbn-cumulative-10k.txt", 'r')
    f2 = open("analysis/zxcvbn-al/zxcvbn-cumulative-10k.txt", 'r')
    ctr = 0
    for line1, line2 in zip(f1, f2):
        if line1 != line2:
            ctr += 1

    print(ctr)