# encoding=utf-8
# Author: kellyhwong
# Date: 2018.4.25
import requests
from bs4 import BeautifulSoup

DEF_DEBUG = 0

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

# https://www.sanseido.biz/User/Dic/Index.aspx?TWords=%E6%84%9B&st=0&DORDER=151617&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox
# https://www.sanseido.biz/User/Dic/Index.aspx?TWords=%E6%84%9B&st=0&DORDER=151617&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox
def get_eng_def(word):
    word_url = look_up_prefix + word
    html_doc = download_page(word_url).decode('utf-8')
    soup = BeautifulSoup(html_doc,"lxml")
    all_dict_div = soup.find_all("div", {"class": 'cdo-dblclick-area'})
    eng_dict_b = all_dict_div[0].find("b", {"class": 'def'})
    if DEF_DEBUG:
        filename = 'out.html'
        with open(filename, 'w') as f:
            print(download_page(word_url).decode('utf-8'), file=f)
    return str(eng_dict_b)

# tmp=get_eng_def('apple')
# print(tmp)

tmp_url = "https://www.sanseido.biz/User/Dic/Index.aspx?TWords=%E6%84%9B&st=0&DORDER=151617&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox"

def main(word_list = ["%E6%84%9B"]): # TODO watashi to url encode
    # parser = argparse.ArgumentParser(description='TODO with more options')
    # parser.add_argument(dest='urls',metavar='words', nargs='*', default=[""]])
    args = parser.parse_args()
    jp_url_pre = "https://www.sanseido.biz/User/Dic/Index.aspx?TWords="
    jp_url_sub = "st=0&DORDER=151617&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox"
    for jp_word in word_list:
        jp_url = jp_url_pre + jp_word + jp_url_sub
        doc = download_page(tmp_url).decode('utf-8')
        with open("jptest.html", "w") as f:
            print(doc,file=f)
        doc_soup = BeautifulSoup(doc,"lxml")
        print(doc_soup.find_all(attrs={"class":"text-ll"})[0].text)

if __name__ == '__main__':
    main()
