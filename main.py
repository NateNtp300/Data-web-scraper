from bs4 import BeautifulSoup
import smtplib
import requests
import csv
import datetime
import time

# URL = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}
# # result = requests.get(url)
# # doc = BeautifulSoup(result.text, "html.parser")
# # #print(doc.prettify())

# # prices = doc.find_all(text = "12GB")
# # print(prices)
# today = datetime.date.today()
# page = requests.get(URL, headers=headers)

# soup1 = BeautifulSoup(page.content, "html.parser")
# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# # print(soup2)

# title = soup2.find(class_ = 'product-title').get_text()
# price = soup2.find(class_ = 'btn btn-message btn-wide').get_text()

# price = price.strip()[1:]
# title = title.strip()

# print(price)
# print(title)

# #csv setup
# header = ['Title', 'Price', 'Date']
# data = [title, price, today]

# # with open('NeweggData.csv','w',newline='',encoding='UTF8') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(header)
# #     writer.writerow(data)

# #appending data
# with open('NeweggData.csv','a+',newline='',encoding='UTF8') as f:
#     writer = csv.writer(f)
    
#     writer.writerow(data)

def check_price():
    URL = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(class_ = 'product-title').get_text()
    price = soup2.find(class_ = 'btn btn-message btn-wide').get_text()
    price = price.strip()[1:]
    title = title.strip()
    today = datetime.date.today()
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('NeweggData.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

#checks price data every day. there is 86400 seconds in a day
while(True):
    check_price()
    time.sleep(86400)
