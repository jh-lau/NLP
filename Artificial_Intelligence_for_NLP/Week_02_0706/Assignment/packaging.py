"""
  User: Liujianhan
  Time: 23:43
 """
__author__ = 'liujianhan'

from bs4 import BeautifulSoup
import requests
from Week_02_0706.Assignment.api import baidu_api, gaode_api
import json

url = 'https://dt.8684.cn/bj'


def get_metro_map(url):
    metro_map = {}
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup_content = BeautifulSoup(response.text, features="lxml")
    for link in soup_content.find_all(class_='sLink'):
        temp = link.text.split()
        if '未开通' in temp[0]:
            continue
        temp[0] = temp[0].split('线')[0] + '线'
        metro_map[temp[0]] = temp[1:]
    return metro_map


def get_geoinfo_gaode(address):
    output_type = json
    uri = f"https://restapi.amap.com/v3/geocode/geo?address={address}&output={output_type}&key={gaode_api}"
    r = requests.get(uri).text
    result = json.loads(r)['geocodes'][0]['location']
    lng, lat = result.split(',')
    return float(lat), float(lng)


def get_single_line_geoinfo(metro_line, stations):
    metro_geoinfo = {}
    for station in stations:
        metro_geoinfo[station] = get_geoinfo_gaode(metro_line + station + '地铁站')
    return metro_geoinfo


def get_all_line_geoinfo(metro_map):
    metro_line_geoinfo = {}
    for metro_line, stations in metro_map.items():
        line_info = get_single_line_geoinfo(metro_line, metro_map[metro_line])
        metro_line_geoinfo[metro_line] = line_info
        print(metro_line)
    return metro_line_geoinfo


if __name__ == '__main__':
    map = get_metro_map(url)
    result = get_all_line_geoinfo(map)
    with open('Beijing_metro_geoinfo.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
