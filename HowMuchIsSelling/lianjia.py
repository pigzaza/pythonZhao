import requests
import re


url = 'https://bj.lianjia.com'

headers = {'user-agent': 'my-app/0.0.1'}
#假装自己是浏览器，很重要，反爬虫措施会让请求返回403

r = requests.get(url, headers=headers)

html = r.text
pattern = re.compile(r"[\u4e00-\u9fa5]\s+\d{4,6}\s+[\u4e00-\u9fa5]")
#   正则匹配汉字问题还有待研究
res = pattern.findall(html)

#print(html)
print('----')
print(res)
#输出结果是['房 86452 套', '房 25887 套']

#以下分离出数字部分字符串
num = res[0]
print(num)

numSell = num.split()[1]
#用空格把 房、86452、套 分开，取第二个数字那部分
print(numSell)
print(type(numSell))
