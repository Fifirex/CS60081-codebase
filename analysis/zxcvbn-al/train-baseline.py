from zxcvbn import zxcvbn as zx
from zxcvbn.matching import add_frequency_lists
import math

def default_zxcvbn():
    base2entropy = []
    passwords = []
    fileIn = open("database/pipalInput.txt", "r")
    for line in fileIn:
        passwords.append(line.strip())
        
    add_frequency_lists({
        'my_list': passwords
    })

    print(passwords[:10])

    with open("analysis/zxcvbn-al/zxcvbn-cumulative-baseline.txt", 'w') as file:
        for password in passwords:
            result = zx(password)
            base2entropy.append(math.log(result["guesses"], 2))
            file.write(password + ": " + str(base2entropy[-1]) + "\n")

if __name__ == "__main__":
    default_zxcvbn()