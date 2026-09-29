INPUT_FILE = "weights.txt"
OUTPUT_FILE = "weights_summary.txt"

total_weight = 0.0
valid_count = 0

try:
    with open(INPUT_FILE, "r") as file:
        for line in file:
            cleaned_line = line.strip()

            try:
                weight = float(cleaned_line)

                total_weight += weight
                valid_count += 1
            except ValueError:
                continue

    if valid_count > 0:
        average_weight = total_weight / valid_count
    else:
        average_weight = 0.0

    with open(OUTPUT_FILE, "w") as out_file:
        out_file.write(f"The total number of valid components processed: {valid_count}\n")
        out_file.write(f"The total combined weight: {total_weight:.1f}\n")
        out_file.write(f"The average weight (rounded to 2 decimal places): {average_weight:.2f}\n")
    print(f"Summary successfully written to {OUTPUT_FILE}")
except FileNotFoundError:
    print("Warning: The input file 'weights.text' id missing.")