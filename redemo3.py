#-*-coding:utf-8-*
import requests
import re

html =requests.get('https://segmentfault.com/q/1010000002740016')
str=html.text
tag=re.findall('class="btn btn-primary btn-sm tag-mgr__btn">(.*?)</a>',str,re.S)
print(tag)
