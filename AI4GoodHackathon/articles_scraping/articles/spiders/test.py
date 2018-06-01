import scrapy

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from articles.items import ArticlesItem

class ArtScrap(scrapy.spider):
	name = "opinion_or_fact"
	#allowed_domains = ["https://www.theglobeandmail.com"]
	start_urls = ["https://www.theglobeandmail.com/opinion/editorials/"]

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		article_titles = hxs.select("//div[@class='c-article-title']")
		items = []
		for article_titles in article_titles:
			item = ArticlesItem()
			item["article_title"] = article_titles.select("a/text()").extract()
			items.append(item)
		return items

	# def parse(self, response):
	# 	hxs = HtmlXPathSelector(response)
	# 	titles = hxs.select("//p")
	# 	for titles in titles:
	# 		

	# def parse(self, response):
	# 	for article in response.xpath('//div[@class="l-container"]'):
	# 		yield {
	# 			'title': article.xpath('.//div[@class="c-primary-title"]/text()').extract_first(),
	# 			'article_text': article.xpath('.//div[@class="c-article-body"]/text()').extract_first(),
	# 			'article_label': "opinion"
 #            }

	# def parse(self, response):
	# 	article = "div.l-container"
	# 	for title in response.css(article):
	# 		yield {
	# 			'title': article.css("div.c-primary-title::text").extract_first(),
	# 			'text': article.css("div.c-article-body::text").extract_first(),
	# 			'opinion': "opinion"
 #            }
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
