def find_min_days(prices, profit):
    # Participants code will be here
    deb = [0] * d
    fin = [0] * d
    pot_deb = 0
    pot_fin = 0
    deb_fin = [""] * d
    text_print = ""
    cond_to_enter = False
    length = 0
    pot_length = 0
    inst_prof = 0

    for i in range(d):
        for j in range(n - 1):
            for k in range(j + 1, n):
                inst_prof = prices[k] - prices[j]
                if inst_prof == profit[i]:
                    pot_deb = j + 1
                    pot_fin = k + 1
                    pot_length = pot_fin - pot_deb
                    cond_to_enter = (deb[i] == 0) or (pot_fin < fin[i]) or (pot_fin == fin[i] and pot_length < length)
                    if cond_to_enter:
                        deb[i] = j + 1
                        fin[i] = k + 1
                        length = fin[i] - deb[i]

    for i in range(d):
        if deb[i] == 0:
            new_chunk = str(-1)
        else:
            new_chunk = str(deb[i]) + "  " + str(fin[i])
        text_print = text_print + new_chunk + ","
    text_print = text_print[:-1]
    return text_print

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line
