import collections
# Participants may update the following function parameters
def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):

    list_of_couples = []

    for i in range(numOfQuestions):
        questioner = questionAndAnswerListOfList[i][0]
        for respondant in questionAndAnswerListOfList[i][1:]:
            list_of_couples.append((min(questioner, respondant), max(questioner, respondant)))

    uniq_couples = set(list_of_couples)

    suspects_list1 = list(set([x for x in list_of_couples if list_of_couples.count(x) >= 2]))
    suspects_list_flat = [x for item in suspects_list1 for x in item]
    wl_loop_test = True
    new_suspects_set = set(suspects_list_flat)

    while wl_loop_test:
        wl_loop_test = False
        for lists in questionAndAnswerListOfList:
            resp = lists[1:]
            suspects_set = set(new_suspects_set)
            shared_items = suspects_set & set(resp)
            if len(shared_items) >= 2:
                new_suspects_set = new_suspects_set | {lists[0]}
            if len(suspects_set) != len(new_suspects_set):
                wl_loop_test = True

    final_suspects = ""
    for elem in new_suspects_set:
        final_suspects = (final_suspects + "," + str(elem)).strip()
    final_suspects = final_suspects[1:]
    return final_suspects


def main():
    firstLine = input().split(" ")
    secondLine = input()

    # Sample input:
    # 3
    # 1 2,2 1,3 1 2

    numOfQuestions = int(firstLine[0])
    questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = parseQuestionAndAnswer(questionAndAnswers)

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parseQuestionAndAnswer(questionAndAnswers):
    questionAndAnswerListOfList = []
    for index in range(0, len(questionAndAnswers)):
        questionAndAnswerList = questionAndAnswers[index].split(" ")
        questionAndAnswerListOfList.append([int(x) for x in questionAndAnswerList])
    return questionAndAnswerListOfList


if __name__ == '__main__':
    main()