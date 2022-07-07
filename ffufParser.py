#!/usr/bin/env python
import os,csv
from argparse import ArgumentParser, FileType

parser = ArgumentParser(prog="ffufParser.py", description="I parse ffuf output files")
parser.add_argument("ffufOutputDir", help="Ffuf output directory containing .csv files", type=str)
parser.add_argument("output", help="Output file location", type=str)
args = parser.parse_args()

csvs = []
for item in os.listdir(args.ffufOutputDir):
    if item.endswith('.csv'):
        csvs.append(os.path.join(args.ffufOutputDir, item))

with open(args.output, 'w') as finalFile:
    finalFile.write('URL,size,wordcount,linecount\n')

    for acsv in csvs:
        rows = []
        with open(acsv, newline='\n') as file:
            reader = csv.reader(file)
            for row in reader:
                if 'FUZZ' == row[0] and 'url' == row[1]:
                    pass
                else:
                    rows.append(row)

        for row in rows:
            url = row[1]
            code = row[4]
            size = row[5]
            words = row[6]
            linecount = row[7]
            counterSize = 0
            counterWords = 0
            counterLines = 0

            for otherrow in rows:
                if row == otherrow:
                    pass
                else:
                    othersize = otherrow[5]
                    otherwords = otherrow[6]
                    otherlines = otherrow[7]
                    if othersize == size:
                        counterSize += 1
                    if otherwords == words:
                        counterWords += 1
                    if otherlines == linecount:
                        counterLines += 1

            if counterSize > 5 or counterWords > 5 or counterLines > 5 or code == "429" or code == "502" or code == "504":
                pass
            else:
                finalFile.write(f"{url} size={size} words={words} lines={linecount}\n")
                print(f"{url} size={size} words={words} lines={linecount}")
