import csv
import random
FILENAME = "Users.csv"

list = []
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        list.append(row)

random.shuffle(list)
NEWFILE = "RandUsers.csv"
with open(NEWFILE, "w", newline="") as file:
    columns = ["id", "isBot"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(list)

