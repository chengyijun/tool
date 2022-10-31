from threading import Event, Thread
import time

import pyautogui
from system_hotkey import SystemHotkey
import yaml


class Util:

    @staticmethod
    def get_config() -> dict:
        dict = {}
        with open("config/base.yml", "r", encoding="utf-8") as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        return content


class Caiji(Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Util.get_config()
        self.__flag = Event()
        self.__flag.clear()
        self.__running = Event()
        self.__running.set()
        self.hk = SystemHotkey()
        self.hk.register(("control", "1"), callback=self.pause_resume)
        self.hk2 = SystemHotkey()
        self.hk2.register(("control", "3"), callback=self.stop)

    def task(self):
        print(time.time())
        pyautogui.press(str(self.config.get("key")))

    def run(self) -> None:
        while True:
            self.__flag.wait()
            self.task()
            if not self.__running.isSet():
                break
            time.sleep(self.config.get("sleep"))

    def pause_resume(self, *args, **kwargs):
        if self.__flag.isSet():
            self.pause()
        else:
            self.resume()

    def begin(self, *args, **kwargs):
        print("开始了")
        self.__flag.set()

    def pause(self, *args, **kwargs):
        print("暂停了")
        self.__flag.clear()

    def resume(self, *args, **kwargs):
        print("恢复了")
        self.__flag.set()

    def stop(self, *args, **kwargs):
        print("停止了")
        self.__flag.set()
        self.__running.clear()


if __name__ == "__main__":
    caiji = Caiji()
    caiji.start()
    caiji.join()
    print("main end")