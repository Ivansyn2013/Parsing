#фаил для опосредованного запуска scrapy, что позволяет запустить режим отладки
from twisted.internet import asyncioreactor
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.mvideo import MvideoSpider
import asyncio

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    configure_logging()
    settings = get_project_settings()

    runner = CrawlerRunner(settings)
    runner.crawl(MvideoSpider)
    reactor.run()
