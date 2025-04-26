import urllib.request

import scrapy
from scrapy.http import Request
import json
import logging

from csdnpjt.items import CsdnpjtItem


class CsdndemoSpider(scrapy.Spider):
    name = 'csdndemo'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']
    uidname = "jingtian" # 某些人可能会有专属域名

    # 根据爬取不同用户，修改成对应的用户ID
    # uid = "littlefun591"
    uid = "2302_79177254"

    def start_requests(self):
        # yield Request("http://" + self.uidname + ".blog.csdn.net/?type=blog", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"})
        yield Request("http://blog.csdn.net/" + self.uid + "?type=blog", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"})

    def parse(self, response):
        item = CsdnpjtItem()
        item["name"] = response.xpath('//h4[@data-v-1ffb1322]/text()').extract()
        item["url"] = response.xpath('//a[contains(@href, "article/details")]/@href').extract()
        item["hits"] = response.xpath("//span[@class='view-num']/text()").extract()
        item["comment"] = response.xpath("//span[@class='comment-num']/text()").extract()
        yield item


        page = 2
        while True:
            hurl = "https://blog.csdn.net/community/home-api/v1/get-business-list?page=" + str(
                page) + "&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=" + self.uid
            headers2 = {"User-Agent",
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"}
            headers3 = {"origin",
                        "https://" + self.uidname + ".blog.csdn.net"}
            opener = urllib.request.build_opener()
            opener.addheaders = [headers2, headers3]
            response_data = opener.open(hurl).read()
            data = json.loads(response_data)
            articles = data['data']['list']
            if len(articles) == 0:
                break
            item2 = CsdnpjtItem()
            name_list = []
            url_list = []
            hits_list = []
            comments_list = []
            for article in articles:
                title = article['title']
                url = article['url']
                view_count = article['viewCount']
                comment_count = article['commentCount']
                name_list.append(title)
                url_list.append(url)
                hits_list.append(view_count)
                comments_list.append(comment_count)
            item2["name"] = name_list
            item2["url"] = url_list
            item2["hits"] = hits_list
            item2["comment"] = comments_list
            yield item2
            page = page + 1