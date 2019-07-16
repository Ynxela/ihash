import requests
from lxml import html

url = 'https://wikigrowth.ru/gizn/kak-nayti-sebya/'
response = requests.get(url)
parsed_html = html.fromstring(response.text)
title = parsed_html.xpath('//title/text()')[0]
images_srcs = parsed_html.xpath('//img/@src')
print(title)
print()
for scr in images_srcs:
    print(scr)