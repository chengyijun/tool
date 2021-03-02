# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: locust-01.py
@time: 2020/12/29 8:31
@desc:
"""

from locust import HttpUser, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {"username": "test", "password": "123456"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about")

    # tasks = {index: 2, about: 1}  # 与装饰器效果一致


class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks
    # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "http://127.0.0.1:5000"
    min_wait = 1000
    max_wait = 5000


"""
启动脚本：
locust -f 性能测试locust/locust-01.py
浏览器访问 http://localhost:8089
"""
