import random
from magic5 import magic5

def quickSortK(arr, pivotType = "random"):
    # warunek stopu rekursji
    if len(arr) <= 1:
        return arr

    # wybor typu pivotu, wzgledem ktorego zrobimy partycje
    if pivotType == "magic5":
        pivot = magic5(arr)
    elif pivotType == "notRandom":
        pivot = arr[0]
    else:
        pivot = random.choice(arr)

    # partycja tablicy
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # wywolanie algorytmy na podzbiorach (srodkowy pomiajmy, bo tam sa elementy tej samej wartosci)
    left = quickSortK(left, pivotType)
    right = quickSortK(right, pivotType)

    arr = left + middle + right
    return arr

def quickSortSelectK(arr, k, pivotType = "random"):
    # warunek stopu rekursji
    if len(arr) == 1:
        return arr[0]

    # wybor typu pivotu, wzgledem ktorego zrobimy partycje
    if pivotType == "magic5":
        pivot = magic5(arr)
    elif pivotType == "notRandom":
        pivot = arr[0]
    else:
        pivot = random.choice(arr)

    # partycja tablicy
    left = [x for x in arr if x < pivot]
    #print(left)
    middle = [x for x in arr if x == pivot]
    #print(middle)
    right = [x for x in arr if x > pivot]
    #print(right)

    # wybor podzbioru, na ktorym bedziemy przeprowadzac dalsze poszukiwanie
    if k - 1 < len(left) and len(left) != 0:
        return quickSortSelectK(left, k, pivotType)
    elif k - 1 < len(left) + len(middle) and len(middle) != 0:
        return pivot
    elif len(right) != 0:
        return quickSortSelectK(right, k - len(left) - len(middle), pivotType)
    else:
        return quickSortSelectK(arr, k)