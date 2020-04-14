import csv

def searchByRegion():
    region = input("Enter region name: ")
    csv_file = csv.reader(open('covid19.csv', 'r'))

    for row in csv_file:
        if region in row[1]:
            print(row)



def searchByDate():
    year = str(input("Enter date to show data: "))
    csv_file = csv.reader(open('covid19.csv', 'r'))

    for row in csv_file:
        if year in row[0]:
            print(row)




with open('covid19.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

print("\n\n")
print("Enter 1 to search by date")
print("Enter 2 to search by region name")


src = int(input("Enter here: "))

print("\n\n")
if src == 1:
    searchByDate()
elif src == 2:
    searchByRegion()
else:
    print("Error!")








"""from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        age = request.form['age']
        ed = ""
        if (age == 'a'):
            ed = "Menor"
        if (age == 'b'):
            ed = "Mayor"


        return render_template('age.html', age = age, ed = ed)


    return render_template('index.html')




if __name__ == "__main__":
    app.run()"""
