# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):

    b_s_pref_comb = []

    for i in range(len(bankersPreferences)):
        for j in range(len(bankersPreferences[i])):
            b_s_pref_comb.append((i + 1, bankersPreferences[i][j]))

    for i in range(len(participantsPreferences)):
        for j in range(len(participantsPreferences[i])):
            b_s_pref_comb.append((participantsPreferences[i][j], i + 1))

    b_s_pref_comb = list(set(b_s_pref_comb))

    banker_seq = [coord[0] for coord in b_s_pref_comb]
    banker_nb_meetgs = [0] * numOfBankers
    for i in range(numOfBankers):
        banker_nb_meetgs[i] = banker_seq.count(i + 1)
    need_meetgs_from_bankers = max(banker_nb_meetgs)

    students_seq = [coord[1] for coord in b_s_pref_comb]
    students_nb_meetgs = [0] * numOfParticipants
    for i in range(numOfParticipants):
        students_nb_meetgs[i] = students_seq.count(i + 1)
    need_meetgs_from_students = max(students_nb_meetgs)

    final_nb_meetgs = max(need_meetgs_from_students, need_meetgs_from_bankers)

    return final_nb_meetgs


def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()