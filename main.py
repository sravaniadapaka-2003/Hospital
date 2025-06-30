import csv
bills = 'data.csv'
with open(bills,'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    print("csv created")
