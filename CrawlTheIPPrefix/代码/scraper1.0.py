import urllib.request
from bs4 import BeautifulSoup
import json
import time

i=103

wenjian = open('4538prefix(1).txt','w')

while i<538:
    try:
        urlpage =  'https://radar.qrator.net/api/new-prefixes/ipv4/4538/current?firstseen=1568851200&lastseen=1576713600&lookup=&page='+str(i)
        # query the website and return the html to the variable 'page'
        page = urllib.request.urlopen(urlpage)
    except Exception:
        print('第%d页获取失败' % (i))
        time.sleep(3)
        continue
    else:
        # parse the html using beautiful soup and store in variable 'soup'
        soup = BeautifulSoup(page, 'html.parser')
        #print(type(soup))
        b= soup.get_text().lstrip('"meta":{"status":"success","code":200,"total":5372},"data":{"items"')
        c = b.rstrip('}')
        d = "{\"items\":" + c+"}"
        #print(d)
        #print(type(c))

        user_info = d
        user_dict = json.loads(user_info)
        #print(user_dict)
        print('第 %d 页' % (i))

        #print(type(user_dict))

        print(user_dict['active_now'])

        for items in user_dict['active_now']:
            wenjian.write(items)
            wenjian.write('\n')
        time.sleep(2)

        i=i+1


wenjian.close()










