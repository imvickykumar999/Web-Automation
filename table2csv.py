
def fetchtags():
    from bs4 import BeautifulSoup as bs
    import requests

    link = 'https://up-rera.in/AgentDetails'
    req = requests.get(link)

    soup = bs(req.content, 'html5lib')
    box = soup.findAll('div', attrs = {'class':'container-fluid'}) 

    k = box[3].findAll('div', attrs = {'class':'col-sm-2'})
    # v = box[3].findAll('div', attrs = {'class':'col-sm-4'})

    mylst=[]
    myval=[]
    for i in k:
        mylst.append(i.text.split(' :')[0])
        myval.append('Value')

    out = dict(zip(mylst, myval))
    # print(out)

    import pandas as pd
    df = pd.DataFrame(out, index=[0])
    print(df)
    df.to_csv('output.csv')


    # for i in v:
    #     print(i.text)

    # r = box[3].findAll('span', attrs = {'id':'ctl00_ContentPlaceHolder1_lblbankname'})
    # l = r[0]
    # print(l)

# fetchtags()



def automatetab():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get('https://up-rera.in/agents')
    lst = []

    # for i in range(2, 5778):
    for i in range(2, 5):
        if i < 10:
            i = f'0{i}'
        else:
            i = f'{i}'
        ViewDetails = driver.find_element(By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_grdagents_ctl{i}_lnkView"]')
        ViewDetails.click()

        
        driver.switch_to.window(driver.window_handles[int(i)-1])
        elements = driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/div/div[2]/div/div/div')
        mylst = elements.text.split('\n')
        print(mylst)

        lst.append(mylst[1::2])
        driver.switch_to.window(driver.window_handles[0])

    import pandas as pd
    df = pd.DataFrame(lst, columns = mylst[::2])
    print(df)

automatetab()
