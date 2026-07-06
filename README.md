# **Jacobsthal Spinor Transfer Model from J3 to J2 Space in Collatz Inverse Trees**

**Hiroshi Harada — July 6, 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21221670.svg)](https://doi.org/10.5281/zenodo.21221670)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A theoretical model and accompanying calculation/visualization tools that formalize the generation mechanism of Collatz Inverse Trees as a **Spinor Transfer** from the 3-adic Jacobsthal (J3) space to the 2-adic Jacobsthal (J2) space.

---

## **Overview**

Traditional Collatz inverse tree generation relies on the reverse computation of “$3n+1$”.  
This study demonstrates a structure capable of generating the inverse tree using **only addition and phase (mod 3)** — completely eliminating multiplication and division.

1. **J3 Space (3-adic)**  
   Determines the J3 spinor $J_3(a,b)$ from the local phase (Balanced Ternary) of the odd nuclei.

2. **Spinor Transfer**  
   Transfers the phase directly into the initial conditions of the J2 space via the linear mapping:  

   $$
   J_3(a,b) \rightarrow J_2(b-a,\; b+a)
   $$

3. **J2 Space (2-adic)**  
   Exponential expansion via the recurrence relation combined with parity branching determined by the Balanced Ternary phase, geometrically extracts the parent nodes ($3n+1$ / $3n-1$) of the inverse tree.

   $$
   x_{k+2} = x_{k+1} + 2x_k
   $$ 
   

---

## **Files**

### **`code_01_spinor.py`**
A Python script that:
- Computes the odd-nucleus Collatz orbit from any initial value  
- Calculates J3/J2 spinors for each node  
- Generates the first J2 expansion terms  
- Outputs all results to a CSV file

### **`TITLE_EN.pdf`**
Conceptual architecture diagram illustrating the J3 → J2 spinor transfer.

### **`REPORT_EN.pdf` / `REPORT_JP.pdf`**
Official research reports documenting the full theory (English / Japanese).

---

## **Usage**

Run the following in a Python 3.x environment:

```bash
python code_01_spinor.py
```

When prompted, enter any positive integer (e.g., `7`).  
The spinor transfer results along the inverse tree orbit will be displayed in the console, and detailed data will be saved as:

```
collatz_spinor_orbit_<initial_value>.csv
```

---

## **Output Example (CSV)**

| Node(b) | Phase | a | J3(a,b) | J2(x1,x2) | J2 Sequence |
| --- | --- | --- | --- | --- | --- |
| 1 | +1 | 0 | J3(0, 1) | J2(1, 1) | [1, 1, 3, 5, 11] |
| 5 | -1 | 2 | J3(2, 5) | J2(3, 7) | [3, 7, 13, 27, 53] |
| … | … | … | … | … | … |

---

## **License**

- Research documents: **CC BY 4.0**  
- Python source code: **MIT License**  
- © 2026 Hiroshi Harada

---
