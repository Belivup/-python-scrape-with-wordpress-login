import requests
import csv
import uuid
from requests_html import HTMLSession
from datetime import date
s = HTMLSession()
from login import cookies, headers, data, HTMLSession

s.post('https://plugintheme.net/wp-login.php', cookies=cookies, headers=headers, data=data)


# ----------------------------------- Functions -------------------------------------------


def get_products_links(page):
    url = f'https://plugintheme.net/product-category/wordpress-themes/page/{page}/'
    links = []
    r = s.get(url)
    products = r.html.find('.product-title')
    for item in products:
        links.append(item.find('a', first=True).attrs['href'])
    return links


def parse_products(url):
    r = s.get(url)
    title = r.html.find('h1.product-title.entry-title', first=True) .text.strip()
    price = int(2)
    try:
        demo_link = r.html.find('a.grey-link', first=True).attrs['href']
    except AttributeError as err:
        demo_link = ""

    try:
        download_link = r.html.find('a.red-link', first=True).attrs['href']
    except AttributeError as err:
        download_link = ""

    image = r.html.find('.woocommerce-product-gallery__image a', first=True).attrs['href']

    try:
        fcat = r.html.find('.posted_in', first=True)
        scat = fcat.text.splitlines()
        cat = ' '.join(scat).replace("Categories: ", "WordPress Theme > ")
    except AttributeError as err:
        cat = "WordPress Theme > WordPress Theme"

    try:
        full_des = r.html.find('#tab-description', first=True)
        ff_des = full_des.text.splitlines()
        f_des = ' '.join(ff_des).replace(".", "<br><br>")

    except AttributeError as err:
        f_des = "No Description Given, Please visit the official website for Descriptions, Thank you"

    try:
        versions = r.html.find('.product-short-description ul li:nth-child(7) ', first=True)
        version = versions.text.replace("Product Version : ", "")
    except AttributeError as err:
        version = "Current Version"


    today = date.today()
    update = today.strftime("%d/%m/%Y")

    product_details = {
        'Title': title,
        'Date': update,
        'Author': "wpview",
        'Featured Image': image,
        'Product Version': version,
        'Download Categories': cat,
        'Post type': 'download',
        'Demo Link': demo_link,
        'Status': 'publish',
        'Edd Price': price,
        'Files: File: 1': download_link,
        'Mayosis Features Field: Name: 1': 'Very cheap price & Original product',
        'Mayosis Features Field: Name: 2': 'We Purchase And Download From Original Authors',
        'Mayosis Features Field: Name: 3': 'You’ll Receive Untouched And Unmodified Files',
        'Mayosis Features Field: Name: 4': '100% Clean Files & Free From Virus',
        'Mayosis Features Field: Name: 5': 'Unlimited Domain Usage',
        'Mayosis Features Field: Name: 6': 'Free New Version',
        'Edd Button Behavior': 'add_to_cart',
        'Bundle Required Price: 0: 2': 'all',
        'Content': f_des,

    }
    return product_details


def save_csv(results):
    keys = results[0].keys()

    with open('Products.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


def main():
    results = []

    for x in range(1, 2):
        urls = get_products_links(x)
        for url in urls:
            results.append(parse_products(url))
            print(parse_products(url))
        save_csv(results)

main()


