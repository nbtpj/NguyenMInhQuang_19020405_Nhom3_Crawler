import json
import scrapy


class Vietnamnet(scrapy.Spider):
    page_count = 0
    allowed_domains = ['vietnamnet.vn']
    name = 'vietnamnet'
    start_urls = ['https://vietnamnet.vn/vn/thoi-su/']

    def parse(self, response):
        if response.css('meta[property="og:type"]::attr(content)').get() == "article" and self.page_count < 30000:
            self.page_count += 1
            data = {
                'url': response.url,
                'id': str(str(response.url).rsplit('-', 1)[-1]).split('.')[0],
                'cate': response.css('.top-cate-head-title a::text').get().strip(),
                'title': response.css('.c-3e::text').get().strip(),
                'lead': response.css('.ArticleLead p::text').get().strip(),
                'content_text': [i.strip() for i in response.css('#ArticleContent > p::text').getall()],
                'time': ' '.join(response.css('.ArticleDate::text').get().split()),
                'image': [i.strip() for i in response.css('img::attr(src)').getall()],
                'tag': [i.strip() for i in response.css('#BoxTag a::text').getall()]
            }
            with open('vietnamnet.json', 'a+', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
                self.crawler.stats.set_value('number of pages: ',self.page_count)
        links=response.css('a[href^="/"]::attr(href)').getall()
        for link in links:
            yield response.follow(link, self.parse)


class Vnexpress(scrapy.Spider):
    page_count = 0
    allowed_domains = ['vnexpress.net']
    name = 'vnexpress'
    start_urls = ['https://vnexpress.net/tp-hcm-lam-viec-voi-ca-si-duy-manh-4142549.html']

    def parse(self, response):
        if response.css('meta[property="og:type"]::attr(content)').get() == "article" and self.page_count < 30000:
            self.page_count += 1
            data = {
                'url': response.url,
                'id': response.css('meta[name="its_id"]::attr(content)').get(),
                'cate': response.css('.active a::text').get().strip(),
                'title': response.css('meta[name="its_title"]::attr(content)').get().strip(),
                'lead': response.css('meta[itemprop="description"]::attr(content)').get().strip(),
                'content_text': [i.strip() for i in response.css('.Normal::text').getall()],
                'time': ' '.join(response.css('.date::text').get().split()),
                'image': [i.strip() for i in response.css('.lazied::attr(src)').getall()],
                'tag': response.css('meta[name="news_keywords"]::attr(content)').get().split(',')
            }
            with open('vnexpress.json', 'a+', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
                self.crawler.stats.set_value('number of pages: ', self.page_count)
        if str(response.url).find('shop') == -1:
            links = response.css('a[href^="/"]::attr(href)').getall()
            for link in links:
                yield response.follow(link, self.parse)


class Baomoi(scrapy.Spider):
    page_count = 0
    af_id = be_id = 31565625
    allowed_domains = ['baomoi.com']
    name = 'baomoi'

    def start_requests(self):
        while self.page_count < 30000:
            yield scrapy.Request('https://baomoi.com/x/c/' + str(self.af_id) + '.epi', self.parse)
            self.af_id += 1
            yield scrapy.Request('https://baomoi.com/x/c/' + str(self.be_id) + '.epi', self.parse)
            self.be_id -= 1

    def parse(self, response):
        id = str(str(response.url).rsplit('/', 1)[-1]).split('.')[0]
        if id != '404' and response.css('.split+ .cate::text').get() is not None:
            self.page_count += 1
            print(self.page_count)
            data = {
                'url': response.url,
                'id': id,
                'cate': response.css('.split+ .cate::text').get(),
                'title': response.css('.article__header::text').get(),
                'content': [i.strip() for i in
                            response.css('.body-text::text , .article__sapo::text , .split+ .cate::text').getall()],
                'tag': [i.strip() for i in response.css('.keyword::text').getall()],
                'source': response.css('.bm-source a::attr(href)').get()
            }
            with open('baomoi.json', 'a+', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)


class Foxnews(scrapy.Spider):
    page_count = 0
    allowed_domains = ['foxnews.com']
    name = 'foxnews'
    start_urls = ['https://www.foxnews.com/world/russian-ship-storing-ammonium-'
                  'nitrate-was-left-in-beirut-port-without-safety-precautions-repo']

    def parse(self, response):
        if response.css('meta[name="pagetype"]::attr(content)').get() == "article" and self.page_count < 30000:
            self.page_count += 1
            data = {
                'url': response.url,
                #'id': str(str(response.url).rsplit('-', 1)[-1]).split('.')[0],
                'cate': str(response.url).split('/')[-2],
                'title': response.css('meta[property="og:title"]::attr(content)').get().strip(),
                'lead': response.css('meta[property="og:description"]::attr(content)').get().strip(),
                'content_text': [i.strip() for i in response.css('p::text').getall()],
                'time': response.css('meta[name="dc.date"]::attr(content)').get(),
                'image': [i.strip() for i in response.css('img::attr(src)').getall()],
                'tag': [i.strip() for i in response.css('meta[name="classification-tags"]::attr(content)').get().split(',')]
            }
            with open('foxnews.json', 'a+', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
                self.crawler.stats.set_value('number of pages: ', self.page_count)
        links = response.css('a[href^="/"]::attr(href)').getall()
        for link in links:
            yield response.follow(link, self.parse)