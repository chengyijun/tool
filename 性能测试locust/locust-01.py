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
        self.client.get("/about/")

    # tasks = {index: 2, about: 1}  # 与装饰器效果一致


class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks
    # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "http://debugtalk.com"
    min_wait = 1000
    max_wait = 5000
