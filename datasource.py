import requests as re
import json
import re as re0
from bs4 import BeautifulSoup


url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
r = re.get(url)
r = r.content.decode('utf-8')
r = BeautifulSoup(r, 'html.parser')
r_list0 = r.find_all('script')
r_list1 = list()
print(r_list0[6])
print(r_list0[8])
print(r_list0[10])
# with open('tmp', 'a+') as fb:
#     for i in [r_list0[6], r_list0[8], r_list0[10]]:
#         fb.write(str(i))
