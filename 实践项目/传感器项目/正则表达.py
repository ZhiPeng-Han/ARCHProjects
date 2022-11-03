import re
str = 'a1ffb\naf23b'
print(str)
html = re.findall(r'a(.*?)b',str)
print(html)