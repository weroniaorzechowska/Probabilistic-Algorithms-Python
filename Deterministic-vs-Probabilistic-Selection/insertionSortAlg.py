def insertionSortK(arr):
    # dla kazdego elementu w liscie znajdujemy dla niego nowe miejsce w posortowanym
    # juz fragmencie
    for i in range(0, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            arr[j] = x
            j -= 1
    return arr