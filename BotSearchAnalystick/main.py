import csv
import ScanClass
FILENAME = "BotsRand.csv"
UsersToScan = []

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        UsersToScan.append(row['id'])



CScan = ScanClass.VkScan()
ScannedList = CScan.ScanUserList(UsersToScan)
print(ScannedList)


NEWFILE = "ScannedUserTwo.csv"
with open(NEWFILE, "w", newline="") as file:
    columns = list(ScannedList[0].keys())
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(ScannedList)