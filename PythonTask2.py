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
        del listCSV[0]

    listCSV.sort(key=lambda row: (row[0], row[1]))
    count = int(0)
    sumV = float(0)
    maxV = float(0)
    minV = sys.maxsize
    oldDate = listCSV[0][0]
    oldCompany = listCSV[0][1]
    result = [['DATE', 'DESC', 'MIN', 'MAX', 'AVG']]
    for i in range(0, len(listCSV)):
        try: 
            company = listCSV[i][1]
            date = listCSV[i][0]
        
            if oldCompany != company or oldDate != date:
                avg = sumV / count
                result.append([oldDate, oldCompany, minV, maxV, avg])
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
            oldCompany = company
            count += 1
            if i == len(listCSV)-1:
                avg = sumV / count
                result.append([oldDate, oldCompany, minV, maxV, avg])

        except (ValueError, TypeError):
            raise ValueError('Некорректные данные')
    
    with open('Result_Task2.csv', 'w', newline='') as res_file:
        writer = csv.writer(res_file)
        for row_in_res in result:
            writer.writerow(row_in_res)
    res_file.close()

if __name__ =='__main__':
    analyzer(infile='5000000 BT Records')

print('--- %s second---' % (time.time() - start_time))