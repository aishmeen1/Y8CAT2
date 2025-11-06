from itertools import product

def multiply_vector_matrix(vector, matrix):
    """Multiply a 1x2 vector by a 2x2 matrix"""
    result = []
    for j in range(len(matrix[0])):  # loop over columns
        total = 0
        for i in range(len(vector)):
            total += vector[i] * matrix[i][j]
        result.append(total)
    return result

def predict_weather(initial_state, transition_matrix, days):
    """Predict weather probabilities over given number of days"""
    state = initial_state[:]
    print(f"\n=== Weather probabilities over {days} days ===")
    print(f"Day 0: Sunny={state[0]:.2f}, Rainy={state[1]:.2f}")
    for day in range(1, days+1):
        state = multiply_vector_matrix(state, transition_matrix)
        print(f"Day {day}: Sunny={state[0]:.2f}, Rainy={state[1]:.2f}")
    return state

def equilibrium_state(transition_matrix, tolerance=1e-6, max_iterations=1000):
    """Compute the steady-state vector for a Markov chain"""
    state = [1.0, 0.0]  # arbitrary start
    for _ in range(max_iterations):
        new_state = multiply_vector_matrix(state, transition_matrix)
        if all(abs(a - b) < tolerance for a, b in zip(new_state, state)):
            break
        state = new_state
    return state

def all_two_day_combinations(initial_state, transition_matrix):
    """Print all possible weather sequences for 2 days"""
    states = ['Sunny', 'Rainy']
    print("\n=== All possible 2-day sequences from initial Sunny ===")
    for day1, day2 in product(states, repeat=2):
        # Step 1: probability of day1
        p_day1 = transition_matrix[0][0] if day1=='Sunny' else transition_matrix[0][1]
        # Step 2: probability of day2 depends on day1
        if day1=='Sunny':
            p_day2 = transition_matrix[0][0] if day2=='Sunny' else transition_matrix[0][1]
        else:
            p_day2 = transition_matrix[1][0] if day2=='Sunny' else transition_matrix[1][1]
        probability = initial_state[0] * p_day1 * p_day2
        print(f"{day1} -> {day2}: {probability:.2f}")

# === Example Usage ===
transition_matrix = [
    [0.2, 0.8],  # Sunny -> Sunny/Rainy
    [0.4, 0.6]   # Rainy -> Sunny/Rainy
]

initial_state = [1.0, 0.0]  # Today is Sunny

# All 2-day sequences
all_two_day_combinations(initial_state, transition_matrix)

# Probabilities over next 2 and 10 days
predict_weather(initial_state, transition_matrix, 2)
predict_weather(initial_state, transition_matrix, 10)

# Equilibrium state
eq = equilibrium_state(transition_matrix)
print("\n=== Equilibrium State ===")
print(f"Sunny: {eq[0]:.2f}, Rainy: {eq[1]:.2f}")
