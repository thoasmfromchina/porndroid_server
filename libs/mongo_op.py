#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pymongo import MongoClient as mongoclient
import time,re

class mongo_op(object):
    def __init__(self):
            self.conn = mongoclient("",)
    def authentication(self):
            try:
                self.conn.PornHub.authenticate("pornhub","")
            except Exception as e:
                return e
            return True

    def query(self,collection_name,query_content,display_query_property):
            db = self.conn["PornHub"]
            coll = db[collection_name]
            data_one = coll.find_one(query_content)
            datas_web_api =  coll.find({'video_title':re.compile(query_content)})
            datas_categories_web_api = coll.find({'categorie_name':re.compile(query_content)})
            datas_return_web_api = []
            datas_return_web_categories_api = []
            try:
                if int(display_query_property) == 1:
                    if data_one is None:
                        return {u'Query':"Failure"}
                    else:
                        return data_one
                elif int(display_query_property) == 0:
                       return True
                elif int(display_query_property) == 2:
                    for data in datas_web_api:

                        temp = {}
                        temp['video_title'] = data['video_title']
                        temp['video_duration'] = data['video_duration']
                        temp['image_url'] = data['image_url']
                        temp['viewkey'] = data['viewkey']
                        datas_return_web_api.append(temp)
                    return datas_return_web_api

                elif int(display_query_property) == 3:
                    for data in datas_categories_web_api:

                        temp = {}
                        temp['categorie_image'] = data['categorie_image']
                        temp['categorie_link'] = data['categorie_link']
                        temp['categorie_name'] = data['categorie_name']
                        temp['count'] = data['count']
                        datas_return_web_categories_api.append(temp)
                    return datas_return_web_categories_api
                else:
                    pass
            except Exception as e:
                   return e
            return True

    def insert(self,collection_name,insert_content):
            db = self.conn["PornHub"]
            coll = db[collection_name]
            try:
                   coll.update_one({'time':time.time()},{"$set":insert_content},upsert=True)

            except Exception as e:
                   return e
                   return False
            return True

'''
mon = mongo_op()

if mon.authentication() is True:
    collection_name = 'dataabc'
    insert_content = {'video_title':'My Legs, My Back - Music Video Compilation'}
    print mon.insert(collection_name,insert_content)
'''
