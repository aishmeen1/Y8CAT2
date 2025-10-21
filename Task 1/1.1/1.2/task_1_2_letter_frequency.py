import os

def count_letter_frequencies(filename):
    counts = {}
    total = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            letter = line.strip()
            if letter:
                counts[letter.upper()] = counts.get(letter.upper(), 0) + 1
                total += 1

    # Convert to frequencies
    for k in counts:
        counts[k] = counts[k] / total

    # Fancy printing
    output = ", ".join([f"{k}:{v:.2f}" for k, v in counts.items()])
    print("\n=== Letter Frequencies ===")
    print(output)
    print("==========================\n")


def main():
    # script_dir = folder of this script (1.2)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # parent_dir = go UP one folder → 1.1
    parent_dir = os.path.dirname(script_dir)

    # full path to data_structure_data.txt inside 1.1
    filename = os.path.join(parent_dir, "data_structure_data.txt")

    count_letter_frequencies(filename)


if __name__ == "__main__":
    main()


