# dont run it to generate the plot, saved the file as time-taken.png
# this takes time.

from zxcvbn import zxcvbn as zx
import matplotlib.pyplot as plt

entr = []
timeF = []
timeS = []
ctr = 0

with open("analysis/zxcvbn-al/zxcvbn-cumulative-0k.txt", 'r') as f:
    for line in f:
        if ctr < 20000:
            ctr += 1
            entr.append(float(line.split(':')[1].strip()))
            passw = line.split(':')[0].strip()
            timeF.append(float(zx(passw)['crack_times_seconds']['offline_fast_hashing_1e10_per_second']))
            timeS.append(float(zx(passw)['crack_times_seconds']['offline_slow_hashing_1e4_per_second']))
        else:
            break

entr.sort()
timeF.sort()
timeS.sort()

plt.plot(entr, timeF, marker='o', color='red', label='Fast Hashing', markersize=3)
plt.plot(entr, timeS, marker='o', color='blue', label='Slow Hashing', markersize=3)
plt.xlabel('zxcvbn entropy')
plt.ylabel('Time Taken (s)')
plt.xlim(0, 40)
plt.legend()
plt.show()


