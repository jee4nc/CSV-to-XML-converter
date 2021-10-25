import csv
import os
from sys import exit

print("Ingrese el nombre del archivo csv fuente")
nameFileCSV = input()

def checkIfExistCSV(name):
    if os.path.exists(name) is False:
        print("El archivo csv no existe")
        print("Se dentendrá la ejecución del script")
        exit()
    else:
        last_chars = name[-3:]
        if last_chars != "csv":
            print("El archivo debe tener extension csv")
            print("Se dentendrá la ejecución del script")
            exit()

checkIfExistCSV(nameFileCSV)

print("Ingrese el nombre del archivo xml a generar: ")
nameFileOut = input()

def checkIfFileOutXML(name):
    last_chars = name[-3:]
    if last_chars != "xml":
        print("El archivo debe tener extension xml")
        print("Se dentendrá la ejecución del script")
        exit()        

checkIfFileOutXML(nameFileOut)

csvFileIn = open(nameFileCSV)
csvFileInData = csv.reader(csvFileIn)
dataList = []

if os.path.exists(nameFileOut):
    os.remove(nameFileOut)

xmlFileOut = open(nameFileOut, "x")
xmlFileOut.close()

for row in csvFileInData:
    dataList.append(row)
csvFileIn.close()

firstRow = dataList[0]

if firstRow:
    words =  firstRow[0].split(";")
    fieldName = words[1]

getModelName = nameFileCSV.replace(".csv", "")


def convert_row(row):
    if row:
        words = row[0].split(";")

    return """
            <record id="%s" model="%s">
                <field name="%s">%s</field>
            </record>
    """ % (words[0], getModelName, fieldName, words[1])


def actionConverter(data):
    for row in data:
        if row != data[0]:
            xmlFileOut.write(convert_row(row))

xmlFileOut = open(nameFileOut, "w")

try:
    actionConverter(dataList)
    print("XML generado exitosamente, revise su nuevo archivo: " + nameFileOut)
except:
    print("Algo salio mal generando el archivo xml")
    os.remove(nameFileOut)


xmlFileOut.close()
