import re
pat = re.compile('[a-z]+')
m = pat.match('tem12po')
print(m)