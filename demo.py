import requests
import csv
import uuid
from requests_html import HTMLSession
from datetime import date
s = HTMLSession()


# ----------------------------------- Functions -------------------------------------------


def theme_page_len():
    r = s.get('https://plugintheme.net/product-category/wordpress-themes/')
    products = r.html.find('.page-numbers', first=True).text.splitlines()
    page_len = int(products[-1]) + 1
    print(page_len)
    return page_len


theme_page_len()