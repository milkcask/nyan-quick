# latest nyan.csv NOT generated by this script alone
import csv

quickTable = csv.reader(open('quick.csv'), delimiter='\t')

cantonFile = open('canton.csv')
cantonTable = csv.reader(cantonFile, delimiter='\t')

nyanWriter = csv.writer(open('nyan.csv', 'wb'), delimiter=',',)

for quickRow in quickTable:
    cantonFile.seek(0)
    for cantonRow in cantonTable:
        if quickRow[0] == cantonRow[0]:
            quickRow[1]+=cantonRow[1][:1]
            nyanRow=quickRow[:]
            break
        else:
            nyanRow=quickRow[:]
    nyanWriter.writerow(nyanRow)
