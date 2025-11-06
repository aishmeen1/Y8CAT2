# Author: Aishmeen

import os

def load_network(filename):
    """Read network_traFic.txt and build a transition-probability matrix."""
    connections = []
    routers = set()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Accept both "->" and " → " style arrows and remove spaces
                line = line.replace("→", "->").replace(" ", "")
                if "->" not in line:
                    continue
                start, end = line.split("->")
                if not start or not end:
                    continue
                start, end = start.upper(), end.upper()
                connections.append((start, end))
                routers.update([start, end])
    except FileNotFoundError:
        print("File not found:", filename)
        return [], []

    routers = sorted(list(routers))
    n = len(routers)

    # Build counts matrix
    counts = [[0 for _ in range(n)] for _ in range(n)]
    for s, e in connections:
        i, j = routers.index(s), routers.index(e)
        counts[i][j] += 1

    # Convert to probability matrix
    matrix = []
    for i in range(n):
        row_sum = sum(counts[i])
        if row_sum == 0:
            matrix.append([0 for _ in range(n)])
        else:
            matrix.append([counts[i][j] / row_sum for j in range(n)])

    return routers, matrix


def multiply_state(state, matrix):
    """Multiply a state vector by the transition matrix once."""
    new_state = [0 for _ in range(len(state))]
    for j in range(len(matrix[0])):      # columns
        for i in range(len(state)):      # rows
            new_state[j] += state[i] * matrix[i][j]
    return new_state


def power_state(state, matrix, steps):
    """Apply matrix multiplication for N steps."""
    result = state[:]
    for _ in range(steps):
        result = multiply_state(result, matrix)
    return result


def equilibrium_state(matrix, tolerance=1e-6, max_iter=1000):
    """Approximate the steady-state distribution."""
    n = len(matrix)
    state = [1 / n for _ in range(n)]  # start evenly
    for _ in range(max_iter):
        new_state = multiply_state(state, matrix)
        diff = sum(abs(new_state[i] - state[i]) for i in range(n))
        if diff < tolerance:
            break
        state = new_state
    return state


def print_matrix(matrix, routers):
    """Neatly print the transition matrix."""
    print("\nTransition Matrix (probabilities):")
    header = "     " + "  ".join(f"{r:>4}" for r in routers)
    print(header)
    for i, r in enumerate(routers):
        row = "  ".join(f"{val:>4.2f}" for val in matrix[i])
        print(f"{r:>3} | {row}")
    print()


def main():
    print("=== Perth Modern Router Traffic Analysis ===")

    # Always look in the same folder as this script
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "network_traFic.txt")

    routers, matrix = load_network(file_path)
    if not routers:
        print("⚠️  No valid data found in network_traFic.txt")
        print("   Check that each line looks like:  A->B")
        return

    while True:
        print("\nMenu:")
        print("1. View transition matrix")
        print("2. Simulate traffic after N steps")
        print("3. Find equilibrium (steady-state)")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print_matrix(matrix, routers)

        elif choice == "2":
            print("Routers:", ", ".join(routers))
            start = input("Starting router: ").upper()
            if start not in routers:
                print("Invalid router.")
                continue
            try:
                steps = int(input("Number of steps: "))
            except ValueError:
                print("Please enter a number.")
                continue
            state = [0 for _ in routers]
            state[routers.index(start)] = 1.0
            result = power_state(state, matrix, steps)
            print(f"\nAfter {steps} steps from {start}:")
            for i, r in enumerate(routers):
                print(f"  {r}: {result[i]:.3f}")

        elif choice == "3":
            eq = equilibrium_state(matrix)
            print("\nEquilibrium distribution:")
            for i, r in enumerate(routers):
                print(f"  {r}: {eq[i]:.3f}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

