
def automatetab():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get('https://up-rera.in/agents')
    lst = []

    # for i in range(2, 5778):
    for i in range(2, 45):
        if i < 10:
            i = f'0{i}'
        else:
            i = f'{i}'
        ViewDetails = driver.find_element(By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_grdagents_ctl{i}_lnkView"]')
        ViewDetails.click()

        driver.switch_to.window(driver.window_handles[int(i)-1])
        elements = driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/div/div[2]/div/div/div')
        mylst = elements.text.split('\n')

        for i in range(len(mylst)):
            try:
                if (':' in mylst[i]) and (':' in mylst[i+1]):
                    i+=1
                    mylst.insert(i, 'Null')
            except:
                pass

        print(mylst)
        lst.append(mylst[1::2])
        driver.switch_to.window(driver.window_handles[0])

    import pandas as pd
    df = pd.DataFrame(lst, columns = mylst[::2])
    df.to_csv('output.csv')

automatetab()
