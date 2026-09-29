FILENAME = "machine_log.text"

try:
    with open(FILENAME, "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            print(cleaned_line)
except FileNotFoundError:
    print("Log file is missing.")