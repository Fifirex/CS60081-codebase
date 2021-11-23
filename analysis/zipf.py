import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def Zipf(savefile = True):
    passFreq = pd.read_csv("database/passwordFreq.csv")

    index = (passFreq.index.values + 1).tolist()
    values = passFreq["Passwords"].to_list()

    # cutoff for linear fitting
    # CUTOFF = -28000
    # logA = np.log(index[:CUTOFF])
    # logB = np.log(values[:CUTOFF])

    logA = np.log(index)
    logB = np.log(values)

    def yFit (degree):
        coeffs = np.polyfit(logA,logB,deg=degree)
        poly = np.poly1d(coeffs)
        yfit = lambda x: np.exp(poly(np.log(x)))
        return yfit (index), coeffs

    # log-log plot
    plt.xlabel(r"Rank of password $(r)$")
    plt.ylabel(r"Frequency of password $(f_{r})$")
    plt.loglog(index, values, marker = 'o', markersize = 2, linestyle = 'None', label = "log–log plot")

    # model fitting
    yfit, coeffs = yFit(1)
    coeffs[1] = np.exp(coeffs[1])
    plt.loglog(index, yfit, 'k-', linewidth = 0.75, label = "Linear fit", color='yellow')
    
    yfit2, coeffs2 = yFit(2)
    coeffs2[1] = np.exp(coeffs2[1])
    plt.loglog(index, yfit2, 'k-', linewidth = 0.75, label = "Quadratic fit", color='green')

    yfit3, coeffs3 = yFit(3)
    coeffs3[1] = np.exp(coeffs3[1])
    plt.loglog(index, yfit3, 'k-', linewidth = 0.75, label = "Cubic fit", color='cyan')

    yfit4, coeffs4 = yFit(4)
    coeffs4[1] = np.exp(coeffs4[1])
    plt.loglog(index, yfit4, 'k-', linewidth = 1.75, label = "Bi-Quadratic fit", color='black')

    # plt.text(10, yfit[-1], r"$\ln{(f_{r})} = \ln{(%0.2f)} %0.5f \cdot \ln{(r)}$" % (coeffs[1], coeffs[0]), fontsize = 10)

    print(coeffs4)
    print("r2 = " + str(r2_score(logB, np.log(yfit4))))

    plt.ylim(0, max(values) * 1.5)
    plt.legend()

    if savefile:
        plt.savefig('documentation/zipf_plot_polyfit.png', bbox_inches='tight')
    # plt.show()

if __name__ == "__main__":
    Zipf()