import csv

with open(r'StudentList.csv', mode = 'r' , encoding = 'utf-8-sig') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter = ',')
   data = [row for row in csv_reader]

with open("data.txt", mode = 'w', encoding = 'utf-8-sig') as f:
 for i in data[6:len(data)+1]:
   a = i[0].split(',')
   b = "\t".join(a[:4])
   f.write(b)
   f.write("\n")