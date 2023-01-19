
link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'

def fetch():
    from bs4 import BeautifulSoup as bs
    import requests

    req = requests.get(link)
    soup = bs(req.content, 'html5lib')

    box = soup.findAll('table', attrs = {'class':'wikitable'}) 
    print(box[1])


def save():
    import pandas as pd

    df = pd.read_html(link)[8]
    print(df)

