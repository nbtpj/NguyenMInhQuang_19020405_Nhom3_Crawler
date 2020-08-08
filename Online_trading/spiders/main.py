import scrapy
import json
import time

class Websosanh(scrapy.Spider):
    name = 'websosanh'
    allowed_domains = ['websosanh.vn']
    pro_count = 0
    start_urls = ['https://websosanh.vn/dien-thoai-samsung-galaxy-a71-8gb128gb/1222490345/so-sanh.htm']

    def valid_link(self,link):
        return str(link).find('direct.htm') == -1 \
               and str(link).find('khachsan') == -1 \
               and str(link).find('tai-chinh') == -1 \
               and str(link).find('business') == -1 \
               and str(link).find('tel') == -1 \
               and str(link).find('tin-tuc') == -1 \
               and str(link).find('mail') == -1

    def parse(self, response):
        if str(response.url).find('so-sanh.htm') != -1:
            self.pro_count += 1
            data = {
                '_url': response.url,
                '_name': response.css('meta[name="keywords"]::attr(content)').get(),
                '_id': (str(response.url).split('/'))[-2],
                '_image': response.css('meta[property="og:image"]::attr(content)').get(),
                '_store': response.css('a[merchant-id="0"]::attr(href)').getall(),
                '_price': response.css('a[merchant-id="0"]::attr(price)').getall()
            }
            with open('websosanh.json', 'a+', encoding='utf8') as f:
                json.dump(data, f, ensure_ascii=False)
                self.crawler.stats.set_value('number of products: ', self.pro_count)
        time.sleep(0.1)
        links = response.css('a::attr(href)').getall()
        for link in links:
            if self.valid_link(link):
                yield response.follow(link, self.parse)


class Amazon(scrapy.Spider):
    name = 'amazon'
    number_pro = 0
    page_count = 1
    start_urls = ['https://www.amazon.com/s?rh=n%3A16225007011&page=1&qid=1596369640&ref=lp_16225007011_pg_2']

    def make_price(self, x, y):
        if y is not None:
            return x+'.'+y
        else:
            return x

    def parse(self, response):
        section = response.css('.s-latency-cf-section')
        print(len(section))
        for i in section:
            data = {
                '_url': response.urljoin(i.css('a::attr(href)').get()),
                '_name': i.css('.a-color-base.a-text-normal::text').get(),
                '_price': self.make_price(i.css('.a-price-whole::text').get(), i.css('.a-price-fraction::text').get()),
                '_image': i.css('img::attr(src)').get(),
                '_rate': i.css('.a-icon-alt::text').get()
            }
            if data['_name'] is not None :
                self.number_pro += 1
                with open('amazon.json', 'a+', encoding='utf8') as f:
                    json.dump(data, f, ensure_ascii=False)
                    self.crawler.stats.set_value('number of products: ', self.number_pro)
        if self.page_count <= 400:
            self.page_count += 1
            next_page = 'https://www.amazon.com/s?rh=n%3A16225007011&page=' + str(
                self.page_count) + '&qid=1596357401&ref=lp_16225007011_pg_'
            yield response.follow(next_page, self.parse)
