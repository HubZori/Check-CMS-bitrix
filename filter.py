from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from urllib.request import *
import socket
import ssl
import http.client


def check_cms(url):
    page = urlopen(url).read()

    html = BeautifulSoup(page, 'html.parser', from_encoding="iso-8859-1")

    metas = html.find_all('link')

    for meta in metas:

        if(meta.get('href')):
            href = meta.get('href')
            strBitrix = href.split('/')
            for b in strBitrix:

                if b == 'bitrix':
                    result = 'found use bitrix cms in ' + url
                    print(result)
                    fun = open('result.txt', 'a')
                    fun.write(result)
                    fun.close()

            break


sites = open('list.txt', 'r')

for site in sites:

    print(site)

    try:
        check_cms(site)

    except HTTPError as e:
        continue
    except URLError as e:
        continue
    except socket.timeout:
        continue
    except http.client.HTTPException as e:
        continue
    except ssl.SSLWantReadError:
        continue
    except socket.error as error:
        continue
    except UnicodeEncodeError as e:
        continue
sites.close()
