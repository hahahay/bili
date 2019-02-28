# -*- coding: utf-8 -*-
import random
from random import choice
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from concurrent.futures import ThreadPoolExecutor
from functools import partial

# headless version
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''

# drive = webdriver.Chrome(chrome_options=chrome_options)


def play_video(proxy, av):
    # print(i)
    print(proxy)
    # av = "av41724649"
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http://{0}".format(proxy))

    drive = webdriver.Chrome(options=chrome_options)
    # drive = webdriver.Chrome()
    av_url = "https://www.bilibili.com/video/{0}/".format(av)
    print(av_url)

    # drive.get("https://www.bilibili.com/video/av41724649/")
    drive.get(av_url)
    video = WebDriverWait(drive, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频
    url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
    print(url)

    print("start")
    drive.execute_script("return arguments[0].play()", video)  # 开始播放
    time.sleep(10)

    print("stop")
    drive.execute_script("return arguments[0].pause()", video)  # 暂停

    drive.close()
    return 0

def play_video_1(proxy, av, t):
    # print(i)
    print(proxy)

    ua_list = [
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A306 Safari/6531.22.7',
        'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)',
        'Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN',
        'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9650 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.0.0)',
        'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; SM-G9500 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.3.993 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; SM-G9350 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.8 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1',
        'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Mi Note 3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.0.2',
        'Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone 6s; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.3.0 Mobile/15B87 Safari/604.1 MttCustomUA/2 QBWebViewType/1 WKType/1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/4G Language/zh_CN'
    ]
    ua = choice(ua_list)

    # av = "av41724649"
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http://{0}".format(proxy))
    chrome_options.add_argument('user-agent={0}'.format(ua))
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    drive = webdriver.Chrome(options=chrome_options)
    # drive = webdriver.Chrome()
    drive.set_window_size(240, 480)
    urls = ["https://www.bilibili.com/video/{0}".format(av),
           "https://www.bilibili.com/video/{0}?from=search&seid=11938748742388428234".format(av),
           "https://www.bilibili.com/video/{0}/?spm_id_from=333.788.videocard.1".format(av),
           "https://www.bilibili.com/video/{0}/?spm_id_from=333.788.videocard.6".format(av),
           "https://www.bilibili.com/video/{0}?spm_id_from=333.334.b_62696c695f6d75736963.5".format(av)
           ]
    av_url = choice(urls)

    dummy = ['av39176652', 'av12662385', 'av4147965', 'av27094419', 'av4147965', 'av6776634',
             'av42756772', 'av15570627', 'av2336588'

             ]
    dummy_url = "https://www.bilibili.com/video/{0}".format(choice(dummy))

    # print(av_url)

    # drive.get("https://www.bilibili.com/video/av41724649/")
    try:
        drive.get("https://www.bilibili.com/")
        time.sleep(3)
        drive.get(av_url)
        video = WebDriverWait(drive, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='bofqi']/div/div[2]/video")))   # 找到视频
        url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
        print(url)

        print("start")
        # drive.execute_script("return arguments[0].play()", video)  # 开始播放
        drive.find_elements_by_xpath("//*[@id='bofqi']/div/div[2]/div/div[4]/i")[0].click()
        # t = random.randint(30, 60)
        time.sleep(t)

        print("stop")
        drive.execute_script("return arguments[0].pause()", video)  # 暂停
    except Exception as e:
        print('bili video fail: {0} '.format(e))
    finally:
        drive.close()


def get_proxy(n):
    for i in range(10):
        try:
            s = requests.session()
            r = s.get(
                'http://api3.xiguadaili.com/ip/?tid=559676048748861&num={0}&delay=3&category=2&protocol=https&filter=on'.format(
                    n))
            r1 = r.text
            proxy_list = r1.split("\r\n")
            return proxy_list
        except Exception as e:
            print('proxy --------  except: {0}'.format(e))
            time.sleep(3)


# play_video("av41724649")


def play(av, n):
    t = random.randint(60, 300)
    proxy_list = get_proxy(n)
    executor = ThreadPoolExecutor(max_workers=n)
    play_video_av = partial(play_video_1, av=av, t=t)

    for data in executor.map(play_video_av, proxy_list):
        print("in main: 1 success".format(data))


# 知否
# av = "av41113057"

# 南山南
# av = "av25758075"

# 一生所爱
av = "av35829237"
n = 2
loop = 1000

for i in range(loop):
    print(i)
    play(av, n)
    time.sleep(random.randint(3, 10))

print("end of all")

