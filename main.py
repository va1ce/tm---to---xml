import json
import requests
import openpyxl
import time

time_dep = int(time.time()) // 1
time_nach = 1643572818
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def print_hi():
    response = requests.get(url = f'https://market.csgo.com/api/v2/history?key=X50z12a3531GTbEDl3104nEmH54884W&date={time_nach}&date_end={time_dep}',headers=headers)
    with open('result.json','w',encoding="UTF-8") as file:
        json.dump(response.json(),file,indent=4, ensure_ascii=False)
    with open('result.json') as file:
        data = json.load(file)
    for skins in data['data']:
        name = skins['market_hash_name']
        price = int(skins['received']) / 100
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'name'
    sheet['C1'] = 'продажа на тме'
    row = 2
    for skins in data['data']:
        sheet[row][0].value = skins['market_hash_name']
        sheet[row][2] .value= int(skins['received']) / 100
        row+=1
    book.save("trade10k.xlsx")
    book.close()


if __name__ == '__main__':
    print_hi()
    print('Я даун :)')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
