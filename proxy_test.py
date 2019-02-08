import requests
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()

s = requests.session()
r = s.get('http://api3.xiguadaili.com/ip/?tid=559676048748861&num=10&category=2&protocol=https&filter=off')
r1 = r.text
proxy_list = r1.split("\r\n")


# 设置代理
chromeOptions.add_argument("--proxy-server=http://{0}".format(proxy_list[3]))
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(options=chromeOptions)
#browser = webdriver.Chrome()


# 查看本机ip，查看代理是否起作用
browser.get("https://www.baidu.com/")
print(browser.page_source)

browser.find_element_by_id("kw").send_keys("ip")
browser.find_element_by_id("submit").click()

# 退出，清除浏览器缓存
#browser.close()
