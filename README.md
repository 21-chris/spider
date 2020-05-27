# spider
import  bs4
import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")

soup = BeautifulSoup(r.text,'html.parser')

print('-------# 标签元素内的结构,友好的格式化输出------------------')
print(soup.a.prettify())
# 打印标签的属性
print(soup.a.parent.attrs['class'])
# 打印标签内的内容，nagivable
print(soup.a.string)

print('-------标签外的结构，打印标签的内容，------------------')
print(soup.p.contents)

print('-------------返回标签的第一个对象----------')
print(soup.body.contents)

print('--------------打印标签的子标签并且返回一个可遍历对象-----------------')
print(soup.p.children)

print('--------------打印标签的父亲标签并且返回标签本身-----------------')
print(soup.p.parent)

print('-------------返回一个可迭代对象---------------------')
print(soup.body.descendants)


