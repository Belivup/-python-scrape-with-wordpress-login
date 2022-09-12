
import requests
from requests_html import HTMLSession
s = HTMLSession()


with requests.Session() as s:
    cookies = {
        '_gcl_au': '1.1.1894812994.1662830958',
        '_gid': 'GA1.2.45727059.1662830958',
        '_fbp': 'fb.1.1662830958439.1219977892',
        '__stripe_mid': '51a81887-1e69-49ce-8042-4762284e9dee638f76',
        'wp_woocommerce_session_6e6b7bea34744ce4fa04edb11e766e6c': '82998%7C%7C1663125770%7C%7C1663122170%7C%7C7dcc981ca9541f42ce3549ca8641cd8f',
        'quform_session_6e6b7bea34744ce4fa04edb11e766e6c': 'xhEIcRWBb7Re9sgELCelyKAXwNjdqDMRFN8LAhfO',
        '__cf_bm': 'rftr7YgjmXIEW3fEnw4gM8fVzJzG5vSBxgnRewjdw9A-1662960539-0-AQYuN6wJ24wyXYvtG1BdlxQuiRODL3CP6hNbbtMoDZ1TXE8YXnUD7hVzS4JDV8vonT+QqIrqyiqOGkiO+SzfnUPUbcvGvmyTxacgbUlsskt2cI+85Ffm6WVwIP87HR7l9A==',
        '_ga': 'GA1.1.854280509.1662830958',
        '__stripe_sid': 'e6cb229e-283f-4868-9e53-81ba2366ca6d865394',
        'wordpress_test_cookie': 'WP%20Cookie%20check',
        '_ga_NTC0ZGHL5H': 'GS1.1.1662960538.12.1.1662960598.0.0.0',
    }

    headers = {
        'authority': 'plugintheme.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1894812994.1662830958; _gid=GA1.2.45727059.1662830958; _fbp=fb.1.1662830958439.1219977892; __stripe_mid=51a81887-1e69-49ce-8042-4762284e9dee638f76; wp_woocommerce_session_6e6b7bea34744ce4fa04edb11e766e6c=82998%7C%7C1663125770%7C%7C1663122170%7C%7C7dcc981ca9541f42ce3549ca8641cd8f; quform_session_6e6b7bea34744ce4fa04edb11e766e6c=xhEIcRWBb7Re9sgELCelyKAXwNjdqDMRFN8LAhfO; __cf_bm=rftr7YgjmXIEW3fEnw4gM8fVzJzG5vSBxgnRewjdw9A-1662960539-0-AQYuN6wJ24wyXYvtG1BdlxQuiRODL3CP6hNbbtMoDZ1TXE8YXnUD7hVzS4JDV8vonT+QqIrqyiqOGkiO+SzfnUPUbcvGvmyTxacgbUlsskt2cI+85Ffm6WVwIP87HR7l9A==; _ga=GA1.1.854280509.1662830958; __stripe_sid=e6cb229e-283f-4868-9e53-81ba2366ca6d865394; wordpress_test_cookie=WP%20Cookie%20check; _ga_NTC0ZGHL5H=GS1.1.1662960538.12.1.1662960598.0.0.0',
        'origin': 'https://plugintheme.net',
        'referer': 'https://plugintheme.net/wp-login.php',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    data = {
        'log': 'belivup@gmail.com',
        'pwd': 'DemoPass12',
        'wp-submit': 'Log In',
        'redirect_to': 'https://plugintheme.net/wp-admin/',
        'testcookie': '1',
    }
    s.post('https://plugintheme.net/wp-login.php', cookies=cookies, headers=headers, data=data)

    # page = s.get("https://plugintheme.net/shop/betheme-responsive-multi-purpose-wordpress-theme/").text
    # print (page)




