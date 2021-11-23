import numpy as np
import matplotlib.pyplot as plt

def histo(file, label, color):
    base2entropy = []
    with open (file, 'r') as file:
        for line in file:
            line = line.split(':')
            base2entropy.append(float(line[1]))

    count, bins_count = np.histogram(base2entropy, bins=60000)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    plt.plot(bins_count[1:], cdf, label=label, c=color)

def default_zxcvbn():

    histo("analysis/zxcvbn-al/zxcvbn-cumulative-0k.txt", "zxcvbn", 'blue')
    histo("analysis/zxcvbn-al/zxcvbn-cumulative-1k.txt", "zxcvbn-1k", 'red')
    histo("analysis/zxcvbn-al/zxcvbn-cumulative-10k.txt", "zxcvbn-10k", 'cyan')
    histo("analysis/zxcvbn-al/zxcvbn-cumulative-50k.txt", "zxcvbn-50k", 'green')
    histo("analysis/zxcvbn-al/zxcvbn-cumulative-baseline.txt", "zxcvbn-baseline", 'black')

    plt.xlabel("zxcvbn Entropy")
    plt.ylabel("CDF")
    plt.legend()
    plt.ylim(0, 1)
    plt.xlim(0, 40)
    plt.savefig('documentation/zxcvbn-main.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    default_zxcvbn()