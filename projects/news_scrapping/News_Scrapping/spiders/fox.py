import scrapy


class FoxSpider(scrapy.Spider):
    name = 'fox'
    allowed_domains = ['foxnews.com']
    start_urls = ['http://foxnews.com/']
    base_url = "https://www.foxnews.com/"

    sections = ['Politics', 'Sports', 'Lifestyle']

    def parse(self, response, **kwargs):
        # All sections
        all_sections = response.css('#main-nav > ul > li > a::text').getall()
        # All section links
        all_section_links = response.css('#main-nav > ul > li > a::attr(href)').getall()

        for section, link in zip(all_sections, all_section_links):
            if section in self.sections:
                yield scrapy.Request(link, self.parse_sections, cb_kwargs={'section': section})

    def parse_sections(self, response, section):
        first_section_links = response.css('div.info > header > h2 > a::attr(href)').getall()
        second_section_links = response.css('div.info > header > h4 > a::attr(href)').getall()

        all_links = first_section_links + second_section_links
        for link in all_links:
            article_url = self.base_url + link
            yield scrapy.Request(article_url, self.parse_story, cb_kwargs={'section': section})

    def parse_story(self, response, section):
        title = response.css('main > article > header > h1::text').get()
        article_text = response.css(' div.article-content > div.article-body > p::text').getall()

        article_text = ' '.join([paragraph for paragraph in article_text])

        yield {
            'Title': title,
            'Article': article_text,
            'Section': section,
            'Article_URL': response.url
        }
