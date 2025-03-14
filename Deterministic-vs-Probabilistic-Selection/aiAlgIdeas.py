import random
import heapq
import math
import numpy as np


def insertion_sort(arr, left, right):
    """Sortuje fragment listy przy użyciu Insertion Sort"""
    if left >= right:  # Zabezpieczenie przed pustym zakresem
        return arr[left] if left < len(arr) else None

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    mid_index = left + (right - left) // 2
    return arr[mid_index] if mid_index < len(arr) else None  # Zapobiega zwróceniu None


def partition(arr, left, right, pivot):
    """Dzieli tablicę na mniejsze/większe względem pivota"""
    if pivot not in arr[left:right + 1]:  # Zabezpieczenie przed błędnym pivotem
        return left

    pivot_value = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index


def median_of_medians(arr, left, right):
    """Wybiera medianę median jako pivot (BFPRT)"""
    if right - left < 5:
        return insertion_sort(arr, left, right)

    num_medians = (right - left + 1) // 5
    if num_medians == 0:
        return arr[left]  # Jeśli tablica jest za mała, zwracamy pierwszy element

    for i in range(num_medians):
        sub_left = left + i * 5
        sub_right = min(sub_left + 4, right)
        median = insertion_sort(arr, sub_left, sub_right)
        if median is not None:
            arr[left + i], arr[sub_left + 2] = arr[sub_left + 2], arr[left + i]

    return median_of_medians(arr, left, left + num_medians - 1)


def introspective_quickselect(arr, left, right, k, depth_limit):
    """Introspective QuickSelect z przełączeniem na HeapSelect przy złej strukturze"""
    while left < right:
        if depth_limit == 0:
            return heapq.nsmallest(k - left + 1, arr[left:right + 1])[-1]

        depth_limit -= 1

        pivot = median_of_medians(arr, left, right)
        if pivot is None:  # Zabezpieczenie przed błędnym pivotem
            return arr[left]

        pivot_index = partition(arr, left, right, arr.index(pivot))
        if pivot_index is None or pivot_index < left or pivot_index > right:
            return arr[left]  # Bezpieczny fallback

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

    return arr[left]  # Zwrócenie poprawnego wyniku, jeśli k pozostaje na granicy

def monte_carlo_quickselect(arr, k):
    """Probabilistyczny QuickSelect z agresywnym próbkowaniem."""
    while True:
        if len(arr) == 1:
            return arr[0]

        sample_size = min(len(arr), max(10, int(math.sqrt(len(arr)))))  # Próbkowanie ograniczone do dostępnych elementów
        sample = random.sample(arr, sample_size)  # Pobranie próbki
        sample.sort()

        pivot_index = int(k / len(arr) * sample_size)  # Szacowanie pivota na podstawie percentyla
        pivot = sample[max(0, min(pivot_index, sample_size - 1))]  # Zabezpieczenie indeksu

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        if k < len(left):
            arr = left
        elif k < len(left) + len(middle):
            return pivot
        else:
            arr = right
            k -= len(left) + len(middle)


def hoare_partition(arr, left, right, pivot):
    """Szybszy podział Hoare'a z poprawkami dla stabilności"""
    if pivot not in arr[left:right+1]:  # Zabezpieczenie przed błędnym pivotem
        return left

    pivot_value = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]  # Przeniesienie pivota na koniec
    i, j = left, right - 1

    while True:
        while i < right and arr[i] < pivot_value:
            i += 1
        while j > left and arr[j] > pivot_value:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]  # Umieszczenie pivota na swoim miejscu
    return i if left <= i <= right else left  # Zabezpieczenie przed błędnym indeksem


def ultra_fast_kth(arr, k):
    """Najlepszy deterministyczny algorytm do wyszukiwania k-tego elementu."""
    left, right = 0, len(arr) - 1
    while left < right:
        pivot = median_of_medians(arr, left, right)
        if pivot is None:
            return arr[left]  # Zabezpieczenie przed None

        pivot_index = hoare_partition(arr, left, right, arr.index(pivot))
        if pivot_index is None or pivot_index < left or pivot_index > right:
            return arr[left]  # Zabezpieczenie przed złym pivotem

        if k - 1 == pivot_index:
            return arr[pivot_index]
        elif k - 1 < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

    return arr[left]  # Zabezpieczenie dla małych przypadków


def bitwise_kth_element(arr, k):
    """
    Selekcja k-tego najmniejszego elementu bez sortowania, używając arytmetyki bitowej.
    """
    min_val, max_val = min(arr), max(arr)
    bucket_size = max_val - min_val + 1

    # Tworzymy histogram wartości (bucket selection)
    count = np.zeros(bucket_size, dtype=int)
    for num in arr:
        count[num - min_val] += 1

    # Przechodzimy przez bucket i szukamy k-tego elementu
    running_sum = 0
    for i in range(bucket_size):
        running_sum += count[i]
        if running_sum >= k:
            return i + min_val