# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        #'http://quotes.toscrape.com/'
        'https://www.jobs.ch/en/vacancies/?location=geneva&term='
    ]

    def parse(self, response):
        jobs={}
        key='Java'
        for quote in response.css("a.x--job-link.t--job-link"):

                yield {
                        'Job Title': quote.css("a.x--job-link.t--job-link::text").extract(),
                        'Link to the Job': 'https://www.jobs.ch'+quote.css("a.x--job-link.t--job-link::attr(href)").get()

                    #.attrib["href"]
                    
                }



        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

