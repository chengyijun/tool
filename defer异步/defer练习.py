# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: defer练习.py
@time: 2021/1/22 9:03
@desc:
"""
from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet import task


# 耗时操作的外壳函数，返回一个deferred对象，一般调用这个函数之后，接住deferred对象，然后其addCallbacks加一些在耗时操作
# 完成之后的处理函数。这里使用了task模块来模拟了一个耗时操作，其中实参3模拟了消耗的时间，on_done模拟了耗时操作的返回值
def time_wasted_wrapper(job_id):
    def on_done():
        print('time-wasted job ' + str(job_id) + ' done!')
        # 耗时操作完成了，返回之歌结果
        return job_id

    print('begin time-wasted job ' + str(job_id))
    # 返回一个deferred对象，真实情况下，这里可能是一个直接返回deferred对象的函数，也可能是一个正常阻塞函数，但是你可以用
    # deferToThread来获得一个deferred对象
    return task.deferLater(reactor, 3, on_done)


def on_one_job_done(result):
    print('result plus 1!')
    return result + 1


# 所有deferred完成之后，触发回调提醒我们
def all_jobs_done(result):
    print(str(result))
    print('all jobs are done!')
    reactor.stop()


# 一次搞10个模拟的耗时操作，耗时操作都用时3秒，而后续处理都是对耗时操作的结果加1
def install_jobs():
    job_list = list()
    for i in range(10):
        job = time_wasted_wrapper(i)
        job.addCallback(on_one_job_done)
        job_list.append(job)
    deferred_list = defer.DeferredList(job_list)
    deferred_list.addCallback(all_jobs_done)


# 主函数，在调用完所有耗时操作之后，直接把主线程交给reactor处理，这里我们就能看到，开始调用10个耗时操作很快就能完成，而过一会
# 耗时操作的结果才陆续返回


def main():
    install_jobs()
    print('all obs have started!')
    reactor.run()


if __name__ == '__main__':
    main()
