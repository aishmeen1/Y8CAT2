import os

def build_transition_dict(filename):
    # Initialise dictionary of dictionaries with 0 counts
    transitions = {1: {1: 0, 2: 0, 3: 0},
                   2: {1: 0, 2: 0, 3: 0},
                   3: {1: 0, 2: 0, 3: 0}}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            before, after = line.split("*")
            before, after = int(before), int(after)
            transitions[before][after] += 1

    # Convert counts to percentages
    for key in transitions:
        total = sum(transitions[key].values())
        if total > 0:
            for k in transitions[key]:
                transitions[key][k] = transitions[key][k] / total

    return transitions


def main():
    # Get the folder where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "string_split.txt")

    result = build_transition_dict(filename)

    print("\n=== Transition Dictionary ===")
    for key, subdict in result.items():
        print(f"{key}: {subdict}")
    print("=============================\n")


if __name__ == "__main__":
    main()


