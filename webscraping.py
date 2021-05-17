from selenium import webdriver
from dailyreport import produceReport
from readwow import processWow
from readcoles import processColes
from readhf import processHF
from readmm import processMM
from readm4u import processM4U
from master import makeReport

driver = webdriver.Chrome(executable_path=r"F:/downloads/chromedriver_win32/chromedriver.exe")

with open('webs.txt', 'r') as webs:
    counter =1
    for l in webs:
        print(l)
        driver.get(l)
        name = str(counter)+".html"
        
        with open('webs\\'+name, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        counter+=1
makeReport()
