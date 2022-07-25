import csv
import secrets
import string
import random
import os

currentDirectory = os.getcwd() + '\CSVFile.csv'
f= open(currentDirectory,'w',newline='')



# create the csv writer
fieldnames = ['ColumnName1', 'ColumnName2']
writer = csv.DictWriter(f, fieldnames=fieldnames)
entryCount = 100
# entryCount = int(input('Enter the number of entries required in CSV file'))

for i in range(entryCount):
    N = 15   #number of characters that is required for value
    #value1 contains the combination of alphabets and numbers
    value1= ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
    #value2 contains only numeric values
    writer.writerow({'ColumnName1': 'Label_1', 'ColumnName2': value1})
    value2= ''.join(secrets.choice(string.digits) for i in range(N))
    writer.writerow({'ColumnName1': 'Label_2', 'ColumnName2': value2})

f.close()