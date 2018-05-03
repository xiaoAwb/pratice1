# -*- coding: utf-8 -*-
from scrapy import Spider, Request, FormRequest
import json
from lagouwang.items import LagouwangItem


class LagouSpider(Spider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]
    url = 'https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult={needAddtionalResult}'
    kd = 'python'
    max_pn = 30

    @property
    def start_requests(self):
        city = '北京'
        needAddtionalResult = 'false'
        url = self.url.format(city=city, needAddtionalResult=needAddtionalResult)
        first = 'true'
        for page in range(self.max_pn + 1):
            data = {
                'first': first,
                'kd': self.kd,
                'pn': str(page)
            }
            print(FormRequest(url, formdata=data))
            # yield FormRequest(url, callback=self.parse_info, formdata=data)
            first = 'false'

    def parse_info(self, response):
        pass
        # print(response.text)
        # print(results)
        # item = LagouwangItem()
        # if 'content' in results.keys():
        #     if 'positionResult' in results.get('content').keys():
        #         if 'result' in results.get('content').get('positionResult').keys():
        #             for result in results.get('content').get('positionResult').get('result'):
        #                 for ele in result:
        #                     for field in item.fields():
        #                         if field in ele.keys():
        #                             item[field] = ele.get(field)
        #                 yield item
        # else:
        #     yield None
