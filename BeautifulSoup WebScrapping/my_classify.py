
import pandas as pd, csv, os

link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'
pairs = {
    0 : 'Telecom circles',
    1 : 'Network operators',
    3 : '9 series',
    4 : '8 series',
    5 : '7 series',
    6 : '6 series'
}

try:
    os.mkdir('data')
except:
    pass

def save_tables(i, p=0):
    df = pd.read_html(link)[i]
    df.to_csv(f"data/{pairs[i]}.csv", index=False)

    if p:
        print(df.iloc[:,:2])
        print('-'*40)

save_tables(0,1)
save_tables(1,1)
save_tables(3,0)
save_tables(4,0)
save_tables(5,0)
save_tables(6,0)


def readcsv():
    try:
        with open('OUTPUT.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = list(reader)
            row_count = len(data)
    except:
        o_file = open('OUTPUT.csv', 'a')
        o_file.close()

    print('Index, Series, Operator, Circle	')
    print('-'*40)

    try:
        csv_phno = pd.read_csv('INPUT.csv')
    except:
        print('Rename input csv file as "INPUT.csv"')
    file = open('OUTPUT.csv', 'a')

    for k in range(row_count+1, len(csv_phno.index)):
        phno = str(csv_phno.iloc[k,0])
        csvFile = pd.read_csv(f'data/{pairs[12 - int(phno[0])]}.csv')

        for i in range(len(csvFile.index)):
            for j in range(len(csvFile.iloc[i, :])):

                if (len(str(csvFile.iloc[i, :][j])) == 4) or (len(str(csvFile.iloc[i, :][j])) == 6):
                    try:
                        if int(phno[:4]) == int(csvFile.iloc[i, :][j]):
                            file.write(f'{csv_phno.iloc[k,0]}, {csvFile.iloc[i, :][j+1]}, {csvFile.iloc[i, :][j+2]}' + '\n')
                            print(f'{k} / {len(csv_phno.index)}, {int(csvFile.iloc[i, :][j])} {phno[4:]}, {csvFile.iloc[i, :][j+1]}, {csvFile.iloc[i, :][j+2]}')
                    except:
                        pass
    file.close()

while 1:
    try:
        readcsv()
    except Exception as e:
        pass
