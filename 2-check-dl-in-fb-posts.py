import json
import glob
from tqdm import tqdm
import pandas as pd
import pycld2 as cld2
import random
import numpy as np
import random

def generate_random_boolean():
    return random.randint(1, 1000) == 1

import re
from nltk import ngrams
import string

DL_TERMS = set([
'dual language',
'dl',
'dual-language',
'two-way',
'duallanguage',
'twoway',
'two way',
'language immersion',
'language immersion'
])

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def random_sample(lst, sample_size):
    return random.sample(lst, sample_size)

def get_dl(s):
    s = s.lower()
    tokens = s.split(' ')
    tokens = [token.translate(str.maketrans('', '', string.punctuation)) for token in tokens]
    unigrams = set(tokens)
    bigrams = set([tokens[i]+' '+tokens[i+1] for i in range(len(tokens) - 1)])
    searchspace = unigrams | bigrams
    return len(DL_TERMS&searchspace)>0

#df = pd.read_csv('ca_districts.csv')
#df['facebook_id'] = df['facebook_id'].astype(str)
#print(df.facebook_id)

fail_count = 0
ids, dates, captions, langs, references = [], [], [], [], []
#for f in tqdm(random_sample(glob.glob('json/*.json'), 25)):
for f in tqdm(random.sample(glob.glob('~/fb-privacy/json/*.json'), k=100)):
    dat = read_json_file(f)
    posts = dat['result']['posts']
    for post in posts:
        #try:
        post_id = str(post.get('account').get('platformId'))
        #if str(post_id) not in df.facebook_id.values:
        #    continue # not a ca post
        post_date = post.get('date')
        post_text = post.get('caption')
        post_text = post.get('description') if post_text is None else post_text
        post_text = post.get('message') if post_text is None else post_text
        #except:
            #fail_count += 1
            #continue
        ids.append(post_id)
        dates.append(post_date)
        
        try:
          is_dl = get_dl(post_text)
        except:
          is_dl = False
        langs.append(is_dl)
        
        reference = post_text if not is_dl else ''#'' if not is_dl or generate_random_boolean() else post_text # Sae also every 1,000th text, RAM
        references.append(reference)

res = pd.DataFrame({
    'facebook_id': ids,
    'date': dates,
    #'caption': captions,
    'is_dl': langs,
    'reference': references
})

res.to_csv('all-dl-coding-control.csv', index = False)

print(f'Fail Count: {fail_count}')
