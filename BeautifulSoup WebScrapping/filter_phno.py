
import pandas as pd
import pymongo
import pandas as pd, os


filename = "OUTPUT.csv"
df = pd.read_csv(filename)
df = df.to_dict(orient="records")
# print(df)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["filterphnoDB"]
mycol = mydb["filterphnoColl"]
# mycol.insert_many(df)


link = 'https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India'
pairs = {
    0 : 'Telecom circles',
    1 : 'Network operators',
    3 : '9 series',
    4 : '8 series',
    5 : '7 series',
    6 : '6 series'
}

def save_tables(i):
    df = pd.read_html(link)[i]
    print(df.iloc[:,:2])
    print('-'*40)

save_tables(0)
save_tables(1)


# filter by sim and city
sim = input('Enter SIM Code : ')
city = input('Enter CITY Code : ')
myquery = {"sim" : f" {sim}", "city" : f" {city}"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
    # filtered = pd.DataFrame.from_dict(x)
    # print(filtered)
