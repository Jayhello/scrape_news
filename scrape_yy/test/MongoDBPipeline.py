# import pymongo
# from scrapy.conf import settings
# from scrapy.exceptions import DropItem
# from scrapy import log
#
#
# class MongoDBPipeline(object):
#
#     def __init__(self):
#         connection = pymongo.MongoClient(settings['MONGODB_SERVER'],
#                                          settings['MONGODB_PORT'])
#
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]
#
#
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
#         log.msg('add to mongo sucess', level=log.DEBUG, spider = spider)

