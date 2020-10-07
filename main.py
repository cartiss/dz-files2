import json
from pprint import pprint
import collections
import xml.etree.ElementTree as ET

def count_words(word_list):
    count_dict = collections.Counter(word_list)
    max = 0
    values_list = count_dict.values()
    values_list = sorted(list(values_list))
    top = values_list[:-9:-1]
    for item in top:
        for k, v in count_dict.items():
            if v == item:
                print(str(k) + ' - ' + str(v))


def parse_json(file):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
        news_list = data['rss']['channel']['items']
        all_news = []
        for news in news_list:
            desc_split = news['description'].split(' ')
            for i in desc_split:
                if len(i) > 6:
                    all_news.append(i)
        count_words(all_news)

def parse_xml(file):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, parser)
    root = tree.getroot()
    desc_list = root.findall('channel/item/description')
    all_news = []
    for news in desc_list:
        for i in news.text.split(' '):
            if len(i) > 6:
                all_news.append(i)
    count_words(all_news)

parse_xml('files/newsafr.xml')
# parse_json('files/newsafr.json')
