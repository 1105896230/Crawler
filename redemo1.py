#-*-coding:utf-8-*
import re
old_url='http://www.jikexueyuan.com/course/android/pageNum=2'
total_page=20

f=open('redemo1.txt','r')
html=f.read()
f.close()
# 爬去标题
# title=re.search('<title>(.*?)</title>',html,re.S).group(1)
# print(title)

# 爬去链接
# 但是吧titiel的url也给趴下来了
# links=re.findall('<a href="(.*?)>',html,re.S)
# for url in links:
#     print(url)

# 爬起部分文字
# text_filed=re.findall('<ul>(.*)</ul>',html,re.S)[0]
# text=re.findall('">(.*?)</a>',text_filed,re.S)
# print(text)

# 翻页
for i in range(2,total_page):
    new_link=re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print(new_link)