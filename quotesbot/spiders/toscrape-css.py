# -*- coding: utf-8 -*-
import scrapy
import items 
from items import QuotesbotItem
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ['https://www.jobs.ch/en/vacancies/?location=geneva&term=']

    


    def parse(self, response):
        item= QuotesbotItem()
          
        for quote in response.css("a.x--job-link.t--job-link"):
            
            if 'Directeur' in str(quote.css("a.x--job-link.t--job-link::text").extract()):
                item["name"]= str(quote.css("a.x--job-link.t--job-link::text").extract())
                item["url"]= str('www.jobs.ch'+quote.css("a.x--job-link.t--job-link::attr(href)").get())
                yield item   
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

