
from selenium import webdriver
from selenium.webdriver.common.by import By

def automatetab():
    driver = webdriver.Chrome()
    driver.get('https://up-rera.in/agents')
    file = open('output.csv', 'w')

    # for i in range(2, 5778):
    for i in range(2, 15):
        if i < 10:
            i = f'0{i}'
        else:
            i = f'{i}'
        ViewDetails = driver.find_element(By.XPATH, f'//*[@id="ctl00_ContentPlaceHolder1_grdagents_ctl{i}_lnkView"]')
        ViewDetails.click()

        try:
            driver.switch_to.window(driver.window_handles[int(i)-1])
        except:
            pass

        elements = driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div/div/div[2]/div/div/div')
        mylst = elements.text.split('\n')

        for j in range(len(mylst)):
            try:
                if (':' in mylst[j]) and (':' in mylst[j+1]):
                    j+=1
                    mylst.insert(j, 'Null')
            except:
                pass

        if i=='2':
            file.write(', '.join(mylst[::2])+'\n')
        else:
            file.write(', '.join(mylst[1::2])+'\n')
        driver.switch_to.window(driver.window_handles[0])
    file.close()

automatetab()
