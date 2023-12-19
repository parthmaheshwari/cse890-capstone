import re
import time
import os
import requests
import json
import numpy as np
import pandas as pd
from tqdm import tqdm
import urllib.parse, urllib.request, json


def batch_items(input_list, batch_size=32):
    for i in range(0, len(input_list), batch_size):
        yield input_list[i:i+batch_size]


def clean_text(text):
    try:
        text = text.lower()
        text = re.sub('[^a-zA-Z0-9 ]+', ' ', text)
        text = re.sub(' +', ' ', text)
        text = text.strip()
        
    except:
        text = ""
    return text


def get_concept_tagged_dict_from_tagger(input_json):
    url = 'http://127.0.0.1:5000/invocations'
    response = requests.post(url, json=input_json)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        # Print the response content (the HTML or text returned by your app)
        # print(response.text)
    # else:
        # Handle any error if the request was not successful
        print(f"Request failed with status code: {response.status_code}")
    
    output = json.loads(response.text)
    return output


def prepare_json_for_academic_data(data_list):
    output = []
    for item in tqdm(data_list, total=len(data_list)):
        temp_dict = {
            'paper_id': item['corpusid'],
            'title': item.get('title', ''),
            'journal': '',
            'doc_type': '',
            'abstract': item.get('abstract', '')
        }
        output.append(temp_dict)
    return output


def prepare_json_for_patent_data(data_list):
    output = []
    for item in tqdm(data_list, total=len(data_list)):
        temp_dict = {
            'paper_id': item['generated_id'],
            'title': item.get('invention-title', ''),
            'journal': '',
            'doc_type': '',
            'abstract': item.get('abstract', '')
        }
        output.append(temp_dict)
    return output


def prepare_json_for_finance_data(data_list):
    output = []

    for item in tqdm(data_list, total=len(data_list)):
        temp_dict = {
            'paper_id': item['company_idx'],
            'title': item['short_description'],
            'journal': '',
            'doc_type': '',
            'abstract': item['long_description']
        }
        output.append(temp_dict)
    return output