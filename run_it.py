# Import necessary libraries and modules
from asinGenerator import canadian, american
from Scraper import Scrape
from openpyxl.workbook import Workbook

# Create a new Excel workbook and save it as "data.xlsx"
wb = Workbook()
wb.save("data.xlsx")

# List of Amazon product URLs
product = [
    'https://www.amazon.com/Grandmas-Cookies-Variety-Pack-Count/dp/B076BYR9JP/ref=sr_1_1?dchild=1&keywords=cookies&qid=1618876515&sr=8-1',
    'https://www.amazon.com/Oreo-Double-Chocolate-Sandwich-Cookies/dp/B07ZV2DXDJ/ref=sr_1_7?dchild=1&keywords=cookies&qid=1618877932&sr=8-7'
]

# Get a list of Canadian ASINs
can = canadian()

# Get a list of American ASINs (currently unused in this code)
us = american()

# Loop through the Canadian ASINs and scrape data for each one
for i in can:
    Scrape(i)
