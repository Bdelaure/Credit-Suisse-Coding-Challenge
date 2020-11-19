def findMaxProfit(numOfPredictedTimes, predictedSharePrices):

    #######################################################################

    predictedSharePrices = predictedSharePrices
    positions = [0] * len(predictedSharePrices)

    if predictedSharePrices[0] < predictedSharePrices[1]:  # ouverture ou non de la 1st position
        positions[0] = 1

    for i in range(1, len(predictedSharePrices) - 1):

        test = sum(positions[:i])
        if test % 2 == 0:  # Aucune position ouverte
            if predictedSharePrices[i] < predictedSharePrices[i + 1]:
                positions[i] = 1  # ouverture de position
        else:  # position ouverte
            if predictedSharePrices[i] > predictedSharePrices[i + 1]:
                positions[i] = 1  # fermerture d'une position

    if sum(positions[:len(predictedSharePrices)]) % 2 != 0:
        positions[len(predictedSharePrices) - 1] = 1

    #########################################################################

    nb_pred_days = numOfPredictedTimes
    pred_prices = predictedSharePrices

    max_profit = 0
    positions_scheme = []

    for i in range(nb_pred_days):
        if positions[i] == 1:
            positions_scheme.append(i)

    positions_scheme = positions_scheme[:-1] if len(positions_scheme) % 2 != 0 else positions_scheme

    for i in range(0, len(positions_scheme), 2):
        max_profit = max_profit + pred_prices[positions_scheme[i + 1]] - pred_prices[positions_scheme[i]]

    return max_profit

print(findMaxProfit(4,[5,4,3,2]))