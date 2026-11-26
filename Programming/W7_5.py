DELIMITER = ";"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0


class DAY_USAGE:
    weekday = ""
    usage = 0.0
    cost = 0.0


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
        timestamp.hour = columns[1]
        timestamp.consumption = float(columns[2])
        timestamp.price = float(columns[3])
        Timestamps.append(timestamp)
    file.close()


def analyseTimestamps(Timestamps, Results):
    days = []
    for name in DAYS:
        day = DAY_USAGE()
        day.weekday = name
        days.append(day)
    for timestamp in Timestamps:
        for day in days:
            # Compare the first 3 letters, because the data spells it "Saturnday"
            if timestamp.weekday[:3] == day.weekday[:3]:
                day.usage += timestamp.consumption
                day.cost += timestamp.consumption * timestamp.price
    for day in days:
        Results.append(f" - {day.weekday} usage {day.usage:.2f} kWh, cost {day.cost:.2f} €")


def displayResults(Results):
    print("### Electricity consumption summary ###")
    for result in Results:
        print(result)
    print("### Electricity consumption summary ###")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = []
    readTimestamps(filename, timestamps)
    print("Analysing timestamps.")
    results = []
    analyseTimestamps(timestamps, results)
    print("Displaying results.")
    displayResults(results)
    print("Program ending.")


if __name__ == "__main__":
    main()
