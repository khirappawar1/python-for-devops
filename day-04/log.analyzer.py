import json

def read_logs():
    with open("app.log", "r") as file:
        return file.readlines()

def analyze(lines):
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }

    for line in lines:
        if "INFO" in line:
            log_count["INFO"] += 1
        elif "WARNING" in line:
            log_count["WARNING"] += 1
        elif "ERROR" in line:
            log_count["ERROR"] += 1

    return log_count

def write_json(counts):
    with open("output.json", "w") as json_file:
        json.dump(counts, json_file, indent=4)  # pretty JSON

# ---- Main Script ----
lines = read_logs()
counts = analyze(lines)
print(counts)
write_json(counts)
