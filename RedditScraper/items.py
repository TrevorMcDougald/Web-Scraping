import scrapy


class RedditScraperItem(scrapy.Item):
    """
    Store scraped data in Item classes.
    """
    title = scrapy.Field()
    link = scrapy.Field()
    posting_time = scrapy.Field()
