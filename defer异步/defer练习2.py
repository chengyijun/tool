# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: defer练习2.py
@time: 2021/1/22 9:26
@desc:
"""
from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet import task


# defer提供简单的写法，本身我们需要在拿到deferred之后把后续处理都挂在其callback中，但是这样写，代码就很分散，在debug的时候
# 跳来跳去很难读懂。如果使用defer.inlineCallbacks修饰器，就可以写出更好读懂的defer相关函数。被修饰的函数会返回一个deferred
# 对象，这个deferred对象会在函数中defer.returnValue函数跑成之后获得结果值，函数中间的各种yield都不会产生结果值，他们只是
# 中断点。整个函数中，各种耗时操作都可以被yield，yield一个deferred对象之后，这个函数就中断在yield处，主线程开始执行其他任务
# 当中途yield出来的deferred有了结果之后，这个函数从yield的地方继续往下运行，直到运行到returnValue处，使得这整个函数返回
# 的deferred对象获得结果。
# 其实这个修饰器就是是的代码看起来紧凑一点，吧需要家callback的代码都集中并且串行地写在同一个函数里，并且对于deferred的callback
# 中又要产生deferred的情况，不用return一个deferred对象，而是直接yield出去，看起来更好懂。
@defer.inlineCallbacks
def time_wasted_wrapper(job_id):
    print('begin time-wasted job ' + str(job_id))
    yield task.deferLater(reactor, 3, lambda: None)
    # 其实从现在开始，就想当一个callback函数了
    print('time-wasted job ' + str(job_id) + ' done!')
    print('result plus 1!')
    defer.returnValue(job_id + 1)


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
        job_list.append(job)
    deferred_list = defer.DeferredList(job_list)
    deferred_list.addCallback(all_jobs_done)


# 主函数，在调用完所有耗时操作之后，直接把主线程交给reactor处理，这里我们就能看到，开始调用10个耗时操作很快就能完成，而过一会
# 耗时操作的结果才陆续返回


def main():
    install_jobs()
    print('all job have started!')
    reactor.run()


if __name__ == '__main__':
    main()
