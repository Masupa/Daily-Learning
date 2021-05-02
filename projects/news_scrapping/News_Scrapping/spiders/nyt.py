import scrapy


class NytSpider(scrapy.Spider):
    name = 'nyt'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://nytimes.com/']
    base_url = 'http://nytimes.com/'

    sections = ['Politics', 'Sports', 'Business', 'Travel']

    def parse(self, response, **kwargs):

        # All news sections
        all_sections = response.css('header > div > ul > li > a::text').getall()
        # Links to all news sections
        all_sections_links = response.css('header > div > ul > li > a::attr(href)').getall()

        for section, link in zip(all_sections, all_sections_links):
            if section in self.sections:
                yield scrapy.Request(link, self.parse_sections, cb_kwargs={'section': section})

    def parse_sections(self, response, section):
        first_section_links = response.css('section > div > div > ol > li > article > div > h2 > a::attr(href)').getall()
        second_section_links = response.css('section > div > div > section > div > ol > li > div > div > a::attr(href)').getall()

        all_links = first_section_links + second_section_links
        for link in all_links:
            # if not link.startswith('https'):
            #     link = self.base_url + link
            link = self.base_url + link
            yield scrapy.Request(link, self.parse_article_link, cb_kwargs={'section': section})

    def parse_article_link(self, response, section):
        title = response.css('div > article > header > div > h1::text').getall()
        # title_p = response.css('div > article > header > p::text').getall()
        # time = response.css('div > article > header > div > time::attr(datetime)').getall()
        # article_text = response.css('div > article > section > div > div > p::text').getall()

        print(title)

        # article_text = " .".join([p for p in article_text])

        # yield {
        #     'Title': title,
        #     'Article': article_text,
        #     'Section': section,
        #     'Article_URL': response.url
        # }
