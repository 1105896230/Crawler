#-*-coding:utf-8-*
import re
old_url='http://www.jikexueyuan.com/course/android/pageNum=2'
total_page=20

f=open('redemo1.txt','r')
html=f.read()
f.close()
# ��ȥ����
# title=re.search('<title>(.*?)</title>',html,re.S).group(1)
# print(title)

# ��ȥ����
# ���ǰ�titiel��urlҲ��ſ������
# links=re.findall('<a href="(.*?)>',html,re.S)
# for url in links:
#     print(url)

# ���𲿷�����
# text_filed=re.findall('<ul>(.*)</ul>',html,re.S)[0]
# text=re.findall('">(.*?)</a>',text_filed,re.S)
# print(text)

# ��ҳ
for i in range(2,total_page):
    new_link=re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print(new_link)