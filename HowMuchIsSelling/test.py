import requests
import re
import schedule #pip
import time
import csv      #pip
import datetime

today=datetime.date.today()
print (today)
#str(today)
print (type(today))

url = 'https://bj.lianjia.com'

headers = {'user-agent': 'my-app/0.0.1'}
#假装自己是浏览器，很重要，反爬虫措施会让请求返回403

r = requests.get(url, headers=headers)

if r.status_code == 200:
    r.encoding = r.apparent_encoding        #转换字符编码
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

f = open('lj.csv','a+',encoding='utf-8') #open中的a+方式是增加列

    # 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

    # 4. 写入csv文件内容
csv_writer.writerow([today,numSell])

    # 5. 关闭文件
f.close()
