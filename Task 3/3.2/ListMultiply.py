def multiply_list(state, matrix):
    """Multiply state vector by transition matrix (list of lists)."""
    new_state = []
    for j in range(len(matrix[0])):  # loop over columns
        total = 0
        for i in range(len(state)):  # loop over rows
            total += state[i] * matrix[i][j]
        new_state.append(total)
    return new_state


# === Example 2x2 ===
state2 = [9, 4]
matrix2 = [
    [1, 2],
    [3, 1]
]

print("=== List Multiply (2x2) ===")
print("Input state:", state2)
print("Matrix:", matrix2)
print("Output:", multiply_list(state2, matrix2))
print()

# === Example 3x3 ===
state3 = [2, 5, 7]
matrix3 = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

print("=== List Multiply (3x3) ===")
print("Input state:", state3)
print("Matrix:", matrix3)
print("Output:", multiply_list(state3, matrix3))



\