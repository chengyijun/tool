# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/10/27 13:41

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

executable_path = r"C:\Users\abel\AppData\Local\Google\Chrome\Application\chromedriver.exe"
service = Service(executable_path=executable_path)
wd = webdriver.Chrome(service=service)

wd.get("http://127.0.0.1:5500/pywin32_demo/demo.html")
# 设置隐式等待  也就是当dom还没有加载出来的时候 会等待一段时间 括号里设置的是超时时间
wd.implicitly_wait(10)

obj = wd.find_element(By.CSS_SELECTOR, "body > input[type=file]")
print(obj)
# 原生的文件上传对话框 直接使用 send_keys()就行了
obj.send_keys(r"D:\1.jpg")
time.sleep(2)
wd.close()
