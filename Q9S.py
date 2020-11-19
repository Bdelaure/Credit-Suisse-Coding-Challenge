def organizingContainers(container):
    n = len(container)
    capacity = [sum(x) for x in container]
    load = [0] * n
    residual_space = [0] * n
    result = "Possible"
    for i in range(n):
        for elem in container:
            load[i] = load[i] + elem[i]
        residual_space[i] = capacity[i] - load[i]
        if residual_space[i] < 0:
            result = "Impossible"
            break
    return result

if __name__ == "__main__":
    q = int(input().strip())
    answer=""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
             answer = str(result)
        else:
            answer = answer +  "," +str(result)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line