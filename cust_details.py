import csv

filename="bank-data.csv"
# initializing the titles and rows list
fields=[]
rows=[]
# reading csv file
with open(filename,'r') as csvfile:
    # creating a csv reader object
    csvreader =csv.reader(csvfile)
    # extracting field names through first row
    fields=next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
profession = []

for row in rows:
    # Building unique set of profession
    profession.append(row[1])

print("Select profession")
profession=sorted(list(set(profession)))

for prof in profession:
    print("",profession.index(prof),prof)

opt=int(input("Choose Eligible option[service,management,admin,entrepreneur] "))
if opt==1 or opt==3 or opt==5 or opt==7 or opt==8:
    print("Profession Not Eligible for loan")
if opt==0 or opt==2 or opt==4 or opt==6:
    print("Eligible for loan")
    for cust in rows:
        y = ''.join(cust[0])
        z = int(y)
        if cust[1]==profession[opt] and z<58:
            print(cust)
        else:
            pass
