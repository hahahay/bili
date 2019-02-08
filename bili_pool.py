# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import threading
from threading import Thread
import random
from queue import Queue


class ThreadManger(Thread):
    """定义线程类，继承threading.Thread"""
    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        # 启动线程
        while True:
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()

class ThreadPoolManger():
    """线程池管理器"""
    def __init__(self, thread_num):
        # 初始化参数
        self.work_queue = Queue()
        self.thread_num = thread_num
        self.__init_threading_pool(self.thread_num)

    def __init_threading_pool(self, thread_num):
        # 初始化线程池，创建指定数量的线程池
        for i in range(thread_num):
            thread = ThreadManger(self.work_queue)
            thread.start()

    def add_job(self, func, *args):
        # 将任务放入队列，等待线程池阻塞读取，参数是被执行的函数和函数的参数
        self.work_queue.put((func, args))




# headless version
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# drive = webdriver.Chrome(chrome_options=chrome_options)


def play_video(av):
    drive = webdriver.Chrome()
    av_url = "https://www.bilibili.com/video/{0}/".format(av)
    print(av_url)

    print('thread {0} is running '.format(threading.current_thread().name))

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


# play_video("av41724649")

thread_pool = ThreadPoolManger(4)

for i in range(5):
    thread_pool.add_job(play_video, *("av41724649",))

