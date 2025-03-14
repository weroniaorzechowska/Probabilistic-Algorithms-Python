# Probabilistic-Algorithms-Python

## Overview 📌
This project focuses on two key algorithmic problems:
1. **Efficient selection of the k-th smallest element in an array**, comparing deterministic and probabilistic approaches.
2. **Verification of matrix multiplication** using both classic and probabilistic methods.

The project explores algorithmic optimizations for large-scale computations, aiming to minimize time complexity while maintaining accuracy.

---
## **Part 1: Selection of the k-th Smallest Element** 🔢
### **Problem Statement**
Given an unsorted array, find the **k-th smallest element** efficiently. The naive approach involves full sorting (**O(n log n)**), but optimized algorithms achieve **O(n) expected time**.

### **Implemented Algorithms 🛠️**
1. **Insertion Sort Selection (O(n²))** – Simple but inefficient for large datasets.
2. **Selection Sort Selection (O(n²))** – Improves efficiency by terminating early.
3. **QuickSelect (O(n) expected, O(n²) worst-case)** – A modification of QuickSort.
4. **Median of Medians (Deterministic O(n))** – Ensures worst-case linear time.
5. **Probabilistic Sampling Selection (O(2n))** – Uses random sampling to estimate the k-th element efficiently.
6. **AI-Suggested Algorithms:**
   - **Introspective QuickSelect** – Adaptive algorithm switching strategies dynamically.
   - **Monte Carlo QuickSelect** – Uses probabilistic sampling to enhance QuickSelect.
   - **Hoare Partition** – Efficient partitioning method used in QuickSort.
   - **Ultra Fast Kth Selection** – Hybrid approach leveraging multiple strategies.

### **Performance Analysis 📊**
| Algorithm | Expected Time Complexity | Performance on Large Datasets |
|-----------|-------------------------|--------------------------------|
| Insertion Sort | O(n²) | Very slow |
| Selection Sort | O(n²) | Slightly better but still slow |
| QuickSelect | O(n) (avg), O(n²) (worst) | Fast, but worst-case slow |
| Median of Medians | O(n) | Predictable but slightly slower |
| Probabilistic Sampling | O(2n) | Near-linear performance |
| AI-Suggested | Varies | Adaptive performance |

---
## **Part 2: Matrix Multiplication Verification** 🟢
### **Problem Statement**
Given three matrices **A, B, and C**, determine whether:
\[ A \cdot B = C \]
Two approaches are implemented:
1. **Classical O(n³) verification** – Computes the full matrix product and compares results.
2. **Probabilistic O(n²) verification** – Uses random vector multiplication to validate correctness.

### **Implemented Methods 🛠️**
#### **1️⃣ Probabilistic Verification – O(n²)**
- Choose a **large prime number p**.
- Generate a **random vector x**.
- Compute:
  \[ m = B \cdot x \mod p \]
  \[ n = A \cdot m \mod p \]
- Compute:
  \[ k = C \cdot x \mod p \]
- If **n ≠ k**, then A · B ≠ C with high probability.

#### **2️⃣ Deterministic Verification – O(n³)**
- Compute **A · B** using classic matrix multiplication.
- Compare it with **C** entry by entry.

### **Performance Comparison 📊**
| Matrix Size | O(n²) Time (s) | O(n³) Time (s) |
|------------|---------------|---------------|
| 100 × 100  | 0.0000255     | 0.0000373     |
| 500 × 500  | 0.0017941     | 0.0262887     |
| 1000 × 1000| 0.0675542     | 6.8736346     |
| 2000 × 2000| 0.1914609     | 33.7334137    |

### **Key Takeaways 🔎**
✅ The **probabilistic method** is orders of magnitude faster for large matrices.
✅ **Classic multiplication is infeasible** for very large datasets.
✅ Probabilistic verification is **not 100% accurate**, but error probability is negligible.

## **License 📄**
This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---
### 🚀 Optimizing selection & matrix verification through advanced algorithms!

