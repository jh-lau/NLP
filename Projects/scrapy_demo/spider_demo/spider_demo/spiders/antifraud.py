# -*- coding: utf-8 -*-
import re
from urllib import parse

import scrapy

from spider_demo.items import TiebaItem


class AntifraudSpider(scrapy.Spider):
    name = 'antifraud'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%B1%E4%BF%A1']

    def parse(self, response):
        url_list = response.css('.j_th_tit::attr(href)').extract()
        for url in url_list:
            yield scrapy.Request(url=parse.urljoin(response.url, url),
                                 callback=self.parse_detail)

        next_page_url = response.css('.next.pagination-item::attr(href)').extract()[0]

        if next_page_url:
            yield scrapy.Request(url=parse.urljoin(response.url, next_page_url),
                                 callback=self.parse)

    def parse_detail(self, response):
        # 帖子主题
        title = response.css('.core_title_txt.pull-left.text-overflow.vip_red::text ').extract() + \
                response.css('.core_title_txt.pull-left.text-overflow::text ').extract()
        # vip作者的class不一样
        if title:
            authors = response.css('.p_author_name.j_user_card::text').extract() + response.css(
                '.p_author_name.sign_highlight.j_user_card.vip_red::text').extract()
            # 帖子内容
            content_list = response.css('.d_post_content.j_d_post_content').extract()
            # 进一步处理帖子内容
            content_list = self.get_content(content_list)
            bbs_sendtime_list, bbs_floor_list = self.get_send_time_and_floor(response)

            try:
                for i in range(len(authors)):
                    tieba_item = TiebaItem()
                    tieba_item['title'] = title[0]
                    tieba_item['author'] = authors[i]
                    tieba_item['content'] = content_list[i]
                    tieba_item['reply_time'] = bbs_sendtime_list[i]
                    tieba_item['floor'] = bbs_floor_list[i]

                    yield tieba_item
            except:
                pass

    def get_content(self, contents):
        content_list = []
        for content in contents:
            reg = ';\">(.*)</div>'
            result = re.findall(reg, content)[0]
            content_list.append(result)
        return content_list

    def get_send_time_and_floor(self, response):
        time_and_floor_list = response.css('.post-tail-wrap span[class=tail-info]::text').extract()
        bbs_send_time = []
        bbs_floor_list = []
        for element in time_and_floor_list:
            if element == '来自':
                continue
            elif '楼' in element:
                bbs_floor_list.append(element)
            else:
                bbs_send_time.append(element)
        return bbs_send_time, bbs_floor_list
