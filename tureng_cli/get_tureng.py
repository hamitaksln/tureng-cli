from selectolax.parser import HTMLParser
import requests

def get_request(url,word_type):
    r = requests.get(url)
    soup = HTMLParser(r.text)

    if word_type == "en":
        trs = soup.css('table .tr.ts')
    elif word_type == "tr":
        trs = soup.css('table .en.tm')
    else:
        return []

    word_tr_list = []
    for tr in trs:
        word_tr = tr.css_first('a').text(strip=True)
        word_tr_list.append(word_tr)
        # print(word_tr)
    return word_tr_list

def get_word_list(word,word_type):
    url = f"https://tureng.com/en/turkish-english/{word}"
    print(url)
    word_tr_list = get_request(url,word_type)
    return word_tr_list