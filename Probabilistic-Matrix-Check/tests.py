from classicN3 import classicCheckMultiply
from probsN2 import probsCheckMultiply
import time

def matrixMultiplication(A, B, C, a):
    if a == "classicO(n3)":
        result = classicCheckMultiply(A, B, C)
    elif a == "probsO(n2)":
        result = probsCheckMultiply(A, B, C)
    return result


filenames = ["/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in1.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in2.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in3.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in4.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in5.txt",
             "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in6.txt"]
algorithms = ["probsO(n2)", "classicO(n3)"]

# File Read Time Test -------------------------------------------
j = 1
for f in filenames:

    print("File", j)
    output_filename = f"file{j}testRead.txt"
    j += 1

    for i in range(0, 100):

        start_readtime = time.time()
        with open(f, 'r') as file:
            lines = file.readlines()
        end_readtime = time.time()
        execTime = end_readtime - start_readtime

        print(f"File read time: {execTime:.6f} seconds")

        with open(output_filename, 'a') as output_file:
            output_file.write(f"{execTime:.6f}\n")

    print("")
    print("")

# Algorithm Time Test -------------------------------------------

for a in algorithms:

    print(a)
    print("--------------------------------")
    j = 1

    for f in filenames:

        print("File", j)
        output_filename = f"{a}file{j}testTime.txt"
        output_filenameYes = f"{a}file{j}testTimeYES.txt"
        output_filenameNo = f"{a}file{j}testTimeNo.txt"
        j += 1
        with open(f, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        index = 0
        num_test_cases = int(lines[index])
        index += 1

        for _ in range(num_test_cases):
            n = int(lines[index])
            index += 1
            A = [list(map(int, lines[index + i].split())) for i in range(n)]
            index += n
            B = [list(map(int, lines[index + i].split())) for i in range(n)]
            index += n
            C = [list(map(int, lines[index + i].split())) for i in range(n)]
            index += n

            for t in range(0, 100):
                start_time = time.time()
                result = matrixMultiplication(A, B, C, a)
                end_time = time.time()
                execTime = end_time - start_time
                print(f"Execution time: {execTime:.6f} seconds")
                with open(output_filename, 'a') as output_file:
                    output_file.write(f"{execTime:.6f}\n")
                if result == "YES":
                    with open(output_filenameYes, 'a') as output_file:
                        output_file.write(f"{execTime:.6f}\n")
                else:
                    with open(output_filenameNo, 'a') as output_file:
                        output_file.write(f"{execTime:.6f}\n")
        print("")
        print("")