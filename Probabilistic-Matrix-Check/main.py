from classicN3 import classicCheckMultiply
from probsN2 import probsCheckMultiply
import time

def matrixMultiplication(A, B, C, a):
    if a == "classic O(n3)":
        result = classicCheckMultiply(A, B, C)
    elif a == "probs O(n2)":
        result = probsCheckMultiply(A, B, C)
    return result

def main():
    filenames = ["/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in1.txt",
                 "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in2.txt",
                 "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in3.txt",
                 "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in4.txt",
                 "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in5.txt",
                 "/Users/weroniaorzechowska/Desktop/semestr 6/ZTP/lab02/MatrixMultiplication/in6.txt"]

    algorithms = ["probs O(n2)", "classic O(n3)"]

    index = 0
    index += 1

    for a in algorithms:
        print(a)
        print("--------------------------------")
        i = 0
        for f in filenames:
            output_filename = f"{a}_{i}_out.txt"
            with open(filenames[i], 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]
            i += 1
            print("File", i)
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

                start_time = time.time()
                result = matrixMultiplication(A, B, C, a)
                end_time = time.time()
                print(result)
                print(f"Execution time: {end_time - start_time:.6f} seconds")
                with open(output_filename, 'a') as output_file:
                    output_file.write(str(result) + '\n')
        print("")
        print("")



if __name__ == "__main__":
    main()