SEPARATOR = ";"


def readValues(filename):
    values = ""
    file = open(filename)
    for line in file:
        values += line.strip() + SEPARATOR
    file.close()
    return values


def analyseNumbers(values):
    numbers = [int(v) for v in values.split(SEPARATOR)[:-1]]
    count = len(numbers)
    total = sum(numbers)
    return count, total, max(numbers), total / count


def displayResults(filename, results):
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{results[0]};{results[1]};{results[2]};{results[3]:.2f}")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    values = readValues(filename)
    results = analyseNumbers(values)
    displayResults(filename, results)
    print("\n#### Number analysis - END ####")
    print("Program ending.")


main()
