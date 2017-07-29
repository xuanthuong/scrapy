# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from stackoverflow.items import StackoverflowItem


class stackoverflow_spider(Spider):
  print("spider started its job")
  name = 'stackoverflow'
  allowed_domains = ["stackoverflow.com"]
  start_urls = [
    "http://stackoverflow.com/questions?pagesize=50&sort=newest",
  ]
  
  def parse(self, response):
    print("spider call this parse function ...")
    questions = Selector(response).xpath('//div[@class="summary"]/h3')
    for question in questions:
      item = StackoverflowItem()
      item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
      item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
      yield item