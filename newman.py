# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup


class Newman():

    def __init__(self, url):
        self.url = url
        self.html_doc = urlopen(self.url).read()
        self.soup = BeautifulSoup(self.html_doc, from_encoding="gb18030")

    def prtlink(self):
        print '***************all http link avilable**********************'
        for hr in filter(lambda x: 'http' in x, (link.get('href') for link in self.soup.find_all('a'))):
            print hr
            urlretrieve(hr.encode('utf-8'), hr.split('/')[-1])

    def prtpress(self):
        print '***************all download press infomation***************'
        for tag in filter(lambda tag: 'OMB' in tag.text or u'出版信息' in tag.text, self.soup.find_all('div')):
            print tag.text


url = {
    '六年级': 'http://www.chicempire.net/products/productall.asp?smll=A56/A50&BigClassName=A50/A56%BD%CC%B2%C4&nianji=%C1%F9%C4%EA%BC%B6&keyword=%D3%A2%D3%EF&city=%C8%CB%C3%F1%BD%CC%D3%FD%B3%F6%B0%E6%C9%E7',
    '七年级': 'http://www.chicempire.net/products/productall.asp?smll=A56/A50&BigClassName=A50/A56%BD%CC%B2%C4&nianji=%C6%DF%C4%EA%BC%B6&keyword=%D3%A2%D3%EF&city=%C8%CB%C3%F1%BD%CC%D3%FD%B3%F6%B0%E6%C9%E7',
    '八年级': 'http://www.chicempire.net/products/productall.asp?smll=A56/A50&BigClassName=A50/A56%BD%CC%B2%C4&nianji=%B0%CB%C4%EA%BC%B6&keyword=%D3%A2%D3%EF&city=%C8%CB%C3%F1%BD%CC%D3%FD%B3%F6%B0%E6%C9%E7',
    '九年级': 'http://www.chicempire.net/products/productall.asp?smll=A56/A50&BigClassName=A50/A56%BD%CC%B2%C4&nianji=%BE%C5%C4%EA%BC%B6&keyword=%D3%A2%D3%EF&city=%C8%CB%C3%F1%BD%CC%D3%FD%B3%F6%B0%E6%C9%E7'
}


for k, v in url.items():
    print '============' + k + '=============='
    nman = Newman(v)
    nman.prtlink()
    nman.prtpress()
