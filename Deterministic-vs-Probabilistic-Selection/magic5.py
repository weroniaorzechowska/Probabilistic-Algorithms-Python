import math
from insertionSortAlg import insertionSortK

def magic5(arr):

    # warunek stopu rekursji
    if len(arr) <= 1:
        return arr[0]

    # stworzenie tablicy median podzbiorow dlugosci 5
    lenMedianArr = math.ceil(len(arr)/5)
    MedianArr = [0] * lenMedianArr
    for i in range(0, lenMedianArr):
        medianArr = arr[i * 5: min((i + 1) * 5, len(arr))]
        medianArrSorted = insertionSortK(medianArr)
        m = len(medianArr) // 2
        MedianArr[i] = medianArrSorted[m]

    # wywolanie rekurencyjne
    return magic5(MedianArr)