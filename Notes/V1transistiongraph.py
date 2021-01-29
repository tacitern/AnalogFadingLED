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


def graphdifferenceR1R2equallntimingvalues():
    data = []
    x = []
    for i in range(5000):
        z = 1 / 1000 * i
        data.append(np.log(z/(z+1)))
        x.append(z)

    plt.plot(x, data)
    plt.show()


def graphdifferenceR1R3equallntimingvalues():
    data = []
    x = []
    for i in range(5000):
        z = 1 / 100 * i
        data.append(np.log(1/(z+1)))
        x.append(z)

    plt.plot(x, data)
    plt.show()


def graphdifferenceR1R3equaldutycycle():
    data = []
    x = []
    for i in range(5000):
        z = 1 / 100 * i
        data.append(1 / (1 + np.log(2)/np.log(z+1)))
        x.append(z)

    plt.plot(x, data)
    plt.show()


def graphVcapGeneral(R, C, Vcc, v_thres_high, v_thres_low, t_stop=1, t_start=0, t_inc=0.001, Vop_output=False):
    """
    This Function uses the piecewise function defind in the hysteresis oscillator document on the RC section
    of the hysteresis oscillator
    :param R: Resistance used in the RC section
    :param C: Capacitance used in the RC section
    :param Vcc: Supple voltage desired
    :param v_thres_high: this is actually Vthreshigh/Vcc; percentage of Vcc for high threshold voltage
    :param v_thres_low: this is actually Vthreslow/Vcc; percentage of Vcc for low threshold voltage
    :param t_stop: stop time in seconds
    :param t_start: start time to begin graphing Vcap
    :param t_inc: time increment
    :param Vop_output: If true a simulated output voltage, Vop, is added to Vcap graph
    :return:
    """

    t_i = -R*C*np.log(1-v_thres_low)
    t_c = -R*C*np.log((v_thres_high - 1)/(v_thres_low - 1))
    t_d = -R*C*np.log((v_thres_low)/(v_thres_high))

    t = [t_start]
    v = []
    N = 0
    if Vop_output:
        vout = []
    i = 0
    while t[-1] < t_stop:

        if t[-1] < t_i + t_c + t_d:
            N = 0
        else:
            N = np.floor((t[-1] - t_i) / (t_c + t_d))

        # print(f'{t}\t{N}')

        if t[-1] < t_i:
            if Vop_output:
                vout.append(Vcc)
            v.append(Vcc - Vcc * np.exp(-t[-1] / (R * C)))
        elif t[-1] >= t_i + (t_c + t_d) * N and t[-1] < t_i + t_c*(N + 1) + t_d*N:
            if Vop_output:
                vout.append(Vcc)
            v.append(Vcc + (v_thres_low*Vcc - Vcc) * np.exp(-(t[-1] - (t_i + (t_c + t_d) * N)) / (R * C)))
        elif t[-1] >= t_i + t_c*(N + 1) + t_d*N and t_i + (t_c + t_d) * (N + 1):
            if Vop_output:
                vout.append(0)
            v.append(v_thres_high * Vcc * np.exp(-(t[-1] - (t_i + t_c*(N + 1) + t_d*N)) / (R * C)))

        i = i + 1
        t.append(t_start + i * t_inc)

    print(t_i)
    print(t_c)
    print(t_d)

    plt.plot(t[:-1], v)
    if Vop_output:
        plt.plot(t[:-1], vout)
        plt.legend(['Vcap', 'Vop'])
    else:
        plt.legend(['Vcap'])
    plt.show()

if __name__ == '__main__':
    # graphVcapGeneral(10e3, 10e-6, 10, 3/4, 1/4, 0.69, t_start=0.139, Vop_output=True)
    graphdifferenceR1R3equaldutycycle()