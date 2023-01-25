
import pandas as pd, csv, os, pymongo

try:
    os.mkdir('data')
except:
    pass

class filter_series:
    link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'
    pairs = {
        0 : 'Telecom circles',
        1 : 'Network operators',
        3 : '9 series',
        4 : '8 series',
        5 : '7 series',
        6 : '6 series'
    }
    print('\n', pairs, '\n')

    def info_tables(self, i,p=1,d=0):
        df = pd.read_html(self.link)[i]

        if p:
            print(df.iloc[:,:2])
            print('-'*40)

        if d:
            df.to_csv(f"data/{self.pairs[i]}.csv", index=False)


    def readcsv(self):
        try:
            os.remove("OUTPUT.csv")
        except:
            pass
        print('Index, Series, Operator, Circle	')
        print('-'*40)

        try:
            csv_phno = pd.read_csv('INPUT.csv')
            file = open('OUTPUT.csv', 'a')
            file.write('phno,sim,city\n')

            for k in range(0, len(csv_phno.index)):
                phno = str(csv_phno.iloc[k,0])
                csvFile = pd.read_csv(f'data/{self.pairs[12 - int(phno[0])]}.csv')

                for i in range(len(csvFile.index)):
                    for j in range(len(csvFile.iloc[i, :])):

                        if (len(str(csvFile.iloc[i, :][j])) == 4) or (len(str(csvFile.iloc[i, :][j])) == 6):
                            try:
                                if int(phno[:4]) == int(csvFile.iloc[i, :][j]):
                                    file.write(f'{csv_phno.iloc[k,0]}, {csvFile.iloc[i, :][j+1]}, {csvFile.iloc[i, :][j+2]}' + '\n')
                                    print(f'{k+1} / {len(csv_phno.index)}, {int(csvFile.iloc[i, :][j])} {phno[4:]}, {csvFile.iloc[i, :][j+1]}, {csvFile.iloc[i, :][j+2]}')
                            except:
                                pass
            file.close()
        except Exception as e:
            print(e)
            self.info_tables(3,0,1)
            self.info_tables(4,0,1)
            self.info_tables(5,0,1)
            self.info_tables(6,0,1)
            self.readcsv()


    def filter(self):
        filename = "OUTPUT.csv"
        df = pd.read_csv(filename)
        df = df.to_dict(orient="records")

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["filterphnoDB"]
        try:
            mydb.filterphnoColl.drop()
        except:
            pass
        mycol = mydb["filterphnoColl"]
        mycol.insert_many(df)

        print('\n', '-'*40)
        sim = input('Enter SIM Code : ')
        city = input('Enter CITY Code : ')
        myquery = {"sim" : f" {sim}", "city" : f" {city}"}
        mydoc = mycol.find(myquery)

        toapp=[]
        for x in mydoc:
            toapp.append(x)
        filtered = pd.DataFrame.from_dict(toapp)
        print('\n', '-'*40)
        print(filtered[['phno', 'sim', 'city']], '\n')


obj = filter_series()
try:
    obj.info_tables(0,1,0)
except:
    obj.info_tables(0,1,1)
try:
    obj.info_tables(1,1,0)
except:
    obj.info_tables(1,1,1)
obj.readcsv()
obj.filter()
