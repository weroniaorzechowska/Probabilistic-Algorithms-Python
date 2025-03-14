import time
import math
from insertionSortAlg import insertionSortK
from quickSortAlg import quickSortK, quickSortSelectK
from selectionSortAlg import selectionSortK
from probAlg import probSampling
from aiAlgIdeas import introspective_quickselect, monte_carlo_quickselect, ultra_fast_kth, bitwise_kth_element

def kth_smallest(arr, k, alg):
    if alg == "Insertion Sort":
        result = insertionSortK(arr)[k-1]
    elif alg == "Selection Sort":
        result = selectionSortK(arr, k)
    elif alg == "Quick Sort with random pivot":
        result = quickSortK(arr)[k-1]
    elif alg == "Quick Sort with Magic5":
        result = quickSortK(arr, pivotType="magic5")[k - 1]
    elif alg == "Quick Sort with pivot arr[0]":
        result = quickSortK(arr, pivotType="notRandom")[k-1]
    elif alg == "Quick Select with random pivot":
        result = quickSortSelectK(arr, k)
    elif alg == "Quick Select with Magic5":
        result = quickSortSelectK(arr, k, pivotType = "magic5")
    elif alg == "Quick Select with pivot arr[0]":
        result = quickSortSelectK(arr, k, pivotType = "notRandom")
    elif alg == "Probability Sampling":
        result = probSampling(arr, k)
    elif alg == "AI1":
        result = introspective_quickselect(arr, 0, len(arr) - 1, k - 1, math.log2(len(arr)))
    elif alg == "AI2":
        result = monte_carlo_quickselect(arr, k-1)
    elif alg == "AI3":
        result = ultra_fast_kth(arr, k)
    elif alg == "AI4":
        result = bitwise_kth_element(arr, k)
    return result

filenames = ["/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in1.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in2.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in3.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in4.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in5.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab01/kthelement/in6.txt"]
algorithms = [#"Quick Sort with random pivot", "Quick Select with random pivot",
              #"Quick Sort with Magic5", "Quick Select with Magic5",
              #"Quick Sort with pivot arr[0]", "Quick Select with pivot arr[0]",
              "Probability Sampling"]
              #"AI1", "AI2", "AI3", "AI4",
              #"Insertion Sort", "Selection Sort"]

def main():
    for a in algorithms:
        print(a)
        print("--------------------------------")
        i = 1
        for f in filenames:
            #output_filename = f"{a}_{i}_out.txt"
            if (a == "Insertion Sort" or a == "Selection Sort") and i >= 3:
                break
            if a == "Probability Sampling" and i < 3:
                i += 1
                continue
            print("File", i)
            i += 1
            start_readtime = time.time()
            with open(f, 'r') as file:
                lines = file.readlines()
            end_readtime = time.time()
            print(f"File read time: {end_readtime - start_readtime:.6f} seconds")

            z = int(lines[0].strip())
            index = 1
            for _ in range(z):
                n, k = map(int, lines[index].strip().split())
                index += 1
                arr = list(map(int, lines[index].strip().split()))  
                index += 1
                start_time = time.time()
                result = kth_smallest(arr, k, a)
                end_time = time.time()
                print(result)
                execTime = end_time - start_time
                print(f"Execution time: {execTime:.6f} seconds")
            #with open(output_filename, 'a') as output_file:
            #    output_file.write(str(result) + '\n')
        print("")
        print("")

if __name__ == "__main__":
    main()