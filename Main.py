import csv

def searchByRegion():
    region = input("Enter region name: ")
    csv_file = csv.reader(open('covid19.csv', 'r'))

    for row in csv_file:
        if region == row[2]:
            print(row)



def searchByDate():
    year = str(input("Enter date to show data: "))
    csv_file = csv.reader(open('covid19.csv', 'r'))

    for row in csv_file:
        if year in row[0]:
            print(row)



print("Enter 1 to search by region name")
print("Enter 2 to search by date")

src = int(input("Enter here: "))

if src == 1:
    searchByRegion()
elif src == 2:
    searchByDate()
else:
    print("Error!")


