import matplotlib.pyplot as plt
import numpy as np


def intV1transistions():
    """
    Runs through integer value combinations for R1, R2, and R3 from 1 to 100.
    Prints combination which gives largest transistion width for V1 low to V1 high.
    These values can be used as a proportion of R1, R2, and R3 to each other
    """

    R1 = range(1, 100 + 1)
    R2 = range(1, 100 + 1)
    R3 = range(1, 100 + 1)

    V1_low = []
    V1_high = []
    V1_diff = []

    R = []

    for r1 in R1:
        for r2 in R2:
            for r3 in R3:

                 R.append([r1, r2, r3])

                 V1_low.append((r2 * r3) / (r2 * r3 + r1 * r3 + r1 * r2))
                 V1_high.append((r2 * r3 + r1 * r2) / (r2 * r3 + r1 * r3 + r1 * r2))
                 V1_diff.append(V1_high[-1] - V1_low[-1])

    # Very process intensive
    # plt.plot(V1_low)
    # plt.plot(V1_high)
    # plt.plot(V1_diff)
    # plt.legend(['V1 Low', 'V1 High', 'V1 Diff'])
    # plt.show()

    V1_diff_max = max(V1_diff)
    index = V1_diff.index(V1_diff_max)
    V1_low_max_diff = V1_low[index]
    V1_high_max_diff = V1_high[index]
    R_proportions_max_diff = R[index]

    print(f'V1 Diff: {V1_diff_max}')
    print(f'V1 Low: {V1_low_max_diff}')
    print(f'V1 High: {V1_high_max_diff}')
    print(f'R : {R_proportions_max_diff}')


def graphdifferenceR1R2equal():
    data = []
    x = []
    for i in range(5000):
        z = 1/100 * i
        data.append(1/(2*z+1))
        x.append(z)

    plt.plot(x, data)
    plt.show()

def graphdifferenceR1R3equal():
    data = []
    x = []
    for i in range(5000):
        z = 1/100 * i
        data.append(z/(2*z+1))
        x.append(z)

    plt.plot(x, data)
    plt.show()

def graphVcapexample1():
    Vcc = 10
    R = 10e3
    C = 10e-6

    t = []
    v = []
    N = 0
    for i in range(470):
        t.append(i*0.001)
        if t[-1] < 0.029 + 0.11 + 0.11:
            N = 0
        else:
            N = np.floor((t[-1] - 0.029)/(0.11 + 0.11))

        # print(f'{t}\t{N}')

        if t[-1] < 0.029:
            v.append(Vcc - Vcc*np.exp(-t[-1]/(R*C)))
        elif t[-1] >= 0.029 + 0.11*2*N and t[-1] < 0.029 + 0.11*(2*N+1):
            v.append(Vcc - 0.75*Vcc*np.exp(-(t[-1] - (0.029 + 0.11*2*N))/(R*C)))
        elif t[-1] >= 0.029 + 0.11*(2*N+1) and 0.029 + 0.11*(2*N+2):
            v.append(0.75*Vcc*np.exp(-(t[-1] - (0.029 + 0.11*(2*N+1)))/(R*C)))

    plt.plot(t, v)
    plt.show()

def graphHysteresisResistorsR1R2EqualDutyCycle():
    Vcc = 10
    R = 10e3
    C = 10e-6

    v_thres_high = 0.75 * Vcc
    v_thres_low = 0.50 * Vcc

    t_init = -R*C*np.log((v_thres_low - Vcc)/(0 - Vcc))
    t_charge = -R*C*np.log((v_thres_high - Vcc)/(v_thres_low - Vcc))
    t_discharge = -R*C*np.log((v_thres_low)/(v_thres_high))

    t = []
    v = []
    N = 0
    vout = []
    for i in range(800):
        t.append(i * 0.001)
        if t[-1] < t_init + t_charge + t_discharge:
            N = 0
        else:
            N = np.floor((t[-1] - t_init) / (t_charge + t_discharge))

        # print(f'{t}\t{N}')

        if t[-1] < t_init:
            vout.append(Vcc)
            v.append(Vcc - Vcc * np.exp(-t[-1] / (R * C)))
        elif t[-1] >= t_init + t_charge * 2 * N and t[-1] < t_init + t_charge * (2 * N + 1):
            vout.append(Vcc)
            v.append(Vcc + (v_thres_low - Vcc) * np.exp(-(t[-1] - (t_init + t_charge * 2 * N)) / (R * C)))
        elif t[-1] >= t_init + t_discharge * (2 * N + 1) and t_init + t_discharge * (2 * N + 2):
            vout.append(0)
            v.append(v_thres_high * np.exp(-(t[-1] - (t_init + t_discharge * (2 * N + 1))) / (R * C)))

    print(t_init)
    print(t_charge)
    print(t_discharge)

    plt.plot(v)
    plt.plot(vout)
    plt.legend(['Vcap', 'Vop'])
    plt.show()

if __name__ == '__main__':
    graphHysteresisResistorsR1R2EqualDutyCycle()
