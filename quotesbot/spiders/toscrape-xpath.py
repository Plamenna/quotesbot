# -*- coding: utf-8 -*-
import scrapy
import json
from items import QuotesbotItem
from pprint import pprint
from scrapy.http import Request
class ToScrapeSpiderXPath(scrapy.Spider):


    name = 'toscrape-xpath'

    #start_urls = ['https://www.indeed.ch/jobs?q=&l=Geneva%2C+GE']
    
    def readFile(self,name):
        with open (name ,"r") as f:
             self.data=json.load(f)
        return self.data['url'],self.data['selector'],self.data['text'], self.data['link'], self.data['newpage']
    
    def start_requests(self):

        item= QuotesbotItem()
        start_urls= {'https://www.jobs.ch/en/vacancies/?location=geneva&term=': 'out.json'}


        for url in start_urls:

            item['url'],item['selector'],item['text'],item['link'],item['newpage']=self.readFile(start_urls[url])
            request=scrapy.Request(url=url, callback=self.parse)
            request.meta['item']=item
            yield request
    
     
    def parse(self, response):
        item=response.meta['item']
        a_selectors=response.xpath(item['selector'])
        for selector in a_selectors:
            text=selector.xpath(item['text']).extract_first()
            link = selector.xpath(item['link']).extract_first()
            if  text==None and link==None:continue




        next_page_url = response.css(item['newpage']).extract_first()
        if next_page_url is not None:
            request=scrapy.Request(response.urljoin(next_page_url),callback=self.parse)
            request.meta['item']=item
            yield request
        
