#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib
import requests

def query(name):
    api_key = 'AIzaSyCxZZwJBb2utFPK_mC8fdwQ07BzzPuzPzE'
    query = name
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    response = requests.get(service_url, params=params).json()
    # response = json.loads(urllib.urlopen(url, proxies={'http':'http://127.0.0.1:8087', 'https':'http://127.0.0.1:8087'}).read())
    names = ""
    for element in response['itemListElement']:
        print element['result']['name'] + ' (' + str(element['resultScore']) + ')'
        if names == "":
            names = element['result']['name']
        else:
            names = names + "," + element['result']['name']
    # print names
    return names

if __name__ == '__main__':
    dict_file = open('./dict.csv', "r")
    # dict_file = open('D:\\lhq\\openimages\\dict.csv', "r")
    # com_file = open('./dict_combination.tsv', "a")
    # com_file = open('D:\\lhq\\openimages\\dict_combination.tsv', "a")
    for line in dict_file:
        try:
            id, label = line.split(',', 1)
            id = id.strip('\t\r\n')
            label = label.strip('\t\r\n')
            print label
            entity_names = query(label)
            if entity_names == None:
                entity_names = ""
            # com_file.write(id + '\t' + label + '\t' + entity_names + '\n')
        except ValueError:
            print('Ignoring: malformed line: "{}"'.format(line))
    dict_file.close()
    # com_file.close()
