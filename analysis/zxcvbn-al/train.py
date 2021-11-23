from zxcvbn import zxcvbn as zx
from zxcvbn.matching import add_frequency_lists
import math

def train_zxcvbn(k_value):
    ctr = 0
    base_words = []
    base2entropy = []
    passwords = []

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

    fileIn = open("database/pipalInput.txt", "r")
    for line in fileIn:
        passwords.append(line.strip())

    with open("analysis/zxcvbn-al/zxcvbn-cumulative-" + str(k_value) + "k.txt", 'w') as file:
        for password in passwords:
            result = zx(password)
            base2entropy.append(math.log(result["guesses"], 2))
            file.write(password + ": " + str(base2entropy[-1]) + "\n")

    fileIn.close()
    base.close()

if __name__ == "__main__":
    train_zxcvbn(50)