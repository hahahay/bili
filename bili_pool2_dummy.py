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
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.33 Safari/535.11',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/3.0 Chrome/22.0.1229.79 Safari/537.1',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.5.4000 Chrome/26.0.1410.43 Safari/537.1',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.7 (KHTML, like Gecko) Chrome/20.0.1099.0 Safari/536.7 QQBrowser/6.14.15493.201',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.802.30 Safari/535.1 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
        'Opera/9.80 (Windows NT 6.1) Presto/2.12.388 Version/12.15',
        'Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.15'
    ]
    ua = choice(ua_list)

    # av = "av41724649"
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server=http://{0}".format(proxy))
    chrome_options.add_argument('user-agent={0}'.format(ua))

    drive = webdriver.Chrome(options=chrome_options)
    # drive = webdriver.Chrome()

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

    # av_url = "https://www.bilibili.com/video/{0}?from=search&seid=4669482125730411409".format(av)
    print(av_url)

    # drive.get("https://www.bilibili.com/video/av41724649/")
    try:
        drive.get("https://www.bilibili.com/")
        time.sleep(5)

        drive.get(dummy_url)
        video = WebDriverWait(drive, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频

        print("start dummy")
        drive.execute_script("return arguments[0].play()", video)  # 开始播放
        # t = random.randint(60, 190)
        time.sleep(5)

        print("stop dummy")
        drive.execute_script("return arguments[0].pause()", video)  # 暂停

        drive.get(av_url)
        video = WebDriverWait(drive, 15, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='bilibiliPlayer']/div[1]/div[1]/div[8]/video")))  # 找到视频
        # url = drive.execute_script("return arguments[0].currentSrc;", video)  # 打印视频地址
        # print(url)

        print("start")
        drive.execute_script("return arguments[0].play()", video)  # 开始播放
        # t = random.randint(60, 190)
        time.sleep(t)

        print("stop")
        drive.execute_script("return arguments[0].pause()", video)  # 暂停
    except Exception as e:
        print('except: {0}'.format(e))
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
            print('proxy except: {0}'.format(e))
            time.sleep(3)


# play_video("av41724649")


def play(av, n):
    t = random.randint(60, 280)
    proxy_list = get_proxy(n)
    executor = ThreadPoolExecutor(max_workers=n)
    play_video_av = partial(play_video_1, av=av, t=t)

    for data in executor.map(play_video_av, proxy_list):
        print("in main: 1 success".format(data))


# 知否
# av = "av41113057"

# 一生所爱
# av = "av35829237"

# 大鱼
av = "av35826571"

n = 8
loop = 1000

for i in range(loop):
    print(i)
    play(av, n)

print("end of all")

