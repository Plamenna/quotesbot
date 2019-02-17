# -*- coding: utf-8 -*-
import scrapy
import create_new_db 
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ['https://www.jobs.ch/en/vacancies/?location=geneva&term=']

    def parse(self, response):
        key='Controler'
        for quote in response.css("a.x--job-link.t--job-link"):
            if 'Controler' in str(quote.css("a.x--job-link.t--job-link::text").extract()):
                #value1=str(quote.css("a.x--job-link.t--job-link::text").extract())
                #value2='https://www.jobs.ch'+quote.css("a.x--job-link.t--job-link::attr(href)").get()
                value1=100
                value2=300
                create_new_db.insertValuesInDb(value1,value2)

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

