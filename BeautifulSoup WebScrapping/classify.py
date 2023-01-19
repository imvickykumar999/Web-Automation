
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'


def fetch():
    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    box = soup.findAll('table', attrs = {'class':'wikitable'}) 
    print(box[1])

# fetch()


def save():
    df = pd.read_html(link)[4]
    print(df)
    # df.to_csv("8 series.csv", index=False)

# save()


def readcsv(phno='8239957923'):
    csvFile = pd.read_csv('8 series.csv')
    csv_phno = pd.read_csv('sample phno.csv')
    print(str(csv_phno.iloc[0,0]))

    for i in range(len(csvFile.index)):
        for j in range(len(csvFile.iloc[i, :])):
            if (len(str(csvFile.iloc[i, :][j])) == 4) or (len(str(csvFile.iloc[i, :][j])) == 6):
                try:
                    if int(phno[:4]) == int(csvFile.iloc[i, :][j]):
                        print(int(csvFile.iloc[i, :][j]), csvFile.iloc[i, :][j+1], csvFile.iloc[i, :][j+2])
                except:
                    pass

phno = '8239957923'
readcsv(phno)
