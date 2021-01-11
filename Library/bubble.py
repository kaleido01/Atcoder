def BubbleSort(num):
    for i in range(len(num)):
        for j in range(len(num)-1, i, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1], num[j]

    return num
