import argparse
import simplejson as json
from zxcvbn import zxcvbn as zx
from zxcvbn.matching import add_frequency_lists


def train(trainFile = None):
    base_words = []
    custom_words = []
    ctr = 0
    base = open('documentation/pipal-analysis/base-words.txt', 'r')
    for lines in base:
        ctr += 1
        if ctr < 3:
            continue
        base_words.append(lines.split('=')[0].strip())
    base.close()

    if trainFile != None:
        custom = open(trainFile, 'r')
        for lines in custom:
            custom_words.append(lines.strip())
        custom.close()

    return base_words + custom_words

def entropy(password, base_words):
    add_frequency_lists({
        'my_list': base_words
    })
    return zx(password)

def main():
    base_words = []
    parser = argparse.ArgumentParser(description = "The non-English zxcvbn")
    group = parser.add_mutually_exclusive_group()
    group2 = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--train', help = "Train the model with a custom set")
    group2.add_argument('-s', "--single", help = "Sigular password strength")
    group2.add_argument('-i', "--ifile", help = "Strength of batch passwords")
    args = parser.parse_args()

    if (args.train != None):
        try:
            open (args.train, 'r')
            base_words = train(args.train)
        except:
            print("[-] File not found")
            print("[-] Using the default dictionary for training")
            base_words = train()
    elif (args.single != None):
        predict = entropy(args.single, base_words)
        print("[+] Password strength: ")
        print(predict)
    elif (args.ifile != None):
        predict = {}
        try:
            ifile = open(args.ifile, 'r')
            for lines in ifile:
                predict[lines.strip()] = entropy(lines.strip(), base_words)
            ifile.close()
            with open("tool/tool-base/ofiles/def-output.json", "w") as f:
                json.dump(predict, f, use_decimal=True, indent=4, default = str)
            print("[+] Output file generated at tool-base/ofiles/def-output.json")
        except:
            print("[-] Input file not found")
    # train()

if __name__ == '__main__':
    main()
