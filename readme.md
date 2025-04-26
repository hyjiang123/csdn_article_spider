# 基于 scrapy 框架实现对 csdn 指定博主所有文章的爬取 demo



**该项目是利用 scrapy 框架对文章进行爬取，优化了爬取效率和速度；**

**主要功能是对 csdn 指定博主的文章进行全部爬取，并且考虑到了翻页的限制。**



1. csdndemo.py 为主要的爬取脚本，设置了爬取的规则；
2. items.py 定义了爬取信息接受对象；
3. pipelines.py 定义了后续对数据的处理，此项目中主要是将数据存储至数据库中；
4. setting.py 是相关的设置参数。



**启动项目步骤：**

1. 建立 MySQL 数据库， 并根据建表语句建表；
2. 修改 pipelines.py 中数据库的相关配置参数；
3. 修改csdndemo.py 中的 uid; 即指定用户的 ID；
4. 使用 scrapy crawl csdndemo -s -LOGLEVEL=INFO 启动项目；(python要先按照 scrapy 库)；



该项目仅用于交流学习，没有侵犯他人知识的意图；

如有问题和交流的想法请联系： huigjiang@163.com 感谢您的阅读和支持！