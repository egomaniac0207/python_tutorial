import urllib.request as req
import ssl
import json


_src = "https://www.ptt.cc/bbs/movie/index.html"
ssl._create_default_https_context = ssl._create_unverified_context

_request=req.Request(_src
                    , headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})

with req.urlopen(_request) as _response:
    _output=_response.read().decode("utf-8")


import bs4
_doms=bs4.BeautifulSoup(_output,"html.parser")

# prettify(): 進行html美化
# print(_doms.prettify())

# find(): 只會撈第一個dom
# find_all(): 撈出所有dom
_titles=_doms.find_all(name="div",class_="title")

for title in _titles:
    # 只撈出非空的
    if title.a !=None:
        print(title.a.string)