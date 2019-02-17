# -*- coding: utf-8 -*-
import scrapy
import create_new_db 
import Dealing_with_Files 
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ['https://www.jobs.ch/en/vacancies/?location=geneva&term=']

    def parse(self, response):
        key='Controler'
        for quote in response.css("a.x--job-link.t--job-link"):
            
            if 'Packaging' in str(quote.css("a.x--job-link.t--job-link::text").extract()):
                value1=str(quote.css("a.x--job-link.t--job-link::text").extract())
                value2=str('www.jobs.ch'+quote.css("a.x--job-link.t--job-link::attr(href)").get())

                WriteClass=Dealing_with_Files.Dealing_with_Files()
                name="jobs_links.txt"
                info=value1+""+value2
                Fname=WriteClass.open_file(name,info)
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

