# encoding=utf-8
# Author: kellyhwong
# Date: 2018.4.25
import requests
from bs4 import BeautifulSoup

DEF_DEBUG = 1

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

look_up_prefix = 'https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD/'
word = 'apple'
word_url = look_up_prefix + word
html_doc = download_page(word_url).decode('utf-8')

def get_eng_def(word):
    print("word to be searched: ")
    print(word)
    word_url = look_up_prefix + word
    html_doc = download_page(word_url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    # 为啥这么写？
    all_dict_div = soup.find_all("div", {"class": 'cdo-dblclick-area'})
    with open("all_dict_div", 'w') as f:
            print(all_dict_div, file=f)
    eng_dict_b = all_dict_div[0].find("b", {"class": 'def'})
    if DEF_DEBUG:
        filename = 'out.html'
        with open(filename, 'w') as f:
            print(download_page(word_url).decode('utf-8'), file=f)
    return str(eng_dict_b)

# tmp=get_eng_def('apple')
# print(tmp)

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Parsing Words From Text File')
    parser.add_argument("-f", "--file", dest="filename", required=True,
                        help='the name of the text file')
    args = parser.parse_args()
    print(args.filename)
    filename = args.filename
    print(filename)
    file = open(filename, 'r')
    # for word in file.readlines():
        # print(word)

    out_html_head = """<!DOCTYPE html><html lang="zh-CN"><head><title>Kelly's Personal Dict</title></head><body><table border="1">"""
    out_html_tail = """</table></body></html>"""
    th_head = """<th>"""
    th_tail = """</th>"""
    tr_head = """<tr>"""
    tr_tail = """</tr>"""
    out_html = ""
    out_html += out_html_head
    count = 0

    for word in file.readlines():
        # 去掉换行符
        word = word.strip()
        out_html += tr_head # table row begins
        out_html += th_head
        out_html += word
        out_html += th_tail
        out_html += th_head
        word_def = get_eng_def(word)
        word_soup = BeautifulSoup(word_def,"lxml")
        word_def_text = ""
        for i in word_soup.find_all(attrs={"class":"query"}):
            word_def_text += i.text
            word_def_text += " "
        print(word + ":")
        print(word_def_text)
        # with open(str(count) + '.html', 'w') as f:
            # print(word_def, file=f)
        count += 1
        # print(word_def)
        out_html += word_def
        out_html += th_tail # table row ends

    out_html += out_html_tail
    filename = 'out.html'
    with open(filename, 'w') as f:
        print(out_html, file=f)

# Test main
# Please input -f word-list.txt
if __name__ == '__main__':
    main()

    # print(args.filename)

    # main(word_list = args.word_list)
