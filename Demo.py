import requests
import re
import json
import urllib.parse

def get_all_video_url(url):
    print(url)
    all_video_url=[]
    response= requests.get(url)
    # print(response.text+'\n\n\n\n\n')
    video_url=re.search('.*\"adaptive_fmts\"\:(.*url=https.*google.*)',response.text)
    # print(video_url.group(1))
    video_url= urllib.parse.unquote(video_url.group(1))
    for item in video_url.split('\\u0026'):
        if bool(re.search('.*url=(https.*)',item)):
            video_url=re.search('.*url=(https.*[a-zA-Z])',item)
            print(video_url.group(1))
            all_video_url.append(video_url.group(1))
    return all_video_url
    pass


if __name__ == '__main__':
    short_url_list=['OPHOJhema3c']
    for short_url in short_url_list:
        url = 'https://www.youtube.com/watch?v=%s'%(short_url)
        urls=get_all_video_url(url=url)
        print(urls)
    pass