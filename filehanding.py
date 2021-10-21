import csv
with open('stud.csv','r') as file: # To Open the File of Excel File By Python
    r = csv.reader(file)
    for i in r:  # On Apply the for loop function. to cheak the one by one
        print(i)