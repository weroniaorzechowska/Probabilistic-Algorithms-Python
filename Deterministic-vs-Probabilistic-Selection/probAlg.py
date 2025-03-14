import random
import math
from quickSortAlg import quickSortK, quickSortSelectK

def probSampling(arr, k):
    size = len(arr)
    #print(size)
    if size <= 1000:
        return quickSortSelectK(arr, k)
    sampleSize = 1000

    samples = [random.choice(arr) for _ in range(sampleSize)]
    samples = quickSortK(samples)

    x = math.floor((k/size)*sampleSize)
    index1 = max(0, min(sampleSize - 1, x - 40))
    l1 = samples[index1]
    index2 = min(sampleSize - 1, x + 40)
    l2 = samples[index2]

    if l1 > l2:
        probSampling(arr, k)

    belowArr = [x for x in arr if x <= l1]
    arrK = [x for x in arr if l1 <= x <= l2]

    newk = k - len(belowArr) + 1
    if newk <= 0:
        index1 = 0
        l1 = samples[index1]
        arrK = [x for x in arr if l1 <= x <= l2]
        newk = k
        if newk <= 0:
            arrK = [x for x in arr if x <= l1]
    elif len(arrK) <= newk:
        index2 = sampleSize - 1
        l2 = samples[index2]
        arrK = [x for x in arr if l1 <= x <= l2]
        if len(arrK) <= newk:
            arrK = [x for x in arr if l1 <= x]
    return probSampling(arrK, newk)




