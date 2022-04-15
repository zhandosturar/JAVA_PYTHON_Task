import sys
import time
import csv
from memory_profiler import profile

start_time = time.time()

@profile
def analyzer(infile):

    with open(infile, 'r', newline='') as infile:
        rowreader = csv.reader(infile, delimiter=',', quotechar='"')
        listCSV = []
        for row in rowreader:
            for i in range(len(row)):
                row[i] = row[i].replace(',', '')
            listCSV.append(row)

    count = int(0)
    sumV = float(0)
    maxV = float(0)
    minV = sys.maxsize
    oldDate = listCSV[1][0]
    result = [['DATE', 'MIN', 'MAX', 'AVG']]
    for i in range(1, len(listCSV)):
        try:
            date = listCSV[i][0]
            if oldDate != date:
                avg = sumV / count
                result.append([oldDate, minV, maxV, avg])
                count = int(0)
                sumV = float(0)
                maxV = float(0)
                minV = sys.maxsize
            if float(listCSV[i][3]) > maxV:
                maxV = float(listCSV[i][3])
            if float(listCSV[i][3]) < minV:
                minV = float(listCSV[i][3])
            sumV += float(listCSV[i][3])
            oldDate = date
            count += 1
            if i == len(listCSV)-1:
                avg = sumV / count
                result.append([oldDate, minV, maxV, avg])

        except (ValueError, TypeError):
            raise ValueError('Некорректные данные')
    
    with open('Result_Task1.csv', 'w', newline='') as res_file:
        writer = csv.writer(res_file)
        for row_in_res in result:
            writer.writerow(row_in_res)
    res_file.close()
 
if __name__ =='__main__':
    analyzer(infile = '5000000 BT Records')

print('--- %s second---' % (time.time() - start_time))