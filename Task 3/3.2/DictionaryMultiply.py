def multiply_dict(state, matrix):
    """Multiply state vector by transition matrix (dictionary form)."""
    new_state = {}
    for col in matrix[next(iter(matrix))]:  # loop over columns
        total = 0
        for row in state:  # loop over rows
            total += state[row] * matrix[row][col]
        new_state[col] = total
    return new_state


# Example from Q1
state = {"a": 9, "b": 4}
matrix = {
    "a": {"a": 1, "b": 2},
    "b": {"a": 3, "b": 1},
}

print("=== Dictionary Multiply ===")
print("State vector:", state)
print("Matrix:")
for r in matrix:
    print(" ", r, matrix[r])
print("Result:", multiply_dict(state, matrix))
print("===========================\n")


