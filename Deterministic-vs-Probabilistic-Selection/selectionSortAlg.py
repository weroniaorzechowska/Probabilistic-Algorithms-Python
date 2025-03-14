def selectionSortK(arr, k):
    # szukamy kolejnych najmniejszych elementow
    # poszukiwanie konczymy po znalezieniu k-tego najmniejszego elementu
    # czyli po k glownych iteracjach
    for i in range(0, k):
        minArr = arr[i]
        index = i
        for j in range(i, len(arr)):
            if arr[j] < minArr:
                minArr = arr[j]
                index = j
        if index != i:
            arr[index] = arr[i]
            arr[i] = minArr
    return arr[k-1]

