# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 生成词云.py
@time: 2021/1/14 16:55
@desc:
"""

import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


def create_word_cloud_img(txt_file_path: str, font_path: str, background_color: str = "white", max_words: int = 2000,
                          wc_img: str = 'target.png'):
    # 读取制作词云的文本
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        file = f.read()

    # 分词
    default_mode = jieba.cut(file)
    text = " ".join(default_mode)
    # 通过提供的图片 获取一个 填写词云的轮廓mask
    mask = np.array(Image.open("resource.jpg"))
    # 获取停用词表
    stopwords = set(STOPWORDS)
    # 可以自行添加停用词 （停用词 可简单理解为被放弃的词）
    # stopwords.add("said")
    wc = WordCloud(
        # 指定字体
        font_path=font_path,
        # 指定生成词云图片的背景
        background_color=background_color,
        # 制定生成词云的最大词数目
        max_words=max_words,
        # 指定词云生成的范围mask
        mask=mask,
        # 指定停用词表
        stopwords=stopwords)
    # 生成词云
    wc.generate(text)

    # 保存词云图片
    wc.to_file(wc_img)


if __name__ == '__main__':
    create_word_cloud_img(txt_file_path='最后一个道士Ⅱ.txt', font_path='SIMYOU.TTF')
