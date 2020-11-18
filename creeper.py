import re
import os
import json
import requests
import pandas as pd
import threading
from bs4 import BeautifulSoup


def logging_foreignTrendList_data(x):
    tmp0 = x['trend']['updateDate']
    tmp1 = list()
    tmp2 = list()
    for j in x['trend']['list']:
        tmp1.append(j['data'])
        tmp2.append(j['name'])
    tmp3 = pd.DataFrame(tmp1, columns=tmp0, index=tmp2)
    tmp4 = os.path.join('D:/', 'test', 'anacondatest', 'data', i['name'])
    tmp3.to_csv(tmp4)


def logging_globalList_data(x):
    tmp0 = pd.DataFrame(x['subList'])
    tmp0.set_index(['country'], inplace=True)
    del tmp0['relativeTime']
    tmp1 = os.path.join('D:/', 'test', 'anacondatest', 'data', x['area'])
    tmp0.to_csv(tmp1)


def logging_data(x):
    tmp0 = data[x]['updateDate']
    tmp1 = list()
    tmp2 = list()
    for j in data[x]['list']:
        tmp1.append(j['data'])
        tmp2.append(j['name'])
    tmp3 = pd.DataFrame(tmp1, columns=tmp0, index=tmp2)
    tmp4 = os.path.join('D:/', 'test', 'anacondatest', 'data', x)
    tmp3.to_csv(tmp4)


while True:
    try:
        url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
        r = requests.get(url, timeout=5)
        r = r.text
        r = BeautifulSoup(r, 'html.parser')
        r = str(r.find_all('script')[11])
        r = re.sub('<.*?>', '', r)
        data = json.loads(r)
    except BaseException:
        pass
    else:
        break


data = data['component'][0]
data0 = ['allForeignTrend', 'foreignTrendList', 'globalList', 'trend']


logging_data(data0[0])

logging_data(data0[3])

data03 = dict()

for i in data['globalList']:
    th = threading.Thread(target=logging_globalList_data, args=[i])
    th.start()

try:
    for i in data['foreignTrendList']:
        print(True)
        th = threading.Thread(target=logging_foreignTrendList_data, args=[i])
        th.start()
except:
    print('-_-!')
