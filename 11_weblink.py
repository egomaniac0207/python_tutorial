import urllib.request as _request
import json
import ssl

src = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-020066-HPd"
#  不驗證ssl
ssl._create_default_https_context = ssl._create_unverified_context

with _request.urlopen(src) as _response:
    _data = json.load(_response)
    print(_data) 