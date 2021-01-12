"""
表示数量的
    *   表示无限个
    +   表示至少要有一个
    ?   表示 0 或 1
    {}  表示 {3}表示三个 {3,5} 表示3-5个范围之前

表示内容的
    \w  表示 [0-9a-zA-Z] 数字或者字母
    \s  表示空格
    \d  表示数字
    .   表示任意字符
    [abc]   表示a或者b或者c 其中一个字符
    [ab|cd] 表示ab或者cd 其中一组

取反
    [^a]  表示去掉a之外的所有    [^]组合使用表示取反

开头结尾
    ^   表示开头
    $   表示结束
"""
import re

str1 = 'abcd123def456sgs789sgjslgj'
res = re.findall(r'\d+', str1)
print(res)

# 贪婪匹配与非贪婪匹配的区别
res2 = re.findall(r'f(.*)s', str1)
res3 = re.findall(r'f(.*?)s', str1)
print(res2)
print(res3)

res4 = re.search(r".*?(?P<aaa>\d+)", str1)
print(res4)
print(res4.groups())
print(res4.group())
print(res4.group(1))
print(res4.group('aaa'))


def callback(matched):
    print(matched)
    s1 = matched.group('dig')
    s1 += 'abel'
    return s1


# re.sub(正则匹配模式, 将要被替换成的内容, 被替换的字符串)
# 其中第二个参数  可以是普通字符串  也可以是一个回调函数  回调函数将会得到一个匹配结果作为参数
res5 = re.sub(r'(?P<dig>\d+)', callback, str1)
print(res5)
