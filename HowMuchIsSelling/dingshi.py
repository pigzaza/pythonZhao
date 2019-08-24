import schedule #pip
import time
import csv      #pip
import datetime
import requests
import re


today=datetime.date.today()
print (today)
#str(today)
print (type(today))



    # 1. 创建文件对象
f = open('lj.csv','w',encoding='utf-8')

    # 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

    # 3. 构建列表头
csv_writer.writerow(["日期","数量"])

f.close()

def job():
    url = 'https://bj.lianjia.com'

    headers = {'user-agent': 'my-app/0.0.1'}
    #假装自己是浏览器，很重要，反爬虫措施会让请求返回403

    r = requests.get(url, headers=headers)

    #if r.status_code ==200:
    #r.encoding = r.apparent_encoding        #转换字符编码
    html = r.text
    pattern = re.compile(r"[\u4e00-\u9fa5]\s+\d{4,6}\s+[\u4e00-\u9fa5]")
        #   正则匹配汉字问题还有待研究
    res = pattern.findall(html)


    print('----')
    print(res)#输出结果是['房 86452 套', '房 25887 套']


    num = res[0]      #分离出数字部分字符串

    #print(num)

    numSell = num.split()[1]
    #用空格把 房、86452、套 分开，取第二个数字那部分
    print(numSell)
    print(type(numSell))


    # 1. 创建文件对象
    f = open('lj.csv','w',encoding='utf-8')

    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)

    # 4. 写入csv文件内容
    csv_writer.writerow([today,numSell])

    # 5. 关闭文件
    f.close()


schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).days.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
