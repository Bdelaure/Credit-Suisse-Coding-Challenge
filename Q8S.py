# Participants may update the following function parameters
def countNumberOfWays(numOfUnits, numOfCoinTypes, coins):

    max_coef = [numOfUnits // x for x in coins]  # List des valeurs maximales des coeficients des combinaisons lineaires
    list_of_potential_coef = [list(range(x + 1)) for x in max_coef]

    nb_of_n_uplet = 1
    for item in max_coef:
        nb_of_n_uplet = nb_of_n_uplet * (item + 1)  # determination du nombre de n_uplet possible

    combinations_item_chain = [0] * numOfCoinTypes * nb_of_n_uplet  # initialisation de la liste des combinaisons

    filling_divider = [1] * numOfCoinTypes
    for i in range(numOfCoinTypes - 1):
        for x in max_coef[i + 1:]:
            filling_divider[i] = filling_divider[i] * (x + 1)

    ######################################################################################################

    potential = list_of_potential_coef
    fill_mlt = filling_divider
    n = len(combinations_item_chain)  # produit des len des sublists mutiliplié par le type de n_uplets
    dec = len(potential)
    span = []
    test_result = []
    number_seq = [0] * n
    loop_offset = 0
    fill_offset = 0

    for i in range(len(potential)):
        k = 0
        affect_count = 0
        active_potentials = potential[i]
        active_fill_offset = fill_mlt[fill_offset]
        for j in range(loop_offset, len(number_seq), dec):
            if affect_count == active_fill_offset:
                k = k + 1
                if k == len(active_potentials):
                    k = 0
                affect_count = 0
            number_seq[j] = active_potentials[k]
            affect_count = affect_count + 1

        loop_offset = loop_offset + 1
        fill_offset = fill_offset + 1

    sum_test = 0
    for i in range(0, len(number_seq), dec):
        sum_test = 0
        for j in range(len(number_seq[i:(i + dec)])):
            sum_test = sum_test + number_seq[i:(i + dec)][j] * coins[j]
        if sum_test == numOfUnits:
            test_result.append(1)
        else:
            test_result.append(0)
        span.append(number_seq[i:(i + dec)])

    return sum(test_result)

def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")

    numOfUnits = int(firstLine[0])
    numOfCoinTypes = int(firstLine[1])
    coins = list(map(int, secondLine))

    # Participants may update the following function parameters
    answer = countNumberOfWays(numOfUnits, numOfCoinTypes, coins)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()