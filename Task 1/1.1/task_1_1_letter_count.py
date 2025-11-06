import os

def count_letters_dict(filename):
    counts = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            letter = line.strip()
            if letter:
                counts[letter.upper()] = counts.get(letter.upper(), 0) + 1

    # fancy printing
    output = ", ".join([f"{k}:{v}" for k, v in counts.items()])
    print("\n=== Letter Counts ===")
    print(output)
    print("====================\n")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "data_structure_data.txt")
    count_letters_dict(filename)



