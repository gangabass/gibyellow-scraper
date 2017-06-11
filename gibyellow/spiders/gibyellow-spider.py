import scrapy
import re
from gibyellow.items import GibyellowItem

class GibyellowSpider(scrapy.Spider):
    name = "gibyellow"
    start_urls = ['https://gibyellow.gi/result?type=business&query=']

    def parse(self, response):

        for row_node in response.xpath('//div[@class="col-md-8"]/div[contains(@class, "panel-default")][position() > 1]'):
            record = GibyellowItem()
            
            record["Title"] = row_node.xpath('string(.//h5[@id="compname"])').extract_first()
            record["Address"] = row_node.xpath('string(.//p[@class="listing-address"])').extract_first()
            
            record["Address"] = re.sub( r'\s*[\r\n]+\s*', '; ', record["Address"] )
            record["Phone"] = row_node.xpath('.//p[contains(., "Tel:")]/text()').re_first(r'Tel:\s*(\S+)')
            
            categories = row_node.xpath('.//a[@class="search-headings"]/text()').extract()
            
            record["Categories"] = ";".join(categories)
            record["LogoURL"] = row_node.xpath('.//img/@src').extract_first()
            
            yield record
        
        if response.xpath('//ul[@class="pager"]/li[last()][./a]'):
            next_page_url = response.xpath('//ul[@class="pager"]/li[last()]/a/@href').extract_first()
            yield scrapy.Request( url=response.urljoin(next_page_url) )

        
