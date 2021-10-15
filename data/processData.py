import csv


file = open("c:/DataVizGNI/data/gniUsd.csv")
csvreader = csv.reader(file)
gniHeader = next(csvreader)
gniRows = []
for row in csvreader:
    gniRows.append(row)
file.close()


file = open("c:/DataVizGNI/data/population.csv")
csvreader = csv.reader(file)
pHeader = next(csvreader)
pRows = []
for row in csvreader:
    pRows.append(row)
file.close()


file = open("c:/DataVizGNI/data/continents.csv")
csvreader = csv.reader(file)
cHeader = next(csvreader)
cRows = []
for row in csvreader:
    cRows.append(row)
file.close()



## combine 

combRows = []

for cou in range(266):
    for year in range(61):
        continent = ''
        for scan in range(249):
            if cRows[scan][2] == gniRows[cou][1]:
                continent = cRows[scan][3]
        combRows.append([gniRows[cou][0],gniRows[cou][1],continent,gniHeader[2+year],gniRows[cou][2+year],pRows[cou][2+year]])

combHead = ["countryName","countryCode","region","year","gni","population"]

file = open("c:/DataVizGNI/data/combined.csv", 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(combHead)
csvwriter.writerows(combRows)
file.close()
