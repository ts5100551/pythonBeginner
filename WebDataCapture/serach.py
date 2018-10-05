import re
pat = re.compile('[a-z]+')
m = pat.search('3tem12po')
print(m)
