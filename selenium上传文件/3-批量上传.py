# -*- coding:utf-8 -*-
# 作者: 程义军
# 时间: 2022/10/27 13:51

import time

import win32con
import win32gui
from selenium import webdriver
from selenium.webdriver import ActionChains
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
# 打开文件上传窗口
# 由于 file_input 对象不支持 click() 方法 所以这里只能通过鼠标点击事件触发
action = ActionChains(wd)
action.move_to_element(obj).click().perform()
time.sleep(2)
# win32gui
dialog = win32gui.FindWindow(None, u'打开')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
# 确定按钮Button
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
# 往输入框输入绝对地址
# 多文件上传 文件路径作为一个字符串  中间用空格隔开
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'"D:\1.jpg" "D:\2.jpg"')
# 按打开按钮
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

time.sleep(2)
print(obj.get_attribute("value"))
wd.close()
