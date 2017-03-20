#coding:utf-8
from selenium import webdriver
url_index = ('file:///C:/Users/Administrator/Desktop/xiaoshuo/index.htm')
chrome = webdriver.Chrome()
chrome.get(url_index)
all_num = chrome.find_elements_by_xpath('//div[8]//a')
for one in all_num:
    print one.text
    print one.get_attribute('href')
