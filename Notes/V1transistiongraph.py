import matplotlib.pyplot as plt


def intV1transistions():
    """

    :return:
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


if __name__ == '__main__':
    intV1transistions()
