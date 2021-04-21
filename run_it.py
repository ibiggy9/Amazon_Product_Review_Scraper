from asinGenerator import canadian, american
from Scraper import Scrape
from openpyxl.workbook import Workbook

wb = Workbook()
wb.save("data.xlsx")

product = ['https://www.amazon.com/Grandmas-Cookies-Variety-Pack-Count/dp/B076BYR9JP/ref=sr_1_1?dchild=1&keywords=cookies&qid=1618876515&sr=8-1','https://www.amazon.com/Oreo-Double-Chocolate-Sandwich-Cookies/dp/B07ZV2DXDJ/ref=sr_1_7?dchild=1&keywords=cookies&qid=1618877932&sr=8-7']
can = canadian()
us = american()
for i in can:
    Scrape(i)


