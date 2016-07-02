from  re import *
# a='xyz123'
# # 点是站位符号 如果点很多超过原字符串长度 就返回一个空的列表
# b=re.findall('x.....',a)
# print(b)

#
#  查找x所在的位置
# a='xyzx123'
# b=re.findall('x.*',a)
# print(b)

# 结果和*类似
# a='xyx123'
# b=re.findall('x?',a)
# print(b)

# secret_code='hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'
# # .*贪心算法
# # b=re.findall('xx.*xx',secret_code)
# # print(b)
#
# # 非贪心算法
# # b=re.findall('xx.*?xx',secret_code)
# # print(b)
#
# #使用括号和非括号的区别
# # 括号内是我们需要的内容
# b=re.findall('xx(.*?)xx',secret_code)
# print(b)

# s='''sdfxxhell
# oxxfsdfxxworldxxasdf'''
# # 因为有换行符 导致hello后面xx没有 看下re.S
# d=re.findall('xx(.*?)xx',s,re.S)
# print(d)

# 返回一个集合内部是个元祖
# s2='asdfxxIxx123xxlovexxdfd'
# f=re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# f=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(1)
# print(f)
#
# #sub 使用，替换
# s='123abcssfasdfas123'
# # output=re.sub('123(.*?)123','789456',s)
# output=re.sub('123(.*?)123','%d'%789456,s)
#
# print(output)

secret_code='hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

b=findall('(\d+)',secret_code)
print(b)