# Participants may update the following function parameters
def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    p_1 = [0.00] * noOfTradesAvailable
    expected = [0.00] * noOfTradesAvailable
    max_prof = 0.00

    for i in range(noOfTradesAvailable):
        p_1[i] = 1 - p[i]
        expected[i] = p[i] * x[i] - p_1[i] * y[i]

    expected = sorted(expected, reverse=True)

    for i in range(maximumTradesAllowed):
        max_prof = max_prof + expected[i]

        if expected[i] <= 0:
            max_prof = max_prof - expected[i]
            break

    max_prof = round(max_prof, 2)
    max_prof = "%.2f" % max_prof

    return max_prof

def main():
    # This part may require participants to fill in as well.
    noOfTradesAvailable, maximumTradesAllowed = list(map(int, input().split()))
    p = list(map(float, input().split()))
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    # Participants may update the following function parameters
    answer = maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()