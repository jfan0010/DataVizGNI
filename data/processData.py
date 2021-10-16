import csv


file = open("c:/DataVizGNI/data/gniUsdcopy.csv")
csvreader = csv.reader(file)
gniHeader = next(csvreader)
gniRows = []
for row in csvreader:
    gniRows.append(row)
file.close()


file = open("c:/DataVizGNI/data/populationcopy.csv")
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


# combine

combRows = []

for cou in range(266):
    for year in range(61):
        continent = ''
        for scan in range(249):
            if cRows[scan][2] == gniRows[cou][1]:
                continent = cRows[scan][3]
        combRows.append([gniRows[cou][0], gniRows[cou][1], continent,
                        gniHeader[2+year], gniRows[cou][2+year], pRows[cou][2+year]])

combHead = ["countryName", "countryCode",
            "region", "year", "gni", "population"]

file = open("c:/DataVizGNI/data/combined.csv", 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(combHead)
csvwriter.writerows(combRows)
file.close()

file = open("c:/DataVizGNI/data/combinedClean.csv", 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(combHead)
for row in combRows:
    if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '':
        csvwriter.writerow(row)
file.close()

file = open("c:/DataVizGNI/data/happiness.csv")
reader = csv.reader(file)
happyHead = next(reader)
happy = []
for row in reader:
    happy.append(row)
file.close()

file = open("c:/DataVizGNI/data/gpi.csv")
reader = csv.reader(file)
gpiHead = next(reader)
gpi = []
for row in reader:
    gpi.append(row)
file.close()

head2018 = []
head2018.extend(combHead)
head2018.append("gpi")
head2018.append("happiness")

file = open("c:/DataVizGNI/data/combined2018.csv", 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(head2018)
for row in combRows:
    # print(row)
    if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[3] == '2018':
        gpiValue = ''
        happyValue = ''
        for gpiRow in gpi:
            # print(gpiRow)
            if gpiRow[0] == row[0]:
                gpiValue = gpiRow[4]
        for happyRow in happy:
            # print(happyRow)
            if happyRow[1] == row[0]:
                happyValue = happyRow[2]
        if gpiValue != '' and happyValue != '':
            csvwriter.writerow(row + [gpiValue, happyValue])
file.close()
