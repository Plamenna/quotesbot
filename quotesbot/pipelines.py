# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm import sessionmaker
from models import JobsDB, db_connection, create_table

class ScrapySpiderPipeline(object):
    def __init__(self):
        engine=db_connection()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
    def process_item(self, item, spider):
        session=self.Session()
        jobsdb=JobsDB()
        jobsdb.name=item["name"]
        jobsdb.url= item["url"]
        try:
            session.add(jobsdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
