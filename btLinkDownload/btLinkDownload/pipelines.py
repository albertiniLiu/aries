# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class BtlinkdownloadPipeline(object):
   def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='btlinks')
            #self.conn = MySQLdb.connect('host', 'user', 'passwd', 'dbname', charset="utf8", use_unicode=True)
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

   def process_item(self, item, spider):
        try:
            #first check btName has the same or not
            sqlstring = "select * from newlinks where btName='%s'" % item['title'].encode('utf-8')
            self.cursor.execute(sqlstring)
            ret = self.cursor.fetchall()
            if len(ret) > 0:
                # should return due to this item already saved before
                print "==========find duplicate btlinks!=========="
                return item


            sqlstring = "select * from downloadedlinks where btName='%s'" % item['title'].encode('utf-8')
            self.cursor.execute(sqlstring)
            ret = self.cursor.fetchall()
            if len(ret) > 0:
                # should return due to this item already saved before
                print "==========find duplicate btlinks!=========="
                return item

            # write this item to newlink table
            sqlstring = "INSERT INTO `newlinks` (`btName`, `bt_link_content`) VALUES ('%s', '%s')"%\
                    (item['title'].encode('utf-8'),item['link'].encode('utf-8'))
            self.cursor.execute(sqlstring)

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
