"""
import csv
def searchByRegion():
    region = input("Digite el nombre de la región: ")
    csv_file = csv.reader(open('covid19.csv', 'r'))
    for row in csv_file:
        if region in row[1]:
            print(row)
def searchByDate():
    year = str(input("Digite la fecha: "))
    csv_file = csv.reader(open('covid19.csv', 'r'))
    for row in csv_file:
        if year in row[0]:
            print(row)
def searchByHospitalized():
    hospitalized = int(input("Digite "))
with open('covid19.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
print("\n\n")
print("Digite 1 para buscar por fecha: ")
print("Digite 2 para buscar por nombre de región: ")
src = int(input("Digite aquí: "))
print("\n\n")
if src == 1:
    searchByDate()
elif src == 2:
    searchByRegion()
else:
    print("Error!")
"""






"""
from flask import Flask, request, render_template
import csv
app = Flask(__name__)
with open('covid19.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
print("\n\n")
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        age = request.form['age']
        ed = ""
        if (age == 'a'):
            ed = "Menor"
        if (age == 'b'):
            ed = "Mayor"
        return render_template('age.html', age = age, ed = ed, line = line)
    return render_template('index.html')
if __name__ == "__main__":
    app.run()
"""







from flask import Flask, render_template, request
import pandas as pd
import csv

def searchByRegion():
    region = input("Digite el nombre de la región: ")
    csv_file = csv.reader(open('covid19.csv', 'r'))
    for row in csv_file:
        if region in row[1]:
            print(row)


def searchByDate():
    year = str(input("Digite la fecha: "))
    csv_file = csv.reader(open('covid19.csv', 'r'))
    for row in csv_file:
        if year in row[0]:
            print(row)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

age = None
@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        if 'csvfile' in request.form:
            user = request.form['age']
            ed = ""
            #if (user == "c"):
            #ed = "Opción C"
            #return user
            #ed = "Opción c"
            f = request.form
            data = []
            with open('covid19.csv', 'r') as file:
                csvfile = csv.reader(file)
                for row in csvfile:
                    data.append(row)
            data = pd.DataFrame(data)
            return render_template('data.html', data=data.to_html(header=False), user=user)#, ed=ed)

            """else:
                ed = "Error"
                return render_template('data.html', ed = ed)
            #return render_template('data.html', user = user, ed = ed)"""
    """age = request.form['c1']
    ed = ""
    if (age == 'a'):
        ed = "Opción a"
        return render_template('data.html', age=age, ed=ed)
        #searchByRegion()
    if (age == 'b'):
        ed = "Opción b"
        return render_template('data.html', age=age, ed=ed)
        #searchByDate()
    if (age == 'c'):
        ed = "Opción c"
        f = request.form
        data = []
        with open('covid19.csv', 'r') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        data = pd.DataFrame(data)
        return render_template('data.html', data=data.to_html(header=False), age=age, ed=ed)
    else:
        return "Error"
        
        








        age = request.form['age']
        ed = ""
        if (age == 'a'):
            ed = "Opción a"
            return render_template('data.html', age=age, ed=ed)
            #searchByRegion()
        if (age == 'b'):
            ed = "Opción b"
            return render_template('data.html', age=age, ed=ed)
            #searchByDate()
        if (age == 'c'):
            ed = "Opción c"
            f = request.form
            data = []
            with open('covid19.csv', 'r') as file:
                csvfile = csv.reader(file)
                for row in csvfile:
                    data.append(row)
            data = pd.DataFrame(data)
            return render_template('data.html', data=data.to_html(header=False), age=age, ed=ed)"""




"""
@app.route('/age', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        age = request.form['age']
        ed = ""
        if (age == 'a'):
            ed = "Menor"
        if (age == 'b'):
            ed = "Mayor"
        return render_template('age.html', age = age, ed = ed)
    return render_template('data.html')"""


if __name__ == '__main__':
    app.run(debug=True)