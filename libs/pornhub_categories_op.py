#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging
import sys
import requests,time,json,re
from lxml import etree
from libs.mongo_op import mongo_op
from fake_useragent import UserAgent
def pornhub_categories_op():
	logger = logging.getLogger("pornhub_categories")
	formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
	#file_handler = logging.FileHandler("/var/log/pornhub_cateories.log")
	file_handler = logging.FileHandler("/tmp/log")
	file_handler.setFormatter(formatter)
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.formatter = formatter
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)
	logger.setLevel(logging.INFO)
	mon = mongo_op()
	url = "https://www.pornhub.com/categories"
	init_page=requests.get(url,headers={'User-Agent':UserAgent().random}).content
	logger.info(init_page)
	dom_tree = etree.HTML(init_page)
	categories_links = dom_tree.xpath('//div[@class="category-wrapper "]/a/@href')
	categories_names = dom_tree.xpath('//div[@class="category-wrapper "]/a/@alt')
	categories_images = dom_tree.xpath('//div[@class="category-wrapper "]/a/img/@src')
	counts = dom_tree.xpath('//div[@class="category-wrapper "]/h5/a/span/var/text()')
	for (categorie_name,categorie_link,categorie_image,count) in zip(categories_names,categories_links,categories_images,counts):
    		insert_content = {'categorie_name':categorie_name,'categorie_link':categorie_link,'categorie_image':categorie_image,'count':count}
    		logger.info(insert_content)
    		time.sleep(0.000001)
    		try:
        		if mon.authentication() is True:
         			#if mon.query('Categories',insert_content,'0'):
             		#		logger.info("-->Query status:  "+str(True)+"<--")
         			#else:
            				mon.insert('Categories',insert_content)
    		except Exception as e:
         		logger.error(e)




