import requests
import re


url = 'https://bj.lianjia.com'

headers = {'user-agent': 'my-app/0.0.1'}
#假装自己是浏览器，很重要，反爬虫措施会让请求返回403

r = requests.get(url, headers=headers)

html = r.text

pattern = re.compile('(^/s.套$)',re.S)
res = re.match(pattern,html)



print(res)
