import requests

s = requests.session()
r = s.get('http://api3.xiguadaili.com/ip/?tid=559676048748861&num=10&category=2&protocol=https&filter=off')
r1 = r.text
proxy_list = r1.split("\r\n")
print(proxy_list)
