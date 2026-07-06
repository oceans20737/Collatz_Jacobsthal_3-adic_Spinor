# -*- coding: utf-8 -*-
"""code_01_spinor.py
"""

# Spinor Transfer Model from J3 to J2 Space in Collatz Inverse Trees
# Hiroshi Harada
# July 6, 2026
# Released under the MIT License
# © 2026 Hiroshi Harada

import csv

def get_odd_collatz_orbit(n):
    """
    Generate the odd-only Collatz orbit starting from n.

    Even values are reduced by repeated division by 2 until an odd nucleus appears.
    The orbit proceeds via:
        n → 3n + 1 → divide out powers of 2 → next odd nucleus
    and terminates when reaching 1.

    This produces the canonical "odd Collatz orbit" used in inverse-tree analysis.
    """
    orbit = []

    # Normalize initial value to an odd nucleus
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2

    # Generate odd Collatz orbit
    while n != 1:
        orbit.append(n)
        n = 3 * n + 1
        while n % 2 == 0:
            n //= 2

    orbit.append(1)
    return orbit


def calculate_spinors(orbit):
    """
    Compute Spinor Transfer Model data for each odd nucleus b in the orbit.

    For each node b:
        - Balanced Ternary Phase ∈ {−1, 0, +1}
        - Scale-down value a
        - J3 Spinor (a, b)
        - J2 Spinor (x1, x2) = (b − a, b + a)

    Implements the linear transfer:
        J3(a, b)  →  J2(b − a, b + a)

    Notes:
        Phase = 0 corresponds to the "3-adic leaf" case (b ≡ 0 mod 3),
        where the J2 expansion becomes a pure binary stream.
    """
    results = []

    for b in orbit:
        # Balanced Ternary Phase and scale-down value a
        if b % 3 == 0:
            phase = 0
            a = b // 3
        elif b % 3 == 1:
            phase = 1
            a = (b - 1) // 3
        else:  # b % 3 == 2 (equivalent to −1 phase)
            phase = -1
            a = (b + 1) // 3

        # J2 spinor seeds
        x1 = b - a
        x2 = b + a

        # J2 Expansion (First 5 terms: x_k+2 = x_k+1 + 2x_k)
        seq = [x1, x2]
        for _ in range(3):
            seq.append(seq[-1] + 2 * seq[-2])

        results.append({
            'Node(b)': b,
            'Phase': phase,
            'a': a,
            'J3_a': a,
            'J3_b': b,
            'J2_x1': x1,
            'J2_x2': x2,
            'J3(a,b)': f"J3({a}, {b})",
            'J2(x1,x2)': f"J2({x1}, {x2})",
            'J2_Sequence': str(seq)
        })

    return results


def save_to_csv(results, initial_value):
    """
    Export spinor data to a CSV file.

    The CSV includes both numeric fields (J3_a, J3_b, J2_x1, J2_x2)
    and formatted labels (J3(a,b), J2(x1,x2)) for readability.
    """
    filename = f"collatz_spinor_orbit_{initial_value}.csv"

    fieldnames = [
        'Node(b)', 'Phase', 'a',
        'J3_a', 'J3_b',
        'J2_x1', 'J2_x2',
        'J3(a,b)', 'J2(x1,x2)',
        'J2_Sequence'
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    return filename


def main():
    """
    Public execution entry point.

    Prompts the user for an initial value, computes:
        - Odd Collatz orbit
        - Balanced Ternary Phase
        - J3 Spinor
        - J2 Spinor (Spinor Transfer Model)

    Prints results and exports them to CSV.
    """
    try:
        initial_val = int(input("Enter the initial value for the Collatz orbit (positive integer): "))
        if initial_val <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print(f"\nComputing odd Collatz orbit for initial value {initial_val}...")
    orbit = get_odd_collatz_orbit(initial_val)
    print(f"Odd orbit: {orbit}")

    print("\nComputing spinor data (J3 → J2 Transfer)...")
    spinor_data = calculate_spinors(orbit)

    for data in spinor_data:
        print(
            f"Node: {data['Node(b)']}, "
            f"Phase: {data['Phase']:2}, a: {data['a']:2}, "
            f"J3({data['J3_a']}, {data['J3_b']}), "
            f"J2({data['J2_x1']}, {data['J2_x2']}) -> Seq: {data['J2_Sequence']}"
        )

    filename = save_to_csv(spinor_data, initial_val)
    print(f"\nCompleted. Results saved to '{filename}'.")


if __name__ == "__main__":
    main()

