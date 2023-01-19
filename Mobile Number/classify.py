
import pandas as pd

link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'


def fetch():
    from bs4 import BeautifulSoup as bs
    import requests

    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    box = soup.findAll('table', attrs = {'class':'wikitable'}) 
    print(box[1])


def save():
    df = pd.read_html(link)[8]
    df.to_csv("5 series.csv", index=False)
    print(df)


def readcsv():
    csvFile = pd.read_csv('6 series.csv')
    print(csvFile.columns)

readcsv()
