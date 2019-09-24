import requests
import re
import json
import urllib.parse

def get_vedio_url(url):
    print(url)
    response= requests.get(url)
    # print(response.text+'\n\n\n\n\n')
    vedio_url=re.search('.*\"adaptive_fmts\"\:(.*url=https.*google.*)',response.text)
    # print(vedio_url.group(1))
    vedio_url= urllib.parse.unquote(vedio_url.group(1))
    for item in vedio_url.split('\\u0026'):
        if bool(re.search('.*url=(https.*)',item)):
            vedio_url=re.search('.*url=(https.*)',item)
            print(vedio_url.group(1))
    pass


if __name__ == '__main__':
    short_url_list=['OPHOJhema3c']
    for short_url in short_url_list:
        url = 'https://www.youtube.com/watch?v=%s'%(short_url)
        get_vedio_url(url=url)
    pass