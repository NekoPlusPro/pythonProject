import csv
with open('wmau.csv','r',encoding='utf-8') as r:
    with open('nwmau.csv','w',encoding='utf-8-sig') as w:
        reader = csv.reader(r)
        writer = csv.writer(w)
        header_row = next(reader)
        for row in reader:
            row[0]=row[2][:7].replace('-','')
            row[4],row[6]=row[6],row[4]
            row[5], row[6] = row[6], row[5]
            writer.writerow(row)