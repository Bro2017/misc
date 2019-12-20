#import sys
#import urllib2
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#reload(sys)
#sys.setdefaultencoding('utf8') # 设置编码

url = 'https://radar.qrator.net/as4538/prefixes#startDate=2019-09-19&endDate=2019-12-19&tab=current'
driver = webdriver.Chrome('C:\\Users\\Jiang\\AppData\\Local\\Programs\\Python\\Python36-32\\chromedriver.exe')
# 创建一个driver用于打开网页，记得找到安装的chromedriver的位置，在创建driver的时候指定这个位置
driver.get(url) # 打开网页

page =0
rows = []
rows.append(['Prefix'])
wenjian = open('123.txt','w')

while page < 537:
    soup = BeautifulSoup(driver.page_source,"html.parser")
    table = soup.find('table', attrs={'class': 'b-data-table'})
    results = table.find_all('tr')
    print('Number of results', len(results))

    for result in results:
        # find all columns per result
        data = result.find_all('td')
        # check that columns have data
        if len(data) == 0:
            continue
        prefix = data[0].getText()
        rows.append([prefix])

    print(rows)

    if(page %20 == 0):
        for item in rows:
            wenjian.write(str(item[0]))
            wenjian.write('\n')
        rows= []
        time.sleep(2)

    try:
        driver.find_element_by_xpath("//a[contains(text(),'Next')]").click() # selenium的xpath用法，找到包含“下一页”的a标签去点击
    except Exception:
        print("第%d页失败",page+1)
        time.sleep(3)
        continue
    else:
        page = page + 1
        time.sleep(3) # 睡2秒让网页加载完再去读它的html代码



wenjian.close()
driver.quit()