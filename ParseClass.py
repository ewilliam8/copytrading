import urllib.request
import urllib.error
import datetime
import socket
import json


class Parse():
    def get(self, link):
        try:
            fp = urllib.request.urlopen(link)
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
        except:
            mystr = None
        return mystr

    def _is_bad_proxy(self, proxy, link):    
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_handler)
            # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req=urllib.request.Request(link)  # change the URL to test here
            sock=urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
            return e.code
        except Exception as detail:
            print("ERROR:", detail)
            return True
        return False

    def check_proxy_list(self, list):
        socket.setdefaulttimeout(10)

        proxyList = list

        for currentProxy in proxyList:
            if self._is_bad_proxy(currentProxy):
                self._eprint("Bad Proxy %s" % (currentProxy))
            else:
                self._eprint("%s is working" % (currentProxy))

    def _eprint(to_print: str):
        time_now = datetime.datetime.now()
        today_date = time_now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"INFO [{today_date}] {to_print}")