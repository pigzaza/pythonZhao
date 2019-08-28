import requests
import re
import schedule #pip
import time
import csv      #pip
import datetime


def Get_info():

    url = 'https://bj.lianjia.com'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        r.encoding = r.apparent_encoding        #转换字符编码??
        html = r.text
        res = re.findall(r"[\u4e00-\u9fa5]\s+(\d{4,6})\s+[\u4e00-\u9fa5]",html)
        num = res[0]

    return num

def add_data(num):
    today=datetime.date.today()

    now = datetime.datetime.now()
    f = open('lj.csv','a+',encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow([now,num，today])
    f.close()

def job():
    num = Get_info()

    add_data(num)

schedule.every(60).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
