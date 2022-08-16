from sys import argv, exit
import csv

def main():
    #Expects the user to provide two command-line arguments:
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    elif not argv[1].endswith(".csv") and not argv[2].endswith(".csv"):
        exit("Not a CSV file")

        #CSV 1: the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house
        #CSV 2: the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    try:
        outputdict = split_names(argv[1])
    except FileNotFoundError:
        exit("CSV file 1 doesn't exist")
        
    #Converts that input to that output, splitting each name into a first name and last name.
    # Assume that each student will have both a first name and last name.
    try:
        create_output(argv[2], outputdict)
    except FileNotFoundError:
        exit("CSV file 2 doesn't exist")

def split_names(inputfile):
    students = []
    with open(inputfile, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    for student in students:
        last, first = student["name"].split(", ")
        student.update({"first": first, "last": last})
        student.pop("name")

    return students

def create_output(outputfile, outputdict):
    columns = ["first","last","house"]
    with open(outputfile, "w") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(outputdict)


if __name__ == "__main__":
    main()