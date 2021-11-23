import matplotlib.pyplot as plt

def passlen():
    x = [i for i in range(1, 16)]
    y = []
    flag = False
    with open("documentation/pipal-analysis/length-digit.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line == "Password length (length ordered)":
                flag = True
                continue
            if line == "16 = 616 (0.19%)":
                break
            if flag:
                y.append(float(line.split(' ')[2].strip())/266633.0*100.0)
    
    assert len(x) == len(y)

    plt.bar(x, y)
    plt.xlabel("Password length")
    plt.ylabel("Percentage")
    plt.ylim(0, 100)
    plt.show()

def spechar():
    x = []
    y = []
    total = 0
    flag = False
    with open("documentation/pipal-analysis/special-char.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                flag = True
                continue
            if line == "+ = 32 (0.01%)":
                flag = False
            if line == "":
                break
            if flag:
                x.append(line.split(' ')[0].strip())
                y.append(int(line.split(' ')[2].strip()))
            if line != "special characters":
                total += int(line.split(' ')[2].strip())

    for i in range(len(y)):
        y[i] /= total
        y[i] *= 100

    assert len(x) == len(y)

    plt.bar(x, y)
    plt.xlabel("Special character")
    plt.ylabel("Percentage")
    plt.savefig('documentation/specialchar.png', bbox_inches='tight')
    plt.show()

def no10():
    # discontinued this part
    ctr = 0
    lens = [0 for i in range(16)]
    with open("database/pipalInput.txt", 'r') as ifile:
        for line in ifile:
            if len(line.strip()) == 10 and line.strip().isnumeric():
                ctr += 1
                continue
            else:
                if len(line.strip()) < 16:
                    lens[len(line.strip())] += 1

    tot = sum(lens)
    for i in range(len(lens)):
        lens[i] /= tot
        lens[i] *= 100
    
    print(ctr)

    for i in range(len(lens)):
        print (str(i) + " = " + str(lens[i]))

if __name__ == "__main__":
    # passlen()
    spechar()
    # no10()