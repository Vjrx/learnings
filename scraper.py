import requests
from bs4 import BeautifulSoup
import re

url = "https://www.fast2sms.com/dev/bulk"


def get_news():
    source = requests.get("https://www.thehindu.com/news/national").text

    simple = BeautifulSoup(source, 'lxml')
    justin = simple.find_all('div', class_='justIn-story')
    news_list = []
    for div in simple.find_all('div', class_='justIn-story'):
        for ul in div.find_all('ul'):
            for li in ul.find_all('li'):
                for a in li.find_all('a'):
                    news_list.append(str(a.text).strip())

    innoru_list = []
    for item in news_list:
        ii = item.replace("\n", "")
        k = re.sub("\d+(hrs|mins|hr|min)",'',ii)
        innoru_list.append(k)

    return innoru_list


def send_sms():
    url = "https://www.fast2sms.com/dev/bulk"
    headers = {
        'authorization': "53CZHOqWRhUnQmE68rIABTkV2z7ioDS9sPjulKaNGXdeMp4c0xAOwrvx8mUatf96JCeilGsTFybBI0VR",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    msg_list = get_news()[:7]
    msg = '***'.join(msg_list)
    msg = msg.encode('utf-8')
    payload = "sender_id=FSTSMS&message={msg}&language=english&route=p&numbers={no}".format(msg=msg, no=9715617608)
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code <400:
        print("msg sent")



send_sms()