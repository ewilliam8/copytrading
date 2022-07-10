import requests
import multiprocessing
from fake_useragent import UserAgent
from requests_html import HTMLSession

test_link = "https://httpbin.org/headers"
link_1 = "https://www.freeproxylists.net/ru/"
link_2 = "http://free-proxy.cz/ru/proxylist/country/all/http/ping/level1"
link_3 = "https://hidemy.name/ru/proxy-list/"
link_4 = "https://free.proxy-sale.com/"
link_5 = "https://smallseotools.com/ru/free-proxy-list/" # скопировать список прокси

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
    'Accept-Language': '*',
    'Referer': 'https://google.com',
    'DNT': '1'
}

# s = HTMLSession()
# r = requests.get(link_5, headers=headers)
# rh = s.get(link_5)

# print(r.text)
# print("- - - - - - - - - - - - - - - - - -")
# print(rh.text)



def handler(proxy):
    link = 'https://icanhazip.com/'

    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }

    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {response.strip()}')
    except:
        print('Proxy is not valid')


with open("proxies.txt") as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')


# with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
#     process.map(handler, proxy_base)

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxy_base)



