DELIMITER = ";"


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0


def readTimestamps(Filename, Timestamps):
    file = open(Filename, encoding="utf-8")
    file.readline()  # skip header row
    for line in file:
        row = line.rstrip()
        if row == "":
            continue
        columns = row.split(DELIMITER)
        timestamp = TIMESTAMP()
        timestamp.weekday = columns[0]
        timestamp.hour = columns[1] + ":00"
        timestamp.consumption = float(columns[2])
        timestamp.price = float(columns[3])
        Timestamps.append(timestamp)
    file.close()


def displayTimestamps(Timestamps):
    print("Electricity usage:")
    for t in Timestamps:
        total = t.price * t.consumption
        print(f" - {t.weekday} {t.hour}, price {t.price:.2f}, consumption {t.consumption:.2f} kWh, total {total:.2f} €")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = []
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")


if __name__ == "__main__":
    main()
