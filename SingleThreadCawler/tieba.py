import requests

html=requests.get('http://tieba.baidu.com/f?kw=python&fr=wwwt')
print html.text