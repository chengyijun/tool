# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: pywin32库的使用.py
@time: 2021/1/15 8:45
@desc:
"""
import random
import time

import pyautogui
import pyperclip
import win32con
import win32gui


def main():
    win_handle = win32gui.FindWindow(None, 'DFC V1.0')
    # 窗口显示
    win32gui.ShowWindow(win_handle, win32con.SW_SHOWNORMAL)
    # 窗口置顶
    win32gui.SetForegroundWindow(win_handle)

    for _ in range(5):
        add_appointment()


def add_appointment():
    # 添加预约
    click_action(310, 1010)
    # 输入姓名
    patient_name = f'test-患者{str(int(time.time()))}'
    type_action(543, 190, patient_name)
    # 输入电话1
    patient_telno1 = str(random.randint(1370000000000, 1379000000000))
    type_action(543, 240, patient_telno1)
    # 输入电话2
    patient_telno2 = str(random.randint(1370000000000, 1379000000000))
    type_action(543, 290, patient_telno2)
    # 输入年龄
    patient_age = str(random.randint(10, 100))
    type_action(543, 340, f'{patient_age}')

    # 选择性别
    # 0 - 男   467 389
    # 1 - 女   567 389
    # 2 - 未知 667 389
    choice = random.choice([0, 1, 2])
    if choice == 0:
        x = 467
    elif choice == 1:
        x = 567
    else:
        x = 667
    click_action(x, 389)

    # 选择来源
    click_action(564, 440)
    choice = random.choice([0, 1, 2])
    if choice == 0:
        # 自行就诊
        click_action(564, 470)
    elif choice == 1:
        # 朋友介绍
        click_action(564, 500)
    else:
        # 营销推广
        click_action(564, 560)

    # 选择医生
    click_action(543, 640)
    choice = random.choice([0, 1, 2, 3])
    if choice == 0:
        # 检查医生
        click_action(543, 670)
    elif choice == 1:
        # 登记护士
        click_action(543, 700)
    elif choice == 2:
        # 收费用户
        click_action(543, 760)
    else:
        # 未指定医生
        click_action(543, 820)

    # 选择 初诊 复诊
    # 466 684
    # 617 684
    choice = random.choice([0, 1])
    if choice == 0:
        x = 467
    else:
        x = 617
    click_action(x, 684)

    # 添加预约信息
    type_action(543, 734, f'{patient_name} 预约备注信息')

    # 选择 日期 日
    click_action(1085, 277)
    target_pos_y = random.randint(0, 277)
    pyautogui.dragTo(1085, target_pos_y, duration=1.0)
    # 选择日期 时
    click_action(831, 508)
    target_pos_y = random.randint(0, 508)
    pyautogui.dragTo(831, target_pos_y, duration=1.0)
    # 选择日期 分
    click_action(962, 508)
    choice = random.choice([0, 1])
    if choice == 408:
        y = 0
    else:
        y = 608
    pyautogui.dragTo(962, y, duration=1.0)

    # 选择看诊时长
    click_action(856, 729)
    # 816 1106
    target_pos_x = random.randint(816, 1106)
    pyautogui.dragTo(target_pos_x, 729, duration=1.0)
    # 勾选项目
    click_action(1222, 280, duration=0.3)
    click_action(1222, 315, duration=0.3)
    click_action(1222, 350, duration=0.3)
    click_action(1222, 380, duration=0.3)
    click_action(1222, 415, duration=0.3)
    click_action(1222, 445, duration=0.3)
    # 截图
    # pyautogui.screenshot(f'{patient_name}.jpg')
    # 确定添加
    click_action(982, 888)


def click_action(x: int, y: int, duration: float = 0.5) -> None:
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()


def type_action(x: int, y: int, txt: str, duration: float = 0.5) -> None:
    pyperclip.copy(txt)
    click_action(x, y, duration=duration)
    pyautogui.hotkey('ctrl', 'v')


if __name__ == '__main__':
    main()
