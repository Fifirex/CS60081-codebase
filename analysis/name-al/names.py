import pandas as pd
import matplotlib.pyplot as plt

def preproc(delta):
    name_list = []
    with open ("database/indian_names.txt", "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == delta:
                name_list.append(line)

    return name_list

def analysis():

    with open("analysis/name-al/delta-wise-break.txt", 'w') as f:
        for delta in range(3, 11):
            name_list = preproc(delta)
            ctr = 0
            with open("database/pipalInput.txt", 'r') as f:
                for passw in f:
                    passw = passw.strip()
                    for name in name_list:
                        if name in passw:
                            ctr += 1
                            break

            f.write(str(delta) + ' : ' + str(ctr) + '\n')

def prep():
    name_list = []
    with open ("database/indian_names.txt", "r") as f:
        for line in f:
            line = line.strip()
            name_list.append(line)

    length = []
    for name in name_list:
        length.append(len(name))

    print (length.count(5))

    # plotting the frequency distribution of the length of the names
    plt.hist(length, bins=range(1, 20))
    plt.xticks(range(1, 20))
    plt.xlabel('Length of name')
    plt.ylabel('Frequency')
    plt.show()
    print(max(length))

def plot_delta():
    delta = []
    ctr = []
    with open("analysis/name-al/delta-wise.txt", 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(':')
            # 3 ignored because of substring confusion
            # 8+ are very rare
            if int(line[0]) <= 3 or int(line[0]) >= 8:
                continue
            delta.append(int(line[0]))
            # 266633 is the number of passwords in the dataset
            # 168862 is the number of passwords in the dataset that are pure numbers
            ctr.append(float(line[1])/(266633.0 - 168862.0)*100.0) 

    plt.bar(delta, ctr)
    plt.xlabel(r"${\sigma}$")
    plt.ylabel('Percentage')
    plt.xticks(range(4, 8))
    plt.savefig('documentation/sigma.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":  
    plot_delta()
    # prep()


