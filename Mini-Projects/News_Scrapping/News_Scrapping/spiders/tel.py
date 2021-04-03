import scrapy


class TelSpider(scrapy.Spider):
    name = 'tel'
    allowed_domains = ['telegraph.co.uk']
    start_urls = ['http://telegraph.co.uk/']
    base_url = "https://www.telegraph.co.uk"

    sections = ['politics', 'sport', 'business', 'culture']

    def parse(self, response, **kwargs):

        # All sections
        all_sections = response.css('div.site-header__primary-navigation-wrapper > div > nav > ul > li > a::attr(href)').getall()

        for section in all_sections:
            section_split = section.split("/")[1]
            if section_split in self.sections:
                link = response.url + section

                yield scrapy.Request(link, callback=self.parse_sections, cb_kwargs={'section': section_split})

        categories_to_scrap = ['politics', 'sport', 'business', 'culture']

    def parse_sections(self, response, section):
        section_links = response.css('section > ul > li > article > div.card__content > h3 > a::attr(href)').getall()

        for url in section_links:
            article_url = self.base_url + url
            yield scrapy.Request(article_url, callback=self.parse_story, cb_kwargs={'section': section})

    def parse_story(self, response, section):
        title = response.css('article > header > h1::text').get()
        article_text = response.css('article > div.grid-col.grid-col-12.article__layout.article__layout--content > \
        div:nth-child(1) > div.articleBodyText.section > div.component.article-body-text > p::text').getall()

        article_text = ' '.join([paragraph for paragraph in article_text])

        yield {
            'Title': title,
            'Article': article_text,
            'Section': section,
            'Article_URL': response.url
        }
