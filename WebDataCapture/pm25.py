from urllib.parse import urlparse
url = "https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=3"
o = urlparse(url)
print(o)
