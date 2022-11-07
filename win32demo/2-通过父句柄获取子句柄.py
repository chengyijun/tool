import win32gui


def get_all_child_window(parent):
    '''获得parent的所有子窗口句柄 返回子窗口句柄列表'''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(
        parent,
        lambda hwnd, param: param.append({hwnd: win32gui.GetClassName(hwnd)}),
        hwndChildList)
    return hwndChildList


res = get_all_child_window(1511314)
for r in res:
    print(r)