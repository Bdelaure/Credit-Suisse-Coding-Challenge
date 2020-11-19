import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    max_profit = 0
    for i in range(numOfPredictedDay):
        for j in range(i + 1, numOfPredictedDay):
            max_profit = max(predictedSharePrices[j] - predictedSharePrices[i],max_profit)
    return max_profit


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()